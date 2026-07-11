"""Eval harness: gold → infer → extract → RAGChecker."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from eval.base import CheckerInput, CheckerSample, GoldSample

    agent_artifact_to_checker_sample: Callable[..., CheckerSample]
    extract_runner: Callable[..., CheckerInput]
    load_gold: Callable[..., list[GoldSample]]
    rag_artifact_to_checker_sample: Callable[..., CheckerSample]
    write_checker_input: Callable[..., Path]
    ensure_data_dirs: Callable[[], None]
    ragchecker_input_path: Callable[..., Path]

__all__ = [
    "agent_artifact_to_checker_sample",
    "ensure_data_dirs",
    "extract_runner",
    "load_gold",
    "rag_artifact_to_checker_sample",
    "ragchecker_input_path",
    "write_checker_input",
]


def __getattr__(name: str) -> object:
    if name == "agent_artifact_to_checker_sample":
        from eval.harness.extract import agent_artifact_to_checker_sample

        return agent_artifact_to_checker_sample
    if name == "extract_runner":
        from eval.harness.extract import extract_runner

        return extract_runner
    if name == "load_gold":
        from eval.harness.extract import load_gold

        return load_gold
    if name == "rag_artifact_to_checker_sample":
        from eval.harness.extract import rag_artifact_to_checker_sample

        return rag_artifact_to_checker_sample
    if name == "write_checker_input":
        from eval.harness.extract import write_checker_input

        return write_checker_input
    if name == "ensure_data_dirs":
        from eval.harness.paths import ensure_data_dirs

        return ensure_data_dirs
    if name == "ragchecker_input_path":
        from eval.harness.paths import ragchecker_input_path

        return ragchecker_input_path
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
