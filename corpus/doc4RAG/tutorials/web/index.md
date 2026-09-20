---
title: "Web 控制 UI"
sidebarTitle: "Web 控制 UI"
description: "OpenClaw Web 控制 UI 入门：解释浏览器控制台是什么、怎么打开、能做什么，以及远程访问时需要注意哪些安全设置。"
---

# Web 控制 UI

Web 控制 UI 就是 OpenClaw 的浏览器控制面板。

第一次装好 OpenClaw 后，最推荐先打开它。因为它不需要 Telegram、不需要 WhatsApp，也不需要先配置复杂通道。只要 Gateway 正常，你就能在浏览器里直接和 AI 聊。

---

## 怎么打开

运行：

```bash
openclaw dashboard
```

通常会打开：

```text
http://127.0.0.1:18789/
```

如果浏览器能打开，并且你能发消息得到回复，说明这条主链路已经通了：

```text
浏览器 → Gateway → Agent → 模型 → Gateway → 浏览器
```

---

## 它能做什么

不同版本界面细节会变，但核心用途通常包括：

- 和 AI 助手聊天。
- 查看 Gateway 是否健康。
- 查看会话和历史。
- 管理部分配置。
- 查看通道和节点状态。
- 调试本地或远程连接问题。

对新手来说，它就是“先确认 OpenClaw 能工作”的地方。

---

## 为什么先用控制 UI

很多新手一上来就接 Telegram 或 WhatsApp，遇到问题时不知道是哪里坏了：

- 是 AI 模型没配好？
- 是 Gateway 没启动？
- 是聊天软件 Token 错了？
- 是陌生用户还没配对？
- 是网络连不上？

控制 UI 可以先排除一半问题。

如果控制 UI 能聊，说明模型、Gateway、Agent 主链路没大问题。后面再接通道，排查范围就小很多。

---

## 默认只给本机访问

默认地址里的 `127.0.0.1` 表示“只允许这台电脑自己访问”。

这很重要。因为控制 UI 背后能触达你的 Agent、会话和工具能力，不应该随便暴露到公网。

如果你要从手机或另一台电脑访问，优先看：

- [Tailscale 远程访问](/tutorials/gateway/tailscale)
- [网关认证](/tutorials/gateway/authentication)
- [远程访问](/tutorials/gateway/remote)

---

## 常见问题

::: details 浏览器打不开怎么办？

先检查 Gateway：

```bash
openclaw gateway status
openclaw doctor
```

再看日志：

```bash
openclaw logs --follow
```

:::

::: details 我能不能把它放到公网？

不建议直接暴露。至少要配置认证、TLS、allowed origins，并确认你理解风险。

更推荐 Tailscale、VPN 或 SSH 隧道。

:::

::: details 端口不是 18789 怎么办？

如果你手动改过端口，打开对应端口即可。比如你启动了：

```bash
openclaw gateway --port 18790
```

那浏览器地址就是：

```text
http://127.0.0.1:18790/
```

:::

---

## 下一步

- 已经能在控制 UI 聊天：去[连接 Telegram](/tutorials/channels/telegram)。
- 想理解 Gateway：看[网关使用指南](/tutorials/gateway/)。
- 想连接手机或远程机器：看[节点入门](/tutorials/nodes/)。
