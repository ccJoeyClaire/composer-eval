---
title: "openclaw sandbox"
sidebarTitle: "sandbox"
---

# `openclaw sandbox`

`sandbox` 用来查看和管理 Agent 的隔离运行环境。沙盒的作用是把文件、命令、浏览器等危险能力关进一个更小的范围里。

常用：

```bash
openclaw sandbox list
openclaw sandbox explain
openclaw sandbox recreate --all
```

## 什么时候用

- 想确认 Agent 当前能访问哪些目录和工具。
- Docker、OpenShell 或 SSH 沙盒更新后需要重建。
- 浏览器沙盒容器状态异常。
- 安全审计提示沙盒配置不一致。

## 新手怎么读

`explain` 看策略，`list` 看运行实例，`recreate` 重建实例。
如果只是普通使用，不要一上来就 `recreate --all`，先看：

```bash
openclaw sandbox explain
openclaw doctor
```

继续阅读：[沙箱与安全](/tutorials/gateway/sandboxing)。
