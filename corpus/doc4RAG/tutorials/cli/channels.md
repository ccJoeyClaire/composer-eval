---
title: "openclaw channels"
sidebarTitle: "channels"
---

# `openclaw channels`

`channels` 管理聊天软件入口。Telegram、WhatsApp、Discord、Slack、微信、飞书这些都属于通道。

通道的任务很简单：把外面的消息送进 Gateway，再把 OpenClaw 的回复送回去。

常用：

```bash
openclaw channels status
openclaw channels status --probe
openclaw channels login --channel whatsapp
openclaw channels logout --channel zalouser
```

注意：Telegram 不使用 `channels login`，它是 Bot Token 配置型通道。

## 什么时候用

- 机器人在聊天软件里不回消息。
- 你刚加了一个通道，想确认配置是否生效。
- 某个通道需要扫码或 OAuth 登录。
- 升级后想检查所有通道是否仍可用。

## `status` 和 `status --probe` 的区别

`openclaw channels status` 像看登记表：配置里有没有这个通道、是否启用。

`openclaw channels status --probe` 像打电话试一下：真的去检查连接、token、账号状态。排障时优先用 `--probe`。

## 常见排障顺序

```bash
openclaw channels status --probe
openclaw logs --follow
openclaw doctor
```

如果是私聊不回复，还要看配对：

```bash
openclaw pairing list <channel>
```

继续阅读：[连接聊天软件](/tutorials/channels/)。
