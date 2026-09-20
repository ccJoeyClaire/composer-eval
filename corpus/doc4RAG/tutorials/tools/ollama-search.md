---
title: "Ollama Web Search"
sidebarTitle: "Ollama 搜索"
---

# Ollama Web Search：用 Ollama 做网页搜索

OpenClaw 可以把 Ollama Web Search 作为 `web_search` 提供商。它既可以接本地或自托管 Ollama，也可以接 hosted Ollama API。

---

## 前提

本地模式通常需要：

- Ollama 正在运行。
- OpenClaw 能访问 Ollama host。
- 已执行 `ollama signin`。

Hosted 模式需要：

- `https://ollama.com` base URL。
- `OLLAMA_API_KEY`。

---

## 配置本地 Ollama

如果你已经用 Ollama 跑本地模型，OpenClaw 可以复用同一个 host：

```json5
{
  models: {
    providers: {
      ollama: {
        baseUrl: "http://127.0.0.1:11434"
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "ollama"
      }
    }
  }
}
```

---

## 选择搜索提供商

```bash
openclaw configure --section web
```

选择 Ollama Web Search。

---

## 注意事项

- 本地 host 默认是 `http://127.0.0.1:11434`。
- 如果你的 Ollama host 需要认证，OpenClaw 会复用 Ollama provider 的 API Key。
- 如果配置的是 `https://ollama.com`，需要真实 `OLLAMA_API_KEY`。
- 如果本地 host 不支持 web search，但环境里有 hosted key，OpenClaw 可以回退到 hosted API。

---

## 继续阅读

- [Ollama 提供商](/tutorials/providers/ollama)
- [Web 网络工具](/tutorials/tools/web)
- [SearXNG 搜索](/tutorials/tools/searxng-search)

