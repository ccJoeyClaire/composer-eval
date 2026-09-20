---
title: "密钥与 SecretRef"
sidebarTitle: "密钥管理"
---

# 密钥与 SecretRef：不要把钥匙写在门上

OpenClaw 会连接很多外部服务，比如 Telegram、OpenAI、Slack、搜索工具。它们经常需要 Token、API Key、Client Secret。

这些东西就像家门钥匙。可以用，但不要到处明文写。

---

## SecretRef 是什么？

SecretRef 可以理解成“密钥引用”。

配置里不直接写真实密钥，而是写：

```text
这个值去环境变量里拿
这个值去文件里拿
这个值运行一个命令后拿
```

这样配置文件更安全，也更适合部署到服务器。

---

## 常见来源

| 来源 | 适合场景 |
|------|----------|
| env | 本机或容器环境变量 |
| file | 密钥单独放在受保护文件里 |
| exec | 从系统钥匙串、云密钥服务或脚本读取 |

示意：

```yaml
providers:
  openai:
    apiKey:
      secretRef:
        env: OPENAI_API_KEY
```

这表示 OpenClaw 启动时去读 `OPENAI_API_KEY` 环境变量。

---

## 为什么这比明文更好？

明文配置的问题是：

- 容易被提交到 Git。
- 容易被截图发出去。
- 多台机器不好统一轮换。
- 删除配置时容易漏掉备份。

SecretRef 的好处是：

- 配置文件里看不到真实值。
- 可以把密钥交给系统环境、容器、云平台或密钥管理器。
- 换密钥时只换来源，不一定要改 OpenClaw 配置。

---

## 启动时会检查吗？

会。当前启用的通道、提供商、插件如果引用了密钥，Gateway 启动时应该能读到。

如果读不到，通常会快速失败，告诉你哪个 SecretRef 有问题。
这比启动后运行半天才突然报错更好。

::: tip
未启用的配置通常不会强制读取密钥。比如你写了 Slack 配置但没有启用 Slack，OpenClaw 不应该因为 Slack 密钥缺失就阻止整个 Gateway 启动。
:::

---

## last-known-good 是什么？

某些环境会保留“上一次可用的密钥快照”。
它的目的不是让你长期依赖旧密钥，而是在短暂故障时避免服务立刻完全不可用。

比如：

- 密钥服务临时超时。
- 文件挂载短暂不可读。
- 部署过程刚好切换环境变量。

一旦问题修好，仍然应该让 Gateway 读到新的真实来源。

---

## 新手安全清单

1. 不要把 API Key 写进公开仓库。
2. 不要把 `.env` 发给别人。
3. 生产环境优先用环境变量或密钥管理服务。
4. 定期轮换重要 Token。
5. 诊断包发给别人前搜索 `token`、`secret`、`key`。

---

## 继续阅读

- [Gateway 安全说明](/tutorials/gateway/security)
- [认证与远程访问](/tutorials/gateway/authentication)
- [Gateway 诊断包](/tutorials/gateway/diagnostics)

