---
title: "MiniMax Search"
sidebarTitle: "MiniMax Search"
description: "OpenClaw 工具系统：MiniMax Search 通过 MiniMax Token Plan Search API 提供 web_search。"
---

# MiniMax Search

MiniMax Search 通过 MiniMax Token Plan Search API 提供搜索结果。
它适合已经在使用 MiniMax，或需要 CN/global 区域选择的用户。

---

## 凭证

常见环境变量：

```bash
MINIMAX_CODE_PLAN_KEY=...
MINIMAX_CODING_API_KEY=...
MINIMAX_OAUTH_TOKEN=...
MINIMAX_API_KEY=...
```

注意：普通 MiniMax 模型 API Key 不一定能用于 Token Plan Search。

---

## 配置

```json5
{
  plugins: {
    entries: {
      minimax: {
        config: {
          webSearch: {
            apiKey: "sk-cp-...",
            region: "global"
          }
        }
      }
    }
  },
  tools: {
    web: {
      search: {
        provider: "minimax"
      }
    }
  }
}
```

`region` 可选：

- `global`
- `cn`

---

## 适合场景

- 已经使用 MiniMax 账号或 OAuth
- 国内网络环境下需要 CN endpoint
- 想把模型和搜索都放在同一类服务里管理

