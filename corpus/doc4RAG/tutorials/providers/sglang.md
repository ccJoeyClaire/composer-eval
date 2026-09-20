---
title: "SGLang"
sidebarTitle: "SGLang"
---

# SGLang

SGLang 是自托管推理服务路线，适合有服务器和显卡的团队。

基本思路：

1. 部署 SGLang server。
2. 确认它的 OpenAI-compatible endpoint。
3. 在 OpenClaw 中配置 base URL、模型名和可选 API Key。

如果你刚接触本地模型，先从 [Ollama](/tutorials/providers/ollama) 更容易。

## 新手提醒

SGLang 常见本地接口是 30000 端口的 `/v1` 服务。OpenClaw 把它当成 OpenAI-compatible provider 使用。

如果你的 SGLang server 不要求认证，也可以设置一个占位 key 方便 OpenClaw 发现模型：

```bash
export SGLANG_API_KEY="sglang-local"
```

排查时先访问 `/v1/models`，确认服务真的在跑。
