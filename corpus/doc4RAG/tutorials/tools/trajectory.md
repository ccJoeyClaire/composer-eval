---
title: "Trajectory Bundles"
sidebarTitle: "轨迹导出"
---

# Trajectory Bundles：导出一次 Agent 运行的飞行记录

Trajectory 是每个会话的“飞行记录仪”。当你想知道 Agent 为什么这样回答、为什么调用某个工具、为什么失败时，可以导出轨迹包。

---

## 什么时候用？

适合排查：

- Prompt 到底发给了模型什么。
- 工具调用顺序是否正确。
- 模型是否触发 fallback。
- 会话是否被压缩。
- 哪个插件、模型、runtime 当时生效。

如果是 Gateway 整体故障，先用 [诊断包](/tutorials/gateway/diagnostics)。
如果是某个会话的行为问题，再用 trajectory。

---

## 导出命令

在聊天会话中：

```text
/export-trajectory
```

别名：

```text
/trajectory
```

也可以指定相对目录名：

```text
/export-trajectory bug-1234
```

导出位置通常在：

```text
.openclaw/trajectory-exports/
```

---

## 它很敏感

轨迹包可能包含：

- prompt。
- 工具 schema。
- 工具结果。
- 模型消息。
- 本地路径。
- 使用量信息。

所以导出会经过审批。不要把轨迹包直接公开上传，先检查和脱敏。

---

## 继续阅读

- [Gateway 诊断包](/tutorials/gateway/diagnostics)
- [会话管理](/tutorials/concepts/session)
- [上下文引擎](/tutorials/concepts/context-engine)

