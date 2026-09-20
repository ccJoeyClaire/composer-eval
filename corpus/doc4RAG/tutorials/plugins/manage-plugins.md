---
title: "管理插件"
sidebarTitle: "管理插件"
---

# 管理插件

常用命令：

```bash
openclaw plugins list
openclaw plugins list --verbose
openclaw plugins enable <name>
openclaw plugins disable <name>
openclaw plugins install <name>
openclaw plugins inspect <name>
openclaw plugins doctor
```

如果插件不生效，先检查：

1. 是否安装。
2. 是否启用。
3. 是否被 `plugins.allow` 限制。
4. Gateway 是否重启。
5. 日志里是否有加载错误。

## 新手流程

先看列表，再看详情，最后体检：

```bash
openclaw plugins list --verbose
openclaw plugins inspect <name>
openclaw plugins doctor
```

如果插件是新安装的，重启 Gateway 后再判断是否生效。不要只看“安装成功”，要确认 runtime 是否真的注册了能力。

如果你在团队环境里，插件能不能启用还可能受管理员配置限制。遇到这种情况，不要直接删除 `plugins.allow`，先确认这是不是故意设置的安全策略。
