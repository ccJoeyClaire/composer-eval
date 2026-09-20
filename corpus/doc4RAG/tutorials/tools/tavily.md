---
title: "Tavily"
sidebarTitle: "Tavily 搜索"
---

# Tavily：面向 AI 的搜索和网页提取

Tavily 是一个搜索 API，返回的结果更适合给 AI 阅读。OpenClaw 可以把 Tavily 当作 `web_search` 提供商，也可以直接使用 Tavily 插件工具。

---

## 它能做什么？

两类能力：

| 工具 | 用途 |
|------|------|
| `web_search` | 普通统一搜索入口 |
| `tavily_search` | 使用 Tavily 的深度、主题、域名过滤等高级搜索 |
| `tavily_extract` | 从一个或多个 URL 提取正文 |

---

## 获取 API Key

1. 打开 Tavily 官网。
2. 创建账号。
3. 在控制台生成 API Key。
4. 放到 Gateway 环境变量：

```bash
export TAVILY_API_KEY="tvly-..."
```

---

## 配置

```json5
{
  plugins: {
    entries: {
      tavily: {
        enabled: true,
        config: {
          webSearch: {
            apiKey: "tvly-..."
          }
        }
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "tavily"
      }
    }
  }
}
```

也可以通过：

```bash
openclaw configure --section web
```

选择 Tavily。

---

## 什么时候用 tavily_extract？

当你已经知道 URL，只想读页面内容时，用 extract 更合适。

比如：

```text
请用 tavily_extract 读取这 3 个产品页，并比较价格和限制。
```

如果只是“不知道去哪找”，先用 search。

---

## 继续阅读

- [Web 网络工具](/tutorials/tools/web)
- [Web Fetch](/tutorials/tools/web-fetch)
- [Firecrawl](/tutorials/tools/firecrawl)

