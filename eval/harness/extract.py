"""Map infer artifacts + gold into ``CheckerSample`` rows."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Literal, cast

from agent.core.metadata.base import RETRIEVED_CONTEXT_KEY
from eval.base import (
    AgentInferArtifact,
    CheckerContextChunk,
    CheckerInput,
    CheckerSample,
    GoldSample,
    RagInferArtifact,
)
from eval.harness.paths import (
    gold_path,
    infer_dir,
    ragchecker_input_path,
)

_DOC_ID_SEP = "|"
_THINK_ACTION_FENCE = re.compile(
    r"```\s*\nThink:.*?```\s*\n?",
    re.DOTALL | re.IGNORECASE,
)


def load_gold(path: Path | None = None) -> list[GoldSample]:
    """Load ``list[GoldSample]`` from the default gold JSON (or *path*)."""
    target = path or gold_path()
    payload = json.loads(target.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Gold file must be a JSON array: {target}")
    return cast(list[GoldSample], payload)


def extract_runner(
    runner_id: str,
    gold: list[GoldSample],
    *,
    mode: Literal["agent", "rag"],
) -> CheckerInput:
    """Join on-disk infer artifacts with gold into one ``CheckerInput`` batch."""
    gold_by_id = {sample["query_id"]: sample for sample in gold}
    infer_root = infer_dir(runner_id) / mode
    if not infer_root.is_dir():
        raise FileNotFoundError(f"Infer directory not found: {infer_root}")

    results: list[CheckerSample] = []
    for path in sorted(infer_root.glob("*.json")):
        artifact = json.loads(path.read_text(encoding="utf-8"))
        query_id = str(artifact.get("query_id") or path.stem)
        if query_id not in gold_by_id:
            print(f"extract skip {path.name}: not in gold", flush=True)
            continue
        gold_row = gold_by_id[query_id]
        if mode == "agent":
            results.append(
                agent_artifact_to_checker_sample(
                    cast(AgentInferArtifact, artifact),
                    gold_row,
                )
            )
        else:
            results.append(
                rag_artifact_to_checker_sample(
                    cast(RagInferArtifact, artifact),
                    gold_row,
                )
            )

    if not results:
        raise ValueError(f"No infer artifacts under {infer_root}")

    return CheckerInput(results=results)


def write_checker_input(runner_id: str, checker_input: CheckerInput) -> Path:
    """Write assembled ``CheckerInput`` for one runner arm."""
    path = ragchecker_input_path(runner_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(checker_input, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def checker_doc_id(*, source: str, heading_path: str) -> str:
    """Stable chunk id for RAGChecker: ``source|heading_path``."""
    return f"{source}{_DOC_ID_SEP}{heading_path}"


def strip_think_action_fences(text: str) -> str:
    """Drop the leading fenced Think/Action block from agent final answers."""
    return _THINK_ACTION_FENCE.sub("", text, count=1).strip()


def agent_artifact_to_checker_sample(
    artifact: AgentInferArtifact,
    gold: GoldSample,
) -> CheckerSample:
    """Build one checker row from an agent infer dump + gold."""
    run = artifact["run"]
    metadata = run.get("metadata") or {}
    retrieved_context: list[CheckerContextChunk] = []
    raw_context = metadata.get(RETRIEVED_CONTEXT_KEY)
    context_items = raw_context if isinstance(raw_context, list) else []
    for item in context_items:
        if not isinstance(item, dict):
            continue
        source = str(item.get("source") or "")
        heading_path = str(item.get("heading_path") or "")
        content = str(item.get("content") or "")
        if content.startswith("Document:"):
            _header, _, body = content.partition("\n\n")
            text = body if body else content
        else:
            text = content
        retrieved_context.append(
            CheckerContextChunk(
                doc_id=checker_doc_id(source=source, heading_path=heading_path),
                text=text,
            )
        )

    final = run.get("final_message") or {}
    generator_response = strip_think_action_fences(str(final.get("content") or ""))

    return CheckerSample(
        query_id=artifact["query_id"],
        gold_question=gold["user_question"],
        gt_answer=gold["gt_answer"],
        generator_response=generator_response,
        retrieved_context=retrieved_context,
    )


def rag_artifact_to_checker_sample(
    artifact: RagInferArtifact,
    gold: GoldSample,
) -> CheckerSample:
    """Build one checker row from a RAG infer dump + gold."""
    stages = artifact["trace"].get("stages") or {}
    retrieved_context: list[CheckerContextChunk] = []
    for item in stages.get("final") or []:
        if not isinstance(item, dict):
            continue
        source = str(item.get("source") or "")
        heading_path = str(item.get("heading_path") or "")
        content = str(item.get("content") or "")
        header = item.get("contextual_header")
        if isinstance(header, str) and content.startswith(header):
            text = content[len(header) :].lstrip("\n")
        else:
            text = content
        retrieved_context.append(
            CheckerContextChunk(
                doc_id=checker_doc_id(source=source, heading_path=heading_path),
                text=text,
            )
        )

    return CheckerSample(
        query_id=artifact["query_id"],
        gold_question=gold["user_question"],
        gt_answer=gold["gt_answer"],
        generator_response=artifact["generator_response"],
        retrieved_context=retrieved_context,
    )


if __name__ == "__main__":
    from eval.harness.paths import ensure_data_dirs
    from eval.harness.runners import DEFAULT_RUNNERS

    ensure_data_dirs()
    gold = load_gold()
    for runner in DEFAULT_RUNNERS:
        runner_id = runner["runner_id"]
        mode = runner["mode"]
        checker_input = extract_runner(runner_id, gold, mode=mode)
        out = write_checker_input(runner_id, checker_input)
        print(
            f"runner_id={runner_id} mode={mode} "
            f"samples={len(checker_input['results'])} -> {out}"
        )
        for sample in checker_input["results"]:
            print(
                f"  {sample['query_id']}: "
                f"context_chunks={len(sample['retrieved_context'])} "
                f"response_chars={len(sample['generator_response'])}"
            )