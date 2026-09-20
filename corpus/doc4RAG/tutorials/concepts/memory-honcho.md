---
title: "Honcho 记忆"
sidebarTitle: "Honcho 记忆"
---

# Honcho 记忆：外部记忆服务路线

Honcho 是一种外部记忆服务路线。和内置 SQLite 记忆不同，它把记忆能力交给外部服务管理。

如果你只是个人使用，先用 [内置记忆引擎](/tutorials/concepts/memory-builtin)。

---

## 适合场景

适合：

- 你已有 Honcho 基础设施。
- 希望多个环境共享记忆后端。
- 想把记忆作为独立服务管理。
- 对查询、存储、权限有更复杂需求。

不适合：

- 新手第一次安装。
- 单机家庭网关。
- 只是想记住几条偏好。

---

## 和内置记忆怎么选？

| 需求 | 推荐 |
|------|------|
| 单机简单使用 | 内置记忆 |
| 本地资料增强 | QMD |
| 外部服务统一管理 | Honcho |

---

## 迁移提醒

如果你从 Hermes 或其他系统迁移，外部记忆配置通常应该先归档、再手动审查，不要盲目自动启用。

---

## 继续阅读

- [内置记忆引擎](/tutorials/concepts/memory-builtin)
- [QMD 记忆后端](/tutorials/concepts/memory-qmd)
- [从 Hermes 迁移](/tutorials/installation/migrating-hermes)

