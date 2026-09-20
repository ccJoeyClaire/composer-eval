---
title: "QQ Bot"
sidebarTitle: "QQ Bot"
description: "OpenClaw 频道接入：QQ Bot 通过官方 QQ Bot API 连接 OpenClaw，支持私聊、群聊和频道消息。"
---

# QQ Bot

QQ Bot 通过官方 QQ Bot API 接入 OpenClaw。
它适合想让 OpenClaw 在 QQ 私聊、群聊或频道里工作的用户。

::: info 状态
QQ Bot 当前通过插件提供。使用前先确认你的 OpenClaw 版本较新，并按向导或插件命令安装。
:::

---

## 安装插件

```bash
openclaw plugins install @openclaw/qqbot
```

---

## 准备 QQ 机器人

1. 打开 [QQ 开放平台](https://q.qq.com/)。
2. 用手机 QQ 扫码登录。
3. 创建 Bot。
4. 找到 `AppID` 和 `AppSecret`。
5. 立刻保存 `AppSecret`，它就像密码，不要发给别人。

---

## 添加频道

```bash
openclaw channels add --channel qqbot --token "AppID:AppSecret"
openclaw gateway restart
```

也可以走交互式方式：

```bash
openclaw channels add
openclaw configure --section channels
```

---

## 最小配置

```json5
{
  channels: {
    qqbot: {
      enabled: true,
      appId: "YOUR_APP_ID",
      clientSecret: "YOUR_APP_SECRET",
    },
  },
}
```

---

## 安全建议

- AppSecret 不要写进公开仓库。
- 先在测试群里试。
- 群聊默认建议要求 @ 提及。
- 陌生私聊建议使用配对或白名单。

配对相关看 [频道配对](/tutorials/channels/pairing)。

