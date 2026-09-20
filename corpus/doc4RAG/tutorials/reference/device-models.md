---
title: "Device Models"
sidebarTitle: "设备模型"
---

# Device Models

设备模型描述节点、手机、桌面、远程机器如何被 OpenClaw 表示。

关键点：

- Node 是连接进 Gateway 的设备。
- 设备可以声明能力。
- 能力需要配对和权限。
- 状态会影响工具是否可用。

继续阅读：[节点入门](/tutorials/nodes/)。

## 新手比喻

Gateway 像家里的总控，设备像连接进来的手机、电脑、传感器或远程机器。
设备先表明身份和能力，Gateway 再决定给不给它权限。

## 常见排查

```bash
openclaw devices list
openclaw nodes status
openclaw doctor
```
