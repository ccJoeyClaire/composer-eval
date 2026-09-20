---
title: "openclaw flows"
sidebarTitle: "flows"
---

# `openclaw flows`

最新版里，flow 命令主要放在 `openclaw tasks flow` 下面，而不是独立的 `openclaw flows`。

```bash
openclaw tasks flow list
openclaw tasks flow show <lookup>
openclaw tasks flow cancel <lookup>
```

## 什么时候会看到它

- 旧文档或 release note 里出现 `openclaw flows`。
- 你在排查 Task Flow 状态。
- 自动化任务被拆成多个步骤，需要看每一步的记录。

## 新手提醒

看到 flow，先理解成“多步骤任务的流水线”。普通后台任务看 `openclaw tasks`，多步骤任务再看 `tasks flow`。

继续阅读：[Task Flow](/tutorials/automation/taskflow)。
