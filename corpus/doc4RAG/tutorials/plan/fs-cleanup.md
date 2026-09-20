---
title: "fs-safe 清理计划"
sidebarTitle: "fs-safe 清理"
description: "解释 OpenClaw 为什么把文件系统辅助函数收敛到 @openclaw/fs-safe，以及插件 SDK、核心代码和安全边界应该如何迁移。"
---

# fs-safe 清理计划

这是一份面向开发者的架构计划。
它的主题很简单：OpenClaw 里所有“碰文件系统”的代码，应该越来越统一、越来越无聊、越来越好检查。

::: tip 先看人话
以前项目里可能有很多种“读 JSON”“写临时文件”“保存私有状态”的小工具。
名字多了，人就容易选错。

这份计划要做的事，是把这些工具收拢到 `@openclaw/fs-safe` 和 OpenClaw 自己的少量包装层里。以后看到文件操作，开发者能一眼知道：这个路径是不是受限制、写入是不是原子的、密钥文件权限是不是安全。
:::

---

## 当前状态

官方计划标记为：已经在 `codex/extract-fs-safe-primitives` 分支实现，文档保留为后续审查和未来 fs-safe 变更的清单。

也就是说，这不是给普通用户每天照着敲的教程，而是给维护者看：

- 以后改文件系统辅助函数时，别随便新增一套名字。
- 以后改插件 SDK 文件 API 时，别破坏兼容别名。
- 以后做安全审查时，先看清楚每个 helper 的信任边界。

---

## 目标

OpenClaw 想让文件访问变得“无聊而可预测”：

- 核心代码通过少量 OpenClaw wrapper 使用 fs-safe。
- 插件 SDK 的旧名字保留兼容，但要有清楚迁移方向。
- fs-safe 主入口保持小而清楚，重点讲 `root()`。
- JSON、临时目录、私有状态、路径检查这些重复名字逐步减少。
- 安全敏感行为在改名或迁移前先有回归测试。

---

## 不做什么

这份计划也明确了边界：

- 不在这次清理里删除公开的插件 SDK export。
- 不把 fs-safe 描述成沙箱。
- 不把所有绝对路径读取都改成 root-bounded 读取，有些绝对路径本来就是可信配置。
- 不为了“好看”乱改 import，只有能减少重复或说清边界时才改。

---

## fs-safe 怎么被引入

`@openclaw/fs-safe` 是 npm 包，OpenClaw 通过 semver range 消费它。

当前范围：

```text
^0.1.0
```

新 checkout 和 CI 应该从公开 npm registry 安装，不应该依赖本地 `link:../fs-safe` 或 GitHub tarball。

fs-safe 包会带编译后的 `dist` 文件，所以 OpenClaw 不需要把它放进 `pnpm.onlyBuiltDependencies`。

---

## 推荐的分层

### 1. OpenClaw 核心代码

核心代码优先使用 OpenClaw 本地 wrapper。

这些 wrapper 的意义不是“多绕一层”，而是统一 OpenClaw 的默认策略。

典型边界包括：

- 常见 root/error helper。
- JSON 文件兼容层。
- 私有文件 store。
- 原子替换文件。
- 包边界读取。
- 压缩包解压策略。
- 文件锁管理。

### 2. 插件 SDK

插件 SDK 是对外契约。

即使内部换了新名字，也不能随便删旧名字。
正确做法是：

- 保留旧 export。
- 在类型或文档里标记 deprecated。
- 给出新名字。
- 等到版本化迁移时再考虑删除。

### 3. fs-safe 主入口

fs-safe 主入口要小，主要讲：

- `root`
- `FsSafeError`
- 错误分类
- root 相关 option/result 类型
- Python helper 配置

更多能力放在明确 subpath 里，例如：

- `/json`
- `/store`
- `/temp`
- `/atomic`
- `/archive`
- `/walk`
- `/advanced`

---

## 几类最容易混淆的 helper

### JSON 文件

旧代码里可能出现很多名字：

- `readJsonFile`
- `readJsonFileStrict`
- `readDurableJsonFile`
- `writeJsonAtomic`
- `loadJsonFile`
- `saveJsonFile`
- `readJsonFileWithFallback`
- `writeJsonFileAtomically`

新方向是收敛到更清楚的名字：

- `tryReadJson`
- `readJson`
- `readJsonIfExists`
- `writeJson`
- `readJsonSync`
- `tryReadJsonSync`
- `writeJsonSync`

### 私有状态和 store

私有状态应该逐步变成一个 store 家族：

```ts
const store = fileStore({
  rootDir,
  private: true,
  mode: 0o600,
  dirMode: 0o700,
})
```

它应该覆盖：

- 读文本。
- 读 JSON。
- 文件不存在时返回空。
- 写文本。
- 写 JSON。
- 删除。
- 判断是否存在。
- 拷贝进入 store。
- 写流。
- 清理过期文件。

### 临时目录

推荐使用 `tempWorkspace` 表达临时生命周期：

```ts
await using workspace = await tempWorkspace({ prefix: "openclaw-" })
const target = workspace.path("payload.bin")
```

意思是：这块临时地方有明确生命周期，用完就收。

---

## 迁移阶段

### 阶段 1：盘点和护栏

- 加 import-boundary 测试，限制核心代码随意直连 `@openclaw/fs-safe/*`。
- 给 JSON 符号链接行为加回归测试。
- 给插件 SDK 兼容别名加测试。

### 阶段 2：JSON 名字清理

- 内部调用迁移到 canonical 名字。
- 插件 SDK 旧别名继续保留。
- 不改变缺失文件、符号链接、硬链接、权限等行为。

### 阶段 3：store 统一

- 用 `fileStore({ private: true })` 统一私有状态。
- 迁移 auth/profile、device identity、cron run log、commitments、extension state 等调用点。

### 阶段 4：临时目录简化

- 普通临时文件生命周期用 `tempWorkspace`。
- 低层 sibling-temp helper 留给原子写入等底层代码。

### 阶段 5：减少 shim

- 删除没人用的一行转发文件。
- 保留真正表达 OpenClaw 策略的 wrapper。
- 保留公开 SDK 名字需要的兼容 shim。

### 阶段 6：fs-safe 公共面定型

- 主入口保持小。
- `root()` 做主要故事。
- 稀有逃生口放到 advanced。
- root、regular-file、secure-file、archive 分开讲，因为信任模型不同。

---

## 审查时问自己

改文件系统代码时，先问这些问题：

- 这个改动是否减少了重复名字或重复语义？
- 旧名字是不是公开插件 SDK？如果是，要保留兼容别名。
- 新 helper 是否保持原来的符号链接、硬链接、权限、缺失文件行为？
- 调用方处理的是不可信相对路径、可信绝对路径、密钥路径、压缩包条目，还是临时文件？
- 这个 helper 的名字有没有把信任边界说清楚？
- 导出名字变了时，文档和插件 SDK API 快照有没有更新？

---

## 相关页面

- [安全文件操作](/tutorials/gateway/security/secure-file-operations)
- [插件 SDK 迁移](/tutorials/plugins/sdk-migration)
- [SDK Subpaths](/tutorials/plugins/sdk-subpaths)
- [Exec 审批](/tutorials/tools/exec-approvals)
