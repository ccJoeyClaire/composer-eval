---
title: "SDK Migration"
sidebarTitle: "SDK 迁移"
---

# SDK Migration

SDK 迁移是插件跟随 OpenClaw 版本升级时要做的适配。

推荐做法：

1. 看 release notes。
2. 更新 manifest。
3. 更新 SDK import。
4. 跑插件测试。
5. 在测试 Gateway 里验证。

不要直接在生产 Gateway 上试破坏性迁移。

## 新手迁移顺序

1. 备份。
2. 在测试 Gateway 启用新版本插件。
3. 跑 `openclaw plugins doctor`。
4. 做一条真实请求。
5. 看日志和安全审计。

确认稳定后再动生产环境。

## security-runtime 的新重点

新版 `plugin-sdk/security-runtime` 不只包含共享信任、DM gating、外部内容检查和 secret 收集 helper。
它也开始承担 root-bounded file/path helper 的说明入口。

也就是说，插件里如果要处理来自用户、模型、配置或通道事件的路径，不要自己随手写：

```ts
import { readFile } from "node:fs/promises"
```

而应该优先找插件 SDK 或 fs-safe 相关 helper，让路径边界、原子写入、私有文件权限这些规则走统一实现。

::: tip 一句话判断
路径是别人传进来的，就不要当成可信路径。
:::

相关说明：

- [SDK Subpaths](/tutorials/plugins/sdk-subpaths)
- [安全文件操作](/tutorials/gateway/security/secure-file-operations)
