---
title: "节点故障排查"
sidebarTitle: "故障排查"
description: "OpenClaw Nodes：节点已连接但相机、Canvas、位置、屏幕、exec 等工具失败时的排查步骤。"
---

# 节点故障排查

节点出问题时，先别急着重新配对。
按顺序检查：Gateway、节点在线、节点能力、系统权限、工具审批。

---

## 命令阶梯

```bash
openclaw gateway status
openclaw doctor
openclaw nodes status
openclaw nodes describe --node <node-id>
openclaw logs --follow
```

如果涉及命令执行：

```bash
openclaw approvals get --node <node-id>
```

---

## 健康信号

- `nodes status` 能看到节点在线。
- `nodes describe` 里有你要调用的能力。
- 移动端 App 在前台。
- 系统相机、麦克风、位置、录屏权限已授权。
- `exec` 审批或 allowlist 符合预期。

---

## 常见错误

| 错误 | 处理 |
|------|------|
| `NODE_BACKGROUND_UNAVAILABLE` | 把节点 App 切到前台 |
| `CAMERA_DISABLED` | 在节点设置里打开相机 |
| `*_PERMISSION_REQUIRED` | 到系统设置里授权 |
| `LOCATION_PERMISSION_REQUIRED` | 给位置权限 |
| `SYSTEM_RUN_DENIED` | 检查 exec 审批和 allowlist |

---

## 配对和审批不是一回事

节点配对回答的是：

> 这台设备能不能连接 Gateway？

Exec 审批回答的是：

> 这台设备能不能运行这条命令？

所以节点已配对，不代表它能随便运行命令。

