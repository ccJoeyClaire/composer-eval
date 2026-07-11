"""Convert Easy Dataset QA export rows into ``GoldSample`` gold set rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Literal, TypedDict, cast

from eval.base import GoldSample
from eval.harness.paths import gold_path, qa_export_path

GoldQuestionType = Literal["open_ended", "short_answer"]
DEFAULT_TYPES: frozenset[GoldQuestionType] = frozenset({"open_ended", "short_answer"})


class QaPairRow(TypedDict):
    """One row from an Easy Dataset JSON export."""

    questionType: str
    question: str
    options: str
    correctAnswer: str
    tags: str


def load_qa_pairs(path: Path | None = None) -> list[QaPairRow]:
    """Load QA rows from an Easy Dataset JSON export."""
    target = path or qa_export_path()
    payload = json.loads(target.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"QA export must be a JSON array: {target}")
    return cast(list[QaPairRow], payload)


def qa_pairs_to_gold(
    rows: list[QaPairRow],
    *,
    types: frozenset[GoldQuestionType] = DEFAULT_TYPES,
    query_id_prefix: str = "query",
    start_index: int = 1,
) -> list[GoldSample]:
    """Filter *rows* by question type and map to ``GoldSample`` records.

    ``user_question`` and ``gold_query`` both use the source ``question`` text
    because the export does not include a separate retrieval query.
    """
    samples: list[GoldSample] = []
    index = start_index
    for row in rows:
        if row["questionType"] not in types:
            continue
        question = row["question"].strip()
        samples.append(
            GoldSample(
                query_id=f"{query_id_prefix}_{index:03d}",
                user_question=question,
                gold_query=question,
                gt_answer=row["correctAnswer"].strip(),
            )
        )
        index += 1
    return samples


def write_gold(samples: list[GoldSample], path: Path) -> Path:
    """Write ``list[GoldSample]`` as UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(samples, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


if __name__ == "__main__":
    rows = load_qa_pairs()
    samples = qa_pairs_to_gold(rows)
    out = write_gold(samples, gold_path("codex_qa_samples.json"))
    print(f"extracted={len(samples)} -> {out}")
