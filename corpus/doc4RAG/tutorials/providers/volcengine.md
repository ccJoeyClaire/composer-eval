---
title: "Volcengine"
sidebarTitle: "Volcengine"
---

# Volcengine

Volcengine 火山引擎适合使用豆包或火山侧模型能力的用户。

OpenClaw 中火山相关 provider 可能包含普通聊天模型和 coding-plan 变体。配置时要确认 provider id、endpoint、区域和模型名是一组。

使用前准备：

- 火山引擎账号。
- API Key 或访问凭据。
- 区域、endpoint 和模型名。

配置完成后，先用 WebChat 发送一句短消息测试，再接通道。

## 推荐验证

```bash
openclaw configure --section model
openclaw models list --provider volcengine
openclaw models status
```

如果你使用的是 BytePlus 或国际区 endpoint，不要把国内区模型名和国际区凭据混用。
