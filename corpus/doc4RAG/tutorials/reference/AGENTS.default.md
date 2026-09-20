---
title: "AGENTS.default"
sidebarTitle: "AGENTS.default"
---

# AGENTS.default

`AGENTS.default` 是默认 Agent 工作规则模板的参考。它说明 OpenClaw 默认希望 Agent 怎样工作、怎样使用工具、怎样尊重项目边界。

普通用户不需要背模板内容。你只要知道：项目里的 `AGENTS.md` 会覆盖或补充默认行为。

## 它影响什么

- Agent 做事时的默认边界。
- 什么时候该读代码、什么时候该问用户。
- 工具使用和安全习惯。
- 文档、代码、测试的默认风格。

## 新手怎么用

如果你想让 OpenClaw 在某个项目里按你的规矩做事，就在项目根目录写 `AGENTS.md`。
它像“家规”：进入这个项目后，Agent 会优先遵守。
