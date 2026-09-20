---
title: "Zalo User 插件"
sidebarTitle: "Zalo User"
---

# Zalo User 插件

Zalo User 插件用于 Zalo 个人账号相关接入。它和普通 bot 通道的信任边界不同，使用前要特别注意账号风险和平台规则。

先看 [Zalo Personal](/tutorials/channels/zalouser)。
不要把个人账号能力开放给不可信用户。

## 新手提醒

个人账号通道通常比 Bot API 风险更高，因为它代表一个真实用户身份。
启用前先确认平台规则、账号风控、登录方式和 allowlist。测试时只用小范围联系人，不要直接接入大群。

排查时先看：

```bash
openclaw channels status --probe
openclaw logs --follow
```
