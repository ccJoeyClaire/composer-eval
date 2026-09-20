---
title: "openclaw secrets"
sidebarTitle: "secrets"
---

# `openclaw secrets`

`secrets` 用来管理 SecretRef。SecretRef 的意思是：配置里不直接写明文 API Key，而是写“去哪里取这个密钥”。

推荐流程：

```bash
openclaw secrets audit --check
openclaw secrets configure
openclaw secrets apply --from plan.json --dry-run
openclaw secrets apply --from plan.json
openclaw secrets reload
```

## 什么时候用

- 想把明文 API Key 从配置里迁走。
- Gateway 运行中需要重新加载密钥。
- CI 或安全检查要确认没有残留明文。
- SecretRef 无法解析，需要查哪里断了。

## 新手提醒

`apply` 是写入动作，先 `--dry-run`。`reload` 不改配置，只让 Gateway 重新解析密钥并换到新的运行时快照。

如果输出说 unresolved refs，先修密钥来源，不要把明文复制回配置里。

继续阅读：[密钥管理](/tutorials/gateway/secrets)。
