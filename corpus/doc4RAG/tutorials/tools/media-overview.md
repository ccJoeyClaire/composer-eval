---
title: "Media Overview"
sidebarTitle: "媒体能力总览"
---

# 媒体能力总览：图片、视频、音乐、语音和理解

OpenClaw 不只会聊天。配置好提供商后，它可以生成图片、视频、音乐，把文字转成语音，也可以理解用户发来的图片、音频和视频。

::: tip Live speech 走 Talk，不走一次性媒体工具
实时语音对话请优先看 [Talk Mode](/tutorials/nodes/talk)。

Talk 有三种模式：provider-native `realtime`、本地或流式 `stt-tts`、只转写不回答的 `transcription`。
这些模式和电话、会议、浏览器实时语音、原生 push-to-talk 共用 Talk event 和 session 语义。
:::

---

## 能力地图

| 能力 | 工具或页面 | 说明 |
|------|------------|------|
| 图片生成 | [Image Generation](/tutorials/tools/image-generation) | 文字生成图、参考图编辑 |
| 视频生成 | [Video Generation](/tutorials/tools/video-generation) | 异步生成视频 |
| 音乐生成 | [Music Generation](/tutorials/tools/music-generation) | 生成音乐或音频 |
| 文字转语音 | [TTS](/tutorials/tools/tts) | 把回复变成语音 |
| 媒体理解 | [媒体理解](/tutorials/nodes/media-understanding) | 理解图片、音频、视频 |
| 语音输入 | [节点音频](/tutorials/nodes/audio) | 语音识别和音频输入 |
| 实时语音对话 | [Talk Mode](/tutorials/nodes/talk) | 浏览器 realtime、原生 push-to-talk、transcription |

---

## 同步和异步

| 能力 | 通常模式 |
|------|----------|
| 图片生成 | 同步 |
| TTS | 同步 |
| 视频生成 | 异步任务 |
| 音乐生成 | 多数为异步任务 |

异步任务会先返回 task id，完成后再唤醒会话。

---

## 配置原则

1. 先只开一种能力。
2. 先用低成本模型测试。
3. 群聊里谨慎开启自动媒体输出。
4. 生成视频和音乐要注意费用。
5. 入站媒体理解要注意隐私。

---

## 新手路线

推荐顺序：

1. 先配置普通聊天模型。
2. 再配置图片理解或 PDF。
3. 再尝试图片生成。
4. 最后再开视频、音乐和 TTS。
5. 如果要做实时语音对话，走 Talk Mode，不要把它当普通音频附件处理。

一步一步来，出问题好排查。
