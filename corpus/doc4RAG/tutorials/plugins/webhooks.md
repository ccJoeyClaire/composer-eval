---
title: "Webhooks"
sidebarTitle: "Webhooks"
---

# Webhooks

Webhook 插件让外部系统通过 HTTP 事件唤醒或通知 OpenClaw。

常见用途：

- CI 完成后通知 Agent。
- 监控告警进入聊天通道。
- 内部系统把事件交给 Agent 总结。

安全重点：签名校验、重放防护、来源限制和日志脱敏。

## 新手比喻

Webhook 像门铃：外部系统按一下，OpenClaw 就知道有事发生。
但门铃不能谁都能按，所以要有 token、签名或来源限制。

排查顺序：

```bash
openclaw gateway status
openclaw logs --follow
openclaw security audit
```

生产环境里，Webhook 最好每个来源一个 token 或签名密钥。这样某个系统泄漏时，可以只轮换那一路，不影响所有自动化。
