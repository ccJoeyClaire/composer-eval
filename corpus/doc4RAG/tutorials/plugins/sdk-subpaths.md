---
title: "SDK Subpaths"
sidebarTitle: "SDK Subpaths"
---

# SDK Subpaths

SDK subpaths 让插件按需引用不同能力模块，而不是一次引入所有东西。

好处：

- 依赖更清楚。
- 打包更轻。
- 能力边界更明确。

如果你只写 provider 插件，就引用 provider 相关 SDK。不要把 channel、tool、runtime 都混进来。

## 新手提醒

subpath 像工具箱里的分格。你只拿需要的那一格，代码更清楚，未来 SDK 调整时也更容易迁移。

插件作者写 import 时，优先使用官方文档推荐的 SDK subpath。

---

## 安全与文件相关 subpath

新版 SDK 里，`plugin-sdk/security-runtime` 的职责更宽了。
它不仅提供共享信任、DM gating、外部内容、安全文本脱敏、常量时间 secret 比较和 secret 收集 helper，也会覆盖 root-bounded file/path helper。

你可以把它理解成：插件遇到“别人传进来的路径”时，应该先找这里或相关文件 helper，而不是直接碰 Node 原生 `fs`。

它覆盖的典型能力包括：

- 限制路径只能在指定根目录内。
- create-only 写入，避免误覆盖。
- 同步/异步原子文件替换。
- 同目录临时文件写入。
- 跨设备 move fallback。
- 私有 file-store helper。
- 符号链接父目录防护。

`plugin-sdk/temp-path` 也不只是普通临时下载路径，它还包含私有安全临时工作区相关能力。

::: warning 别把 subpath 当装饰
subpath 代表能力边界。插件只 import 自己真正需要的 subpath，安全审查和以后迁移都会轻松很多。
:::
