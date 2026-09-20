---
title: "openclaw sessions"
sidebarTitle: "sessions"
---

# `openclaw sessions`

`sessions` 用来查看已经保存的会话记录。会话记录是“聊过什么、什么时候活跃过”的账本，不等于通道是否在线。

```bash
openclaw sessions
openclaw sessions --limit 200
openclaw sessions --json
```

## 什么时候用

- 想找最近的对话记录。
- 想确认某个 Agent 或通道有没有产生会话。
- 想把会话列表交给脚本处理。

## 不要误用

不要用 `sessions` 判断 Discord、Telegram、Slack 是否在线。安静的通道可能已经连上了，但还没有产生新会话。

检查通道在线状态请用：

```bash
openclaw channels status --probe
openclaw status --deep
```

会话里可能有敏感上下文，导出或分享前先确认目的和权限。
