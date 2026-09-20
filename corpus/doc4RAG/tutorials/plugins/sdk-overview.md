---
title: "SDK Overview"
sidebarTitle: "SDK 总览"
---

# SDK Overview

OpenClaw 插件 SDK 给插件提供统一入口，让插件注册工具、通道、provider、hooks 和 runtime helper。

你不用直接改核心代码，也能扩展 OpenClaw。

先学顺序：

1. manifest。
2. setup。
3. runtime。
4. 对应能力 SDK。

## 新手路线

先写最小插件，不要一开始就做完整平台：

1. 一个 `openclaw.plugin.json`。
2. 一个 runtime 入口。
3. 注册一个很小的工具。
4. `openclaw plugins install <path>`。
5. `openclaw plugins doctor`。

跑通后再加 provider、channel 或 hooks。
