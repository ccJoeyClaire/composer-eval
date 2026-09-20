---
title: "Channel 配置"
sidebarTitle: "Channel 配置"
---

# Channel 配置：谁能从聊天软件叫醒 OpenClaw

`channels.*` 配置决定 Telegram、Discord、Slack、WhatsApp、Matrix 等通道如何接入、谁能发消息、群聊里什么时候回复。

---

## 每个通道默认怎么启动？

当某个通道的配置块存在，并且没有 `enabled: false`，OpenClaw 通常会尝试启动它。

这意味着：配置写进去之前，先准备好 token、账号状态和 allowlist。

---

## DM 策略

| 策略 | 说明 |
|------|------|
| `pairing` | 默认。陌生私信先生成配对码，主人批准后才能用 |
| `allowlist` | 只允许名单里的人 |
| `open` | 允许所有私信，通常还要显式 `allowFrom: ["*"]` |
| `disabled` | 禁用私信 |

新手推荐 `pairing`。它最像门禁。

---

## 群聊策略

| 策略 | 说明 |
|------|------|
| `allowlist` | 默认。只允许指定群或房间 |
| `open` | 允许群消息，但仍可要求 mention |
| `disabled` | 禁用群聊 |

群聊里强烈建议开启 mention gating。否则 Agent 可能对每句话都回应。

---

## 通道模型覆盖

有时你希望某个群用更强模型，另一个群用便宜模型。可以做 channel 级模型映射。

示意：

```json5
{
  channels: {
    modelByChannel: {
      telegram: {
        "-1001234567890": "openai/gpt-4.1-mini"
      }
    }
  }
}
```

---

## 心跳和上下文可见性

`channels.defaults` 可以配置全局默认：

- 群组策略。
- quoted/thread/history 上下文是否可见。
- 通道健康心跳是否显示 OK 或告警。

团队环境尤其要注意 `contextVisibility`。不要让未授权发言者的历史上下文悄悄进入 Agent。

---

## 继续阅读

- [连接聊天软件](/tutorials/channels/)
- [访问组](/tutorials/channels/access-groups)
- [配对说明](/tutorials/channels/pairing)

