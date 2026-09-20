"""Run RAGChecker over extract-stage ``input.json`` files.

Harness extract writes ``gold_question`` / ``generator_response``. RAGChecker
requires ``query`` / ``response``; this module remaps before scoring.

Uses the official ``custom_llm_api_func`` hook plus ``eval.RAGChecker.LLM``.

    python -m eval.RAGChecker --runner agent_self_rag_hyde
    python -m eval.harness.main --stage score
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path
from typing import Any, cast

from dotenv import load_dotenv

from eval.RAGChecker.LLM import LLMClient
from eval.harness.paths import (
    RAGCHECKER_DIR,
    ragchecker_checking_output_path,
    ragchecker_input_path,
    ragchecker_llm_snapshot_path,
    ragchecker_scores_path,
)

_REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUNNER = "agent_self_rag_hyde"
METRIC_CHOICES = (
    "all_metrics",
    "overall_metrics",
    "retriever_metrics",
    "generator_metrics",
)

_LLM_CLIENT: LLMClient | None = None


def to_official_schema(payload: dict[str, Any]) -> dict[str, Any]:
    """Map harness ``CheckerInput`` rows onto RAGChecker ``results[]`` fields."""
    rows: list[dict[str, Any]] = []
    for raw in payload.get("results") or []:
        if not isinstance(raw, dict):
            raise TypeError("Each results[] item must be an object")
        query = str(raw.get("query") or raw.get("gold_question") or "")
        response = str(raw.get("response") or raw.get("generator_response") or "")
        context_raw = raw.get("retrieved_context") or []
        retrieved_context: list[dict[str, str]] = []
        for chunk in context_raw:
            if not isinstance(chunk, dict):
                continue
            retrieved_context.append(
                {
                    "doc_id": str(chunk.get("doc_id") or ""),
                    "text": str(chunk.get("text") or ""),
                }
            )
        rows.append(
            {
                "query_id": str(raw.get("query_id") or ""),
                "query": query,
                "gt_answer": str(raw.get("gt_answer") or ""),
                "response": response,
                "retrieved_context": retrieved_context,
            }
        )
    if not rows:
        raise ValueError("RAGChecker input has no results[] rows")
    return {"results": rows}


def my_llm_api_func(prompts: list[str]) -> list[str]:
    """Get responses from LLM for the input prompts."""
    if _LLM_CLIENT is None:
        raise RuntimeError("LLMClient is not initialized")
    heads = [str(p).replace("\n", " ")[:80] for p in prompts]
    print(
        f"[RAGChecker LLM] custom_llm_api_func n={len(prompts)} heads={heads}",
        flush=True,
    )
    return _LLM_CLIENT.complete_batch(prompts)


def _log_claim_counts(rag_results: Any) -> None:
    rows = getattr(rag_results, "results", None) or []
    print(f"[RAGChecker LLM] claim snapshot rows={len(rows)}", flush=True)
    for row in rows:
        response_claims = getattr(row, "response_claims", None) or []
        gt_claims = getattr(row, "gt_answer_claims", None) or []
        print(
            f"[RAGChecker LLM] {getattr(row, 'query_id', '?')} "
            f"response_claims={len(response_claims)} "
            f"gt_answer_claims={len(gt_claims)}",
            flush=True,
        )


def _to_rag_results(official: dict[str, Any]) -> Any:
    """Build ``RAGResults`` from the official schema (avoids dataclasses_json stubs)."""
    from ragchecker.container import RAGResult, RAGResults, RetrievedDoc

    results = []
    for row in official["results"]:
        results.append(
            RAGResult(
                query_id=row["query_id"],
                query=row["query"],
                gt_answer=row["gt_answer"],
                response=row["response"],
                retrieved_context=[
                    RetrievedDoc(
                        doc_id=chunk["doc_id"] or None,
                        text=chunk["text"],
                    )
                    for chunk in row["retrieved_context"]
                ],
            )
        )
    return RAGResults(results=results)


def run_checker(
    *,
    input_path: Path,
    output_path: Path,
    checking_output_path: Path | None = None,
    snapshot_path: Path | None = None,
    batch_size: int = 4,
    metrics: str = "all_metrics",
    max_concurrency: int = 4,
    extractor_max_new_tokens: int = 2000,
) -> dict[str, Any]:
    """Score one RAGChecker input file; write metrics JSON and print aggregates."""
    global _LLM_CLIENT
    from ragchecker import RAGChecker

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"RAGChecker input must be a JSON object: {input_path}")
    official = to_official_schema(payload)
    rag_results = _to_rag_results(official)

    checker_dump = checking_output_path or output_path.with_name("checking_outputs.json")
    snapshot_path = snapshot_path or checker_dump.with_name("llm_snapshots.jsonl")
    checker_dump.parent.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text("", encoding="utf-8")

    print(
        f"[RAGChecker LLM] start rows={len(official['results'])} "
        f"snapshot={snapshot_path}",
        flush=True,
    )
    _LLM_CLIENT = LLMClient(
        max_tokens=extractor_max_new_tokens,
        max_concurrency=max_concurrency,
        snapshot_path=snapshot_path,
    )
    evaluator = RAGChecker(
        custom_llm_api_func=my_llm_api_func,
        batch_size_extractor=batch_size,
        batch_size_checker=batch_size,
        extractor_max_new_tokens=extractor_max_new_tokens,
    )
    try:
        scored = evaluator.evaluate(
            rag_results,
            metrics=metrics,
            save_path=str(checker_dump),
        )
        _log_claim_counts(rag_results)
    finally:
        _LLM_CLIENT.close()
        _LLM_CLIENT = None

    metrics_out = cast(dict[str, Any], scored)
    output_path.write_text(
        json.dumps(metrics_out, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"RAGChecker: {input_path} -> {output_path}")
    print(json.dumps(metrics_out, ensure_ascii=False, indent=2))
    return metrics_out


def run_checker_for_runner(
    runner_id: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Score ``data/ragchecker/{runner_id}/input.json``."""
    return run_checker(
        input_path=ragchecker_input_path(runner_id),
        output_path=ragchecker_scores_path(runner_id),
        checking_output_path=ragchecker_checking_output_path(runner_id),
        snapshot_path=ragchecker_llm_snapshot_path(runner_id),
        **kwargs,
    )


def discover_runner_ids() -> list[str]:
    """Runner ids that already have an extract-stage ``input.json``."""
    if not RAGCHECKER_DIR.is_dir():
        return []
    found = [
        path.parent.name
        for path in sorted(RAGCHECKER_DIR.glob("*/input.json"))
        if path.is_file()
    ]
    return found


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Run RAGChecker scoring on extract-stage inputs",
    )
    parser.add_argument(
        "--runner",
        action="append",
        dest="runners",
        help=(
            "runner_id under data/ragchecker/ "
            f"(repeatable; default: {DEFAULT_RUNNER})"
        ),
    )
    parser.add_argument(
        "--all-runners",
        action="store_true",
        help="Score every data/ragchecker/*/input.json",
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="Explicit input JSON (overrides --runner)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Metrics JSON path (default: <input_dir>/scores.json)",
    )
    parser.add_argument(
        "--metrics",
        choices=METRIC_CHOICES,
        default="all_metrics",
        help="RAGChecker metric group (default: all_metrics)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=4,
        help="Extractor/checker batch size (default: 4)",
    )
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=4,
        help="Concurrent LLM requests inside each batch (default: 4)",
    )
    args = parser.parse_args(argv)

    load_dotenv(_REPO_ROOT / ".env")

    shared = {
        "batch_size": args.batch_size,
        "metrics": args.metrics,
        "max_concurrency": args.max_concurrency,
    }

    if args.input is not None:
        input_path = args.input
        output_path = args.output or input_path.with_name("scores.json")
        run_checker(input_path=input_path, output_path=output_path, **shared)
        return

    if args.all_runners:
        runner_ids = discover_runner_ids()
        if not runner_ids:
            raise SystemExit(f"No input.json files under {RAGCHECKER_DIR}")
    else:
        runner_ids = args.runners or [DEFAULT_RUNNER]

    for runner_id in runner_ids:
        run_checker_for_runner(runner_id, **shared)


if __name__ == "__main__":
    main()
