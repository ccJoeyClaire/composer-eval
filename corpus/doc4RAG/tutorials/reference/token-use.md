---
title: "Token Use"
sidebarTitle: "Token 用量"
---

# Token Use

Token 是模型计费和上下文长度的基本单位。上下文越长，通常越贵、越慢。

减少 token 的方法：

- 写清楚问题。
- 开启上下文修剪。
- 不把大日志全塞给模型。
- 使用 Tokenjuice 压缩命令输出。

## 新手比喻

Token 像模型读字时用的小格子。你给它的上下文越长，小格子越多，费用和等待时间通常也越高。

## 什么时候特别注意

- 让 Agent 读很长的日志。
- 把整个仓库文件塞进一次对话。
- 群聊长期不清理上下文。
- 使用视频、图片说明或长语音转写。

继续阅读：[Tokenjuice](/tutorials/tools/tokenjuice)。
