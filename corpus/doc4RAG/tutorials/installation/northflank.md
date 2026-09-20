---
title: "Northflank 部署"
sidebarTitle: "Northflank"
---

# Northflank 部署 OpenClaw

Northflank 适合想“一键部署云端 Gateway”，但不想自己 SSH 到服务器上配置太多东西的用户。

---

## 你会得到什么？

- 云端 OpenClaw Gateway。
- 浏览器 Control UI。
- 挂载到 `/data` 的持久卷。
- `openclaw.json`、凭据、会话、工作区等状态随 redeploy 保留。

---

## 快速步骤

1. 打开 Northflank 的 OpenClaw 模板。
2. 登录或注册 Northflank。
3. 点击部署。
4. 设置 `OPENCLAW_GATEWAY_TOKEN`，用强随机值。
5. 等部署完成。
6. 打开服务 URL 的 `/openclaw`。
7. 用刚才设置的 token 连接。

---

## 安全提醒

`OPENCLAW_GATEWAY_TOKEN` 是管理员级秘密。
不要发到群里，也不要写进公开仓库。

云端部署一定要确认：

- 有持久卷。
- 有认证。
- 不把管理口裸奔开放。
- 定期备份状态。

---

## 下一步

- 先打开 [Web 控制 UI](/tutorials/web/)。
- 再接 [Telegram](/tutorials/channels/telegram) 或 [Discord](/tutorials/channels/discord)。
- 定期看 [更新说明](/tutorials/installation/updating)。

