---
title: "构建 Extensions"
sidebarTitle: "Extensions"
---

# 构建 Extensions

Extension 是比普通插件更完整的扩展形态，可能包含插件、前端、配置、文档和运行时代码。

适合：

- 团队内部能力包。
- 一组通道和工具一起交付。
- 需要 UI 或配置页面的扩展。

如果只是接一个 API，先从普通插件开始。

## 新手怎么选

- 只接一个 provider：写 provider 插件。
- 只加一个工具：写 tool 插件。
- 同时要 UI、配置、技能、多个能力：再考虑 extension。

先把小插件跑通，再打包成 extension。这样失败时更容易定位。
