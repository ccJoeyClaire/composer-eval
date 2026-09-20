---
title: "构建插件"
sidebarTitle: "构建插件"
---

# 构建插件

构建插件的最小路线：

1. 创建插件目录。
2. 写 `openclaw.plugin.json`。
3. 写 runtime 入口。
4. 注册一个能力。
5. 启用插件。
6. 重启 Gateway。
7. 用 `openclaw plugins list` 验证。

不要一开始就写大插件。先做一个只注册小工具或小 hook 的插件，跑通加载流程。

## 最小成功标准

一个新插件至少要做到：

- `openclaw plugins list` 能看到。
- `openclaw plugins inspect` 能读 manifest。
- `openclaw plugins doctor` 不报加载错误。
- 调用一次能力能返回清楚结果。

先让最小插件站起来，再慢慢加配置、权限和错误处理。
