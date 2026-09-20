---
title: "Google Gemini"
sidebarTitle: "Google"
---

# Google Gemini

Google/Gemini 可用于文本、图像理解、图像生成、视频生成、音乐和语音等多种能力。

provider id 是 `google`。常见认证方式有 API key，也可以在某些场景复用 Gemini CLI OAuth。

配置：

```bash
export GEMINI_API_KEY="..."
```

或：

```bash
export GOOGLE_API_KEY="..."
```

验证：

```bash
openclaw configure --section model
openclaw models list --provider google
```

新手先用聊天模型跑通 WebChat，再逐步开启媒体理解、图像、视频、TTS 或网页搜索能力。

## 常见坑

- `GEMINI_API_KEY` 和 `GOOGLE_API_KEY` 都可用，但不要两个地方填出冲突值。
- OAuth 路线更适合熟悉 Gemini CLI 的用户。
- 多媒体能力通常还要看对应工具或插件是否启用。
