---
title: "Voice Wake 语音唤醒"
sidebarTitle: "语音唤醒"
description: "OpenClaw Nodes：Voice Wake 唤醒词由 Gateway 统一保存，并同步给连接的节点和客户端。"
---

# Voice Wake 语音唤醒

Voice Wake 是“听到某个词就唤醒”的能力。
OpenClaw 当前把唤醒词当作 Gateway 统一管理的全局列表。

---

## 关键点

- 唤醒词由 Gateway 保存。
- 不是每个节点各自一套唤醒词。
- 任意支持的客户端修改后，Gateway 会广播给其他客户端。
- macOS / iOS 可能有本地开关。
- Android 当前更偏手动麦克风流程。

---

## 存储位置

Gateway 机器上：

```text
~/.openclaw/settings/voicewake.json
```

大概长这样：

```json
{
  "triggers": ["openclaw", "claude", "computer"]
}
```

---

## 使用建议

- 唤醒词不要太短，比如“嘿”这种容易误触发。
- 家庭或办公室场景先少量测试。
- 语音唤醒涉及麦克风权限，先确认系统授权。
- 如果误触发太多，减少唤醒词数量。

