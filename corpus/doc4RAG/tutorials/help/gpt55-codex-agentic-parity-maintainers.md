---
title: "GPT-5.5 Codex Parity Maintainers"
sidebarTitle: "Codex Parity 维护"
---

# GPT-5.5 Codex Parity：维护者检查点

维护者关注的是：OpenClaw 的 Codex 路线是否在关键行为上保持一致。

检查方向：

- 工具权限和审批。
- 文件读写与 patch。
- 长任务状态。
- `/steer`、队列和中断。
- 轨迹导出。
- 通道消息投递。

用户侧问题先看 [轨迹导出](/tutorials/tools/trajectory) 和 [Gateway 诊断包](/tutorials/gateway/diagnostics)。

## 普通读者怎么理解

这页不是模型宣传页，而是维护者检查清单。
它关心的是：当 OpenClaw 接入 Codex 风格 runtime 时，工具权限、长任务、文件修改、轨迹记录这些行为是否一致、可解释、可排查。

如果你只是使用 OpenClaw，不需要逐项验证 parity。
