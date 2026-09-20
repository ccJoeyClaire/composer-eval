---
title: "ComfyUI"
sidebarTitle: "ComfyUI"
---

# ComfyUI

ComfyUI 常用于本地图像、视频或音乐工作流。OpenClaw 可以把它作为媒体能力后端。

ComfyUI 路线是 workflow-driven：OpenClaw 不会替你猜图里每个节点是什么意思，你需要准备 workflow JSON，并告诉 OpenClaw 哪个节点接收 prompt、哪个节点产出结果。

适合：

- 你已经会运行 ComfyUI。
- 想使用自定义 workflow。
- 想把生成能力留在自己的机器或工作站。

常见认证：

```bash
export COMFY_API_KEY="..."
export COMFY_CLOUD_API_KEY="..."
```

## 新手提醒

如果你还不会单独运行 ComfyUI，先不要把它作为第一个媒体 provider。
先在 ComfyUI 自己的界面里跑通 workflow，再接入 OpenClaw。

常见本地地址是 `http://127.0.0.1:8188`，但服务器部署时要注意 SSRF 和内网访问边界。

继续阅读：[媒体能力总览](/tutorials/tools/media-overview)。
