---
title: "Runway"
sidebarTitle: "Runway"
---

# Runway

Runway 主要用于视频生成等媒体能力。

OpenClaw 的 provider id 是 `runway`。官方推荐的环境变量是 `RUNWAYML_API_SECRET`，`RUNWAY_API_KEY` 也可能作为兼容别名被识别。

配置：

```bash
export RUNWAYML_API_SECRET="..."
openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
```

适合：

- 视频创作。
- 图像到视频。
- 创意媒体工作流。

## 新手提醒

Runway 是任务型视频生成：提交任务后需要等待结果，不像普通聊天那样马上返回。
如果任务卡住，先看：

```bash
openclaw tasks list
openclaw logs --follow
```

继续阅读：[视频生成](/tutorials/tools/video-generation)。
