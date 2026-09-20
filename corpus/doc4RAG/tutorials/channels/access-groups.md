---
title: "Access Groups 访问组"
sidebarTitle: "访问组"
---

# Access Groups：把允许说话的人分成小组

OpenClaw 接到聊天软件以后，不是所有人都应该能随便找你的 AI。Access Groups 就是把“允许的人”整理成一个个名单。

你可以把它想成门禁名单：

- 家人一组。
- 同事一组。
- 测试账号一组。
- 只读通知一组。

---

## 它解决什么问题？

没有访问组时，每个通道都要自己写一串 sender ID。通道一多，就很难维护。

访问组可以让你把名单写一次，然后在多个地方复用：

```text
accessGroup:family
accessGroup:work
accessGroup:testers
```

以后增加或删除成员，只改组，不用到处找配置。

---

## 它不会自动授权一切

访问组只是“名单”。
真正是否能发消息，还要看通道配置、会话规则、配对规则和路由规则。

换句话说：

```text
在名单里  不等于  拥有所有权限
```

它只是告诉 OpenClaw：“这个发送者属于这个组，可以被规则引用。”

---

## 典型用法

你可以把常用联系人放进组里，然后在通道 allowlist 里引用它。

示意：

```yaml
accessGroups:
  family:
    - telegram:user:123
    - whatsapp:user:alice

channels:
  telegram:
    allow:
      - accessGroup:family
```

实际字段以你的版本配置为准，示意只是为了说明思路。

---

## sender ID 从哪里来？

不同通道的发送者 ID 格式不一样。最稳的方式是：

1. 让对方发一条测试消息。
2. 查看 Gateway 日志或配对请求。
3. 复制 OpenClaw 识别出的 sender ID。

常用命令：

```bash
openclaw pairing list
openclaw logs --follow
```

---

## 新手建议

一开始不要设计太复杂。

个人使用可以先分三组：

| 组名 | 放谁 |
|------|------|
| `me` | 你自己的账号 |
| `family` | 家人 |
| `testers` | 帮你测试的人 |

等 OpenClaw 真正进入团队使用，再细分部门、项目和权限。

---

## 继续阅读

- [配对说明](/tutorials/channels/pairing)
- [通道路由配置](/tutorials/channels/channel-routing)
- [群组接入指南](/tutorials/channels/groups)

