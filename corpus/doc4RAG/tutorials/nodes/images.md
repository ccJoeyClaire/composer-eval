---
title: "图片与媒体"
sidebarTitle: "图片"
description: "OpenClaw Nodes：说明图片、附件、MEDIA 指令和媒体理解在 OpenClaw 回复链路中的作用。"
---

# 图片与媒体

OpenClaw 不只处理文字，也能处理图片、音频、视频和文件。
不同频道对媒体大小和格式有不同限制，所以 OpenClaw 会尽量做统一处理。

---

## 出站媒体

发送媒体时，常见形式是：

```text
MEDIA:/path/to/file.png
```

Agent 回复里出现独立一行 `MEDIA:<path-or-url>` 时，OpenClaw 会尝试把它作为附件发送。

---

## 入站媒体

别人发图片或文件给 OpenClaw 时，OpenClaw 会保存临时路径，并提供变量：

- `{{MediaPath}}`：本地临时文件路径
- `{{MediaUrl}}`：媒体 URL 或伪 URL
- `{{Transcript}}`：音频转写结果

这些变量让命令、工具和 Agent 能继续处理附件。

---

## 媒体理解

如果启用了媒体理解，OpenClaw 可以先把图片、音频、视频转成简短文字说明，再交给 Agent。

例如图片可能变成：

```text
[Image]
这是一张白板照片，包含三条待办事项……
```

详见 [Media Understanding](/tutorials/nodes/media-understanding)。

---

## 注意限制

- 图片可能会被压缩。
- 音频和视频通常有大小上限。
- 不同聊天平台限制不同。
- 大文件处理会增加延迟和费用。

新手先用小图片测试，确认流程正常后再处理大文件。

