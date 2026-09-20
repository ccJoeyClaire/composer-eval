---
title: "Media Understanding 媒体理解"
sidebarTitle: "媒体理解"
description: "OpenClaw Nodes：媒体理解会在回复前把图片、音频、视频预处理成文字说明，帮助 Agent 更好理解附件。"
---

# Media Understanding 媒体理解

媒体理解就是：在 Agent 正式回复前，先把图片、音频、视频“翻译”成文字摘要。

这样做有两个好处：

- Agent 更容易理解附件内容。
- 斜杠命令和自动化更容易从媒体里提取指令。

---

## 基本流程

1. 收集入站附件。
2. 判断是图片、音频还是视频。
3. 选择合适的模型或本地 CLI。
4. 处理成功后插入 `[Image]`、`[Audio]` 或 `[Video]` 文本块。
5. 继续正常回复流程。

如果媒体理解失败，原始附件仍会尽量保留，回复链路不会轻易中断。

---

## 配置入口

```json5
{
  tools: {
    media: {
      image: { enabled: true },
      audio: { enabled: true },
      video: { enabled: true },
    },
  },
}
```

也可以对每类媒体设置大小、超时、模型列表和作用范围。

---

## 什么时候要关掉

- 群聊里附件很多，费用容易上涨
- 你不希望自动分析图片或语音
- 你只想把原始附件直接交给主模型
- 你的模型本身已经能直接看图/听音频

禁用音频示例：

```json5
{
  tools: {
    media: {
      audio: { enabled: false },
    },
  },
}
```

