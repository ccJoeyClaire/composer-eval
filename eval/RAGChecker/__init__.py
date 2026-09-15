"""Score extract-stage inputs with RAGChecker."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    run_checker: Callable[..., dict]
    run_checker_for_runner: Callable[..., dict]
    to_official_schema: Callable[..., dict]

__all__ = [
    "run_checker",
    "run_checker_for_runner",
    "to_official_schema",
]


def __getattr__(name: str) -> object:
    if name in {"run_checker", "run_checker_for_runner", "to_official_schema"}:
        from eval.RAGChecker.run import (
            run_checker,
            run_checker_for_runner,
            to_official_schema,
        )

        return {
            "run_checker": run_checker,
            "run_checker_for_runner": run_checker_for_runner,
            "to_official_schema": to_official_schema,
        }[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
