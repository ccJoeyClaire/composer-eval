---
title: "Kimi Search"
sidebarTitle: "Kimi 搜索"
---

# Kimi Search：用 Moonshot/Kimi 做带引用搜索

OpenClaw 可以用 Kimi 作为 `web_search` 提供商，通过 Moonshot 的网页搜索能力返回带引用的答案。

---

## API Key

你可以使用：

- `KIMI_API_KEY`
- `MOONSHOT_API_KEY`

设置到 Gateway 环境：

```bash
export KIMI_API_KEY="sk-..."
```

或者放到：

```text
~/.openclaw/.env
```

---

## 国际站和中国站

Moonshot 有不同 API host。常见：

```text
https://api.moonshot.ai/v1
https://api.moonshot.cn/v1
```

如果你的 key 来自中国站，就要注意 base URL 不要打到国际站，否则可能 401。

---

## 配置示意

```json5
{
  plugins: {
    entries: {
      moonshot: {
        config: {
          webSearch: {
            apiKey: "sk-...",
            baseUrl: "https://api.moonshot.cn/v1",
            model: "kimi-k2.6"
          }
        }
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "kimi"
      }
    }
  }
}
```

---

## 如果返回“不能联网”怎么办？

OpenClaw 会检查 Kimi 是否真的返回了搜索证据。
如果模型只是普通聊天回答“我不能联网”，OpenClaw 会把它当作未落地搜索，而不是假装搜索成功。

解决方式：

- 重试更明确的问题。
- 换 Brave、Exa、Tavily 等结构化搜索。
- 已知 URL 时使用 `web_fetch`。

---

## 继续阅读

- [Web 网络工具](/tutorials/tools/web)
- [Gemini Search](/tutorials/tools/gemini-search)
- [Grok Search](/tutorials/tools/grok-search)

