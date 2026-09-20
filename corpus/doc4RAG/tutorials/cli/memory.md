---
title: "openclaw memory"
sidebarTitle: "memory"
---

# `openclaw memory`

`memory` 用来查看、索引、搜索和整理 OpenClaw 的记忆。记忆能让 Agent 在未来对话中找回重要背景。

```bash
openclaw memory status
openclaw memory status --deep
openclaw memory index --force
openclaw memory search "deployment notes"
openclaw memory promote --apply
```

## 什么时候用

- 想确认记忆插件是否可用。
- Agent 记不住某些资料，需要重新索引。
- 想搜索历史知识。
- 想把短期记忆提升到长期记忆。

## 新手提醒

`status` 是看状态，`index` 是重建索引，`search` 是查记忆，`promote` 是整理沉淀。
不确定时先跑：

```bash
openclaw memory status --deep
```

继续阅读：[记忆 Memory](/tutorials/concepts/memory)。
