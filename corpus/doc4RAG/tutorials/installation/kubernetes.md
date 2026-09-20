---
title: "Kubernetes 部署"
sidebarTitle: "Kubernetes"
description: "OpenClaw 安装部署：在 Kubernetes 集群里运行 Gateway 的最小思路。"
---

# Kubernetes 部署

Kubernetes 适合团队或已有集群的用户。
如果你只是个人第一次体验，不建议从这里开始。

---

## 你需要什么

- 一个可用 Kubernetes 集群
- `kubectl`
- 至少一个模型 API Key
- 持久化存储 PVC
- Gateway token

---

## 最小结构

```text
Namespace: openclaw
├── Deployment/openclaw
├── Service/openclaw
├── PVC
├── ConfigMap/openclaw-config
└── Secret/openclaw-secrets
```

OpenClaw 本身是单进程 Gateway，Kubernetes 主要负责长期运行、配置和持久化。

---

## 本地访问

```bash
kubectl port-forward svc/openclaw 18789:18789 -n openclaw
```

然后打开：

```text
http://localhost:18789/
```

---

## 安全提醒

- API Key 放到 Secret，不要写进 ConfigMap。
- `~/.openclaw` 状态要持久化。
- 外部访问要有 HTTPS 和认证。
- 更新前先备份 PVC。

官方示例使用 Kustomize 思路，不一定适合所有生产集群。团队环境建议让熟悉 Kubernetes 的同事一起评审。

