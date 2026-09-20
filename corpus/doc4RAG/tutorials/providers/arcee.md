---
title: "Arcee"
sidebarTitle: "Arcee"
---

# Arcee

Arcee 是可作为 OpenClaw 模型 provider 的服务之一，适合已经在 Arcee 平台上有模型或企业配置的用户。

新手配置顺序：

1. 在 Arcee 控制台准备 API Key。
2. 把 key 放进 Gateway 环境。
3. 在 `openclaw configure --section model` 中选择或填写 provider。
4. 用 WebChat 发一条测试消息。

如果请求失败，先检查 key、base URL、模型名和账单状态。
