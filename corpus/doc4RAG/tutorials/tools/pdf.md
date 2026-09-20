---
title: "PDF Tool"
sidebarTitle: "PDF 分析"
---

# PDF Tool：让 Agent 阅读 PDF

`pdf` 工具可以让 Agent 分析一个或多个 PDF 文件。它会尽量使用模型原生 PDF 能力；如果模型不支持，就先提取文字，再交给模型理解。

---

## 支持哪些输入？

常见输入：

- 本地 PDF 路径。
- `file://` URL。
- `http://` 或 `https://` PDF。
- OpenClaw 管理的入站媒体引用。

一次最多可以处理多个 PDF，具体上限以当前版本配置为准。

---

## 两种执行模式

| 模式 | 说明 |
|------|------|
| 原生 PDF | Anthropic、Google 等支持直接上传 PDF |
| 提取回退 | 先提取文字，必要时渲染页面图片 |

如果你指定了页码范围，原生 PDF 模式可能不支持，需要走提取回退。

---

## 常见用法

你可以对 Agent 说：

```text
帮我总结这个 PDF 的重点，并列出第 3 页提到的风险。
```

如果 PDF 来自聊天附件，Agent 通常能直接使用入站媒体引用。

---

## 安全与限制

- 沙盒模式下可能禁止远程 URL。
- workspace-only 文件策略会阻止读取工作区外文件。
- 太大的 PDF 会被拒绝或截断。
- 扫描件可能需要视觉模型帮助识别页面图像。

---

## 继续阅读

- [媒体能力总览](/tutorials/tools/media-overview)
- [Web Fetch](/tutorials/tools/web-fetch)
- [节点媒体理解](/tutorials/nodes/media-understanding)

