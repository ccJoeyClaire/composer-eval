---
title: "BTW Side Questions"
sidebarTitle: "BTW 临时问题"
---

# BTW：问一个不进入主线的小问题

`/btw` 用来问当前会话里的临时旁支问题。`/side` 是它的别名。

它的重点是：回答完就算了，不把这次问答写进长期会话历史。

---

## 适合什么？

适合：

```text
/btw 现在我们改了哪些文件？
/btw 这个错误大概是什么意思？
/side 用一句话总结当前任务
```

这些问题只是临时了解情况，不需要影响主任务。

---

## 它怎么工作？

OpenClaw 会：

1. 复制当前会话上下文快照。
2. 做一次无工具的模型调用。
3. 只回答旁支问题。
4. 不写入主会话历史。
5. 不打断主任务。

---

## 它不做什么？

`/btw` 不会：

- 创建持久新会话。
- 继续主任务。
- 调用工具。
- 修改文件。
- 进入未来上下文。

---

## 新手理解

普通消息像“正式写进会议记录”。
BTW 像你在旁边小声问一句：“刚刚说到哪儿了？”

---

## 继续阅读

- [斜杠命令](/tutorials/tools/slash-commands)
- [队列引导](/tutorials/concepts/queue-steering)
- [会话管理](/tutorials/concepts/session)
- [思考等级](/tutorials/tools/thinking)
- [Steer 命令](/tutorials/tools/steer)
