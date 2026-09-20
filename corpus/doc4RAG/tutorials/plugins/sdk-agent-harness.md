---
title: "Agent Harness SDK"
sidebarTitle: "Agent Harness"
---

# Agent Harness SDK

Agent Harness SDK 用于接入或扩展 Agent 运行时。它比普通工具插件更接近核心执行流程。

适合：

- Codex 风格 runtime。
- 外部 harness。
- 自定义 Agent 执行器。

先理解 [Agent 运行时](/tutorials/concepts/agent-runtimes)，再改 harness。

## 新手提醒

Harness 不是普通工具。它会影响 Agent 如何执行任务、如何使用文件、如何汇报进度、如何处理中断。

如果你只是想给 Agent 加一个 API，写 tool 插件就够了。只有需要接入新的 Agent runtime 时，才碰 harness。
