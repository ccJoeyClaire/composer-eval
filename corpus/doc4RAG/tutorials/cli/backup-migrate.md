---
title: "备份和迁移命令"
sidebarTitle: "备份迁移"
---

# 备份和迁移命令

## 备份

```bash
openclaw backup create
```

备份配置、状态、auth profiles、会话和工作区。云端部署和升级前尤其建议先备份。

## 迁移

```bash
openclaw migrate claude --dry-run
openclaw migrate hermes --dry-run
openclaw migrate apply claude --yes
openclaw migrate apply hermes --yes
```

先 dry-run，看清楚计划，再 apply。

继续阅读：[从 Claude 迁移](/tutorials/installation/migrating-claude)、[从 Hermes 迁移](/tutorials/installation/migrating-hermes)。

## 新手提醒

迁移前备份，迁移时 dry-run，迁移后 doctor。
不要在没看计划的情况下直接 apply，因为迁移可能涉及凭据、会话、技能和工作区路径。
