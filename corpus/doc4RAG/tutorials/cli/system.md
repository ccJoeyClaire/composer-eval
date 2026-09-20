---
title: "openclaw system"
sidebarTitle: "system"
---

# `openclaw system`

`system` 是 Gateway 系统级辅助命令，常用于发送系统事件、控制 heartbeat、查看 presence。

普通用户先用 `openclaw doctor`。

```bash
openclaw system event --text "Check for urgent follow-ups" --mode now
openclaw system heartbeat last
openclaw system heartbeat enable
openclaw system presence
```

## 什么时候用

- 想手动触发一次系统事件。
- heartbeat 被暂停，需要重新开启。
- 想看 Gateway 当前知道哪些系统 presence。

## 新手提醒

`system event` 不等于普通聊天消息，它会进入系统事件通道，通常给 heartbeat 或运行时调度使用。不了解时不要拿它当日常聊天入口。
