---
title: "DuckDuckGo Search"
sidebarTitle: "DuckDuckGo 搜索"
---

# DuckDuckGo Search：不用 API Key 的搜索兜底

OpenClaw 可以用 DuckDuckGo 作为 `web_search` 提供商。它最大的好处是不用 API Key。

但它不是官方 API，而是解析 DuckDuckGo 的非 JavaScript 搜索页面，所以稳定性不如正式搜索 API。

---

## 适合谁？

适合：

- 新手想先试试网页搜索。
- 不想申请 API Key。
- 轻量个人使用。
- 作为临时兜底。

不适合：

- 大量自动化搜索。
- 生产环境稳定依赖。
- 需要严格结构化结果。

---

## 配置

运行：

```bash
openclaw configure --section web
```

选择 DuckDuckGo。

配置示意：

```json5
{
  tools: {
    web: {
      search: {
        provider: "duckduckgo"
      }
    }
  }
}
```

---

## 可调选项

| 选项 | 说明 |
|------|------|
| `region` | 区域，比如 `us-en` |
| `safeSearch` | `strict`、`moderate` 或 `off` |
| `count` | 返回结果数量 |

---

## 风险提醒

DuckDuckGo 可能返回验证码、限制自动访问，或因为页面结构变化导致解析失败。

如果你要稳定使用，优先考虑 [Brave Search](/tutorials/tools/brave-search)、[Exa Search](/tutorials/tools/exa-search) 或 [Tavily](/tutorials/tools/tavily)。

---

## 继续阅读

- [Web 网络工具](/tutorials/tools/web)
- [Brave Search](/tutorials/tools/brave-search)
- [SearXNG 搜索](/tutorials/tools/searxng-search)

