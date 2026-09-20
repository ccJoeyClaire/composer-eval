---
title: "Brave Search"
sidebarTitle: "Brave Search"
description: "OpenClaw 工具系统：Brave Search 作为 web_search provider，适合返回结构化搜索结果。"
---

# Brave Search

Brave Search 适合做“给我几条网页结果”的搜索。
它返回标题、链接和摘要，比较直接，也容易控制成本。

---

## 获取 API Key

1. 打开 [brave.com/search/api](https://brave.com/search/api)。
2. 注册并创建 API Key。
3. 把 Key 放到 Gateway 环境里。

```bash
BRAVE_API_KEY=...
```

对于后台服务，建议写入：

```text
~/.openclaw/.env
```

---

## 配置

```json5
{
  tools: {
    web: {
      search: {
        provider: "brave"
      }
    }
  }
}
```

---

## 适合场景

- 查新闻、文档、网页列表
- 要原始链接而不是 AI 摘要
- 希望搜索结果可追溯
- 成本敏感

如果你想要网页正文抽取和语义搜索，可以看 [Exa Search](/tutorials/tools/exa-search)。

