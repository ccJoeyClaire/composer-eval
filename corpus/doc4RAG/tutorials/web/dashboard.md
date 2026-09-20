---
title: "Dashboard"
sidebarTitle: "Dashboard"
---

# Dashboard：先看这里判断 OpenClaw 是否健康

Dashboard 是 Control UI 的首页。它像汽车仪表盘，帮你快速看：

- Gateway 是否在线。
- 模型是否配置。
- 通道是否连接。
- 节点是否在线。
- 最近任务是否失败。

新手排查顺序：

```bash
openclaw doctor
openclaw gateway status
openclaw dashboard
```

如果 Dashboard 打不开，先回到 [Gateway 使用指南](/tutorials/gateway/)。

## 常见问题

- 页面打不开：Gateway 没启动或端口不通。
- 提示未授权：token、密码或浏览器 URL 不对。
- 通道显示异常：先跑 `openclaw channels status --probe`。
- 节点离线：先跑 `openclaw nodes status`。

Dashboard 是入口，不是全部答案。看不懂时回到 `doctor` 和日志。
