---
title: "openclaw reset"
sidebarTitle: "reset"
---

# `openclaw reset`

`reset` 用来重置本地配置或状态。这个命令有破坏性，所以它应该排在“备份”和“确认范围”后面。

执行前先备份：

```bash
openclaw backup create
openclaw reset --dry-run
openclaw reset --scope config --yes --non-interactive
```

## scope 怎么理解

- `config`：只重置配置。
- `config+creds+sessions`：配置、凭据、会话一起重置。
- `full`：更彻底的本地状态重置。

## 新手路线

```bash
openclaw backup create --verify
openclaw reset --dry-run
```

看清楚会删什么，再决定是否加 `--yes`。如果只是配置写坏了，优先从 `config` 这种小范围开始。
