---
title: "openclaw commitments"
sidebarTitle: "commitments"
---

# `openclaw commitments`

`commitments` 用来查看 OpenClaw 记下来的“之后要跟进”的事情。比如你让它明天提醒、稍后检查、过一阵继续某件事，这类记录就会进入 commitments。

```bash
openclaw commitments
openclaw commitments list
openclaw commitments --all
openclaw commitments dismiss <id>
```

## 什么时候用

- 你想知道 OpenClaw 还记着哪些后续事项。
- 某个提醒不需要了，想手动清掉。
- 自动化或跟进没有出现，想查是否真的被记录。

## 常见流程

先列出记录：

```bash
openclaw commitments list
```

查看所有状态，包括已经发送、忽略或过期的记录：

```bash
openclaw commitments --all
```

确认不用了再忽略：

```bash
openclaw commitments dismiss <id>
```

## 新手提醒

commitment 不是立即执行的命令，更像备忘录加闹钟。它能不能准时触发，还要看 Gateway 是否在线、自动化是否启用、时间设置是否正确。

继续阅读：[自动化总览](/tutorials/automation/)。
