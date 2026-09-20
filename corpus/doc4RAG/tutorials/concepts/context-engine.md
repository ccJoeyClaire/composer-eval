---
title: "Context Engine 上下文引擎"
sidebarTitle: "上下文引擎"
description: "OpenClaw 核心概念：Context Engine 决定模型每次运行时能看到哪些消息、记忆和压缩摘要。"
---

# Context Engine 上下文引擎

上下文引擎负责回答一个问题：

> 模型这次回复前，应该看到哪些内容？

聊天历史、系统提示词、记忆、工具说明、压缩摘要，都会影响模型回答。
Context Engine 就是整理这些材料的人。

---

## 新手需要改它吗

通常不需要。

OpenClaw 默认使用内置的 `legacy` 引擎，已经能处理大多数场景：

- 保存新消息
- 组装模型输入
- 对过长会话做压缩
- 保留最近消息
- 支持 `/compact`

只有你想换一种上下文组织方式，或者安装了专门的上下文插件，才需要动它。

---

## 它做哪几件事

| 阶段 | 人话解释 |
|------|----------|
| Ingest | 新消息进来时，先记录下来 |
| Assemble | 模型运行前，把该看的内容整理好 |
| Compact | 对话太长时，把旧内容压缩成摘要 |
| After turn | 回复完成后，保存状态或更新索引 |

你可以把它想成开会前的秘书：把历史记录、重点摘要、相关材料都整理成一份会议包。

---

## 插件引擎

高级用户可以安装上下文引擎插件：

```bash
openclaw plugins install <context-engine-plugin>
```

然后在配置里选择：

```json5
{
  plugins: {
    slots: {
      contextEngine: "my-engine",
    },
  },
}
```

改完后重启 Gateway：

```bash
openclaw gateway restart
```

---

## 什么时候该关注它

- 对话很长，模型经常忘事
- 你在调试记忆和压缩
- 你想让子智能体继承父会话上下文
- 你在开发上下文插件
- 你想让 Agent 更稳定地引用长期资料

普通使用者先看 [上下文](/tutorials/concepts/context) 和 [压缩](/tutorials/concepts/compaction) 就够了。

