"""Eval runner catalog: one ``EvalRunner`` arm per ``runner_id``.

Default infer arm is direct RAG on the OpenClaw docs collection.
Agent pattern arms stay in the catalog via ``--runner``.
"""

from __future__ import annotations

from eval.base import EvalRunner

COLLECTION = "openclaw_docs_b"
INDEX_PROFILE_ID = "baseline"
RETRIEVE_PROFILE = "rerank_hyde"
PRESET_ID = "baseline_hyde"
RAG_TOP_K = 10

_WAVE1_PATTERNS = ("self_rag", "crag", "crag_self_rag")


def _rag_runner() -> EvalRunner:
    """RAG arm: ``rag_{retrieve_profile}`` on ``COLLECTION``."""
    return EvalRunner(
        runner_id=f"rag_{RETRIEVE_PROFILE}",
        mode="rag",
        collection=COLLECTION,
        agent_config={},
        rag_config={"profile_id": RETRIEVE_PROFILE, "top_k": RAG_TOP_K},
    )


def _agent_runner(pattern_id: str) -> EvalRunner:
    """Agent arm: ``agent_{pattern}_{preset}`` on ``COLLECTION``."""
    return EvalRunner(
        runner_id=f"agent_{pattern_id}_{PRESET_ID}",
        mode="agent",
        collection=COLLECTION,
        agent_config={
            "pattern_id": pattern_id,
            "profile_id": RETRIEVE_PROFILE,
            "index_profile_id": INDEX_PROFILE_ID,
            "enable_web_search": False,
        },
        rag_config={"profile_id": RETRIEVE_PROFILE, "top_k": RAG_TOP_K},
    )


_CATALOG: list[EvalRunner] = [
    _rag_runner(),
    *[_agent_runner(pattern) for pattern in _WAVE1_PATTERNS],
]
DEFAULT_RUNNERS: list[EvalRunner] = [_CATALOG[0]]


def known_runner_ids() -> list[str]:
    """``runner_id`` values in catalog order."""
    return [runner["runner_id"] for runner in _CATALOG]


def resolve_runners(runner_ids: list[str] | None) -> list[EvalRunner]:
    """Select catalog arms. Empty / None → the default RAG arm."""
    catalog = {runner["runner_id"]: runner for runner in _CATALOG}
    if not runner_ids:
        return list(DEFAULT_RUNNERS)
    missing = [runner_id for runner_id in runner_ids if runner_id not in catalog]
    if missing:
        known = ", ".join(known_runner_ids())
        raise SystemExit(f"Unknown --runner {missing}. Known: {known}")
    return [catalog[runner_id] for runner_id in runner_ids]
