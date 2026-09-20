---
title: "Perplexity Provider"
sidebarTitle: "Perplexity Provider"
---

# Perplexity Provider

Perplexity 可以作为模型或搜索相关能力接入。这里讲 provider 侧，搜索工具另见 [Perplexity Search](/tutorials/tools/perplexity-search)。

如果你想让 Agent 用 Perplexity 当模型回答，配置 provider；如果你只是想让 Agent 搜网页，配置 Search 工具。

配置：

```bash
export PERPLEXITY_API_KEY="..."
openclaw configure --section model
openclaw models status
```

如果你的目标是网页搜索，请优先配置工具里的 Perplexity Search。

## 新手怎么选

- “让模型回答”：看本页。
- “让工具去搜索网页”：看 [Perplexity Search](/tutorials/tools/perplexity-search)。
- “两者都要”：分别配置 provider 和 tool，不要混为一个开关。
