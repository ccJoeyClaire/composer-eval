---
title: "Tools 配置"
sidebarTitle: "Tools 配置"
---

# Tools 配置：给 AI 工具箱上锁

`tools.*` 配置决定 Agent 能用哪些工具、哪些工具被禁止、不同模型能不能使用不同工具。

工具越强，越要管好。

---

## Tool profile

`tools.profile` 是一组基础工具集合。

| Profile | 适合场景 |
|---------|----------|
| `minimal` | 只保留很少状态工具 |
| `coding` | 代码任务常用，含文件、运行时、网页、会话、记忆等 |
| `messaging` | 主要做消息投递 |
| `full` | 不限制，等同放开 |

本地 onboarding 通常会偏向 `coding`。

---

## Tool groups

OpenClaw 用 group 简化配置：

| Group | 包含什么 |
|-------|----------|
| `group:runtime` | `exec`、`process`、`code_execution` |
| `group:fs` | 读写编辑文件、`apply_patch` |
| `group:web` | `web_search`、`web_fetch`、`x_search` |
| `group:ui` | `browser`、`canvas` |
| `group:automation` | `heartbeat_respond`、`cron`、`gateway` |
| `group:agents` | `agents_list`、`update_plan` |
| `group:media` | `image`、`image_generate`、`music_generate`、`video_generate`、`tts` |
| `group:messaging` | `message` |
| `group:nodes` | 节点能力 |

---

## allow 和 deny

示意：

```json5
{
  tools: {
    deny: ["browser", "canvas"]
  }
}
```

deny 优先级更高。
要禁止所有文件修改，不要只禁 `write`，还要考虑 `edit` 和 `apply_patch`。

```json5
{
  tools: {
    deny: ["write", "edit", "apply_patch"]
  }
}
```

---

## 按 provider 限制工具

某些模型不适合跑工具，或者你只信任某些模型做文件修改：

```json5
{
  tools: {
    profile: "coding",
    byProvider: {
      "google-antigravity": { profile: "minimal" },
      "openai/gpt-5.4": { allow: ["group:fs", "sessions_list"] }
    }
  }
}
```

---

## 新手建议

1. 先用默认 profile。
2. 只在明确需要时放开工具。
3. 命令执行看 [执行审批](/tutorials/tools/exec-approvals)。
4. 团队环境用 deny 做底线。
5. 对外通道不要默认开放危险工具。

---

## 继续阅读

- [工具系统](/tutorials/tools/)
- [执行审批](/tutorials/tools/exec-approvals)
- [高级执行审批](/tutorials/tools/exec-approvals-advanced)
