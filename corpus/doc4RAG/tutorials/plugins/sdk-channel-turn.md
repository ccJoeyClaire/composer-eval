---
title: "Channel Turn"
sidebarTitle: "Channel Turn"
---

# Channel Turn

Channel Turn 是一次通道消息进入 OpenClaw 后，被标准化、路由、处理和回复的过程。

通道插件要把不同平台的消息格式转换成 OpenClaw 能理解的结构，再把 Agent 回复转换回平台格式。

这层越稳，多通道体验越一致。

## 一次 Channel Turn 包含什么

1. 通道收到原始消息。
2. 插件把它变成 OpenClaw 标准消息。
3. Gateway 决定路由到哪个 Agent/session。
4. Agent 生成回复或工具调用。
5. 插件把回复翻译回平台消息。

任何一步失败，都可能表现为“机器人不回”。排查时要配合通道状态和日志。
