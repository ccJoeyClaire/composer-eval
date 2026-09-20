---
title: "openclaw dashboard"
sidebarTitle: "dashboard"
---

# `openclaw dashboard`

`dashboard` 用来打开 OpenClaw 的 Web 控制台。新手装好以后，通常第一时间就跑它。

```bash
openclaw dashboard
openclaw dashboard --no-open
```

## 什么时候用

- 想打开 Control UI。
- 想查看当前 Gateway 的浏览器入口。
- 不想自动打开浏览器，只想打印 URL。

## 安全提醒

如果 Gateway 使用 token，`dashboard` 会尽量避免把 SecretRef 管理的 token 直接打印到终端或塞进剪贴板。远程服务器上打不开浏览器时，先用：

```bash
openclaw dashboard --no-open
```

继续阅读：[Web 控制台](/tutorials/web/dashboard)。
