---
title: "Vydra"
sidebarTitle: "Vydra"
---

# Vydra

Vydra 可用于图像、视频、TTS 等媒体能力，具体取决于当前插件和 provider 支持。

OpenClaw 的 Vydra 插件常见能力包括图像生成、视频生成和语音合成。provider id 和模型 ref 以 `vydra/` 开头。

配置：

```bash
export VYDRA_API_KEY="..."
```

如果你只是想先体验媒体生成，从 [媒体能力总览](/tutorials/tools/media-overview) 开始更清楚。

## 新手排查

媒体 provider 的失败常常不是“模型不聪明”，而是：

- key 没配置在 Gateway 所在机器。
- 默认图片、视频或 TTS 模型没有指向 Vydra。
- 生成任务还在后台排队。

先看 `openclaw tasks list` 和 `openclaw logs --follow`。
