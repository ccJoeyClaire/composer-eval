---
title: "Grok Search"
sidebarTitle: "Grok 搜索"
---

# Grok Search：用 xAI 做带引用的网页搜索

OpenClaw 可以用 Grok 作为 `web_search` 提供商。它会通过 xAI 的 web-grounded responses 返回带引用的综合答案。

同一个 `XAI_API_KEY` 还可以用于 X 搜索能力。

---

## 获取 API Key

到 xAI 控制台创建 API Key，然后设置：

```bash
export XAI_API_KEY="xai-..."
```

Gateway 安装场景可以放到：

```text
~/.openclaw/.env
```

---

## 配置

```json5
{
  plugins: {
    entries: {
      xai: {
        config: {
          webSearch: {
            apiKey: "xai-..."
          }
        }
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "grok"
      }
    }
  }
}
```

也可以运行：

```bash
openclaw configure --section web
```

选择 Grok。

---

## 它和普通搜索有什么不同？

Grok 返回的不是一串传统搜索结果，而是一个综合回答，并带上引用。

所以：

- `query` 是核心参数。
- `count` 可能只作为兼容参数接受。
- 搜索耗时可能比普通搜索 API 更长。

---

## 什么时候用 x_search？

如果你要查 X 上的帖子、转发、回复、浏览量等，优先用 `x_search`，不要用宽泛的网页搜索。

---

## 继续阅读

- [Web 网络工具](/tutorials/tools/web)
- [Code Execution](/tutorials/tools/code-execution)
- [Gemini Search](/tutorials/tools/gemini-search)

