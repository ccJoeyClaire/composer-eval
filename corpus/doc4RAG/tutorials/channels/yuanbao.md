---
title: "Yuanbao 元宝"
sidebarTitle: "Yuanbao"
description: "OpenClaw 频道接入：Tencent Yuanbao 元宝机器人通过 WebSocket 接入 OpenClaw。"
---

# Yuanbao 元宝

Yuanbao 是腾讯的 AI 助手平台。OpenClaw 可以通过 Yuanbao 频道插件，把 Yuanbao 机器人接到 Gateway，再交给 OpenClaw Agent 处理。

::: info 版本提醒
官方文档要求较新的 OpenClaw 版本。先运行 `openclaw --version`，必要时执行 `openclaw update`。
:::

---

## 快速添加

```bash
openclaw channels add --channel yuanbao --token "appKey:appSecret"
openclaw gateway restart
```

`appKey:appSecret` 来自 Yuanbao 应用/机器人设置。

也可以交互式登录：

```bash
openclaw channels login --channel yuanbao
```

---

## 私聊控制

`dmPolicy` 控制谁能私聊机器人：

| 值 | 含义 |
|----|------|
| `pairing` | 陌生用户先拿配对码，批准后才能用 |
| `allowlist` | 只有白名单用户能用 |
| `open` | 所有人都能用 |
| `disabled` | 禁用私聊 |

新手建议先用 `pairing` 或 `allowlist`。

---

## 群聊控制

群聊里建议默认要求 @ 提及：

```json5
{
  channels: {
    yuanbao: {
      requireMention: true,
    },
  },
}
```

这样可以减少机器人误回复，也能降低模型费用。

---

## 配对命令

```bash
openclaw pairing list yuanbao
openclaw pairing approve yuanbao <CODE>
```

更多访问控制看 [频道配对](/tutorials/channels/pairing)。

