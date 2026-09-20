---
title: "Perplexity Search"
sidebarTitle: "Perplexity"
description: "OpenClaw 工具系统：Perplexity Search 可作为 web_search provider，支持结构化搜索或 Sonar/OpenRouter 兼容路径。"
---

# Perplexity Search

Perplexity 适合“帮我查并总结”的搜索。
它可以返回搜索结果，也可以通过 Sonar/OpenRouter 兼容路径返回带引用的 AI 综合答案。

---

## 获取 API Key

1. 打开 [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)。
2. 创建 API Key。
3. 放到 Gateway 环境：

```bash
PERPLEXITY_API_KEY=...
```

如果你走 OpenRouter Sonar 兼容路径，也可能使用：

```bash
OPENROUTER_API_KEY=...
```

---

## 原生 Search API 配置

```json5
{
  plugins: {
    entries: {
      perplexity: {
        config: {
          webSearch: {
            apiKey: "pplx-..."
          }
        }
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "perplexity"
      }
    }
  }
}
```

---

## 什么时候用

- 想要带引用的综合答案
- 想快速了解一个新主题
- 想让 Agent 先查再回答

如果你需要可控的原始搜索结果，Brave 或 Exa 可能更合适。

