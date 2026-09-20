---
title: "openclaw proxy"
sidebarTitle: "proxy"
---

# `openclaw proxy`

`proxy` 是代理相关命令，适合网络受限、团队代理或远程访问场景。

注意不要让代理绕过 SSRF 和内网访问保护。

## 什么时候用

- 公司网络需要 HTTP/HTTPS 代理。
- 模型 provider 或搜索 provider 需要走代理。
- 远程 Gateway 访问链路需要诊断。

## 安全提醒

代理不是“万能通行证”。配置代理时仍要保留 SSRF 防护、内网访问限制和凭据保护。
如果只是某个 provider 连不上，先用更具体的命令排查：

```bash
openclaw status --deep
openclaw doctor
openclaw logs --follow
```
