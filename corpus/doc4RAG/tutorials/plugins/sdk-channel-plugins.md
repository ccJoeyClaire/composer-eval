---
title: "Channel Plugin SDK"
sidebarTitle: "Channel SDK"
---

# Channel Plugin SDK

Channel Plugin SDK 用来接入新的聊天软件或消息入口。

通道插件通常要处理：

- 登录和凭据。
- 收消息。
- 发消息。
- 群聊和私聊策略。
- allowlist 和 pairing。
- 附件、引用、线程和反应。

先看 [Channel 配置](/tutorials/gateway/config-channels)。

## 新手怎么理解

通道插件像翻译和快递员：把平台消息翻译成 OpenClaw 消息，再把 Agent 回复送回平台。

最容易出错的地方：

- 登录凭据。
- 私聊/群聊 allowlist。
- pairing。
- 附件和长消息。
- 平台 rate limit。
