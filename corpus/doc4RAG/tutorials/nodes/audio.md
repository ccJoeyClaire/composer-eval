---
title: "音频与语音消息"
sidebarTitle: "音频"
description: "OpenClaw Nodes：解释入站音频、语音消息、转写和 Transcript 在回复链路中的作用。"
---

# 音频与语音消息

OpenClaw 可以处理语音消息和音频附件。
如果配置了音频理解，它会先把音频转成文字，再交给 Agent。

---

## 处理流程

1. 收到音频附件。
2. 下载到本地临时文件，或读取已有本地路径。
3. 检查文件大小是否超过限制。
4. 选择可用的转写模型或本地 CLI。
5. 转写成功后，把 `{{Transcript}}` 填好。
6. Agent 用转写文本理解用户意思。

如果转写失败，OpenClaw 会尽量继续保留原始附件，不会因为一次转写失败就直接中断整个回复链路。

---

## 自动检测

如果你没有手动配置，OpenClaw 会尽量自动寻找可用方式，例如：

- 当前模型是否支持音频
- 本地是否有 Whisper 类 CLI
- 是否配置了 OpenAI、Deepgram、Google、Mistral 等可转写服务

想禁用音频理解：

```json5
{
  tools: {
    media: {
      audio: { enabled: false },
    },
  },
}
```

---

## 什么时候需要配置

- 语音消息经常很长
- 想指定某个转写提供商
- 群聊里不想自动转写所有语音
- 想限制音频文件大小或超时时间

更完整的媒体入口看 [Media Understanding](/tutorials/nodes/media-understanding)。

