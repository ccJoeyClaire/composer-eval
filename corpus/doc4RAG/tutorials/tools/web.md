---
title: "网络工具"
sidebarTitle: "网络工具"
description: "OpenClaw 工具系统：web_search 和 web_fetch，让 Agent 搜索最新信息、抓取网页，并按不同提供商选择 Brave、Exa、Perplexity、Gemini、MiniMax 等。"
---

# 网络工具

网络工具让 Agent 不只依赖模型训练时的旧知识。
它可以搜索网页、读取页面、整理资料，再把结果放进回复里。

OpenClaw 里常见两类能力：

- `web_search`：搜索网络，找到相关网页。
- `web_fetch`：抓取某个网页内容。

---

## 先怎么选

| 你想要什么 | 推荐 |
|------------|------|
| 便宜、直接的搜索结果 | [Brave Search](/tutorials/tools/brave-search) |
| 语义搜索、内容抽取、摘要 | [Exa Search](/tutorials/tools/exa-search) |
| AI 综合答案 + 引用 | [Perplexity Search](/tutorials/tools/perplexity-search) |
| Google Search grounding | [Gemini Search](/tutorials/tools/gemini-search) |
| MiniMax Token Plan 搜索 | [MiniMax Search](/tutorials/tools/minimax-search) |
| 页面抓取失败，需要浏览器级抓取 | [Firecrawl](/tutorials/tools/firecrawl) |

新手可以先选 Brave 或 Exa。
如果你更想要“带引用的综合答案”，再试 Perplexity 或 Gemini。

---

## 基本配置形状

```json5
{
  tools: {
    web: {
      search: {
        provider: "brave"
      },
      fetch: {
        enabled: true
      }
    }
  }
}
```

API Key 建议放到 `~/.openclaw/.env`，不要写进公开仓库。

```bash
BRAVE_API_KEY=...
EXA_API_KEY=...
PERPLEXITY_API_KEY=...
GEMINI_API_KEY=...
MINIMAX_CODE_PLAN_KEY=...
```

---

## 搜索和抓取有什么区别

搜索像问图书管理员：

> 有哪些网页可能讲这个主题？

抓取像把其中一本书拿出来读：

> 打开这个 URL，把正文拿回来。

很多任务需要两步一起用：先搜索，再抓取最相关的页面。

---

## 安全提醒

`web_fetch` 能访问 URL，所以要注意：

- 不要让 Agent 抓内部管理后台。
- 不要抓包含私密 Token 的 URL。
- 对大页面设置合理大小限制。
- 做研究时优先让 Agent 保留来源链接。
- 遵守目标网站的使用条款和 robots 规则。

如果页面需要登录，通常应该用 [浏览器工具](/tutorials/tools/browser) 的已登录会话，而不是让搜索工具硬抓。
