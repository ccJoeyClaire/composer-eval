---
title: "Voice Call"
sidebarTitle: "Voice Call"
---

# Voice Call 插件

Voice Call 插件用于实时语音通话、流式 STT/TTS 和电话类场景。

它比普通 TTS 更复杂，因为它涉及：

- 实时音频流。
- 低延迟转写。
- 中途打断。
- 语音回复。
- 通话状态。

先理解 [TTS](/tutorials/tools/tts) 和 [节点音频](/tutorials/nodes/audio)，再做 Voice Call。

## 新手排查

语音通话链路很长，至少包含：电话入口、STT、Agent、TTS、音频返回。
一段失败，用户听起来就是“没反应”。

先看：

```bash
openclaw voicecall status --json
openclaw logs --follow
```
