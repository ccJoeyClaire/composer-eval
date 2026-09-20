---
title: "Azure 部署"
sidebarTitle: "Azure"
description: "OpenClaw 安装部署：在 Azure Linux VM 上 24/7 运行 Gateway，并用 Bastion、NSG 和 SSH 隧道保护访问。"
---

# Azure 部署

Azure 适合想把 OpenClaw 长期放在云服务器上的用户。
这条路线比本机安装复杂，但好处是 Gateway 可以 24 小时运行。

---

## 适合谁

- 你已经在用 Azure。
- 你想要一台稳定的 Linux VM。
- 你希望通过 Azure Bastion 管理 SSH。
- 你愿意配置网络安全组（NSG）和私有网络。

如果你只是个人第一次体验，先用[快速入门](/tutorials/getting-started/getting-started)更简单。

---

## 基本流程

1. 创建资源组、VNet、子网和 NSG。
2. 创建 Ubuntu Linux VM。
3. 通过 Azure Bastion 或 SSH 登录。
4. 安装 OpenClaw。
5. 运行 `openclaw onboard --install-daemon`。
6. 用 SSH 隧道、Tailscale 或受保护反向代理访问控制 UI。

---

## 安装 OpenClaw

登录 VM 后运行：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
openclaw gateway status
```

---

## 安全建议

不要直接把 `18789` 暴露到公网。

推荐访问方式：

```bash
ssh -N -L 18789:127.0.0.1:18789 azureuser@YOUR_VM
```

然后在本机浏览器打开：

```text
http://127.0.0.1:18789/
```

生产环境建议：

- VM 不挂公网 IP，使用 Azure Bastion。
- NSG 只开放必要端口。
- Gateway 使用 token 认证。
- 远程访问优先走 Tailscale、VPN 或 SSH 隧道。

