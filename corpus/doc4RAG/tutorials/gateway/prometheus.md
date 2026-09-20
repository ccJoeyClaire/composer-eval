---
title: "Prometheus 指标"
sidebarTitle: "Prometheus 指标"
---

# Prometheus 指标：用数字看 Gateway 是否健康

Prometheus 是很常见的监控系统。它会定时访问一个指标地址，把数字拉回去保存，然后你可以用 Grafana 画图。

OpenClaw 的 Prometheus 能力通常通过诊断插件提供，适合服务器和团队环境。

---

## 先理解一个比喻

日志像“日记”：

```text
今天 10:03 Telegram 收到消息，Agent 回复成功。
```

指标像“体温计”：

```text
最近 5 分钟请求数 120
平均耗时 1.8 秒
错误率 0.3%
```

排查问题时，两者都重要。

---

## 安装 Prometheus 诊断插件

```bash
openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
openclaw gateway restart
```

如果插件已经随你的安装包提供，可以先检查：

```bash
openclaw plugins list
```

---

## 指标地址

官方诊断插件会提供受保护的 Prometheus 路由，常见形式是：

```text
http://127.0.0.1:18789/api/diagnostics/prometheus
```

注意两点：

1. 它应该受认证保护。
2. 不要把它裸露到公网。

Prometheus 抓取时需要带上你的认证方式，例如 Bearer Token。具体 token 来源以你的 Gateway 配置为准。

---

## Prometheus 配置示意

下面只是一个结构示意，字段名和 token 请按你的环境调整：

```yaml
scrape_configs:
  - job_name: openclaw-gateway
    metrics_path: /api/diagnostics/prometheus
    static_configs:
      - targets:
          - 127.0.0.1:18789
    authorization:
      type: Bearer
      credentials: YOUR_GATEWAY_TOKEN
```

如果 Prometheus 不在同一台机器，建议通过 VPN、Tailscale 或内网访问，不建议公网直连。

---

## 重点看哪些数字？

| 指标方向 | 你能判断什么 |
|----------|--------------|
| 请求数量 | 是否突然暴涨 |
| 错误数量 | 是否有通道或插件异常 |
| 耗时 | Agent 或工具是否变慢 |
| 队列长度 | 消息是否堆积 |
| 连接数 | 节点、控制台、通道是否稳定 |

新手不用一开始就懂所有指标。先看“有没有错误”“有没有变慢”“有没有堆积”就够了。

---

## 安全提醒

::: warning
不要为了省事开放一个公开 `/metrics`。指标里即使没有聊天内容，也可能暴露系统规模、服务名、内部路径和运行状态。
:::

推荐方式：

- 本机 Prometheus 抓本机 Gateway。
- 内网 Prometheus 抓内网 Gateway。
- 远程访问走 Tailscale、VPN 或安全代理。

---

## 继续阅读

- [OpenTelemetry 可观测性](/tutorials/gateway/opentelemetry)
- [Gateway 诊断包](/tutorials/gateway/diagnostics)
- [认证与远程访问](/tutorials/gateway/authentication)

