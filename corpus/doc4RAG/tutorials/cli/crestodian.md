---
title: "openclaw crestodian"
sidebarTitle: "crestodian"
---

# `openclaw crestodian`

`crestodian` 是 OpenClaw 的本地设置、修复和配置助手。它的设计目标是：即使普通 Agent 路径坏了，也还有一个本地入口能帮你检查和修复。

```bash
openclaw
openclaw crestodian
openclaw crestodian --message "validate config"
```

## 什么时候用

- 直接运行 `openclaw`，想进入本地修复助手。
- 配置坏了，普通对话入口起不来。
- 想用一句话让本地助手帮你检查模型、Gateway、配置。
- 维护者在源码 checkout 中排查环境。

## 新手提醒

你平时不需要主动记住它。遇到“OpenClaw 起不来、dashboard 也打不开”的时候，可以把它当成备用维修入口。

先试：

```bash
openclaw crestodian --message "health"
```
