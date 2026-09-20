---
title: "openclaw dns"
sidebarTitle: "dns"
---

# `openclaw dns`

`dns` 和 DNS、远程访问、域名诊断有关。云部署、自定义域名、Bonjour 或远程 Gateway 发现时可能会用到。

## 什么时候用

- 服务器绑定了域名，但客户端连不上。
- 你怀疑 DNS 解析到了错误地址。
- 团队环境需要排查内部域名。
- Gateway 发现机制和 DNS-SD 有关。

## 新手提醒

普通本机使用通常不需要 `dns`。如果你只是第一次安装，先跑：

```bash
openclaw onboard --install-daemon
openclaw dashboard
```

只有远程访问、域名或局域网发现出问题时，再看 DNS。
