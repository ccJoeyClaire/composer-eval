"""OpenAI SDK client for RAGChecker (DeepSeek-flash via LLM_*).

RAGChecker calls ``custom_llm_api_func`` synchronously and in large batches.
OpenAI chat has no native batch API, so each batch is issued concurrently
with ``asyncio`` (as the official docs recommend). The async client is
created and closed inside the same ``asyncio.run`` so Windows does not
hit a closed event loop on teardown.
"""

from __future__ import annotations

import asyncio
import json
import os
import threading
from pathlib import Path
from typing import Any

from openai import AsyncOpenAI

DEFAULT_MODEL_ID = "deepseek-flash"
_PREVIEW_CHARS = 400
_REASONING_SNAPSHOT_CHARS = 8000


def _preview(text: str | None, limit: int = _PREVIEW_CHARS) -> str:
    if not text:
        return ""
    normalized = text.replace("\r\n", "\n")
    if len(normalized) <= limit:
        return normalized
    return normalized[:limit] + f"... <{len(normalized) - limit} more chars>"


def _reasoning_of(message: Any) -> str | None:
    value = getattr(message, "reasoning_content", None)
    if value:
        return str(value)
    extra = getattr(message, "model_extra", None)
    if isinstance(extra, dict) and extra.get("reasoning_content"):
        return str(extra["reasoning_content"])
    return None


class LLMClient:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        timeout: int | None = None,
        max_tokens: int = 2000,
        max_concurrency: int = 4,
        snapshot_path: Path | None = None,
    ) -> None:
        self.model = model or os.environ.get("LLM_MODEL_ID") or DEFAULT_MODEL_ID
        api_key = api_key or os.environ.get("LLM_API_KEY")
        base_url = base_url or os.environ.get("LLM_BASE_URL")
        if not all([self.model, api_key, base_url]):
            raise ValueError("必须同时拥有模型名称、API密钥和基础url")

        self._client_kwargs: dict[str, Any] = {
            "api_key": api_key,
            "base_url": base_url,
        }
        if timeout is not None:
            self._client_kwargs["timeout"] = timeout

        self.max_tokens = max_tokens
        self.max_concurrency = max(1, max_concurrency)
        self.snapshot_path = snapshot_path
        self._snapshot_lock = threading.Lock()
        self._request_seq = 0

    def _next_seq(self) -> int:
        with self._snapshot_lock:
            self._request_seq += 1
            return self._request_seq

    def _append_snapshot(self, row: dict[str, Any]) -> None:
        if self.snapshot_path is None:
            return
        line = json.dumps(row, ensure_ascii=False)
        with self._snapshot_lock:
            with self.snapshot_path.open("a", encoding="utf-8") as handle:
                handle.write(line + "\n")

    async def _arequest(
        self,
        client: AsyncOpenAI,
        prompt: str,
        max_tokens: int,
        seq: int,
    ) -> str:
        print(
            f"[RAGChecker LLM] request#{seq} start prompt_len={len(prompt)} "
            f"max_tokens={max_tokens} model={self.model} thinking=disabled",
            flush=True,
        )
        try:
            # deepseek-flash turns thinking on by default (effort=high).
            # CoT fills max_tokens and leaves message.content empty.
            response = await client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0,
                extra_body={"thinking": {"type": "disabled"}},
            )
        except Exception as exc:
            print(f"[RAGChecker LLM] request#{seq} ERROR {type(exc).__name__}: {exc}", flush=True)
            self._append_snapshot(
                {
                    "seq": seq,
                    "ok": False,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                    "prompt_len": len(prompt),
                    "prompt_preview": _preview(prompt, 200),
                }
            )
            raise

        choice = response.choices[0]
        message = choice.message
        content = message.content
        reasoning = _reasoning_of(message)
        usage = response.usage
        usage_dump: dict[str, Any] = {}
        if usage is not None:
            usage_dump = {
                "prompt_tokens": getattr(usage, "prompt_tokens", None),
                "completion_tokens": getattr(usage, "completion_tokens", None),
                "total_tokens": getattr(usage, "total_tokens", None),
            }
            details = getattr(usage, "completion_tokens_details", None)
            if details is not None:
                usage_dump["reasoning_tokens"] = getattr(details, "reasoning_tokens", None)

        returned = str(content or "")
        print(
            f"[RAGChecker LLM] request#{seq} done finish={choice.finish_reason} "
            f"content_is_none={content is None} content_len={len(returned)} "
            f"reasoning_len={0 if reasoning is None else len(reasoning)} "
            f"usage={usage_dump}",
            flush=True,
        )
        print(
            f"[RAGChecker LLM] request#{seq} content_preview={_preview(returned, 240)!r}",
            flush=True,
        )
        self._append_snapshot(
            {
                "seq": seq,
                "ok": True,
                "model": self.model,
                "finish_reason": choice.finish_reason,
                "content_is_none": content is None,
                "content_len": len(returned),
                "content": returned,
                "reasoning_is_none": reasoning is None,
                "reasoning_len": 0 if reasoning is None else len(reasoning),
                "reasoning_preview": _preview(reasoning, _REASONING_SNAPSHOT_CHARS),
                "refusal": getattr(message, "refusal", None),
                "usage": usage_dump,
                "prompt_len": len(prompt),
                "prompt_preview": _preview(prompt, 200),
            }
        )
        return returned

    async def _acomplete_batch(
        self,
        prompts: list[str],
        max_tokens: int,
        max_concurrency: int,
    ) -> list[str]:
        client = AsyncOpenAI(**self._client_kwargs)
        sem = asyncio.Semaphore(max_concurrency)
        try:

            async def _one(prompt: str) -> str:
                seq = self._next_seq()
                async with sem:
                    return await self._arequest(client, prompt, max_tokens, seq)

            return list(await asyncio.gather(*[_one(p) for p in prompts]))
        finally:
            await client.close()

    def complete_batch(
        self,
        prompts: list[str],
        *,
        max_tokens: int | None = None,
        max_concurrency: int | None = None,
    ) -> list[str]:
        """Sync RAGChecker entry: run one batch concurrently via asyncio."""
        n = len(prompts)
        tokens = max_tokens or self.max_tokens
        workers = max(1, max_concurrency or self.max_concurrency)
        try:
            asyncio.get_running_loop()
            loop_running = True
        except RuntimeError:
            loop_running = False
        print(
            f"[RAGChecker LLM] complete_batch enter n={n} max_tokens={tokens} "
            f"concurrency={workers} loop_running={loop_running}",
            flush=True,
        )
        texts = asyncio.run(
            self._acomplete_batch(
                prompts,
                max_tokens=tokens,
                max_concurrency=workers,
            )
        )
        lengths = [len(text) for text in texts]
        empty = sum(1 for text in texts if not text.strip())
        print(
            f"[RAGChecker LLM] complete_batch exit n={len(texts)} lens={lengths} "
            f"empty={empty}/{len(texts)}",
            flush=True,
        )
        return texts

    def close(self) -> None:
        """No long-lived HTTP client; batches open/close their own."""
        print("[RAGChecker LLM] close()", flush=True)
