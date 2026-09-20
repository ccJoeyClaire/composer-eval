---
title: "RPC 和协议"
sidebarTitle: "RPC 协议"
---

# RPC 和协议

OpenClaw 的控制 UI、CLI、节点和 Gateway 之间会通过 HTTP、WebSocket 和 RPC 风格消息通信。

新手只要知道：

- Gateway 是中心。
- 控制 UI 和节点都要认证。
- 节点要配对。
- 协议字段变化时，旧客户端可能需要更新。

开发者再去看具体接口和事件结构。

## 为什么新手也要知道一点

当 Control UI 显示断开、节点离线、CLI 报 unauthorized 时，背后通常就是 RPC 连接、认证或版本匹配出了问题。

先排查：

```bash
openclaw status
openclaw gateway status
openclaw logs --follow
```
