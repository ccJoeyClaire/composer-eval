---
title: "openclaw agent"
sidebarTitle: "agent"
---

# `openclaw agent`

`agent` 用来从 CLI 发起一次 Agent 回合。它适合脚本触发、自动化任务和指定 Agent 执行一次明确工作。

```bash
openclaw agent --agent ops --message "Summarize logs"
openclaw agent --to +15555550123 --message "status update" --deliver
openclaw agent --session-id 1234 --message "continue"
```

## 什么时候用

- 脚本需要让 Agent 做一件事。
- 想指定某个 Agent，而不是走默认路由。
- 想把结果送回某个聊天通道。

## 新手提醒

至少要告诉它目标：`--agent`、`--to` 或 `--session-id`。
`--deliver` 表示把回复送回通道；不加时通常只在 CLI 输出里看结果。

新手先从 [Agent 是什么](/tutorials/concepts/agent) 开始。
