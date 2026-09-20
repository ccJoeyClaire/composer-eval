---
title: "openclaw uninstall"
sidebarTitle: "uninstall"
---

# `openclaw uninstall`

`uninstall` 用来移除 Gateway 服务、本地状态、工作区或 macOS App。它不会自动帮你保留数据，所以先备份。

```bash
openclaw backup create --verify
openclaw uninstall --dry-run
openclaw uninstall --service --yes --non-interactive
openclaw uninstall --all --yes
```

## 什么时候用

- 想移除后台服务。
- 想清理本机状态和工作区。
- 迁移到另一台机器后，旧机器要退役。

## 新手路线

1. `openclaw backup create --verify`
2. `openclaw uninstall --dry-run`
3. 看清楚范围后再执行真正卸载。

`--all` 范围很大，确认不需要本机数据后再用。

继续阅读：[卸载说明](/tutorials/installation/uninstall)。
