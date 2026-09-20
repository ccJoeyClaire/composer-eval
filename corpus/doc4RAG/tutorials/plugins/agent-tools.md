---
title: "Agent Tools"
sidebarTitle: "Agent Tools"
---

# Agent Tools

Agent Tools 是插件向 Agent 暴露可调用能力的一种方式。

好的工具应该：

- 参数清楚。
- 返回结构稳定。
- 错误可读。
- 权限边界明确。
- 不把密钥塞进结果。

工具越强，越需要和 [Tools 配置](/tutorials/gateway/config-tools) 配合。

## 新手提醒

工具不是普通函数。Agent 会根据描述决定什么时候调用它，所以工具名称、参数说明和错误信息要写得很清楚。

高风险工具要配：

- 权限检查。
- 沙箱。
- 审批。
- 日志脱敏。
