---
title: "Tokenjuice"
sidebarTitle: "Tokenjuice"
---

# Tokenjuice：把吵闹的命令输出压短

有些命令输出很长，比如 `git status`、构建日志、测试日志。它们会占很多上下文，让 Agent 更难抓重点。

Tokenjuice 是一个可选插件，用来压缩 noisy 的 `exec` 和 `bash` 工具结果。

---

## 它会改命令吗？

不会。

Tokenjuice 只改“命令结果返回给模型的样子”。
它不会重写命令、不会重新执行、不会改变退出码。

---

## 启用

OpenClaw 已经内置这个插件，通常不需要单独安装：

```bash
openclaw config set plugins.entries.tokenjuice.enabled true
```

或：

```bash
openclaw plugins enable tokenjuice
```

关闭：

```bash
openclaw config set plugins.entries.tokenjuice.enabled false
```

---

## 适合什么？

适合：

- 命令输出很长。
- Agent 总被日志淹没。
- 想保留重点，不想每次塞完整原文。

不适合：

- 需要逐字核对输出。
- 读取文件内容。
- 调试必须看完整日志的场景。

---

## 继续阅读

- [Exec 命令工具](/tutorials/tools/exec)
- [上下文引擎](/tutorials/concepts/context-engine)
- [执行审批](/tutorials/tools/exec-approvals)

