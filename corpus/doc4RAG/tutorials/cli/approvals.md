---
title: "openclaw approvals"
sidebarTitle: "approvals"
---

# `openclaw approvals`

`approvals` 管理执行审批和 allowlist。它常用于控制 `exec`、文件写入、外部命令等高风险动作。

```bash
openclaw approvals get
openclaw approvals get --gateway
openclaw approvals set --file ./exec-approvals.json
openclaw exec-policy show
```

## 什么时候用

- 想查看本机、Gateway 或节点的 exec 审批策略。
- 想把审批策略从文件写入。
- 想收紧或放宽 `exec` allowlist。
- 想让本地 `tools.exec.*` 配置和 host approvals 文件保持一致。

## 新手提醒

审批策略不是烦人的确认框，而是安全边界。
看不懂策略含义时，不要直接套“全放开”配置。先看当前策略：

```bash
openclaw approvals get
openclaw exec-policy show
```

继续阅读：[执行审批](/tutorials/tools/exec-approvals)。
