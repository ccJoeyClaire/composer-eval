---
title: "ElevenLabs"
sidebarTitle: "ElevenLabs"
---

# ElevenLabs

ElevenLabs 主要用于语音能力，尤其是 TTS 和语音体验。

它不是普通聊天模型，而是语音 provider。你通常会在消息 TTS、语音通道或 Voice Call 场景里用到它。

配置：

```bash
export ELEVENLABS_API_KEY="..."
```

适合：

- 想要更自然的语音回复。
- 需要多声音、多语种。
- 语音通道或 Talk 场景。

## 新手排查

先确认三件事：

1. API Key 在 Gateway 运行环境中可见。
2. TTS provider 已经指向 ElevenLabs。
3. 目标通道支持音频或语音消息。

继续阅读：[TTS 文字转语音](/tutorials/tools/tts)。
