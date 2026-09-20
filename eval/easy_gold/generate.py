"""Split markdown → LLM QA pairs → gold JSON.

Easy Dataset flow, minus the UI: chunk text, ask the model for
questions+answers, write ``GoldSample`` rows.

  python -m eval.easy_gold.generate --limit 1 --dry-run
  python -m eval.easy_gold.generate --docs corpus/doc4RAG/beginner-openclaw-framework-focus
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from pathlib import Path

from dotenv import load_dotenv

from eval.base import GoldSample
from eval.harness.paths import DOC4RAG_DIR, GOLD_DIR, REPO_ROOT
from eval.harness.qa_pairs_to_gold import write_gold
from llm.client import LLMClient

DEFAULT_DOCS = DOC4RAG_DIR / "beginner-openclaw-framework-focus"
DEFAULT_OUT = GOLD_DIR / "openclaw_docs_qa.json"
MAX_CHARS = 1500
_FRONTMATTER = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n?", re.DOTALL)
_HEADING = re.compile(r"(?m)^(#{1,3} .+)$")
_FENCE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)

_SYSTEM = (
    "你根据给定文档片段出评测用 QA。"
    "只依据片段内容，不编造。问题必须自洽，不要写“根据上文”。"
    "只输出 JSON。"
)


def iter_markdown(root: Path) -> list[Path]:
    if not root.is_dir():
        raise SystemExit(f"docs dir not found: {root}")
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def chunk_markdown(text: str, max_chars: int = MAX_CHARS) -> list[str]:
    body = _FRONTMATTER.sub("", text, count=1).strip()
    if not body:
        return []
    parts = _HEADING.split(body)
    sections: list[str] = []
    if parts[0].strip():
        sections.append(parts[0].strip())
    for i in range(1, len(parts), 2):
        heading = parts[i]
        rest = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append(f"{heading}\n{rest}".strip())
    chunks: list[str] = []
    buf = ""
    for section in sections:
        if buf and len(buf) + 2 + len(section) > max_chars:
            chunks.append(buf)
            buf = section
        else:
            buf = f"{buf}\n\n{section}".strip() if buf else section
        while len(buf) > max_chars:
            chunks.append(buf[:max_chars].rsplit("\n", 1)[0] or buf[:max_chars])
            buf = buf[len(chunks[-1]) :].strip()
    if buf:
        chunks.append(buf)
    return [c for c in chunks if c.strip()]


def _parse_pairs(raw: str) -> list[dict]:
    text = _FENCE.sub("", (raw or "").strip()).strip()
    if not text:
        return []
    data = json.loads(text)
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    if isinstance(data, dict):
        rows = data.get("pairs") or data.get("questions") or []
        return [row for row in rows if isinstance(row, dict)]
    return []


def _prompt(chunk: str, n: int) -> str:
    return (
        f"从下面文档片段生成 {n} 条 QA。\n"
        "返回 JSON：{\"pairs\":[{\"user_question\":\"\",\"gold_query\":\"\",\"gt_answer\":\"\"}]}\n"
        "user_question=用户会怎么问；gold_query=检索用问法（可与问题相同）；"
        "gt_answer=依据片段的标准答案。\n\n"
        f"片段：\n{chunk}"
    )


async def _pairs_for_chunk(
    llm: LLMClient,
    sem: asyncio.Semaphore,
    chunk: str,
    n: int,
) -> list[dict]:
    async with sem:
        message = await llm.arequest_llm(
            [
                {"role": "system", "content": _SYSTEM},
                {"role": "user", "content": _prompt(chunk, n)},
            ],
            json_output=True,
            temperature=0.2,
            max_tokens=2500,
            extra_body={"thinking": {"type": "disabled"}},
        )
    try:
        return _parse_pairs(str(message.content or ""))
    except json.JSONDecodeError:
        return []


async def generate(
    *,
    docs: Path,
    out: Path,
    limit: int | None,
    pairs_per_chunk: int,
    concurrency: int,
    dry_run: bool,
) -> Path | None:
    files = iter_markdown(docs)
    if limit is not None:
        files = files[: max(0, limit)]
    jobs: list[tuple[str, str]] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        source = path.relative_to(docs).as_posix()
        for chunk in chunk_markdown(text):
            jobs.append((source, chunk))
    print(
        f"docs={docs} files={len(files)} chunks={len(jobs)} "
        f"pairs_per_chunk={pairs_per_chunk}",
        flush=True,
    )
    if dry_run:
        for source, chunk in jobs:
            print(f"  {source} chars={len(chunk)}", flush=True)
        return None

    load_dotenv(REPO_ROOT / ".env", override=True)
    llm = LLMClient()
    sem = asyncio.Semaphore(max(1, concurrency))
    samples: list[GoldSample] = []
    try:
        results = await asyncio.gather(
            *[_pairs_for_chunk(llm, sem, chunk, pairs_per_chunk) for _, chunk in jobs]
        )
    finally:
        await llm.aclose()

    index = 1
    for (source, _), rows in zip(jobs, results):
        for row in rows:
            question = str(row.get("user_question") or "").strip()
            query = str(row.get("gold_query") or question).strip()
            answer = str(row.get("gt_answer") or "").strip()
            if not question or not answer:
                continue
            samples.append(
                GoldSample(
                    query_id=f"query_{index:03d}",
                    user_question=question,
                    gold_query=query or question,
                    gt_answer=answer,
                )
            )
            index += 1
        print(f"ok {source} +{len(rows)}", flush=True)

    written = write_gold(samples, out)
    print(f"gold={len(samples)} -> {written}", flush=True)
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Docs → gold QA (Easy Dataset MVP)")
    parser.add_argument("--docs", type=Path, default=DEFAULT_DOCS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--limit", type=int, default=None, help="Max markdown files")
    parser.add_argument("--pairs-per-chunk", type=int, default=2)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    asyncio.run(
        generate(
            docs=args.docs,
            out=args.out,
            limit=args.limit,
            pairs_per_chunk=args.pairs_per_chunk,
            concurrency=args.concurrency,
            dry_run=args.dry_run,
        )
    )


if __name__ == "__main__":
    main()
