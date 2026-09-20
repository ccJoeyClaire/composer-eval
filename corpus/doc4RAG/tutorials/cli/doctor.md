---
title: "openclaw doctor"
sidebarTitle: "doctor"
---

# `openclaw doctor`

`doctor` 是 OpenClaw 的体检命令。你可以把它当成“先别猜，先检查”的按钮。

```bash
openclaw doctor
openclaw doctor --deep
openclaw doctor --fix
openclaw doctor --generate-gateway-token
```

安装后、升级后、出问题时，都先跑它。

## 它会检查什么

- 配置文件是不是合法。
- Gateway 服务是否安装、启动、可访问。
- 通道 token、allowlist、配对、账号状态是否可疑。
- 插件是否缺失、无效或配置坏了。
- 沙箱、记忆、模型、SecretRef 是否准备好。

## 新手最稳流程

```bash
openclaw doctor
```

先读输出。如果它建议修复，再运行：

```bash
openclaw doctor --fix
```

如果是在服务器或无人值守环境里，可以用：

```bash
openclaw doctor --fix --non-interactive
```

## 重要提醒

`doctor --fix` 会修改配置前备份。它适合修复常见问题，但不应该代替你理解高风险改动。看到 Gateway token、公网暴露、插件权限这类提示时，要认真看。

继续阅读：[Gateway 故障排查](/tutorials/gateway/troubleshooting)。
