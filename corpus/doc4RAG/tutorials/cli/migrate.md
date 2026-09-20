---
title: "openclaw migrate"
sidebarTitle: "migrate"
---

# `openclaw migrate`

`migrate` 用来把 Claude、Hermes 或旧版状态迁到 OpenClaw。迁移属于高风险操作，因为它可能碰到凭据、会话、技能、配置路径。

先预览：

```bash
openclaw migrate claude --dry-run
openclaw migrate hermes --dry-run
```

## 新手路线

1. 先备份当前 OpenClaw：

```bash
openclaw backup create --verify
```

2. 再预览迁移：

```bash
openclaw migrate claude --dry-run
```

3. 看清楚会复制什么，再执行真正迁移。

## 迁移 Codex 技能时怎么选

如果你运行：

```bash
openclaw migrate codex
```

OpenClaw 会先给你看迁移计划，然后打开一个技能选择界面。
这里的“技能”可以理解成 Agent 的工具包。

选择界面里有几种状态：

- planned skills：计划复制的技能，默认是勾选的。
- conflict skills：目标位置已经有同名内容，默认不勾选，避免覆盖你现有文件。
- `Toggle all on`：全部选上。
- `Toggle all off`：全部取消。
- `Skip for now`：这次先不处理技能，其他迁移步骤继续按提示走。

如果你在脚本里执行，不想打开选择界面，可以明确写要迁移哪些技能：

```bash
openclaw migrate codex --dry-run --skill my-skill-name
```

::: warning 不要急着全选
如果某个技能显示为冲突，先看清楚它要复制到哪里。迁移最怕“旧文件被新文件盖掉”，所以冲突项默认不选是为了保护你的现有配置。
:::

## 迁移后检查

```bash
openclaw doctor
openclaw status
openclaw plugins list
```

继续阅读：[从 Claude 迁移](/tutorials/installation/migrating-claude)。
