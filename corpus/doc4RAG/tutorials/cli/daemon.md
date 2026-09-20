---
title: "openclaw daemon"
sidebarTitle: "daemon"
---

# `openclaw daemon`

`daemon` 是 Gateway 服务管理的旧入口。最新版文档更推荐看 `openclaw gateway`，但老脚本里还可能见到 `daemon`。

```bash
openclaw daemon status
openclaw daemon install
openclaw daemon restart
openclaw daemon stop
```

## 新手怎么选

第一次安装后台服务，仍然推荐：

```bash
openclaw onboard --install-daemon
```

日常管理更推荐：

```bash
openclaw gateway status
openclaw gateway restart
```

`daemon` 和 `gateway` 的服务命令大体指向同一件事：让 Gateway 在后台长期运行。

继续阅读：[Gateway 命令](/tutorials/cli/gateway)。

## 为什么还保留 daemon

一些老脚本和老文档还会写 `daemon`。OpenClaw 保留它是为了兼容。
新教程统一引导到 `gateway`，这样读者更容易理解“后台服务就是 Gateway 服务”。
