---
title: "openclaw clawbot"
sidebarTitle: "clawbot"
---

# `openclaw clawbot`

`clawbot` 是兼容旧 ClawdBot/ClawBot 相关入口时可能出现的命令。新文档统一使用 OpenClaw。

## 什么时候会看到它

- 从旧版本迁移。
- 老脚本还在调用 ClawBot 名称。
- 排查历史配置或兼容层。

## 新手建议

如果你是新安装，不需要主动使用它。
如果你从旧版本升级，先运行：

```bash
openclaw doctor
openclaw migrate --help
```

## 新手提醒

旧名字出现在路径、配置或日志里不一定代表系统坏了，可能只是兼容层还在工作。
迁移时不要手动重命名一堆状态文件，优先使用官方 migrate 命令和 `doctor`。
