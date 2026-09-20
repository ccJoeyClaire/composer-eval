---
title: "openclaw gateway"
sidebarTitle: "gateway"
---

# `openclaw gateway`

`gateway` 管理 OpenClaw 的核心服务。Gateway 是聊天通道、Web 控制台、节点、插件和 Agent 会话之间的中转站。

```bash
openclaw gateway run
openclaw gateway status
openclaw gateway install
openclaw gateway restart
openclaw gateway stop
```

## 什么时候用

- 想查看 Gateway 是否在线。
- 安装或重装后台服务。
- 配置改完需要重启。
- 服务器上排查端口、鉴权、服务状态。

## 新手路线

第一次安装仍然推荐：

```bash
openclaw onboard --install-daemon
```

日常排障：

```bash
openclaw gateway status
openclaw doctor
openclaw logs --follow
```

默认本机端口通常是 `127.0.0.1:18789`。不要在没有 token 或反向代理保护的情况下直接暴露到公网。

继续阅读：[Gateway 使用指南](/tutorials/gateway/)。
