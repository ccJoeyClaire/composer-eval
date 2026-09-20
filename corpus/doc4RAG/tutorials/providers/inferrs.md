---
title: "Inferrs"
sidebarTitle: "Inferrs"
---

# Inferrs

Inferrs 是可接入 OpenClaw 的模型服务之一。适合已经在 Inferrs 平台上管理模型的用户。

如果它暴露 OpenAI-compatible endpoint，就按自定义 provider 的方式理解：base URL、API Key、模型名三件事必须对应。

配置思路：

```bash
export INFERRS_API_KEY="..."
openclaw configure --section model
```

如果平台提供 OpenAI-compatible endpoint，可参考 [自定义模型提供商](/tutorials/providers/custom)。

## 新手排查

最常见问题是模型名和 endpoint 不属于同一个平台环境。先用平台自己的示例 curl 跑通，再复制 base URL 和模型名到 OpenClaw。
