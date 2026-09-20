---
title: "openclaw configure"
sidebarTitle: "configure"
---

# `openclaw configure`

`configure` 是配置向导。它适合新手，因为它会按问题一步步问你，而不是让你直接手写一大段 JSON。

```bash
openclaw configure --section model
openclaw configure --section web
openclaw configure --section channels
```

## 什么时候用

- 你要配置模型 API Key、base URL 或默认模型。
- 你要配置 Web 控制台、Gateway 地址或 token。
- 你要开启插件、技能、通道等某个模块。
- 你不确定配置项写在哪里。

## 常见 section

- `model`：模型 provider、模型名、API Key。
- `web`：Web 控制台和 Gateway 连接。
- `channels`：聊天通道相关配置。
- `plugins`：插件安装和启用。
- `gateway`：Gateway 运行位置和连接方式。
- `daemon`：后台服务安装。
- `skills`：技能配置。
- `health`：健康检查相关设置。

## 新手建议

能用 `configure` 就先用它。手写配置适合熟悉以后再做。配置完之后运行：

```bash
openclaw doctor
openclaw status
```

如果 `doctor` 提示有可修复项，先看提示，再决定是否执行：

```bash
openclaw doctor --fix
```

继续阅读：[配置总览](/tutorials/gateway/configuration-reference)。
