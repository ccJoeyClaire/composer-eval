---
title: "Render 部署"
sidebarTitle: "Render"
---

# Render 部署 OpenClaw

Render 可以用 Blueprint 部署 OpenClaw。Blueprint 像一张云端施工图，服务、磁盘、环境变量都写在 YAML 里。

---

## 适合谁？

适合：

- 想用 Docker 云部署。
- 喜欢基础设施配置可版本化。
- 需要持久磁盘。
- 想从 Dashboard 看日志和打开 Shell。

---

## Blueprint 里通常有什么？

示意：

```yaml
services:
  - type: web
    name: openclaw
    runtime: docker
    healthCheckPath: /health
    envVars:
      - key: OPENCLAW_GATEWAY_PORT
        value: "8080"
      - key: OPENCLAW_STATE_DIR
        value: /data/.openclaw
      - key: OPENCLAW_WORKSPACE_DIR
        value: /data/workspace
      - key: OPENCLAW_GATEWAY_TOKEN
        generateValue: true
    disk:
      name: openclaw-data
      mountPath: /data
      sizeGB: 1
```

---

## Free plan 注意

免费计划适合测试，但可能没有持久磁盘或会休眠。
长期使用建议选择带持久磁盘的 plan。

否则每次 redeploy 后，OpenClaw 状态可能重置。

---

## 部署后

打开：

```text
https://<service-name>.onrender.com/
```

使用 `OPENCLAW_GATEWAY_TOKEN` 连接控制 UI。
token 可在 Render Dashboard 的 Environment 中查看。

---

## 继续阅读

- [Docker 部署](/tutorials/installation/docker)
- [Gateway 安全说明](/tutorials/gateway/security)
- [更新 OpenClaw](/tutorials/installation/updating)

