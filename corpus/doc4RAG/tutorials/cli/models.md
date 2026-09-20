---
title: "openclaw models"
sidebarTitle: "models"
---

# `openclaw models`

`models` 用来列出、检查和切换模型。模型问题常常不是 OpenClaw 坏了，而是 provider、API Key、base URL、模型名或额度其中一项不对。

```bash
openclaw models list
openclaw models status
openclaw models set <provider/model>
```

## 什么时候用

- 想看当前可用模型。
- 想切换默认模型。
- 模型不回复或报 401/403/404。
- 想确认 provider 是否能连通。

## 新手排查顺序

1. API Key 有没有填。
2. provider 名称是否正确。
3. 模型名是否真实存在。
4. base URL 是否写错。
5. 账号是否还有额度。

配置入口：

```bash
openclaw configure --section model
```

继续阅读：[模型提供商](/tutorials/providers/)。
