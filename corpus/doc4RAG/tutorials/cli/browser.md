---
title: "openclaw browser"
sidebarTitle: "browser"
---

# `openclaw browser`

`browser` 用来调试或控制 OpenClaw 浏览器能力，包括启动浏览器、打开网页、查看 tabs、截图、snapshot 和排查 CDP 连接。

```bash
openclaw browser profiles
openclaw browser start
openclaw browser open https://example.com
openclaw browser snapshot
openclaw browser doctor
```

## 什么时候用

- 浏览器工具启动失败。
- Agent 无法打开网页或拿不到页面内容。
- 想测试某个 browser profile。
- 想通过节点上的浏览器执行自动化。

## 新手排查顺序

```bash
openclaw browser doctor
openclaw browser start
openclaw browser tabs
```

高级接口见 [Browser Control API](/tutorials/tools/browser-control)。
