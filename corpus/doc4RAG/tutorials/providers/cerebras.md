---
title: "Cerebras"
sidebarTitle: "Cerebras"
---

# Cerebras

Cerebras 提供高速推理服务，适合追求低延迟或已经使用 Cerebras 平台的用户。

provider id 是 `cerebras`，API 是 OpenAI-compatible，环境变量是 `CEREBRAS_API_KEY`。

配置思路：

```bash
export CEREBRAS_API_KEY="..."
openclaw configure --section model
openclaw models list --provider cerebras
```

排查重点：

- API Key 是否有效。
- 模型名是否属于 Cerebras。
- 账号是否有对应模型权限。

## 新手提醒

Cerebras 的部分模型可能是 preview 或有下线计划。生产使用前，去 Cerebras 控制台确认模型仍然可用。
