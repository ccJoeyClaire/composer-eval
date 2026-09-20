---
title: "openclaw tasks"
sidebarTitle: "tasks"
---

# `openclaw tasks`

`tasks` 用来查看 OpenClaw 正在后台做的事情。比如长时间的视频生成、自动化任务、子智能体任务、cron 任务，不一定马上完成，OpenClaw 会把它们记在任务账本里。

```bash
openclaw tasks
openclaw tasks list
openclaw tasks list --status running
openclaw tasks show <taskId>
openclaw tasks cancel <taskId>
openclaw tasks audit
openclaw tasks maintenance
```

## 什么时候用

- 你发起了一个长任务，想知道它跑到哪了。
- 通知里出现 task id，但你不知道是什么意思。
- 自动化没有按预期完成，需要查记录。
- 想取消一个还在运行的任务。

## 常见流程

先列出任务：

```bash
openclaw tasks list
```

看到任务 ID 后查看详情：

```bash
openclaw tasks show <taskId>
```

确认不需要了再取消：

```bash
openclaw tasks cancel <taskId>
```

如果任务账本看起来乱了，先审计，不要急着清理：

```bash
openclaw tasks audit
```

## 新手提醒

`queued` 是排队中，`running` 是正在跑，`succeeded` 是成功，`failed` 是失败，`cancelled` 是被取消。看到 `lost` 不一定代表数据丢了，通常表示 Gateway 已经找不到那个运行中的进程，需要结合日志看。

继续阅读：[后台任务](/tutorials/automation/tasks)。
