---
title: "Exa Search"
sidebarTitle: "Exa Search"
description: "OpenClaw 工具系统：Exa Search 支持语义搜索、关键词搜索和内容抽取，适合研究型任务。"
---

# Exa Search

Exa 更像“会按意思找资料的搜索工具”。
它支持语义搜索、关键词搜索、混合搜索，还能返回正文、重点句子和摘要。

---

## 获取 API Key

1. 打开 [exa.ai](https://exa.ai/)。
2. 创建账号并生成 API Key。
3. 写入 Gateway 环境：

```bash
EXA_API_KEY=...
```

---

## 配置

```json5
{
  plugins: {
    entries: {
      exa: {
        config: {
          webSearch: {
            apiKey: "exa-..."
          }
        }
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "exa"
      }
    }
  }
}
```

---

## 常用搜索模式

| 模式 | 说明 |
|------|------|
| `auto` | Exa 自动选择 |
| `neural` | 按语义理解搜索 |
| `fast` | 更快的关键词搜索 |
| `deep` | 更深入 |
| `instant` | 最快 |

---

## 内容抽取

Exa 可以在搜索结果里直接带内容：

```js
await web_search({
  query: "transformer architecture explained",
  type: "neural",
  contents: {
    text: true,
    highlights: { numSentences: 3 },
    summary: true
  }
});
```

这适合研究、竞品分析、资料整理。

