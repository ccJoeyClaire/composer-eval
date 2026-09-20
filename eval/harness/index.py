"""Index OpenClaw usage docs under ``corpus/doc4RAG`` into Qdrant.

Collection names use a short profile code, not the word ``baseline``:
  openclaw_docs_b   → index profile ``baseline``

Does not write into ``getstart_codex_baseline``.

  python -m eval.harness.index
  python -m eval.harness.index --recreate
"""

from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

_REPO_ROOT = Path(__file__).resolve().parents[2]
# Load eval .env before rag.embedder (its import-time load_dotenv would
# otherwise pick AgenticRAG/.env and refuse to override).
load_dotenv(_REPO_ROOT / ".env", override=True)

from openai import APIConnectionError
from qdrant_client import AsyncQdrantClient

from eval.harness.paths import DOC4RAG_DIR, RAG_CONFIG_PATH
from rag.build import build_RAG_indexer
from rag.config import get_index_profile, get_rag_config
from rag.core import RAGIndexer
from rag.embedder.openai_embedder import OpenAIEmbedder
QDRANT_HOST = "127.0.0.1"
QDRANT_PORT = 6333
CORPUS_ID = "openclaw_docs"
DEFAULT_INDEX_PROFILE = "baseline"
_PLACEHOLDER_HOSTS = frozenset({"api.example.com", "example.com"})

# YAML index_profile_id → collection suffix. Keep ``baseline`` out of the name.
INDEX_PROFILE_CODES: dict[str, str] = {
    "token": "tk",
    "semantic": "sem",
    "baseline": "b",
    "s2b": "s2b",
    "predict_q": "pq",
    "full": "x",
}


def collection_for(index_profile_id: str) -> str:
    """``openclaw_docs_<code>`` for a YAML index profile."""
    code = INDEX_PROFILE_CODES.get(index_profile_id)
    if code is None:
        known = ", ".join(sorted(INDEX_PROFILE_CODES))
        raise SystemExit(
            f"No collection code for index profile {index_profile_id!r}. Known: {known}"
        )
    return f"{CORPUS_ID}_{code}"


def iter_markdown(root: Path) -> list[Path]:
    """Markdown files under *root*, excluding empty paths."""
    if not root.is_dir():
        raise SystemExit(f"corpus/doc4RAG directory not found: {root}")
    return sorted(
        (path for path in root.rglob("*.md") if path.is_file()),
        key=lambda path: path.as_posix().lower(),
    )


def _url_host(url: str) -> str:
    rest = url.split("://", 1)[-1]
    return rest.split("/", 1)[0].split("@")[-1].lower()


def require_embedding_config() -> str:
    """Reject placeholder embedding URLs before touching the corpus."""
    model = os.environ.get("EMBEDDING_MODEL_ID") or "text-embedding-3-small"
    url = (
        os.environ.get("EMBEDDING_BASE_URL")
        or os.environ.get("LLM_BASE_URL")
        or ""
    ).strip()
    if not url:
        raise SystemExit(
            "Missing EMBEDDING_BASE_URL (or LLM_BASE_URL fallback). "
            "Indexing needs an OpenAI-compatible embedding endpoint."
        )
    host = _url_host(url)
    if host in _PLACEHOLDER_HOSTS:
        raise SystemExit(
            f"EMBEDDING_BASE_URL is still the placeholder {url!r}. "
            "That host is not reachable, so every doc fails with "
            "APIConnectionError. Set it to your real embedding API "
            "(not DeepSeek chat). LLM_BASE_URL can stay api.deepseek.com."
        )
    print(f"embedding model={model} host={host}", flush=True)
    return url


async def require_embedding() -> None:
    """Fail fast if the embedding API cannot be reached."""
    url = require_embedding_config()
    embedder = OpenAIEmbedder()
    if getattr(embedder, "_native", False):
        print(
            f"embedding via DashScope TextEmbedding {embedder._native_endpoint}",
            flush=True,
        )
    try:
        vectors = await embedder.aembed_query("openclaw index ping")
    except Exception as exc:
        raise SystemExit(
            f"Embedding API failed ({url}). "
            f"{type(exc).__name__}: {exc}. Fix EMBEDDING_BASE_URL / key "
            "before indexing 798 docs."
        ) from exc
    print(f"embedding ping ok dim={len(vectors)}", flush=True)


async def require_qdrant() -> None:
    """Fail if Qdrant is not on 127.0.0.1:6333. Do not switch host."""
    client = AsyncQdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT,
        trust_env=False,
        check_compatibility=False,
    )
    try:
        await client.get_collections()
    except Exception as exc:
        raise SystemExit(
            f"Qdrant is not reachable at {QDRANT_HOST}:{QDRANT_PORT}. "
            "Start it there; will not switch host. "
            f"({type(exc).__name__}: {exc})"
        ) from exc
    finally:
        await client.close()


async def drop_collection_if_exists(indexer: RAGIndexer) -> None:
    store = indexer.store
    if await store.client.collection_exists(store.collection):
        await store.client.delete_collection(store.collection)
        print(f"dropped collection {store.collection}", flush=True)


async def index_docs(
    *,
    docs_dir: Path,
    index_profile_id: str,
    collection: str,
    recreate: bool,
    skip_existing: bool,
    limit: int | None,
) -> None:
    rag_config = get_rag_config(RAG_CONFIG_PATH)
    profile = get_index_profile(rag_config, index_profile_id)
    indexer = build_RAG_indexer(
        collection,
        use_token_chunker=profile.use_token_chunker,
        use_contextual=profile.use_contextual,
        use_predict_questions=profile.use_predict_questions,
        use_small_to_big=profile.use_small_to_big,
    )

    files = iter_markdown(docs_dir)
    if limit is not None:
        files = files[: max(0, limit)]

    print(
        f"index corpus={CORPUS_ID} collection={collection} "
        f"profile={index_profile_id} code={INDEX_PROFILE_CODES[index_profile_id]} "
        f"docs={len(files)} root={docs_dir}",
        flush=True,
    )

    ok = 0
    skipped = 0
    failed = 0
    try:
        if recreate:
            await drop_collection_if_exists(indexer)
        for i, path in enumerate(files, start=1):
            source = path.relative_to(docs_dir).as_posix()
            text = path.read_text(encoding="utf-8").strip()
            if not text:
                print(f"[{i}/{len(files)}] skip empty {source}", flush=True)
                skipped += 1
                continue
            if skip_existing and not recreate:
                existing = await indexer.store.acount_by_source(source)
                if existing > 0:
                    print(
                        f"[{i}/{len(files)}] skip existing {source} chunks={existing}",
                        flush=True,
                    )
                    skipped += 1
                    continue
            try:
                stored = await indexer.aindex(text, source=source)
            except APIConnectionError as exc:
                raise SystemExit(
                    f"[{i}/{len(files)}] embedding connection failed on "
                    f"{source}: {exc}. Stopping so the rest of the corpus "
                    "is not retried against a dead endpoint."
                ) from exc
            except Exception as exc:
                failed += 1
                print(
                    f"[{i}/{len(files)}] FAIL {source} "
                    f"{type(exc).__name__}: {exc}",
                    flush=True,
                )
                continue
            if stored:
                ok += 1
                print(f"[{i}/{len(files)}] ok {source}", flush=True)
            else:
                failed += 1
                print(f"[{i}/{len(files)}] verify failed {source}", flush=True)
    finally:
        await indexer.store.aclose()

    print(
        f"index done collection={collection} ok={ok} skipped={skipped} failed={failed}",
        flush=True,
    )
    if failed:
        raise SystemExit(f"Indexing finished with {failed} failures")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Index OpenClaw usage docs (doc4RAG) into Qdrant",
    )
    parser.add_argument(
        "--docs",
        type=Path,
        default=DOC4RAG_DIR,
        help=f"Markdown root (default: {DOC4RAG_DIR})",
    )
    parser.add_argument(
        "--profile",
        default=DEFAULT_INDEX_PROFILE,
        help=(
            "YAML index profile id (default: baseline → collection "
            f"{collection_for(DEFAULT_INDEX_PROFILE)})"
        ),
    )
    parser.add_argument(
        "--collection",
        help="Override collection name (default: openclaw_docs_<code>)",
    )
    parser.add_argument(
        "--recreate",
        action="store_true",
        help="Drop the target collection before indexing",
    )
    parser.add_argument(
        "--no-skip-existing",
        action="store_true",
        help="Re-index sources even if chunks already exist (can duplicate)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Index at most N markdown files (debug)",
    )
    args = parser.parse_args()

    os.environ.setdefault("RAG_CONFIG_PATH", str(RAG_CONFIG_PATH))

    collection = args.collection or collection_for(args.profile)
    require_embedding_config()
    asyncio.run(require_qdrant())
    asyncio.run(require_embedding())
    asyncio.run(
        index_docs(
            docs_dir=args.docs,
            index_profile_id=args.profile,
            collection=collection,
            recreate=args.recreate,
            skip_existing=not args.no_skip_existing,
            limit=args.limit,
        )
    )


if __name__ == "__main__":
    main()
