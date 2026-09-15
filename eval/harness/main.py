"""End-to-end eval harness: qa_export → gold → infer → extract → RAGChecker score."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from dotenv import load_dotenv

from eval.base import EvalRunner, GoldSample
from eval.harness.extract import extract_runner, load_gold, write_checker_input
from eval.harness.infer.agent import run_agent_infer
from eval.harness.infer.rag import run_rag_infer
from eval.harness.paths import (
    RAG_CONFIG_PATH,
    agent_infer_path,
    ensure_data_dirs,
    gold_path,
    rag_infer_path,
)
from eval.harness.qa_pairs_to_gold import load_qa_pairs, qa_pairs_to_gold, write_gold

_REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GOLD = "codex_qa_samples.json"

DEFAULT_RUNNERS: list[EvalRunner] = [
    EvalRunner(
        runner_id="agent_self_rag_hyde",
        mode="agent",
        collection="getstart_codex_baseline",
        agent_config={
            "pattern_id": "self_rag",
            "profile_id": "rerank_hyde",
            "enable_web_search": False,
        },
        rag_config={"profile_id": "rerank_hyde", "top_k": 10},
    ),
    EvalRunner(
        runner_id="rag_rerank_hyde",
        mode="rag",
        collection="getstart_codex_baseline",
        agent_config={},
        rag_config={"profile_id": "rerank_hyde", "top_k": 10},
    ),
]


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
    parser = argparse.ArgumentParser(description="Eval harness pipeline")
    parser.add_argument(
        "--stage",
        choices=("gold", "infer", "extract", "score", "all"),
        default="all",
        help="Pipeline stage to run (default: all = gold+infer+extract; score is separate)",
    )
    parser.add_argument(
        "--gold",
        default=DEFAULT_GOLD,
        help=f"Gold JSON filename under eval/data/gold/ (default: {DEFAULT_GOLD})",
    )
    args = parser.parse_args()

    load_dotenv(_REPO_ROOT / ".env")
    os.environ.setdefault("RAG_CONFIG_PATH", str(RAG_CONFIG_PATH))
    ensure_data_dirs()

    if args.stage == "score":
        run_score(DEFAULT_RUNNERS)
        return

    if args.stage in ("gold", "all"):
        run_gold(args.gold)

    gold = load_gold(gold_path(args.gold))

    if args.stage in ("infer", "all"):
        asyncio.run(run_infer(DEFAULT_RUNNERS, gold))

    if args.stage in ("extract", "all"):
        run_extract(DEFAULT_RUNNERS, gold)


if __name__ == "__main__":
    main()
