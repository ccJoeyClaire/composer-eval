---
title: "Chutes"
sidebarTitle: "Chutes"
---

# Chutes

Chutes 是可接入 OpenClaw 的模型/推理服务之一。适合已经在 Chutes 上部署或使用模型的用户。

OpenClaw 可通过 API key 或 OAuth 路线接入 Chutes。模型 ref 通常以 `chutes/` 开头。

基本步骤：

```bash
export CHUTES_API_KEY="..."
openclaw configure --section model
openclaw models list --provider chutes
```

如果它提供 OpenAI-compatible endpoint，也可以按 [自定义模型提供商](/tutorials/providers/custom) 配置 base URL 和模型名。

## 新手排查

如果模型列表和你在 Chutes 平台看到的不一样，可能是 discovery 失败后回落到了内置 catalog。先确认 key 有效，再看 `openclaw logs --follow`。
