---
title: "Video Generation"
sidebarTitle: "视频生成"
---

# Video Generation：生成视频时，OpenClaw 会先排队再通知

`video_generate` 可以让 Agent 生成短视频。视频比图片慢很多，所以 OpenClaw 会把它当成后台任务处理。

你可以把它想成洗衣机：按下开始后不用站在旁边等，洗好会提醒你。

---

## 支持哪些输入？

根据提供商不同，可能支持：

- 文本生成视频。
- 图片生成视频。
- 视频参考生成视频。

常见提供商包括 Google、OpenAI、MiniMax、fal、BytePlus、Alibaba、ComfyUI、DeepInfra 等。

---

## 快速配置

至少准备一个视频提供商的 API Key，例如：

```bash
export GEMINI_API_KEY="..."
export OPENAI_API_KEY="..."
export MINIMAX_API_KEY="..."
```

可选设置默认模型：

```bash
openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
```

---

## 异步任务怎么走？

当 Agent 调用 `video_generate`：

1. OpenClaw 把任务提交给提供商。
2. 立刻记录一个 task id。
3. 提供商在后台生成视频。
4. 完成后，OpenClaw 唤醒同一个会话。
5. Agent 告诉用户视频已完成，并附上文件或链接。

查看任务：

```bash
openclaw tasks list
openclaw tasks show <taskId>
openclaw tasks cancel <taskId>
```

---

## 常见状态

| 状态 | 意思 |
|------|------|
| `queued` | 已排队 |
| `running` | 提供商正在生成 |
| `succeeded` | 成功，可以发送结果 |
| `failed` | 失败，需要看错误 |

---

## 新手建议

先用 5 秒、低分辨率、小尺寸测试。
视频生成费用和等待时间都比图片更高，不要一开始就生成很长的视频。

---

## 继续阅读

- [媒体能力总览](/tutorials/tools/media-overview)
- [图像生成](/tutorials/tools/image-generation)
- [任务自动化](/tutorials/automation/tasks)

