---
title: "Agent Runtimes"
sidebarTitle: "Agent 运行时"
---

# Agent Runtimes：同一个 Gateway 可以叫不同“办事员”

OpenClaw 里有几个词很容易混：

- Provider。
- Model。
- Agent。
- Agent Runtime。
- Channel。

这一页专门把 Agent Runtime 讲清楚。

---

## 先用人话区分

| 名词 | 像什么 |
|------|--------|
| Channel | 前台入口，比如 Telegram |
| Gateway | 总服务台 |
| Provider | AI 大脑供应商，比如 OpenAI |
| Model | 具体大脑型号，比如某个 GPT 模型 |
| Agent Runtime | 办事方式，比如用 Codex、Claude CLI 或 ACP Agent |
| Agent | 被配置出来的那位助手 |

Agent Runtime 不是模型本身。它更像“这位助手用哪套工作方式办事”。

---

## 常见运行时

OpenClaw 官方架构里会出现多种运行时，例如：

| Runtime | 大概用途 |
|---------|----------|
| `pi` | OpenClaw 自己的默认 Agent 路线 |
| `codex` | 使用 Codex 风格的代码/任务执行能力 |
| `claude-cli` | 通过 Claude CLI 运行任务 |
| `acp` | 接入符合 ACP 思路的外部 Agent |

具体可用项取决于你的版本、插件和本机环境。

---

## 为什么要分 Runtime？

因为不同任务需要不同办事方式。

比如：

- 日常聊天：默认 Agent 就够。
- 代码仓库修改：Codex 风格运行时更合适。
- 已经有外部 Agent 平台：可能走 ACP。
- 你习惯某个 CLI 工具：可以接对应运行时。

Gateway 负责把消息送到合适的 Agent。Agent Runtime 决定这个 Agent 怎么工作。

---

## 和 Provider 有什么区别？

Provider 是“大脑从哪里来”。
Runtime 是“拿到大脑以后怎么做事”。

你可以想成：

```text
Provider 提供思考能力
Runtime 提供工作流程
Channel 提供消息入口
Gateway 负责调度
```

---

## 新手建议

刚开始不要急着改 runtime。

推荐顺序：

1. 先用默认配置跑通 `openclaw dashboard`。
2. 再接 Telegram 或你常用的通道。
3. 确认模型 provider 稳定。
4. 最后再研究不同 Agent Runtime。

运行时属于进阶配置。基础没跑通之前，改它只会增加排查难度。

---

## 继续阅读

- [Agent 是什么](/tutorials/concepts/agent)
- [智能体循环](/tutorials/concepts/agent-loop)
- [模型提供商概念](/tutorials/concepts/model-providers)
- [工具系统](/tutorials/tools/)

