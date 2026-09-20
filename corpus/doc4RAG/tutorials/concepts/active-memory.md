---
title: "Active Memory 主动记忆"
sidebarTitle: "主动记忆"
description: "OpenClaw 核心概念：Active Memory 会在主回复前主动检索相关记忆，让 Agent 更自然地想起重要信息。"
---

# Active Memory 主动记忆

普通记忆像一本笔记本。
模型要想起来，通常得自己决定去翻，或者你提醒它“你还记得吗”。

Active Memory 更主动一点：
在主回复生成前，它会先派一个小的记忆子任务，看看有没有相关记忆值得带进来。

---

## 它适合什么

- 你希望 Agent 记得你的偏好
- 你经常和同一个 Agent 长期聊天
- 你希望回复更像“它真的知道我之前说过什么”
- 你不想每次都手动说“去查记忆”

---

## 为什么默认要谨慎

主动记忆会在回复前多跑一步。
这意味着：

- 可能增加延迟
- 可能增加模型费用
- 需要控制哪些会话可以启用
- 群聊里更要谨慎，避免把不该混用的记忆带进来

所以新手建议先只在私聊、主 Agent 上启用。

---

## 配置示例

```json5
{
  plugins: {
    entries: {
      "active-memory": {
        enabled: true,
        config: {
          enabled: true,
          agents: ["main"],
          allowedChatTypes: ["direct"],
          queryMode: "recent",
          promptStyle: "balanced",
          timeoutMs: 15000,
        },
      },
    },
  },
}
```

改完后重启 Gateway：

```bash
openclaw gateway restart
```

---

## 会话内开关

在当前聊天里可以这样查看或切换：

```text
/active-memory status
/active-memory off
/active-memory on
```

全局开关要更谨慎：

```text
/active-memory status --global
/active-memory off --global
/active-memory on --global
```

---

## 和普通 Memory 的关系

- [Memory](/tutorials/concepts/memory) 是记忆系统本身。
- Active Memory 是“回复前主动查一下记忆”的机制。

可以先理解 Memory，再决定是否启用 Active Memory。

