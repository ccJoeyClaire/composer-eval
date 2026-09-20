---
title: "openclaw health"
sidebarTitle: "health"
---

# `openclaw health`

`health` 用来快速检查 Gateway 和核心服务健康状态。它比完整 `doctor` 更像监控探针，适合脚本、部署后验证和定时检查。

```bash
openclaw health
openclaw health --verbose
openclaw health --json
```

## 什么时候用

- 部署脚本跑完后确认服务活着。
- 监控系统定期检查 OpenClaw。
- 想快速知道 Gateway 能不能响应。

## 和 doctor 的区别

`health` 偏“快”；`doctor` 偏“细”。
如果 health 失败，再跑：

```bash
openclaw doctor
openclaw logs --follow
```

## 监控场景

服务器上可以让监控系统定期跑 `openclaw health --json`。
如果它失败，再通知管理员查看 `doctor` 和日志。这样比等用户发现机器人不回复更早。
