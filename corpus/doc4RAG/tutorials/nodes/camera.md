---
title: "节点相机"
sidebarTitle: "相机"
description: "OpenClaw Nodes：通过已配对的 iOS、Android 或 macOS 节点拍照、录短视频，并把结果交给 Agent 使用。"
---

# 节点相机

节点相机让 Agent 可以请求已配对设备拍一张照片，或录一小段视频。
常见场景：看一眼桌面、识别物品、拍白板、记录现场状态。

---

## 能做什么

- `camera.list`：列出可用摄像头
- `camera.snap`：拍照，通常返回 jpg
- `camera.clip`：录短视频，通常返回 mp4

这些能力通过 Gateway 调用节点，不是 Gateway 自己拍照。

---

## 最简单的 CLI 用法

```bash
openclaw nodes camera snap --node <node-id>
openclaw nodes camera snap --node <node-id> --facing front
openclaw nodes camera clip --node <node-id> --duration 3000
```

CLI 会把媒体写到临时文件，并输出类似：

```text
MEDIA:/tmp/openclaw-camera-xxx.jpg
```

Agent 可以把这个文件当作附件继续理解。

---

## 权限要求

相机能力需要设备授权：

- iOS / Android：需要相机权限，录视频带声音时还需要麦克风权限。
- macOS：需要相机权限，录屏/录音还可能需要额外系统权限。
- 移动端通常要求 App 在前台。

如果看到 `NODE_BACKGROUND_UNAVAILABLE`，把节点 App 切回前台再试。

---

## 安全建议

相机是敏感能力。建议：

- 只批准你认识的节点。
- 不要在群聊里默认开放相机能力。
- 第一次使用先手动触发测试。
- 远程节点要配合 Tailscale、VPN 或 SSH 隧道。

