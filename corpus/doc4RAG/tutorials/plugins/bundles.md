---
title: "插件 Bundles"
sidebarTitle: "Bundles"
---

# 插件 Bundles

Bundle 是把一组插件能力一起交付的方式。它适合官方打包、团队内部发行或一组功能共同启用。

比如一个 bundle 可能同时提供：

- 通道插件。
- 工具插件。
- provider 插件。
- 配置 schema。
- 文档和技能。

新手不用手动做 bundle，先学单个插件。

## 什么时候需要 bundle

- 团队要一次性安装一套能力。
- 插件之间有明确配套关系。
- 需要统一发布版本、文档和配置。

如果只是“我想接一个 API”，bundle 反而太重。先写一个原生插件。
