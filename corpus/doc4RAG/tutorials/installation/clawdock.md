---
title: "ClawDock"
sidebarTitle: "ClawDock"
description: "OpenClaw 安装部署：ClawDock 是 Docker 安装的 shell 辅助工具，简化启动、日志、控制台和配对命令。"
---

# ClawDock

ClawDock 是给 Docker 用户准备的一组 shell 辅助命令。
它不是新的 OpenClaw 版本，而是把很长的 `docker compose ...` 命令变短。

---

## 适合谁

- 你经常用 Docker 跑 OpenClaw。
- 你不想每次都输入长命令。
- 你需要快速打开 dashboard、看日志、批准设备。

如果你还没用 Docker，先看 [Docker 部署](/tutorials/installation/docker)。

---

## 安装辅助脚本

```bash
mkdir -p ~/.clawdock
curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh \
  -o ~/.clawdock/clawdock-helpers.sh
echo 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc
source ~/.zshrc
```

---

## 常用命令

| 命令 | 作用 |
|------|------|
| `clawdock-start` | 启动 Gateway 容器 |
| `clawdock-stop` | 停止 Gateway 容器 |
| `clawdock-restart` | 重启 |
| `clawdock-logs` | 看日志 |
| `clawdock-dashboard` | 打开控制 UI |
| `clawdock-devices` | 查看待配对设备 |
| `clawdock-approve <id>` | 批准配对 |

---

## 第一次使用

```bash
clawdock-start
clawdock-dashboard
```

如果控制台要求配对：

```bash
clawdock-devices
clawdock-approve <request-id>
```

