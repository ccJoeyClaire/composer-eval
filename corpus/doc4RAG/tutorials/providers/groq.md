---
title: "Groq"
sidebarTitle: "Groq"
---

# Groq

Groq 以高速推理著称，适合追求快速回复的场景。

它通过 OpenAI-compatible API 接入，provider id 是 `groq`，环境变量是 `GROQ_API_KEY`。

配置：

```bash
export GROQ_API_KEY="..."
openclaw configure --section model
openclaw models list --provider groq
```

注意模型名要使用 Groq 支持的名称，不要把 OpenAI 或 Anthropic 的模型名直接搬过来。

## 什么时候选 Groq

- 你更在意回复速度。
- 你使用 Llama、Gemma、Mistral 等 Groq 支持的开源模型。
- 你想先低成本验证 Agent 工作流。

如果模型列表为空，先去 Groq 控制台确认 key 是否有效，再跑 `openclaw models status`。
