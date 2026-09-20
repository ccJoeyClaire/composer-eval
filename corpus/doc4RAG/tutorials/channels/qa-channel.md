---
title: "QA 测试通道"
sidebarTitle: "QA 测试通道"
---

# QA 测试通道：给自动化测试用的假聊天入口

QA 通道不是给真实用户聊天用的。它是给开发、测试和 CI 使用的“模拟通道”。

你可以把它想成排练舞台：灯光、台词、走位都能练，但观众不会真的进场。

---

## 它有什么用？

QA 通道可以稳定地模拟：

- 私聊消息。
- 群聊消息。
- 指定 sender。
- 指定 channel 或 room。
- OpenClaw 回复后的输出检查。

这样你就能写自动化测试，确认通道路由、权限、工具调用和 Agent 回复流程没有坏。

---

## 为什么不用真实 Telegram 测试？

真实通道会有很多不稳定因素：

- 网络波动。
- 第三方限流。
- 机器人账号状态。
- 推送延迟。
- 群组权限变化。

QA 通道把这些外部因素拿掉，让测试专心检查 OpenClaw 自己。

---

## 常见目标格式

QA 通道通常会使用类似下面的目标描述：

```text
dm:alice
channel:test-room
thread:test-thread
```

意思分别是：

| 格式 | 含义 |
|------|------|
| `dm:alice` | 模拟给 alice 的私聊 |
| `channel:test-room` | 模拟某个频道或房间 |
| `thread:test-thread` | 模拟某个线程 |

具体格式以当前版本的 QA 通道文档和测试脚本为准。

---

## 适合谁阅读？

如果你只是安装 OpenClaw 自己用，可以跳过这一页。

如果你在做下面的事，就需要它：

- 开发新通道插件。
- 修改通道路由。
- 写端到端测试。
- 在 CI 里验证 OpenClaw。
- 排查“真实通道不好复现”的问题。

---

## 新手理解重点

QA 通道不是另一个聊天软件。
它是一个测试工具。

你不会让家人通过 QA 通道找你的 AI，但你会用它确认“家人通过 Telegram 找 AI”这条路没有坏。

---

## 继续阅读

- [通道路由配置](/tutorials/channels/channel-routing)
- [访问组](/tutorials/channels/access-groups)
- [通道故障排查](/tutorials/channels/troubleshooting)

