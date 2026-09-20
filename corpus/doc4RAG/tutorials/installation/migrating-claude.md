---
title: "从 Claude 迁移"
sidebarTitle: "迁移 Claude"
---

# 从 Claude 迁移到 OpenClaw

如果你以前使用 Claude Code 或 Claude Desktop，OpenClaw 可以导入部分本地状态，比如说明文件、MCP 服务器、技能和命令。

迁移前先预览，不要一上来直接覆盖。

---

## 两种方式

### onboarding 导入

适合新安装：

```bash
openclaw onboard --flow import
```

指定来源：

```bash
openclaw onboard --import-from claude --import-source ~/.claude
```

### CLI 导入

适合脚本化：

```bash
openclaw migrate claude --dry-run
openclaw migrate apply claude --yes
```

---

## 会导入什么？

| 来源 | 导入到哪里 |
|------|------------|
| `CLAUDE.md` | OpenClaw 工作区的 `AGENTS.md` |
| `~/.claude/CLAUDE.md` | 工作区 `USER.md` |
| `.mcp.json` / Claude 配置 | MCP 服务器定义 |
| Claude skills | OpenClaw skills |
| `.claude/commands/` | 转成 OpenClaw skills |

---

## 什么不会自动信任？

OpenClaw 不会自动执行或信任：

- Claude hooks。
- 旧权限 allowlist。
- Desktop 凭据。
- 缓存和历史目录。
- `CLAUDE.local.md`。
- 子 agent 配置。

这些会进入迁移报告，供你手动检查。

---

## 推荐流程

```bash
openclaw migrate claude --dry-run
openclaw migrate apply claude --yes
openclaw doctor
openclaw gateway restart
```

有冲突时不要急着 `--overwrite`。先看迁移报告，确认覆盖的是你想覆盖的东西。

---

## 继续阅读

- [安装 OpenClaw](/tutorials/installation/)
- [迁移旧版本](/tutorials/installation/migrating)
- [技能 Skills](/tutorials/tools/skills)

