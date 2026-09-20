---
title: "openclaw backup"
sidebarTitle: "backup"
---

# `openclaw backup`

`backup` 用来备份本机 OpenClaw 状态、配置、凭据、会话和可选工作区。做升级、迁移、重置前，先备份是最稳的。

常用：

```bash
openclaw backup create
openclaw backup create --dry-run
openclaw backup create --verify
openclaw backup verify <archive>
```

## 什么时候用

- 升级 OpenClaw 前。
- 执行 `openclaw reset` 前。
- 从一台机器迁移到另一台机器前。
- 配置已经坏了，但你想先保留现场。

## 新手路线

先预览：

```bash
openclaw backup create --dry-run
```

确认范围后创建并验证：

```bash
openclaw backup create --verify
```

如果配置坏了导致工作区发现失败，可以先只备份配置：

```bash
openclaw backup create --only-config
```

## 备份放哪里

不要把备份文件放进正在备份的状态目录或工作区里，否则可能出现自我包含。
推荐放到单独目录，比如 `~/Backups` 或服务器的专用备份盘。
