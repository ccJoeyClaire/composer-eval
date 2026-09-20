---
title: "openclaw security"
sidebarTitle: "security"
---

# `openclaw security`

`security` 用来检查 OpenClaw 的安全设置。它会提醒你哪些地方太宽松，比如 Gateway 没有鉴权、群聊权限太开放、插件没有锁版本、日志可能泄漏敏感信息。

常用方向：

```bash
openclaw security audit
openclaw security audit --deep
openclaw security audit --fix
openclaw security audit --json
```

## 什么时候用

- 第一次把 OpenClaw 放到服务器上。
- 开启新通道、新插件、新工具以后。
- 升级前后做一次安全巡检。
- 准备让团队多人共用时。

## 新手怎么跑

先只审计，不自动修改：

```bash
openclaw security audit
```

如果想做更深入检查：

```bash
openclaw security audit --deep
```

确认提示以后，再考虑自动修复：

```bash
openclaw security audit --fix
```

## `--fix` 不会做什么

它不会帮你轮换 API Key，不会替你关掉所有工具，也不会删除插件。它只做相对安全、确定性的修复，比如收紧文件权限、修正部分过宽的策略、打开敏感信息脱敏。

继续阅读：[安全加固](/tutorials/gateway/security)。
