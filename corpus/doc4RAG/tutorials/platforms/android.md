---
title: "Android"
sidebarTitle: "Android"
---

# Android：手机 Node 和移动能力

Android App 也作为 Node 接入 Gateway。它不会自己托管 Gateway。

连接方式：

- 同一 LAN。
- Tailscale 或安全 `wss://` 地址。
- 手动 host/port。

Android 远程接入时，不建议裸用公网 `ws://`。优先用 Tailscale Serve 或其他 TLS 终止方式。

继续阅读：[节点入门](/tutorials/nodes/) 和 [Android 节点排查](/tutorials/nodes/troubleshooting)。

