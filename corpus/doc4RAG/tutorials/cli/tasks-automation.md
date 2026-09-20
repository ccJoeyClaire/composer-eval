---
title: "任务和自动化命令"
sidebarTitle: "任务自动化命令"
---

# 任务和自动化命令

OpenClaw 的长任务、视频生成、音乐生成、cron 和自动化会进入任务体系。

常用命令：

```bash
openclaw tasks list
openclaw tasks show <taskId>
openclaw tasks cancel <taskId>
```

自动化相关：

```bash
openclaw cron list
openclaw tasks audit
openclaw tasks maintenance
```

长视频、音乐生成这类任务不会总是当场完成。看到 task id 不要慌，它表示 OpenClaw 已经把任务记下来了。

继续阅读：[任务自动化](/tutorials/automation/tasks)。

## 新手怎么区分

- `tasks`：看已经发生或正在发生的后台任务。
- `cron`：管理固定时间运行的计划任务。
- `webhook`：外部系统触发 OpenClaw。

如果只是想知道“我刚才那个任务跑完没”，先看 `openclaw tasks list`。如果是“每天几点自动跑”，再看 cron。
