---
title: "Matrix Push Rules"
sidebarTitle: "Matrix 推送规则"
---

# Matrix Push Rules：减少流式回复带来的打扰

OpenClaw 回复消息时，可能会一段段更新。Matrix 客户端如果每次更新都提醒，你的手机可能会一直响。

Matrix Push Rules 的目标很简单：让最终回复值得提醒，过程中的临时编辑尽量安静。

---

## 先理解 streaming 模式

Matrix 通道可以把回复分成几种方式：

| 模式 | 体验 |
|------|------|
| partial | 一段段发新消息 |
| quiet | 先更新预览，最后再正式提醒 |
| off | 等完整答案出来后再发 |

如果你不想手机一直响，优先考虑 `quiet` 或 `off`。

---

## quiet 模式适合谁？

适合这些场景：

- 你希望看到 OpenClaw 正在生成。
- 但不希望每个小更新都有推送。
- 你使用的 Matrix 客户端支持较好的消息编辑显示。

如果你的客户端对编辑消息支持不好，用 `off` 会更省心。

---

## 自托管 Matrix 可以做更多

如果你自己管理 Matrix homeserver，可以配置更细的 push rule，让某些预览消息不提醒，只让最终消息提醒。

普通用户不一定能改服务器规则。
如果你用的是公共 homeserver，先在客户端里调整通知设置即可。

---

## 推荐配置顺序

1. 先用默认模式确认 Matrix 通道能正常回复。
2. 如果提醒太多，改成 `quiet`。
3. 如果客户端显示混乱，改成 `off`。
4. 自托管 homeserver 再考虑服务端 push rule。

不要一开始就同时改很多配置。一步一步改，出问题才知道是哪一步造成的。

---

## 常见问题

::: details 为什么我还是会收到很多提醒？

可能是 Matrix 客户端把编辑消息也当作提醒，或 homeserver push rule 没有正确识别预览消息。

:::

::: details quiet 会不会丢消息？

正常不会。它只是让过程更安静，最终回复仍然应该出现。

:::

::: details 我应该选 quiet 还是 off？

想看生成过程选 `quiet`。只想要最终答案选 `off`。

:::

---

## 继续阅读

- [Matrix 通道](/tutorials/channels/matrix)
- [Matrix 通道迁移](/tutorials/channels/matrix-migration)
- [流式输出](/tutorials/concepts/streaming)

