---
title: "openclaw hooks"
sidebarTitle: "hooks"
---

# `openclaw hooks`

`hooks` 用来管理 Agent hooks。Hooks 能在关键生命周期点插入逻辑，比如 Gateway 启动、`/new`、`/reset`、会话保存等。

```bash
openclaw hooks list
openclaw hooks list --verbose
openclaw hooks info <name>
```

## 什么时候用

- 想看当前有哪些 hook。
- 某个 hook 没有触发，需要查是否 eligible。
- 想启用工作区 hook 或排查依赖缺失。

## 新手提醒

Hook 像“自动触发的小机关”。它很方便，但也可能改变流程。
如果你只是想扩展插件能力，先看插件 hooks；如果你想给 Agent 工作流加自动动作，再看 agent hooks。

继续阅读：[Hooks](/tutorials/plugins/hooks)。
