---
title: "ACP Agents Setup"
sidebarTitle: "ACP 设置"
---

# ACP Agents 设置：把外部 harness 跑起来

这一页是 [ACP Agents](/tutorials/tools/acp-agents) 的安装和配置补充。只有明确要走 ACP/acpx 路线时才需要读。

---

## 最小配置

示意：

```json5
{
  acp: {
    enabled: true,
    dispatch: {
      enabled: true
    },
    backend: "acpx",
    defaultAgent: "codex",
    allowedAgents: ["claude", "codex", "gemini", "opencode"],
    maxConcurrentSessions: 8
  }
}
```

`allowedAgents` 是安全阀。你允许哪些 harness，OpenClaw 才能调哪些。

---

## 先检查外部工具

ACP 只是桥。真正干活的是外部 harness。

所以要确认：

- 对应 CLI 已安装。
- CLI 在 Gateway 主机上能启动。
- Provider 登录或 API Key 已配置。
- 工作目录存在。
- 非交互环境下不会卡在权限弹窗。

---

## 权限模式

写代码、运行命令、改文件都可能需要权限。
如果 ACP session 在聊天通道里跑，用户无法点击本机弹窗，所以要配置适合 headless 运行的权限模式。

不要给所有外部 harness 无限制权限。
先小范围允许，再按需求扩大。

---

## MCP bridge

OpenClaw 的内置工具默认不会自动暴露给外部 ACP harness。
只有当你明确需要外部 harness 调用 OpenClaw 工具时，才启用对应 MCP bridge。

这一步很强，也更危险。新手先不用。

---

## 继续阅读

- [ACP Agents](/tutorials/tools/acp-agents)
- [执行审批](/tutorials/tools/exec-approvals)
- [高级执行审批](/tutorials/tools/exec-approvals-advanced)

