---
title: "openclaw onboard"
sidebarTitle: "onboard"
---

# `openclaw onboard`

`onboard` 是新手向导。第一次安装 OpenClaw 时，它会帮你把 Gateway、配置、服务守护进程这些基础东西串起来。

推荐：

```bash
openclaw onboard --install-daemon
```

## 什么时候用

- 第一次在一台机器上安装 OpenClaw。
- 你想让 Gateway 作为后台服务长期运行。
- 你不确定配置文件、端口、服务该怎么准备。

## 推荐流程

```bash
openclaw onboard --install-daemon
openclaw dashboard
openclaw doctor
```

这三条可以理解成：

1. 安装并启动后台服务。
2. 打开控制台。
3. 做一次体检。

## 跑完以后看哪里

默认 Gateway 监听本机 `127.0.0.1:18789`。如果你在服务器上安装，通常不要直接暴露到公网，而是用 SSH tunnel、反向代理和 token 保护。

如果向导中断，不要从头乱改配置，先跑：

```bash
openclaw doctor
openclaw logs --follow
```

继续阅读：[安装向导](/tutorials/getting-started/wizard)。
