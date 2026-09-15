"""On-disk layout for the eval harness (under ``eval/data/``)."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "config"
RAG_CONFIG_PATH = CONFIG_DIR / "arg_config.yaml"
AGENT_CONFIG_PATH = CONFIG_DIR / "agent_arg_config.yaml"

EVAL_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = EVAL_ROOT / "data"

GOLD_DIR = DATA_ROOT / "gold"
QA_EXPORTS_DIR = DATA_ROOT / "qa_exports"
INFER_DIR = DATA_ROOT / "infer"
RAGCHECKER_DIR = DATA_ROOT / "ragchecker"

DEFAULT_QA_EXPORT = "eval-datasets-1783174091039.json"


def gold_path(name: str = "samples.json") -> Path:
    """QA generator output: ``list[GoldSample]``."""
    return GOLD_DIR / name


def qa_export_path(name: str = DEFAULT_QA_EXPORT) -> Path:
    """Easy Dataset JSON export under ``eval/data/qa_exports/``."""
    return QA_EXPORTS_DIR / name


def infer_dir(runner_id: str) -> Path:
    """Root for one runner's infer artifacts (``agent/`` and ``rag/`` subdirs)."""
    return INFER_DIR / runner_id


def agent_infer_path(runner_id: str, query_id: str) -> Path:
    """``AgentInferArtifact`` JSON for one query."""
    return infer_dir(runner_id) / "agent" / f"{query_id}.json"


def rag_infer_path(runner_id: str, query_id: str) -> Path:
    """``RagInferArtifact`` JSON for one query."""
    return infer_dir(runner_id) / "rag" / f"{query_id}.json"


def ragchecker_input_path(runner_id: str) -> Path:
    """Assembled ``CheckerInput`` for one runner arm."""
    return RAGCHECKER_DIR / runner_id / "input.json"


def ragchecker_scores_path(runner_id: str) -> Path:
    """Aggregate RAGChecker metrics for one runner arm."""
    return RAGCHECKER_DIR / runner_id / "scores.json"


def ragchecker_checking_output_path(runner_id: str) -> Path:
    """Full RAGChecker dump (claims + checks) for one runner arm."""
    return RAGCHECKER_DIR / runner_id / "checking_outputs.json"


def ragchecker_llm_snapshot_path(runner_id: str) -> Path:
    """Per-request LLM debug dump (content / reasoning / finish_reason)."""
    return RAGCHECKER_DIR / runner_id / "llm_snapshots.jsonl"


def ensure_data_dirs() -> None:
    """Create artifact directories if missing."""
    for path in (GOLD_DIR, INFER_DIR, RAGCHECKER_DIR):
        path.mkdir(parents=True, exist_ok=True)
