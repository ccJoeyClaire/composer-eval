---
title: "Releasing"
sidebarTitle: "发布流程"
---

# Releasing

发布流程是维护者参考，用来说明 OpenClaw 如何打包、验证、发布新版本。

普通用户升级只需要：

```bash
openclaw update
openclaw doctor
openclaw gateway restart
```

## 谁需要读

- 维护者：确认版本号、构建、测试、发布渠道和回滚方案。
- 插件作者：确认 SDK 或 manifest 有没有破坏性变化。
- 普通用户：通常不需要读发布流程，只要按更新教程升级。

## 新手怎么理解

发布不是“把代码推上去”这么简单。它还要确认文档能构建、插件能加载、常见通道能跑、升级后 `doctor` 不报关键错误。

继续阅读：[更新 OpenClaw](/tutorials/installation/updating)。
