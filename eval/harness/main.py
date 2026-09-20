"""End-to-end eval harness: gold → infer → extract → RAGChecker score."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from dotenv import load_dotenv

_REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(_REPO_ROOT / ".env", override=True)

from eval.base import EvalRunner, GoldSample
from eval.harness.extract import extract_runner, load_gold, write_checker_input
from eval.harness.infer.agent import run_agent_infer
from eval.harness.infer.rag import run_rag_infer
from eval.harness.paths import (
    DEFAULT_GOLD,
    RAG_CONFIG_PATH,
    agent_infer_path,
    ensure_data_dirs,
    gold_path,
    rag_infer_path,
)
from eval.harness.qa_pairs_to_gold import load_qa_pairs, qa_pairs_to_gold, write_gold
from eval.harness.runners import DEFAULT_RUNNERS, known_runner_ids, resolve_runners


def run_gold(gold_name: str) -> Path:
    """qa_export → gold JSON."""
    rows = load_qa_pairs()
    samples = qa_pairs_to_gold(rows)
    out = write_gold(samples, gold_path(gold_name))
    print(f"gold: {len(samples)} samples -> {out}")
    return out


async def run_infer(runners: list[EvalRunner], gold: list[GoldSample]) -> None:
    """gold → infer artifacts (agent / rag)."""
    for runner in runners:
        runner_id = runner["runner_id"]
        if runner["mode"] == "agent":
            artifacts = await run_agent_infer(runner, gold)
            for artifact in artifacts:
                path = agent_infer_path(runner_id, artifact["query_id"])
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(
                    json.dumps(artifact, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                print(f"infer agent: {artifact['query_id']} -> {path}")
        else:
            artifacts = await run_rag_infer(runner, gold)
            for artifact in artifacts:
                path = rag_infer_path(runner_id, artifact["query_id"])
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(
                    json.dumps(artifact, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                print(f"infer rag: {artifact['query_id']} -> {path}")


def run_extract(runners: list[EvalRunner], gold: list[GoldSample]) -> None:
    """infer artifacts + gold → RAGChecker input."""
    for runner in runners:
        runner_id = runner["runner_id"]
        mode = runner["mode"]
        checker_input = extract_runner(runner_id, gold, mode=mode)
        out = write_checker_input(runner_id, checker_input)
        print(
            f"extract: runner_id={runner_id} mode={mode} "
            f"samples={len(checker_input['results'])} -> {out}"
        )


def run_score(runners: list[EvalRunner]) -> None:
    """RAGChecker input → overall / retriever / generator metrics."""
    from eval.RAGChecker.run import run_checker_for_runner

    for runner in runners:
        runner_id = runner["runner_id"]
        run_checker_for_runner(runner_id)


def main() -> None:
    known = ", ".join(known_runner_ids())
    default_ids = ", ".join(runner["runner_id"] for runner in DEFAULT_RUNNERS)
    parser = argparse.ArgumentParser(description="Eval harness pipeline")
    parser.add_argument(
        "--stage",
        choices=("gold", "infer", "extract", "score", "all"),
        default="all",
        help="Pipeline stage (default: all = infer+extract+score; gold is separate)",
    )
    parser.add_argument(
        "--gold",
        default=DEFAULT_GOLD,
        help=f"Gold JSON filename under gold/ (default: {DEFAULT_GOLD})",
    )
    parser.add_argument(
        "--runner",
        action="append",
        dest="runners",
        metavar="RUNNER_ID",
        help=f"Catalog runner_id (repeatable; default: {default_ids}; known: {known})",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Use only the first N gold rows (debug / smoke)",
    )
    args = parser.parse_args()

    os.environ.setdefault("RAG_CONFIG_PATH", str(RAG_CONFIG_PATH))
    ensure_data_dirs()

    if args.stage == "gold":
        run_gold(args.gold)
        return

    runners = resolve_runners(args.runners)

    if args.stage == "score":
        run_score(runners)
        return

    gold_file = gold_path(args.gold)
    if not gold_file.is_file():
        raise SystemExit(
            f"Gold file not found: {gold_file}. Run --stage gold first."
        )
    gold = load_gold(gold_file)
    if args.limit is not None:
        gold = gold[: max(0, args.limit)]
        print(f"gold limited to {len(gold)} rows", flush=True)

    if args.stage in ("infer", "all"):
        asyncio.run(run_infer(runners, gold))

    if args.stage in ("extract", "all"):
        run_extract(runners, gold)

    if args.stage == "all":
        run_score(runners)


if __name__ == "__main__":
    main()
