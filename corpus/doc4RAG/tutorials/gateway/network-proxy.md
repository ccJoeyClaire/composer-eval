---
title: "网络代理安全"
sidebarTitle: "网络代理"
---

# 网络代理安全：让流量走代理，但别绕过边界

OpenClaw 可以在某些网络环境里使用 HTTP(S) 代理。代理能解决访问问题，也可能带来 SSRF、内网暴露和凭据泄漏风险。

原则：

- 只信任你控制的代理。
- 不让公开代理访问内网。
- 私有网络访问要显式 opt-in。
- 诊断时记录代理配置来源。

如果某个工具突然能访问内网地址，先检查代理和 SSRF policy。

## 新手排查

```bash
openclaw config get proxy
openclaw security audit
openclaw logs --follow
```

代理问题不要只看“能不能访问外网”。还要看它有没有扩大访问范围。
团队环境里，代理配置应该由可信管理员统一维护。
