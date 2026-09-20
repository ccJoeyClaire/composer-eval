---
title: "DeepSeek"
sidebarTitle: "DeepSeek"
---

# DeepSeek

DeepSeek 适合中文、代码和性价比场景。OpenClaw 可以把它作为模型 provider 使用。

provider id 通常是 `deepseek`，环境变量是 `DEEPSEEK_API_KEY`。

常见配置：

```bash
export DEEPSEEK_API_KEY="..."
openclaw configure --section model
openclaw models list --provider deepseek
```

如果你用的是 OpenAI 兼容接口，也可以参考 [自定义模型提供商](/tutorials/providers/custom)。

## 新手提醒

DeepSeek 模型名更新较快。复制模型名时以 DeepSeek 控制台或 `openclaw models list --provider deepseek` 为准。
如果能连上但回复失败，检查账号额度、模型权限和 base URL。
