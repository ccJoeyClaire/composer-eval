---
title: "诊断专题"
sidebarTitle: "诊断专题"
---

# 诊断专题

这里收集更偏排查和日志的内容。

- [诊断 Flags](/tutorials/diagnostics/flags)
- [Node + tsx 崩溃排查](/tutorials/diagnostics/node-issue)
- [Gateway 诊断包](/tutorials/gateway/diagnostics)

## 新手排查三步

```bash
openclaw status --all
openclaw doctor
openclaw logs --follow
```

只有当普通日志不够时，再打开 diagnostics flags 或导出诊断包。
分享诊断信息前，先检查 token、手机号、邮箱、群 ID、API Key 是否被带出来。
