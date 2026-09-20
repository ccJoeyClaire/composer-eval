---
title: "Message Presentation"
sidebarTitle: "消息呈现"
---

# Message Presentation

不同聊天平台支持的格式不同。插件需要把 Agent 输出转成适合该平台的消息。

需要考虑：

- Markdown 差异。
- 附件。
- 线程。
- 编辑消息。
- 语音和图片。
- 长消息切分。

这就是为什么 OpenClaw 不把所有通道都当成纯文本管道。

## 新手例子

同一条“任务完成”消息：

- 在 Slack 里可能是 block + button。
- 在 Telegram 里可能是 Markdown + 附件。
- 在 Discord 里可能是 embed。

插件要做的，就是把 OpenClaw 的统一输出翻译成这些平台各自舒服的格式。
