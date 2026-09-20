---
title: "Linux"
sidebarTitle: "Linux"
---

# Linux：服务器和 VPS 的主力平台

Linux 适合把 OpenClaw 跑成 24 小时在线的 Gateway。

推荐：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
```

远程访问控制 UI 推荐 SSH 隧道：

```bash
ssh -N -L 18789:127.0.0.1:18789 user@server
```

然后本机打开：

```text
http://127.0.0.1:18789/
```

Linux 上注意内存压力。小 VPS 容易 OOM，建议留 swap，避免同时跑太多重任务。

## 新手提醒

Linux 最适合长期在线，但也最容易因为公网暴露而出安全问题。

建议：

- Gateway 只绑定本机或可信内网。
- 远程访问用 SSH tunnel、Tailscale 或反向代理加认证。
- 定期跑 `openclaw update` 和 `openclaw doctor`。
- 小机器不要同时跑视频生成、本地模型和大量 cron。
