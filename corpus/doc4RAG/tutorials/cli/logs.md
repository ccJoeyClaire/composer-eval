---
title: "openclaw logs"
sidebarTitle: "logs"
---

# `openclaw logs`

`logs` 用来看 Gateway 日志。排障时，日志像病历：它不一定直接告诉你答案，但会告诉你事情在哪一步坏了。

```bash
openclaw logs
openclaw logs --follow
openclaw logs --limit 500
openclaw logs --json
```

排查通道、Gateway、插件问题时非常常用。

## 什么时候用

- 聊天软件发了消息但 OpenClaw 没回复。
- 插件安装或加载失败。
- Gateway 看起来在线，但功能没有反应。
- 想实时观察刚刚触发的操作。

## 常用写法

实时跟随日志：

```bash
openclaw logs --follow
```

多看一点历史：

```bash
openclaw logs --limit 500
```

脚本读取：

```bash
openclaw logs --json
```

连接远程 Gateway：

```bash
openclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
```

## 新手怎么看日志

先找这几类词：

- `error`：已经出错。
- `warn`：可能有问题。
- `unauthorized`：token、权限或配对有问题。
- `plugin`：插件加载或运行问题。
- `channel`：通道连接、登录、消息收发问题。

继续阅读：[Gateway 日志](/tutorials/gateway/logging)。
