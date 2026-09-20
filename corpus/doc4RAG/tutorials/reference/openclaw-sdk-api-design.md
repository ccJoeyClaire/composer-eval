---
title: "OpenClaw SDK API Design"
sidebarTitle: "SDK API 设计"
---

# OpenClaw SDK API Design

SDK API 设计关注插件作者如何用稳定接口扩展 OpenClaw，而不是直接改核心。

设计目标：

- 能力边界清晰。
- 类型稳定。
- 错误可读。
- 插件不用知道核心内部细节。

继续阅读：[SDK 总览](/tutorials/plugins/sdk-overview)。

## 为什么不直接改核心

直接改核心像把所有电器都焊在墙里，短期快，长期难维护。
SDK 像统一插座：插件按约定接入，核心可以升级，插件也能独立发布。

## 插件作者先记住

先写 manifest，再写 runtime；先注册小能力，再扩展复杂场景。

## 当前常用接口状态

下面这段不是让新手背 API，而是帮助你判断“现在能不能用”。

```ts
oc.models.list();
oc.models.status();

oc.tools.list();
oc.tools.invoke("tool-name", { sessionKey, idempotencyKey });

oc.artifacts.list({ runId });
oc.artifacts.get(artifactId, { runId });
oc.artifacts.download(artifactId, { runId });

oc.approvals.list();
oc.approvals.respond(approvalId, { decision: "approve" });

oc.environments.list();
oc.environments.status(environmentId);
```

环境接口现在只读可用：

- `oc.environments.list()`：列出 Gateway 本机和已发现节点环境。
- `oc.environments.status(environmentId)`：查询某个环境是否可用。

还不能做的事情：

```ts
oc.environments.create(...); // 当前仍未接通
oc.environments.delete(environmentId); // 当前仍未接通
```

人话解释：现在 SDK 能“看环境”，还不能“造环境”或“删环境”。
