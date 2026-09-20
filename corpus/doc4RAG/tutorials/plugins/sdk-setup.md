---
title: "SDK Setup"
sidebarTitle: "SDK 设置"
---

# SDK Setup

SDK 设置主要解决：插件项目如何安装依赖、如何引用 OpenClaw SDK、如何让 Gateway 找到插件。

检查清单：

- package 依赖安装完成。
- manifest 指向正确入口。
- 插件目录在加载路径里。
- `plugins.entries.<name>.enabled` 为 true。
- Gateway 重启过。

## 新手路线

本地开发插件时，先做这几步：

```bash
openclaw plugins install ./my-plugin
openclaw plugins list --verbose
openclaw plugins doctor
```

如果列表里看不到插件，先查路径和 manifest。
如果看得到但不能用，再查 runtime 和日志。
