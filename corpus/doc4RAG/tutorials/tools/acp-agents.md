---
title: "ACP Agents"
sidebarTitle: "ACP Agents"
---

# ACP Agents：把外部编码助手接进 OpenClaw

ACP 是 Agent Client Protocol。OpenClaw 可以通过 ACP 后端运行外部编码 harness，比如 Claude Code、Gemini CLI、Codex ACP、OpenCode、Cursor 等。

这不是新手默认路线。默认 Agent 能用就先不用 ACP。

---

## 什么时候需要 ACP？

适合：

- 你已经在用某个外部编码 CLI。
- 想把聊天会话绑定到一个长期编码会话。
- 想通过 `/acp` 命令创建、查看、引导外部 Agent。
- 做多 Agent 或开发工具集成。

不适合：

- 只是想在控制 UI 里普通聊天。
- 只是想用默认 Codex runtime。
- 没有在 Gateway 主机上安装对应外部工具。

---

## 安装 acpx 插件

```bash
openclaw plugins install @openclaw/acpx
openclaw config set plugins.entries.acpx.enabled true
```

然后检查：

```text
/acp doctor
```

---

## 常见 harness id

可能包括：

| id | 说明 |
|----|------|
| `claude` | Claude Code |
| `codex` | Codex ACP 适配 |
| `gemini` | Gemini CLI |
| `cursor` | Cursor CLI |
| `opencode` | OpenCode |
| `openclaw` | OpenClaw ACP bridge |
| `qwen` | Qwen Code / CLI |

具体可用列表取决于 acpx 插件版本和本机环境。

---

## 基本流程

```text
/acp doctor
/acp spawn codex
/acp steer --session <session-id> focus on tests
```

每个 ACP session 会作为后台任务追踪。

---

## 继续阅读

- [ACP Agents 设置](/tutorials/tools/acp-agents-setup)
- [Agent 运行时](/tutorials/concepts/agent-runtimes)
- [任务自动化](/tutorials/automation/tasks)

