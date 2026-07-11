"""Batch agent-graph infer for ``EvalRunner(mode='agent')``."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from agent.output import OutputState
from agent.pattern.common import RequestConfig, build_run
from eval.base import AgentInferArtifact, EvalRunner, GoldSample
from eval.harness.extract import strip_think_action_fences
from eval.harness.paths import AGENT_CONFIG_PATH

_GETSTART_COLLECTION_PREFIX = "getstart_codex_"
_REPO_ROOT = Path(__file__).resolve().parents[3]


async def run_agent_infer(
    runner: EvalRunner,
    gold: list[GoldSample],
) -> list[AgentInferArtifact]:
    """Invoke ``user_question`` for each gold row (see ``get_start.agent_example``).

    Builds the agent graph from ``runner.agent_config`` and ``runner.collection``,
    runs ``graph.ainvoke`` per gold row, and returns artifacts whose ``run``
    metadata includes ``retrieved_context`` and a ``final_message`` with
    Think/Action fences stripped from the answer text.
    """
    agent_cfg = runner["agent_config"]
    collection = runner["collection"]
    prefix = _GETSTART_COLLECTION_PREFIX
    if not collection.startswith(prefix):
        raise ValueError(
            f"collection {collection!r} must start with {prefix!r} "
            "to derive index_profile_id"
        )
    index_profile_id = collection[len(prefix) :]

    request_config = RequestConfig(
        pattern_id=str(agent_cfg.get("pattern_id", "")),
        collection=collection,
        index_profile_id=index_profile_id,
        retrieve_profile_id=str(agent_cfg.get("profile_id", "")),
        enable_web_search=bool(agent_cfg.get("enable_web_search", False)),
        config_path=AGENT_CONFIG_PATH,
    )
    run = build_run(request_config)
    artifacts: list[AgentInferArtifact] = []

    try:
        for sample in gold:
            query = sample["user_question"]
            raw = await run.graph.ainvoke(
                {"messages": [HumanMessage(content=query)], "metadata": {}}
            )
            output = OutputState.from_state(
                raw,
                query=query,
                request_config=request_config,
            )
            record = output.to_record_schema()
            final = record.get("final_message")
            if final is not None:
                record["final_message"] = {
                    **final,
                    "content": strip_think_action_fences(
                        str(final.get("content") or "")
                    ),
                }

            artifacts.append(
                AgentInferArtifact(
                    query_id=sample["query_id"],
                    invoked_query=query,
                    run=record,
                )
            )
    finally:
        await run.aclose()

    return artifacts


if __name__ == "__main__":
    from eval.harness.extract import load_gold
    from eval.harness.paths import agent_infer_path, ensure_data_dirs

    runner = EvalRunner(
        runner_id="agent_self_rag_hyde",
        mode="agent",
        collection="getstart_codex_baseline",
        agent_config={
            "pattern_id": "self_rag",
            "profile_id": "rerank_hyde",
            "enable_web_search": False,
        },
        rag_config={
            "profile_id": "rerank_hyde",
            "top_k": 10,
        },
    )
    load_dotenv(_REPO_ROOT / ".env")
    ensure_data_dirs()
    gold_samples = load_gold()
    artifacts = asyncio.run(run_agent_infer(runner, gold_samples))
    for artifact in artifacts:
        path = agent_infer_path(runner["runner_id"], artifact["query_id"])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(artifact, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"query_id={artifact['query_id']} -> {path}")
