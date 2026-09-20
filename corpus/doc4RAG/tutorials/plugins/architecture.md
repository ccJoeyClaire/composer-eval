---
title: "插件架构"
sidebarTitle: "插件架构"
---

# 插件架构

OpenClaw 插件把能力放在清晰边界里：插件声明自己提供什么，Gateway 决定是否加载，运行时再注册通道、工具、provider 或 hooks。

这样做的好处是：核心不必知道每个服务细节，第三方也能扩展能力。

关键概念：

- manifest-first：先读 `openclaw.plugin.json`。
- capability：共享能力契约。
- runtime：插件真正注册能力的代码。
- policy：Gateway 统一控制权限和加载范围。

