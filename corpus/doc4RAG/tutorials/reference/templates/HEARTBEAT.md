---
title: "HEARTBEAT.md template"
---

# HEARTBEAT.md template

::: tip 先看人话
`HEARTBEAT.md` 是给 Agent 的“定时检查清单”。  
如果这个文件是空的，或者只有注释，Agent 就不会发起 heartbeat API 调用。
:::

最简单的理解：

- 没有定时任务：保持空文件。
- 想让 Agent 定期看一眼某件事：把任务写在这个文件里。
- 不要把密码、API Key、私人 Token 写进这里。

模板如下：

```markdown
# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.
```

## Related

- [Heartbeat config](/tutorials/gateway/config-agents)
