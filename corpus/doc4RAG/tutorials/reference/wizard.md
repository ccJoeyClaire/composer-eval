---
title: "Wizard Reference"
sidebarTitle: "Wizard 参考"
---

# Wizard Reference

Wizard 是安装和配置向导。它负责带你完成模型、Gateway、通道、技能和后台服务配置。

推荐命令：

```bash
openclaw onboard --install-daemon
```

继续阅读：[命令行向导安装](/tutorials/getting-started/wizard)。

## Wizard 会问什么

通常会围绕这些问题：

- Gateway 运行在哪里。
- 使用哪个模型 provider。
- 是否安装后台服务。
- 是否配置 Web 控制台。
- 是否接入通道、插件或技能。

## 新手提醒

向导不是魔法，它只是帮你少手写配置。跑完后仍然要做一次体检：

```bash
openclaw doctor
openclaw status
```
