"""Direct RAG + LLM infer for ``EvalRunner(mode='rag')``."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from agent.messages import format_rag_chunks_for_llm
from eval.base import EvalRunner, GoldSample, RagInferArtifact
from eval.harness.paths import RAG_CONFIG_PATH
from llm.client import LLMClient
from rag.build import build_RAG_retriever
from rag.config import get_rag_config, get_retrieve_profile
from rag.core import RAGRetriever
from rag.serialize import chunk_to_tool_record, trace_to_record

_REPO_ROOT = Path(__file__).resolve().parents[3]

_RAG_INFER_SYSTEM_PROMPT = (
    "你是一个 AI 助手。\n"
    "根据用户提供的参考文档回答用户问题；仅依据给定证据作答，证据不足时如实说明。"
)


async def run_rag_infer(
    runner: EvalRunner,
    gold: list[GoldSample],
) -> list[RagInferArtifact]:
    """Retrieve with ``gold_query``, generate with ``user_question`` + context.

    Builds a retriever from ``runner.collection`` and ``runner.rag_config``,
    runs ``aquery_trace`` per gold row (see ``get_start.retrieve_example``),
    then calls ``LLMClient`` once with retrieved chunks injected as a tool
    result — no agent graph.
    """
    rag_cfg = runner["rag_config"]
    profile_id = str(rag_cfg["profile_id"])
    rag_config = get_rag_config(RAG_CONFIG_PATH)
    retrieve_profile = get_retrieve_profile(rag_config, profile_id)
    top_k = int(rag_cfg.get("top_k") or rag_config.retriever.top_k)

    retriever = build_RAG_retriever(
        runner["collection"],
        use_reranker=retrieve_profile.use_reranker,
        use_contextual=retrieve_profile.use_contextual,
        use_hyde=retrieve_profile.use_hyde,
        use_small_to_big=retrieve_profile.use_small_to_big,
    )
    llm = LLMClient()
    artifacts: list[RagInferArtifact] = []

    try:
        for sample in gold:
            gold_query = sample["gold_query"]
            user_question = sample["user_question"]
            result = await retriever.aquery_trace(gold_query, top_k=top_k)
            trace = trace_to_record(result, top_k=top_k)
            context_text = format_rag_chunks_for_llm(
                [chunk_to_tool_record(chunk) for chunk in result.chunks]
            )
            messages = _rag_infer_messages(
                user_question=user_question,
                context_text=context_text,
            )
            response = await llm.arequest_llm(messages, tool_calls=False)
            artifacts.append(
                RagInferArtifact(
                    query_id=sample["query_id"],
                    user_question=user_question,
                    gold_query=gold_query,
                    trace=trace,
                    generator_response=str(response.content or "").strip(),
                )
            )
    finally:
        await llm.aclose()
        await _close_retriever_store(retriever)

    return artifacts


def _rag_infer_messages(
    *,
    user_question: str,
    context_text: str,
) -> list[dict[str, Any]]:
    """OpenAI chat messages: user question plus retrieved passages."""
    user_content = user_question
    if context_text.strip():
        user_content = (
            f"{user_question}\n\n"
            "以下是检索到的参考文档：\n"
            f"{context_text}"
        )
    return [
        {"role": "system", "content": _RAG_INFER_SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]


async def _close_retriever_store(retriever: RAGRetriever) -> None:
    chain = retriever.retriever
    store = getattr(chain, "store", None) or getattr(
        getattr(chain, "inner", None), "store", None
    )
    if store is not None:
        await store.aclose()


if __name__ == "__main__":
    from eval.harness.extract import load_gold
    from eval.harness.paths import ensure_data_dirs, rag_infer_path

    runner = EvalRunner(
        runner_id="rag_rerank_hyde",
        mode="rag",
        collection="getstart_codex_baseline",
        agent_config={},
        rag_config={
            "profile_id": "rerank_hyde",
            "top_k": 10,
        },
    )
    load_dotenv(_REPO_ROOT / ".env")
    ensure_data_dirs()
    gold_samples = load_gold()
    artifacts = asyncio.run(run_rag_infer(runner, gold_samples))
    for artifact in artifacts:
        path = rag_infer_path(runner["runner_id"], artifact["query_id"])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(artifact, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"query_id={artifact['query_id']} -> {path}")
