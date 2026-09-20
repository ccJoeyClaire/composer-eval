---
title: "WeChat / 微信"
sidebarTitle: "WeChat"
description: "OpenClaw 频道接入：微信通过腾讯 openclaw-weixin 外部插件接入，适合需要微信私聊入口的用户。"
---

# WeChat / 微信

OpenClaw 通过腾讯提供的外部插件接入微信。
插件包名是：

```text
@tencent-weixin/openclaw-weixin
```

频道 ID 通常是：

```text
openclaw-weixin
```

---

## 它怎么工作

微信接入不直接写在 OpenClaw 核心里。
OpenClaw 负责插件框架和消息路由，微信插件负责登录、收消息、发消息和媒体处理。

这就像插排和电器：

- OpenClaw 是插排
- 微信插件是插上去的电器
- Gateway 负责把消息送到 Agent

---

## 安装插件

快速安装：

```bash
npx -y @tencent-weixin/openclaw-weixin-cli install
```

手动安装：

```bash
openclaw plugins install "@tencent-weixin/openclaw-weixin"
openclaw config set plugins.entries.openclaw-weixin.enabled true
openclaw gateway restart
```

---

## 登录微信

在运行 Gateway 的机器上执行：

```bash
openclaw channels login --channel openclaw-weixin
```

用手机微信扫码确认。登录成功后，插件会把账号凭证保存到 OpenClaw 状态目录。

---

## 访问控制

微信私聊同样使用 OpenClaw 的配对和白名单模型。

```bash
openclaw pairing list openclaw-weixin
openclaw pairing approve openclaw-weixin <CODE>
```

不建议一开始就开放给所有人。先用自己的小号测试，再逐步扩大范围。

---

## 兼容性提醒

如果插件提示 OpenClaw 版本太旧，先更新：

```bash
openclaw update
openclaw doctor
openclaw gateway restart
```

微信生态变化比较快，如果遇到登录、风控或媒体问题，优先查看插件自己的说明和 OpenClaw GitHub Issues。

