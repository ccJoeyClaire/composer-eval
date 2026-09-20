---
title: "SearXNG Search"
sidebarTitle: "SearXNG 搜索"
---

# SearXNG Search：自托管的免费元搜索

SearXNG 是开源元搜索引擎。它可以聚合多个搜索来源，而且可以跑在你自己的机器或内网里。

对重视隐私、自托管和无 API Key 的用户很有吸引力。

---

## 什么时候选它？

适合：

- 想把搜索留在自己的网络里。
- 不想依赖商业搜索 API。
- 需要可控的内网搜索入口。
- 有 Docker 或服务器运维经验。

不适合：

- 完全不想维护服务。
- 想要商业 API 那种稳定 SLA。
- 不清楚 SearXNG 实例来源是否可信。

---

## 快速运行一个实例

本地测试：

```bash
docker run -d -p 8888:8080 searxng/searxng
```

然后配置 OpenClaw：

```bash
export SEARXNG_BASE_URL="http://localhost:8888"
openclaw configure --section web
```

选择 SearXNG。

---

## 配置示意

```json5
{
  tools: {
    web: {
      search: {
        provider: "searxng"
      }
    }
  },
  plugins: {
    entries: {
      searxng: {
        config: {
          webSearch: {
            baseUrl: "http://localhost:8888",
            categories: "general,news",
            language: "zh"
          }
        }
      }
    }
  }
}
```

---

## 网络安全

公共地址请使用 HTTPS。
内网 HTTP 只适合你明确信任的私有网络或本机。

不要随便使用陌生人提供的 SearXNG 实例来搜索敏感内容。

---

## 继续阅读

- [Web 网络工具](/tutorials/tools/web)
- [DuckDuckGo 搜索](/tutorials/tools/duckduckgo-search)
- [Ollama Web Search](/tutorials/tools/ollama-search)

