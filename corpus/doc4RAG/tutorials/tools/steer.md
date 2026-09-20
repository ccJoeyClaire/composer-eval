---
title: "Steer"
sidebarTitle: "Steer 引导"
---

# Steer：在 Agent 正忙时轻轻纠偏

`/steer` 用来给正在运行的任务追加指导。它不会新开一轮普通对话，而是把你的提示送到当前活跃 run 的下一个可接收边界。

---

## 什么时候用？

当 Agent 还在工作，你想补一句：

```text
/steer 这次补丁保持小一点，测试只加关键用例
```

或者：

```text
/tell 下一次调用工具前先总结当前判断
```

`/tell` 是常见别名。

---

## 它和普通消息不同

| 方式 | 作用 |
|------|------|
| 普通消息 | 可能按队列策略处理 |
| `/steer` | 明确引导当前活跃 run |
| `/queue steer` | 改变以后普通消息到来时的默认行为 |

如果当前会话没有活跃 run，`/steer` 不会自动启动新任务。

---

## 子任务和 ACP

如果要引导子智能体，用子智能体自己的命令。
如果要引导 ACP session，用 `/acp steer`。

顶层 `/steer` 只针对当前会话的活跃 run。

---

## 继续阅读

- [队列引导](/tutorials/concepts/queue-steering)
- [命令队列](/tutorials/concepts/queue)
- [ACP Agents](/tutorials/tools/acp-agents)

