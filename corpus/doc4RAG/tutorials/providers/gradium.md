---
title: "Gradium"
sidebarTitle: "Gradium"
---

# Gradium

Gradium 是 OpenClaw 支持的语音相关 provider 之一，常用于 TTS 场景。

配置时先准备平台 API Key，再在对应插件或 provider 配置中启用。

如果你只是想先听到语音回复，优先从 [TTS 文字转语音](/tutorials/tools/tts) 的通用流程开始。

## 新手提醒

TTS provider 只负责“把文字变成声音”。要让声音发出去，还需要通道支持音频消息，或 Voice Call 这类语音通路已经配置好。

排查顺序：

```bash
openclaw doctor
openclaw logs --follow
openclaw plugins list
```
