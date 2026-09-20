---
title: "SenseAudio"
sidebarTitle: "SenseAudio"
---

# SenseAudio

SenseAudio 是语音识别相关 provider 之一，适合音频转文字和语音输入场景。

使用前确认：

- API Key 已配置。
- 目标通道支持音频附件。
- OpenClaw 的媒体理解或音频路径已启用。

## 新手排查

语音识别链路通常有三段：

1. 通道收到了音频文件。
2. OpenClaw 能下载或读取这个音频。
3. SenseAudio 能把音频转成文字。

任何一段断了，最终都像“机器人没听懂”。先看 `openclaw logs --follow`，确认音频是否真的进了 Gateway。

继续阅读：[节点音频](/tutorials/nodes/audio)。
