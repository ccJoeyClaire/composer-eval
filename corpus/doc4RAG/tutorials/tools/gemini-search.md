---
title: "Gemini Search"
sidebarTitle: "Gemini Search"
description: "OpenClaw 工具系统：Gemini Search 使用 Google Search grounding，为 web_search 提供带引用的综合答案。"
---

# Gemini Search

Gemini Search 使用 Google Search grounding。
它不是简单返回一排链接，而是让 Gemini 根据实时搜索结果生成带引用的答案。

---

## 获取 API Key

1. 打开 [Google AI Studio](https://aistudio.google.com/apikey)。
2. 创建 API Key。
3. 写入 Gateway 环境：

```bash
GEMINI_API_KEY=...
```

---

## 配置

```json5
{
  plugins: {
    entries: {
      google: {
        config: {
          webSearch: {
            model: "gemini-2.5-flash"
          }
        }
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "gemini"
      }
    }
  }
}
```

---

## 支持的常见参数

- `query`
- `freshness`
- `date_after`
- `date_before`

`count` 可能被接受为兼容参数，但 Gemini 通常返回一个综合答案，而不是严格的 N 条结果列表。

---

## 适合场景

- 想用 Google Search grounding
- 想要综合答案和引用
- 不想自己再抓取多个网页

