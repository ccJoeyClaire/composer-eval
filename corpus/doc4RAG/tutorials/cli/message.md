---
title: "openclaw message"
sidebarTitle: "message"
---

# `openclaw message`

`message` 用来从 CLI 向聊天通道发送消息或执行通道动作。它适合脚本通知、自动化回执和管理员手动测试。

```bash
openclaw message send --channel telegram --target <chat-id> --message "hello"
openclaw message send --channel slack --target channel:<id> --message "done"
```

## 什么时候用

- 脚本跑完后给 Telegram/Slack 发通知。
- 想测试某个通道是否能发出消息。
- 自动化任务需要把结果送回指定聊天。

## 新手提醒

发送前确认三件事：

1. `--channel` 是哪个通道。
2. `--target` 是谁或哪个群。
3. 这个通道的凭据和权限是否已经配置。

不知道 target 怎么写时，先用：

```bash
openclaw directory peers list --channel <channel>
```
