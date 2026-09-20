---
title: "SecretRef 凭据面"
sidebarTitle: "SecretRef 凭据面"
---

# SecretRef 凭据面

SecretRef 凭据面指哪些配置路径可以安全地引用密钥。

常见范围：

- 模型 provider API Key。
- 通道 token。
- OAuth profile。
- 搜索或媒体 provider key。
- MCP server 的 env 或 header。

不要把 SecretRef 写到不支持的路径。批量应用前使用 dry-run。

继续阅读：[Secrets Apply Plan](/tutorials/gateway/secrets-plan-contract)。

