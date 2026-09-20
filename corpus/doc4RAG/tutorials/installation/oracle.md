---
title: "Oracle Cloud 部署"
sidebarTitle: "Oracle Cloud"
description: "OpenClaw 安装部署：在 Oracle Cloud Always Free ARM 实例上运行 OpenClaw。"
---

# Oracle Cloud 部署

Oracle Cloud Always Free ARM 实例可以免费跑一台长期在线的 Linux 机器。
它适合愿意折腾云账号和网络规则的用户。

---

## 推荐思路

1. 创建 Ubuntu 24.04 ARM 实例。
2. 用 SSH 登录。
3. 安装基础编译工具。
4. 安装 Tailscale。
5. 安装 OpenClaw。
6. 用 `openclaw onboard --install-daemon` 配置 Gateway。
7. 用 Tailscale 或 SSH 隧道访问控制 UI。

---

## 安装命令

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl git
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
```

---

## 为什么推荐 Tailscale

Oracle 免费实例容易被误配置成公网暴露。
Tailscale 可以让你的电脑、手机、服务器像在同一个私人局域网里。

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --ssh --hostname=openclaw
```

然后尽量关闭不必要的公网入站规则。

---

## 检查安全姿势

最安全的思路是：

- Oracle VCN 只放行 Tailscale 需要的 UDP 41641。
- Gateway 只监听本机回环地址，也就是 `127.0.0.1`。
- 管理入口只通过 Tailscale 或 SSH 隧道访问。

这样公网流量在云网络边界就被挡住了，不会直接打到 OpenClaw。

| 传统加固步骤 | 还必须做吗 | 原因 |
| --- | --- | --- |
| UFW 防火墙 | 通常不需要 | VCN 已经在实例外面挡住流量。 |
| fail2ban | 通常不需要 | 如果 22 端口没暴露，公网无法暴力猜 SSH。 |
| sshd 加固 | 使用 Tailscale SSH 时不需要 | Tailscale SSH 走 tailnet 身份，不走普通公网 sshd。 |
| 禁用 root 登录 | 使用 Tailscale SSH 时不需要 | 重点是不要把公网 SSH 暴露出去。 |
| IPv6 加固 | 看实际情况 | 要确认子网有没有给实例分配公网 IPv6。 |

仍然建议做：

```bash
chmod 700 ~/.openclaw
openclaw security audit
sudo apt update && sudo apt upgrade -y
```

还要定期打开 [Tailscale 管理后台](https://login.tailscale.com/admin) 看看有没有陌生设备。

快速检查命令：

```bash
# 看看有没有非本机地址的监听端口
sudo ss -tlnp | grep -v '127.0.0.1\|::1'

# 确认 Tailscale SSH 是否启用
tailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active"
```

确认 Tailscale SSH 可用后，如果你真的不再需要系统 SSH，可以关闭：

```bash
sudo systemctl disable --now ssh
```

::: warning 先确认再关 SSH
只有在你已经能通过 Tailscale SSH 登录时，才关闭系统 SSH。否则你可能把自己锁在服务器外面。
:::

---

## ARM 架构注意事项

Oracle Always Free ARM 实例通常是 `aarch64`。
先确认一下：

```bash
uname -m
```

如果输出是 `aarch64`，说明你在 ARM 机器上。

多数 OpenClaw 能力都没问题：

- Node.js：支持 ARM64。
- Telegram：正常。
- WhatsApp/Baileys：正常。
- 大多数 npm 原生依赖：通常有 `linux-arm64` 预构建包。

少数技能自带的 Go/Rust CLI 工具可能没有 ARM 包。
遇到“binary not found”或“exec format error”时，先找对应工具有没有：

- `linux-arm64`
- `aarch64`

没有的话，再考虑源码编译或暂时不用这个技能。

---

## 数据与备份

OpenClaw 的重要文件在：

- `~/.openclaw/`：配置、授权、通道状态、会话数据。
- `~/.openclaw/workspace/`：Agent 工作区、记忆、产物。

这些文件会跨重启保留。
迁移、升级、重装系统前先做备份：

```bash
openclaw backup create
```

---

## 注意事项

- 免费实例容量可能抢不到，失败可以换可用区或稍后重试。
- ARM 架构下某些二进制工具要选 arm64 版本。
- 不要开放 `18789` 到公网。
- 定时任务要确认服务器时区。
