---
title: "Experimental Features"
sidebarTitle: "实验功能"
---

# 实验功能：可以试，但别当成地基

OpenClaw 发展很快，有些能力会先以实验功能出现。它们可能很好用，但接口、配置和行为还可能变化。

---

## 怎么判断是不是实验功能？

常见信号：

- 文档写着 experimental。
- 配置需要显式开启。
- 默认关闭。
- 只在源码 checkout 或特定插件里出现。
- 报错信息提示 API 可能变化。

---

## 使用原则

1. 先在测试环境试。
2. 不要直接接生产数据。
3. 不要把实验功能写进关键业务流程。
4. 升级前看 release notes。
5. 出问题时保留最小复现。

---

## 适合谁？

适合：

- 开发者。
- 早期试用者。
- 愿意接受破坏性变化的人。
- 想给官方反馈的人。

不适合：

- 家庭日常主力网关。
- 团队生产流程。
- 不方便维护的人。

---

## 继续阅读

- [功能特性](/tutorials/concepts/features)
- [系统架构设计](/tutorials/concepts/system-architecture)
- [Gateway 诊断包](/tutorials/gateway/diagnostics)

