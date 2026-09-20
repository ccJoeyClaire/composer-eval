---
title: "macOS"
sidebarTitle: "macOS"
---

# macOS：最适合个人桌面体验的平台

macOS 可以运行 Gateway，也可以通过伴生 App 提供本机能力，比如通知、屏幕、摄像头、Canvas 和系统命令。

推荐路线：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
openclaw dashboard
```

macOS 后台服务通常由 LaunchAgent 管理。普通用户不需要手写 launchd 配置，向导会处理。

如果要让远程 Gateway 使用这台 Mac 的能力，可以把 Mac 作为 Node 接入。

## 什么时候选 macOS

- 你主要在个人电脑上使用 OpenClaw。
- 想用桌面能力、通知、屏幕、摄像头或浏览器。
- 想先体验完整交互，再决定是否搬到服务器。

如果 Mac 休眠，Gateway 或节点能力也可能中断。长期在线场景要调整电源和睡眠设置。
