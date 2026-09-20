---
title: "Music Generation"
sidebarTitle: "音乐生成"
---

# Music Generation：让 Agent 生成音乐或音频片段

`music_generate` 可以根据文字提示生成音乐。它通常用于背景音乐、短音频、氛围片段或创意草稿。

---

## 支持哪些提供商？

官方能力目前主要围绕：

- Google Lyria。
- MiniMax Music。
- ComfyUI 工作流。

不同提供商支持的歌词、纯音乐、时长、格式和参考输入不一样。

---

## 快速配置

准备至少一个提供商的认证：

```bash
export GEMINI_API_KEY="..."
export MINIMAX_API_KEY="..."
```

可选设置默认模型：

```json5
{
  agents: {
    defaults: {
      musicGenerationModel: {
        primary: "google/lyria-3-clip-preview"
      }
    }
  }
}
```

---

## 怎么使用？

直接说：

```text
生成一段温暖的钢琴背景音乐，不要人声，适合教程视频开头。
```

如果工具可用，Agent 会自动调用 `music_generate`。

---

## 同步和异步

共享提供商通常是异步任务：先提交，生成完再通知。
某些 ComfyUI 本地工作流可能同步返回。

查看任务：

```bash
openclaw tasks list
openclaw tasks show <taskId>
```

---

## 继续阅读

- [媒体能力总览](/tutorials/tools/media-overview)
- [视频生成](/tutorials/tools/video-generation)
- [TTS 文字转语音](/tutorials/tools/tts)

