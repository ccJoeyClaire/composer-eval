---
title: "fal"
sidebarTitle: "fal"
---

# fal

fal 常用于图像和视频生成模型。OpenClaw 可以通过它调用多种媒体生成能力。

provider id 是 `fal`。官方推荐环境变量是 `FAL_KEY`，部分环境也兼容 `FAL_API_KEY`。

配置：

```bash
export FAL_KEY="..."
```

适合：

- 快速试用不同图像/视频模型。
- 不想自己维护 GPU。
- 媒体生成实验。

## 新手验证

先确认默认图片或视频模型是否指向 fal：

```bash
openclaw config get agents.defaults.imageGenerationModel
openclaw config get agents.defaults.videoGenerationModel
```

生成失败时看 `openclaw tasks list`，因为媒体生成常常是后台任务。

继续阅读：[图像生成](/tutorials/tools/image-generation)、[视频生成](/tutorials/tools/video-generation)。
