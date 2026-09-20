---
title: "OpenTelemetry 可观测性"
sidebarTitle: "OpenTelemetry"
---

# OpenTelemetry：把 Gateway 的运行情况送到监控平台

OpenTelemetry 常简称 OTel。它的作用是把程序里的指标、链路和日志，用统一格式送到 Grafana、Datadog、Honeycomb、Tempo、Jaeger 这类平台。

如果你只是自己在家跑 OpenClaw，先不需要它。
如果你把 OpenClaw 放在服务器、团队环境或多网关环境里，OTel 就很有用。

---

## 它解决什么问题？

普通日志像“日记”，你要一行行翻。
OpenTelemetry 像“仪表盘”，可以回答：

- Gateway 最近有没有变慢？
- 哪个通道最常超时？
- Agent 调用花了多久？
- 插件有没有频繁报错？
- 多个 Gateway 里，是哪一台出问题？

---

## 安装诊断 OTel 插件

官方诊断能力通过插件提供。常见安装方式是：

```bash
openclaw plugins install clawhub:@openclaw/diagnostics-otel
```

安装后重启 Gateway：

```bash
openclaw gateway restart
```

然后在配置里启用插件，并填上你的 OTLP 接收地址。

::: tip
如果你用的是官方安装向导或打包版本，先运行 `openclaw plugins list` 看插件是否已经可用。不要重复安装。
:::

---

## 典型配置思路

你需要准备一个 OTLP HTTP 端点，例如：

```text
https://otel.example.com/v1/traces
```

或者本地 Collector：

```text
http://127.0.0.1:4318
```

配置时通常会包含：

| 配置 | 意思 |
|------|------|
| endpoint | 数据发到哪里 |
| headers | 鉴权头，比如 API Key |
| serviceName | 在监控平台里显示的服务名 |
| traces | 是否发送链路 |
| metrics | 是否发送指标 |
| logs | 是否发送日志 |

---

## 隐私边界

默认的诊断数据应该关注“系统怎么运行”，不是“用户具体说了什么”。

也就是说，监控里适合出现：

- 请求数量。
- 耗时。
- 错误码。
- 插件名称。
- 通道类型。

不适合出现：

- 用户私聊内容。
- API Key。
- 完整提示词。
- 未脱敏的账号信息。

配置监控平台前，请先确认你收集的字段符合自己的隐私要求。

---

## 新手推荐做法

如果你刚开始运维 OpenClaw：

1. 先只打开 metrics。
2. 确认没有敏感字段。
3. 再打开 traces。
4. logs 只在你知道日志会发到哪里时启用。

这样更稳。监控是为了看清系统，不是把家里每张纸都贴到墙上。

---

## 继续阅读

- [Gateway 诊断包](/tutorials/gateway/diagnostics)
- [Prometheus 指标](/tutorials/gateway/prometheus)
- [Gateway 日志](/tutorials/gateway/logging)

