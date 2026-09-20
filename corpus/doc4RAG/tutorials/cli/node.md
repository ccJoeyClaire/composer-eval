---
title: "openclaw node"
sidebarTitle: "node"
---

# `openclaw node`

`node` 用来运行一个轻量节点主机，让另一台机器连接到 Gateway 并提供能力，比如远程执行受控命令、浏览器代理或设备能力。

```bash
openclaw node run --host 127.0.0.1 --port 18789
openclaw node install --host <gateway-host> --port 18789
```

## 什么时候用

- 想让远程 Linux/Windows 机器给 OpenClaw 执行受控命令。
- Gateway 在一台机器上，工具能力在另一台机器上。
- 需要无界面、轻量的 node host。

## 新手提醒

节点连接非本机 `ws://` Gateway 时要特别注意安全。优先使用 `wss://`、SSH tunnel 或 Tailscale。
不要把节点当成绕过审批的后门；执行仍应该受 allowlist 和审批约束。

继续阅读：[节点入门](/tutorials/nodes/)。
