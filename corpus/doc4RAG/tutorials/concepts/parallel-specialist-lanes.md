---
title: "Parallel Specialist Lanes"
sidebarTitle: "并行专家通道"
---

# Parallel Specialist Lanes：让多个专家并行看问题

Parallel Specialist Lanes 是一种进阶 Agent 架构思路：把一个复杂问题拆给多个“专家通道”并行处理，再合并结果。

---

## 一个例子

用户问：

```text
帮我评估这个新功能能不能上线。
```

可以拆成：

- 代码专家看实现风险。
- 测试专家看覆盖缺口。
- 安全专家看权限和数据。
- 文档专家看用户说明。

最后主 Agent 汇总。

---

## 和普通子智能体的关系

它可以建立在 subagents 之上，但重点不是“开很多 Agent”，而是“每个 lane 有清楚职责”。

并行不是为了热闹，而是为了让不同角度同时推进。

---

## 风险

- 成本更高。
- 上下文更复杂。
- 合并结果需要判断冲突。
- 如果分工不清，会变成重复劳动。

---

## 继续阅读

- [子智能体](/tutorials/tools/subagents)
- [多智能体路由](/tutorials/concepts/multi-agent)
- [队列引导](/tutorials/concepts/queue-steering)

