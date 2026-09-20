---
title: "Matrix QA"
sidebarTitle: "Matrix QA"
---

# Matrix QA：用临时 homeserver 测真实 Matrix 通道

Matrix QA 是维护者测试 Matrix 插件的端到端路线。它会在 Docker 里启动临时 homeserver，注册临时账号，跑真实 Matrix 通道场景。

普通用户不需要运行它。

---

## 它会做什么？

1. 启动临时 Tuwunel homeserver。
2. 注册 driver、SUT、observer 用户。
3. 创建测试房间。
4. 启动子 OpenClaw Gateway。
5. 加载真实 Matrix 插件。
6. 跑场景并观察事件。
7. 写报告和 JSON summary。
8. 清理 Docker 资源。

---

## 快速命令

在源码 checkout 里：

```bash
pnpm openclaw qa matrix --profile fast --fail-fast
```

完整跑法：

```bash
pnpm openclaw qa matrix
```

---

## 常见 profile

| Profile | 用途 |
|---------|------|
| `fast` | 发布前快速门禁 |
| `transport` | 传输、线程、DM、房间 |
| `media` | 图片、音频、视频、PDF |
| `e2ee-smoke` | 加密房间基础冒烟 |
| `e2ee-deep` | 加密状态和恢复深度测试 |

---

## 输出文件

通常写到：

```text
.artifacts/qa-e2e/matrix-<timestamp>/
```

里面会有 Markdown 报告、JSON summary、观察到的事件和输出日志。

---

## 继续阅读

- [Matrix 通道](/tutorials/channels/matrix)
- [Matrix 迁移](/tutorials/channels/matrix-migration)
- [QA 自动化](/tutorials/concepts/qa-e2e-automation)

