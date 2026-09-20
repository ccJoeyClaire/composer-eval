---
title: "SOUL.md"
sidebarTitle: "SOUL.md"
---

# SOUL.md：写给 Agent 的性格说明书

OpenClaw 里常见两类说明文件：

- `AGENTS.md`
- `SOUL.md`

它们都能影响 Agent，但职责不同。

---

## 一句话区分

| 文件 | 主要用途 |
|------|----------|
| `AGENTS.md` | 工作规则、项目约定、怎么改代码 |
| `SOUL.md` | 说话风格、人格气质、陪伴方式 |

`AGENTS.md` 像工作手册。
`SOUL.md` 像相处说明。

---

## SOUL.md 适合写什么？

适合写：

- 希望 Agent 语气温和还是直接。
- 希望它多解释还是少解释。
- 希望它如何鼓励新手。
- 希望它如何处理不确定性。
- 希望它和家人、团队、用户相处的方式。

例如：

```md
# SOUL.md

你说话要耐心、清楚，不催促用户。
遇到复杂概念时，先用生活比喻解释，再给命令。
不要假装确定，不知道就说不知道，并给出下一步检查方法。
```

---

## 不适合写什么？

不要把 SOUL.md 变成超长规章制度。

不适合塞进去：

- 大段 API 文档。
- 密钥。
- 临时任务清单。
- 和人格无关的项目构建步骤。
- 会和 `AGENTS.md` 打架的硬性规则。

如果是“项目怎么运行”，放 `AGENTS.md`。
如果是“Agent 应该怎么像它自己一样说话和陪伴”，放 `SOUL.md`。

---

## 为什么要有它？

很多人使用 AI 不只是要答案，还希望它的表达方式稳定。

SOUL.md 能让 Agent 更一致：

- 今天不会特别冷。
- 明天不会突然像客服话术。
- 面对老人、新手、孩子或团队成员时，有明确表达原则。

这对长期使用很重要。

---

## 新手建议

SOUL.md 不用长。
先写 5 到 10 条你最在意的风格要求就够。

好的 SOUL.md 应该像一张小纸条：读完以后，Agent 知道该怎么和你相处。

---

## 继续阅读

- [系统提示词](/tutorials/concepts/system-prompt)
- [Agent 是什么](/tutorials/concepts/agent)
- [OpenClaw App SDK](/tutorials/concepts/openclaw-sdk)

