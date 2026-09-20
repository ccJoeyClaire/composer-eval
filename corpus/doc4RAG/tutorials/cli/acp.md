---
title: "openclaw acp"
sidebarTitle: "acp"
---

# `openclaw acp`

`acp` 用来运行 Agent Client Protocol bridge。简单说，它让 IDE 或支持 ACP 的客户端通过标准协议把请求转发到 OpenClaw Gateway。

```bash
openclaw acp
openclaw acp --url wss://gateway-host:18789 --token <token>
```

## 什么时候用

- IDE 或 ACP 客户端要连接 OpenClaw。
- 想把编辑器会话路由进 Gateway。
- 调试 ACP session 和 Gateway session 的映射。

## 不要混淆

`openclaw acp` 是 OpenClaw 对外提供 ACP bridge。
[ACP Agents](/tutorials/tools/acp-agents) 是 OpenClaw 去启动 Codex、Claude Code 等外部 harness。
