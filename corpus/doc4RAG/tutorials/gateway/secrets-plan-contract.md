---
title: "Secrets Apply Plan"
sidebarTitle: "Secrets Apply"
---

# Secrets Apply Plan：批量写入密钥前的安全合同

`openclaw secrets apply` 可以按计划文件把 SecretRef 写进配置。计划文件必须符合严格规则，否则 OpenClaw 会在修改前失败。

你可以把它理解成：换锁前先检查钥匙清单，清单不合格就不动门。

---

## 计划文件长什么样？

计划文件里有 `targets` 数组。每个 target 说明：

- 要写哪个配置路径。
- 这个路径是什么类型。
- 密钥引用从哪里来。
- 是否属于某个 agent 或 provider。

示意：

```json5
{
  version: 1,
  targets: [
    {
      type: "models.providers.apiKey",
      path: "models.providers.openai.apiKey",
      providerId: "openai",
      ref: {
        source: "env",
        id: "OPENAI_API_KEY"
      }
    }
  ]
}
```

---

## 为什么这么严格？

因为密钥写错位置很危险。

OpenClaw 会检查：

- `type` 是否认识。
- `path` 是否是允许的密钥路径。
- `pathSegments` 和 `path` 是否一致。
- 是否包含危险字段名，比如 `__proto__`。
- `providerId` 是否和路径里的 provider 对上。
- auth profile 目标是否带了 `agentId`。

任何一项不对，就不写入。

---

## 推荐流程

先 dry-run：

```bash
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run
```

确认没问题再应用：

```bash
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json
```

如果计划里包含 `exec` SecretRef，要显式允许：

```bash
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-exec
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
```

---

## 新手建议

如果你不是在做自动化迁移或团队密钥管理，先不用手写 plan。
优先用向导或 `openclaw secrets configure` 生成，再 review。

---

## 继续阅读

- [密钥与 SecretRef](/tutorials/gateway/secrets)
- [Gateway 安全说明](/tutorials/gateway/security)
- [Agent 配置](/tutorials/gateway/config-agents)

