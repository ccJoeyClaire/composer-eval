---
title: "openclaw directory"
sidebarTitle: "directory"
---

# `openclaw directory`

`directory` 用来查询通道里的联系人、群组、房间和自己的 ID。它不是文件目录命令，而是“通讯录查询”命令。

```bash
openclaw directory self --channel zalouser
openclaw directory peers list --channel slack --query "jane"
openclaw directory groups list --channel matrix
```

## 什么时候用

- 想找到 `openclaw message send --target` 需要的目标 ID。
- 想确认机器人看到的群、联系人、房间名称。
- 配置 allowlist 时需要稳定 ID，而不是容易改名的昵称。

## 新手提醒

不同通道 ID 格式不一样。Slack 可能是 `user:U...`，Discord 可能是 `channel:<id>`，Matrix 可能是 `!room:server`。能用稳定 ID 就不要只写昵称。
