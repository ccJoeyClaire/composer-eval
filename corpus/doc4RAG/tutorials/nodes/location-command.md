---
title: "位置命令"
sidebarTitle: "位置"
description: "OpenClaw Nodes：location.get 节点命令、权限模式和移动端前台限制。"
---

# 位置命令

`location.get` 可以让已配对节点提供当前位置。
它适合“我在哪”“附近天气”“到家提醒”这类场景。

---

## 默认关闭

位置是敏感信息，所以默认应该谨慎启用。

常见权限：

- Off：关闭
- While Using：App 前台使用时允许
- Precise Location：是否允许精确位置

不同系统最终以 OS 授权为准。OpenClaw 只能请求权限，不能绕过系统设置。

---

## CLI 用法

```bash
openclaw nodes location get --node <node-id>
```

可能返回：

```json
{
  "lat": 31.2304,
  "lon": 121.4737,
  "accuracyMeters": 20,
  "timestamp": "2026-05-05T12:00:00.000Z"
}
```

---

## 常见错误

| 错误 | 含义 |
|------|------|
| `LOCATION_DISABLED` | 节点里关闭了位置 |
| `LOCATION_PERMISSION_REQUIRED` | 系统权限没给 |
| `LOCATION_BACKGROUND_UNAVAILABLE` | App 在后台，不能取位置 |
| `LOCATION_TIMEOUT` | 定位超时 |
| `LOCATION_UNAVAILABLE` | 系统定位不可用 |

移动端取位置时，先把节点 App 打开到前台最稳。

