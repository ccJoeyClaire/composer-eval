---
title: "插件清单"
sidebarTitle: "插件清单"
---

# 插件清单

插件清单是 Gateway 知道“当前有哪些插件可用”的来源之一。

团队环境常用它来控制：

- 哪些插件允许加载。
- 哪些插件来自官方。
- 哪些插件来自本地工作区。
- 哪些插件来自第三方。

如果 `plugins.allow` 被设置，它通常是限制清单，不在里面的插件会被故意挡住。

## 排查口诀

插件明明安装了但不生效时，先看三样：

```bash
openclaw plugins list --verbose
openclaw config get plugins.allow
openclaw plugins doctor
```

团队环境里，清单和 allowlist 往往是故意的安全边界，不要直接删掉。

如果你是管理员，建议把“为什么允许这些插件”写进团队文档。半年后排查问题时，清单不只是配置，也是审计线索。
