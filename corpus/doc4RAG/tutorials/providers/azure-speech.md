---
title: "Azure Speech"
sidebarTitle: "Azure Speech"
---

# Azure Speech

Azure Speech 常用于 TTS 或语音识别。它不是普通聊天模型，而是语音能力 provider。

你通常需要：

```bash
export AZURE_SPEECH_KEY="..."
export AZURE_SPEECH_REGION="..."
```

适合：

- 企业已有 Azure 账号。
- 想使用 Microsoft 语音。
- 需要稳定的 TTS/STT 服务。

## 新手排查

Azure Speech 至少要同时匹配 key 和 region。常见错误是 key 来自 `eastus`，配置里却写了另一个 region。

语音输出还要看 `messages.tts` 配置和目标通道支持的音频格式。Voice Call 等电话场景可能需要更低采样率或特定编码。

继续阅读：[TTS 文字转语音](/tutorials/tools/tts)、[节点音频](/tutorials/nodes/audio)。
