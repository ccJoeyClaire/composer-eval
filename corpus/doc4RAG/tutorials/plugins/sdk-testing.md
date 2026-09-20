---
title: "SDK Testing"
sidebarTitle: "SDK 测试"
---

# SDK Testing

插件测试至少覆盖：

- manifest 是否可解析。
- runtime 是否能加载。
- 配置缺失时是否报清楚错误。
- 工具或通道是否按契约返回。
- 敏感信息是否不进日志。

真实通道插件还要做端到端测试，不能只测函数。

## 最小测试顺序

1. `openclaw plugins inspect <id>` 看 manifest。
2. `openclaw plugins doctor` 看加载诊断。
3. 在测试 Gateway 里启用插件。
4. 触发一次真实能力。
5. 查看日志是否有密钥、token 或大对象泄漏。

插件越靠近通道、浏览器、exec、支付、文件系统，测试越不能省。
