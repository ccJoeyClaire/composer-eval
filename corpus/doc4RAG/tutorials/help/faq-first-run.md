---
title: "首次运行 FAQ"
sidebarTitle: "首次运行 FAQ"
---

# 首次运行 FAQ

## 第一次应该跑哪个命令？

推荐：

```bash
openclaw onboard --install-daemon
openclaw dashboard
```

第一个命令安装并配置后台 Gateway，第二个命令打开控制 UI。

## 没反应怎么办？

按顺序检查：

```bash
openclaw doctor
openclaw gateway status
openclaw logs --follow
```

## 我应该先接哪个通道？

先用 WebChat。能回复后，再接 Telegram。不要第一步就挑战最复杂的通道。

## 我需要先懂架构吗？

不需要。第一次只记住三件事：

1. Gateway 要在线。
2. 至少一个模型要可用。
3. 先用 WebChat 测通，再接外部通道。

等你能稳定收到回复，再学习插件、节点、记忆和自动化。
