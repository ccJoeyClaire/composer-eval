---
title: "从 Hermes 迁移"
sidebarTitle: "迁移 Hermes"
---

# 从 Hermes 迁移到 OpenClaw

OpenClaw 可以从 Hermes 导入模型配置、MCP、工作区文件、记忆和技能。迁移会先生成计划、隐藏敏感值、创建备份，再应用。

---

## 推荐新安装时导入

```bash
openclaw onboard --flow import
```

指定来源：

```bash
openclaw onboard --import-from hermes --import-source ~/.hermes
```

也可以用 CLI：

```bash
openclaw migrate hermes --dry-run
openclaw migrate apply hermes --yes
```

---

## 会导入什么？

| 内容 | 说明 |
|------|------|
| 模型配置 | 默认模型、provider、自定义 endpoint |
| MCP servers | Hermes 配置里的 MCP 服务 |
| `SOUL.md` / `AGENTS.md` | 复制到 OpenClaw 工作区 |
| `MEMORY.md` / `USER.md` | 追加到对应记忆文件 |
| skills | 带 `SKILL.md` 的技能目录 |
| API keys | 只有显式 `--include-secrets` 才导入 |

---

## 什么只归档不启用？

这些会进入迁移报告，但不会直接变成 OpenClaw 运行状态：

- `plugins/`
- `sessions/`
- `logs/`
- `cron/`
- `mcp-tokens/`
- `auth.json`
- `state.db`

原因是格式和信任边界不同，不能自动照搬。

---

## 密钥默认不导入

OpenClaw 默认不复制 API Key。
如果你明确要导入支持的 `.env` key，再加：

```bash
openclaw migrate apply hermes --yes --include-secrets
```

迁移后仍建议检查 [密钥与 SecretRef](/tutorials/gateway/secrets)。

---

## 继续阅读

- [安装 OpenClaw](/tutorials/installation/)
- [迁移旧版本](/tutorials/installation/migrating)
- [记忆 Memory](/tutorials/concepts/memory)

