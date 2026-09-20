---
title: "RPC"
sidebarTitle: "RPC"
---

# RPC

RPC 是控制 UI、CLI、节点和 Gateway 通信时会用到的请求/响应风格协议。

新手只要知道：

- 调用方需要认证。
- 不同客户端通过 Gateway 协调。
- 版本不匹配时可能需要升级客户端。

继续阅读：[RPC 和协议](/tutorials/reference/rpc-protocol)。

## 常见现象

- token 错：请求被拒绝。
- Gateway 地址错：客户端连不上。
- 版本太旧：字段对不上。
- 节点未配对：能力不会出现。

遇到这些问题，不要先改代码，先确认 Gateway URL、token 和版本。
