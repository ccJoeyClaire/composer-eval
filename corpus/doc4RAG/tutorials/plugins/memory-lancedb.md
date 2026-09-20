---
title: "LanceDB 记忆插件"
sidebarTitle: "LanceDB 记忆"
---

# LanceDB 记忆插件

LanceDB 可作为向量记忆或检索后端。适合比内置 SQLite 更复杂的语义搜索场景。

如果你只是个人使用，先从 [内置记忆](/tutorials/concepts/memory-builtin) 开始。
如果数据量大、检索需求复杂，再考虑 LanceDB。

## 什么时候值得换

- 记忆条目很多。
- 语义搜索响应慢。
- 团队想用更专业的向量检索后端。
- 需要更强的索引和维护能力。

切换前先备份，再用 `openclaw memory status --deep` 验证。
