---
title: "插件 Manifest"
sidebarTitle: "Manifest"
---

# 插件 Manifest：插件的身份证

`openclaw.plugin.json` 是插件的身份证。它告诉 OpenClaw：

- 插件叫什么。
- 版本是多少。
- 提供哪些能力。
- 需要哪些入口文件。
- 有哪些配置项。
- 是否有 hooks、tools、channels 或 providers。

没有 manifest，Gateway 就不知道该不该信任和加载这个插件。

## 新手先看哪些字段

- `id`：插件唯一名字。
- `version`：插件版本。
- `runtime`：真正执行注册的入口。
- `configSchema`：用户可以配置什么。
- `capabilities`：插件提供哪些能力。

manifest 写清楚，Control UI、doctor、插件列表和安全检查才有东西可读。
