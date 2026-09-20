---
title: "安全和密钥命令"
sidebarTitle: "安全密钥命令"
---

# 安全和密钥命令

密钥、token、审批和安全审计是团队使用 OpenClaw 时最容易忽略的部分。

常用命令方向：

```bash
openclaw security audit
openclaw secrets apply --from plan.json --dry-run
openclaw approvals get
openclaw approvals allowlist add <command>
openclaw doctor
```

处理密钥时先 dry-run，再 apply。
怀疑泄漏时先轮换 key，再看日志。

继续阅读：[密钥与 SecretRef](/tutorials/gateway/secrets)、[安全事件响应](/tutorials/gateway/incident-response)。

## 新手顺序

1. `security audit` 看风险。
2. `secrets audit --check` 查明文和 unresolved refs。
3. `approvals get` 看 exec 审批策略。
4. 需要改密钥时先 dry-run。

不要把 API Key 贴到群聊或日志里。
