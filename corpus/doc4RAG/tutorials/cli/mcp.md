---
title: "openclaw mcp"
sidebarTitle: "mcp"
---

# `openclaw mcp`

`mcp` 有两类用途：让 OpenClaw 作为 MCP server 暴露会话能力，或者管理 OpenClaw 运行时可能使用的 MCP server 定义。

```bash
openclaw mcp serve
openclaw mcp list
openclaw mcp set <name> <command>
```

## 什么时候用

- 想让 Codex、Claude Code 或其他 MCP 客户端连接 OpenClaw 会话。
- 想管理一组外部 MCP server。
- 开发工具链需要通过标准 MCP 协议读写会话。

## 新手提醒

如果你只是想聊天或打开控制台，不需要 MCP。
MCP 更像“工具之间的插座”，适合开发者把多个系统接在一起。

继续阅读：[MCP 与 OpenClaw](/tutorials/concepts/openclaw-sdk)。
