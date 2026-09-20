---
title: "通道和模型命令"
sidebarTitle: "通道模型命令"
---

# 通道和模型命令

## 通道

```bash
openclaw channels status --probe
openclaw pairing list
openclaw pairing approve <channel> <code>
```

`channels status --probe` 用来确认 Telegram、Discord、WhatsApp 等通道是否真的能工作。

Telegram 不使用 `channels login`；请用 BotFather Token 配置 `channels.telegram.botToken`。WhatsApp、Zalo Personal、WeChat 这类需要扫码或交互登录的通道，才会用 `channels login`。

## 模型

```bash
openclaw configure --section model
openclaw models list
```

模型问题先看 API Key、模型名、base URL 和额度。

继续阅读：[连接聊天软件](/tutorials/channels/) 和 [模型提供商](/tutorials/providers/)。

## 新手排查顺序

机器人不回复时，先判断是哪一边坏了：

```bash
openclaw models status
openclaw channels status --probe
openclaw logs --follow
```

模型坏了，WebChat 也会不回。通道坏了，WebChat 可能正常但 Telegram/Slack 不回。
