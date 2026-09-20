---
title: "Rich Output Protocol"
sidebarTitle: "富输出协议"
---

# Rich Output Protocol

富输出协议描述 Agent 如何返回不只是纯文本的内容，例如文件、图片、音频、视频、diff、卡片或结构化结果。

通道插件需要把这些输出翻译成目标平台支持的格式。

继续阅读：[消息呈现](/tutorials/plugins/message-presentation)。

## 新手例子

同一段 Agent 输出，在不同通道里长得不一样：

- Telegram 可以发文本、图片、文件。
- Slack 可以发 block、按钮、线程回复。
- Discord 可以发 embed、附件、反应。

富输出协议就是中间的统一描述，让插件再翻译成各平台自己的样子。
