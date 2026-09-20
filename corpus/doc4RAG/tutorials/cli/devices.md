---
title: "openclaw devices"
sidebarTitle: "devices"
---

# `openclaw devices`

`devices` 用来管理设备配对请求和设备 token。它更偏“谁被允许连进 Gateway”，而 `nodes` 更偏“连进来的节点能提供什么能力”。

```bash
openclaw devices list
openclaw devices approve <requestId>
openclaw devices reject <requestId>
openclaw devices remove <deviceId>
```

## 什么时候用

- 手机、桌面 App 或节点发起配对。
- 想批准或拒绝某个设备。
- 设备丢失，需要撤销 token。
- 设备请求更高权限，需要人工确认。

## 新手提醒

批准前先看清设备名、角色、scope 和来源地址。
不要只因为“有个请求”就批准；设备 token 代表它以后可以按批准范围访问 Gateway。

继续阅读：[节点入门](/tutorials/nodes/)。
