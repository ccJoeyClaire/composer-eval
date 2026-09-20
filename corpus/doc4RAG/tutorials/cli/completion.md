---
title: "openclaw completion"
sidebarTitle: "completion"
---

# `openclaw completion`

生成 shell 自动补全脚本，让终端能提示 OpenClaw 子命令。

适合经常使用 CLI 的用户。

## 什么时候用

- 经常记不住完整命令。
- 想在 zsh、bash、fish 里按 Tab 自动提示。
- 团队机器要统一安装补全。

## 新手提醒

补全只是在终端里帮你提示命令，不会改变 OpenClaw 配置。
如果你很少用终端，可以先不管它；等你每天都敲 `openclaw` 时再装也不晚。

## 新手提醒

补全脚本通常要按 shell 类型安装。zsh、bash、fish 的安装方式不同。
如果你不确定自己用哪个 shell，先运行 `echo $SHELL`。
