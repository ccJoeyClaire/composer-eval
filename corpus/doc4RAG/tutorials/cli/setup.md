---
title: "openclaw setup"
sidebarTitle: "setup"
---

# `openclaw setup`

`setup` 是安装后或特定功能前的设置入口。很多新手场景已经被 `onboard` 和 `configure` 覆盖。

## 新手怎么选

- 第一次安装后台服务：`openclaw onboard --install-daemon`
- 配置模型、通道、Web：`openclaw configure`
- 文档明确要求 setup：按该页面上下文执行 `openclaw setup`

## 排障

如果 setup 后仍然不能用，先不要反复跑：

```bash
openclaw doctor
openclaw status
openclaw logs --follow
```
