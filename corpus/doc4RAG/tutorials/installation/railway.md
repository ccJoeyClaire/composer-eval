---
title: "Railway 部署"
sidebarTitle: "Railway"
---

# Railway 部署 OpenClaw

Railway 适合想用一键模板跑云端 OpenClaw 的用户。它会帮你跑 Gateway，你通过浏览器访问 Control UI。

---

## 新手清单

1. 使用 Railway OpenClaw 模板部署。
2. 添加 Volume，挂载到 `/data`。
3. 设置 `OPENCLAW_GATEWAY_PORT=8080`。
4. 设置 `OPENCLAW_GATEWAY_TOKEN`。
5. 开启 HTTP Proxy，端口 `8080`。
6. 打开：

```text
https://<your-railway-domain>/openclaw
```

---

## 推荐环境变量

```text
OPENCLAW_GATEWAY_PORT=8080
OPENCLAW_GATEWAY_TOKEN=<strong random token>
OPENCLAW_STATE_DIR=/data/.openclaw
OPENCLAW_WORKSPACE_DIR=/data/workspace
```

Volume 很重要。没有持久卷，重部署后状态可能丢失。

---

## 备份

部署稳定后，定期备份：

```bash
openclaw backup create
```

备份应包含配置、auth profiles、会话状态和工作区。

---

## 继续阅读

- [Web 控制 UI](/tutorials/web/)
- [Gateway 安全说明](/tutorials/gateway/security)
- [更新 OpenClaw](/tutorials/installation/updating)

