---
title: "Commitments"
sidebarTitle: "自然跟进"
---

# Commitments：让 OpenClaw 记得自然跟进

Commitments 是短期跟进记忆。它不是精确定时提醒，而是让 OpenClaw 记住“过一阵子可以自然问一下”的事情。

---

## 例子

你说：

```text
我明天有面试，有点紧张。
```

如果启用了 commitments，OpenClaw 可能之后自然问：

```text
面试怎么样？需要一起复盘吗？
```

这不是你明确设置的提醒，而是系统推断出的有用跟进。

---

## 开启

默认关闭。开启：

```bash
openclaw config set commitments.enabled true
openclaw config set commitments.maxPerDay 3
```

---

## 和提醒的区别

| 需求 | 用什么 |
|------|--------|
| “下午 3 点提醒我” | 定时任务 |
| “每周一发报告” | cron |
| “我明天有面试” | commitments |
| “我昨晚没睡好” | commitments |

明确时间用任务。自然关心用 commitments。

---

## 管理

```bash
openclaw commitments
openclaw commitments --all
openclaw commitments dismiss <id>
```

---

## 继续阅读

- [定时任务](/tutorials/automation/cron-jobs)
- [Standing Orders](/tutorials/automation/standing-orders)
- [主动记忆](/tutorials/concepts/active-memory)

