---
title: "openclaw tui"
sidebarTitle: "tui"
---

# `openclaw tui`

`tui` 打开终端界面。它适合 SSH、服务器环境，或者喜欢在终端里聊天和排障的用户。

新手先用 `openclaw dashboard`。

```bash
openclaw tui
```

## 什么时候用

- 服务器没有浏览器。
- 你通过 SSH 管理 OpenClaw。
- 想在终端里查看状态、输入命令、和 Agent 对话。

## 新手建议

如果你在本机使用，先用：

```bash
openclaw dashboard
```

如果 dashboard 打不开，再用 TUI 作为备用入口。

## 和 dashboard 的区别

Dashboard 更适合点选和总览；TUI 更适合 SSH 和纯终端。
两者都连接 Gateway，所以如果 Gateway 本身没启动，两个界面都会出问题。
