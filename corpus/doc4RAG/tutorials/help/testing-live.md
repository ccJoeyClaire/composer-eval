---
title: "Live Testing"
sidebarTitle: "Live 测试"
---

# Live Testing：真实环境测试怎么做

Live 测试不是单元测试。它会碰真实模型、真实通道或真实外部服务。

新手原则：

1. 用小账号测试。
2. 用私有群或测试通道。
3. 不用生产密钥。
4. 先跑 `openclaw doctor`。
5. 测完清理 token 和测试会话。

维护者可以继续看 [QA 自动化](/tutorials/concepts/qa-e2e-automation)。

## 新手提醒

Live 测试会真的花钱、发消息、调用外部服务。
不要用生产群、真实客户、主账号或高额度 key 做第一次测试。

建议建一个测试 Agent、测试通道和测试 provider key，确认稳定后再接入正式环境。
