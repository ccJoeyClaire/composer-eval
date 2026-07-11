"""Batch infer: ``run_agent_infer`` (agent.py) and ``run_rag_infer`` (rag.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

__all__ = ["run_agent_infer", "run_rag_infer"]

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from eval.base import AgentInferArtifact, EvalRunner, GoldSample, RagInferArtifact

    run_agent_infer: Callable[
        [EvalRunner, list[GoldSample]], Awaitable[list[AgentInferArtifact]]
    ]
    run_rag_infer: Callable[
        [EvalRunner, list[GoldSample]], Awaitable[list[RagInferArtifact]]
    ]


def __getattr__(name: str) -> object:
    if name == "run_agent_infer":
        from eval.harness.infer.agent import run_agent_infer

        return run_agent_infer
    if name == "run_rag_infer":
        from eval.harness.infer.rag import run_rag_infer

        return run_rag_infer
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
