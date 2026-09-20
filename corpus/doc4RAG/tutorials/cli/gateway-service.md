---
title: "Gateway 服务命令"
sidebarTitle: "Gateway 命令"
---

# Gateway 服务命令

Gateway 是 OpenClaw 的总服务台。它不在线，通道、节点和控制 UI 都会受影响。

常用命令：

```bash
openclaw gateway status
openclaw gateway restart
openclaw gateway stop
openclaw health
openclaw status --deep
```

排查顺序：

1. `openclaw gateway status`
2. `openclaw doctor`
3. `openclaw logs --follow`
4. `openclaw gateway diagnostics export`

继续阅读：[Gateway 使用指南](/tutorials/gateway/)。

