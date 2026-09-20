---
title: "安全事件响应"
sidebarTitle: "事件响应"
---

# 安全事件响应：怀疑泄漏时先做什么

如果你怀疑 token、API Key、Gateway URL 或通道账号泄漏，不要先写长复盘，先止血。

1. 立即撤销或轮换泄漏密钥。
2. 停止公网入口或收紧访问。
3. 重启 Gateway。
4. 查看日志和诊断包。
5. 检查通道配对和 allowlist。
6. 记录时间线。

常用命令：

```bash
openclaw gateway stop
openclaw logs --follow
openclaw gateway diagnostics export
```

继续阅读：[密钥与 SecretRef](/tutorials/gateway/secrets)、[Gateway 安全说明](/tutorials/gateway/security)。

