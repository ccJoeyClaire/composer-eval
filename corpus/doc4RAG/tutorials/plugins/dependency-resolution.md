---
title: "插件依赖解析"
sidebarTitle: "依赖解析"
---

# 插件依赖解析

插件可能依赖其他包、SDK 或能力。OpenClaw 需要在加载前判断依赖是否可用。

排查方向：

- 依赖包是否安装。
- 插件路径是否正确。
- 版本是否兼容。
- source checkout 是否执行过依赖安装。
- 打包版是否包含该插件。

不要把依赖错误误认为“通道坏了”。先看 Gateway 启动日志。

## 新手排查顺序

```bash
openclaw plugins inspect <id>
openclaw plugins doctor
openclaw logs --follow
```

如果是本地插件，确认你在插件目录安装过依赖，并且 `openclaw.plugin.json` 指向的入口文件真实存在。
如果是 npm 或 ClawHub 插件，确认安装记录没有损坏。
