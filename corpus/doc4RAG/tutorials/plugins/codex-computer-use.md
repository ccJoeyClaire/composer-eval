---
title: "Codex Computer Use"
sidebarTitle: "Computer Use"
---

# Codex Computer Use

Computer Use 能让 Agent 操作桌面应用或浏览器界面。它能力很强，也需要严格权限。

适合：

- 本地自动化。
- UI 检查。
- 桌面流程辅助。

不适合无保护地暴露给远程陌生通道。先理解工具权限和审批。

## 安全边界

Computer Use 可以点击、输入、读取界面状态。它像一双能操作电脑的手，所以权限要比普通文本工具更谨慎。

建议：

- 只给可信 Agent 使用。
- 配合沙箱、审批和 allowlist。
- 不在含敏感数据的桌面环境随便开放。
- 出问题先看轨迹、日志和工具调用记录。
