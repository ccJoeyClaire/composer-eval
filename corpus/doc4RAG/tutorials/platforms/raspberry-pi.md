---
title: "Raspberry Pi"
sidebarTitle: "Raspberry Pi"
---

# Raspberry Pi：家里常驻的小网关

Raspberry Pi 适合做低功耗、常在线的家庭 OpenClaw Gateway。

推荐：

- Pi 5 或 Pi 4。
- 2GB+ RAM。
- 64-bit Lite OS。
- 16GB+ 存储，USB SSD 更好。
- 小内存机器加 swap。

安装路线：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
```

继续阅读：[Raspberry Pi 安装](/tutorials/installation/raspberry-pi)。

## 新手提醒

树莓派适合轻量 Gateway，不适合承担所有重活。
模型推理、视频生成、图片生成这类任务最好交给云 provider 或更强的节点。

如果经常卡顿，先检查：

```bash
openclaw status
openclaw logs --follow
free -h
```
