---
title: "插件内部架构"
sidebarTitle: "插件内部"
---

# 插件内部架构

插件内部架构更偏维护者。它关注插件如何被发现、解析 manifest、加载 runtime、捕获注册项，并把能力暴露给 Gateway。

普通插件作者先不用钻这里。
如果你在改核心加载器、插件注册表、capability contract 或 SDK runtime，再读这一页。

继续阅读：[添加能力 Cookbook](/tutorials/tools/capability-cookbook)。

## 新手提醒

这里讲的是“插件加载器怎么造”，不是“插件怎么用”。
如果你只是安装插件，看 [管理插件](/tutorials/plugins/manage-plugins)。
如果你只是写普通插件，看 [构建插件](/tutorials/plugins/building-plugins)。
