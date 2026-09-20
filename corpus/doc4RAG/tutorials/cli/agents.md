---
title: "openclaw agents"
sidebarTitle: "agents"
---

# `openclaw agents`

`agents` 用来管理多个 Agent。每个 Agent 可以有自己的工作区、模型、技能、身份和通道路由。

```bash
openclaw agents list
openclaw agents add work --workspace ~/.openclaw/workspace-work
openclaw agents bindings
openclaw agents bind --agent work --bind telegram:ops
```

## 什么时候用

- 想把“工作助手”和“生活助手”分开。
- 不同通道消息要路由给不同 Agent。
- 不同 Agent 使用不同模型、技能或工作区。

## 新手建议

先跑通默认 Agent，再加第二个。多 Agent 能力很强，但配置面也更大。
加完以后检查：

```bash
openclaw agents list --bindings
openclaw doctor
```

## 常见坑

多 Agent 不是多开几个名字而已。你还要想清楚：

- 哪个通道消息归哪个 Agent。
- 每个 Agent 的工作区在哪里。
- 技能和模型是否继承默认配置。
- 是否需要单独的权限边界。
