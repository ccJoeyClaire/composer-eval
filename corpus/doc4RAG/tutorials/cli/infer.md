---
title: "openclaw infer"
sidebarTitle: "infer"
---

# `openclaw infer`

`infer` 是面向脚本的推理入口。它可以直接跑模型、图片、音频转录、TTS、网页搜索、embedding 等 provider 能力。

```bash
openclaw infer model run --prompt "Say hello"
openclaw infer image generate --prompt "a clean icon"
openclaw infer audio transcribe --file ./voice.wav
openclaw infer web search --query "OpenClaw"
```

## 什么时候用

- 想绕过聊天界面，直接测试 provider。
- 写自动化脚本，需要稳定 JSON 输出。
- 排查模型、图片、音频、TTS、搜索能力是否可用。

## 新手排障

如果 WebChat 不回复，可以先确认模型是否能 infer：

```bash
openclaw infer model run --prompt "ping"
openclaw models status
```

如果 infer 也失败，问题多半在 provider 配置、凭据、网络或额度。
