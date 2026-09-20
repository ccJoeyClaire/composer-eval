---
title: "openclaw skills"
sidebarTitle: "skills"
---

# `openclaw skills`

`skills` 用来管理技能。技能不是插件，它更像给 Agent 的“做事说明书”，告诉它遇到某类任务时应该按什么步骤来。

```bash
openclaw skills list
openclaw skills validate <path>
openclaw skills search <query>
```

## 什么时候用

- 想看当前有哪些技能。
- 写了一个本地技能，想先校验格式。
- 想从 ClawHub 搜索可安装技能。
- 某个 Agent 看不到技能，需要排查配置。

## 新手提醒

插件给 OpenClaw 增加能力；技能教 Agent 怎么用能力。
如果你只是想沉淀经验，比如“写周报按这个格式”，通常用技能就够了。

继续阅读：[技能系统](/tutorials/tools/skills)。
