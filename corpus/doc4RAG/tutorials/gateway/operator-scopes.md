---
title: "Operator 权限范围"
sidebarTitle: "Operator 权限"
---

# Operator 权限范围：谁能看，谁能改，谁能批准

OpenClaw 的 Gateway 不只服务聊天通道，也服务控制 UI、CLI、节点和运维工具。不同客户端不应该拥有同样大的权限。

这就像家里有不同钥匙：有人只能进客厅，有人能进书房，有人能改门锁。

---

## 两类常见身份

| 身份 | 说明 |
|------|------|
| operator | 控制端，比如控制 UI、CLI、运维脚本 |
| node | 连接进来的设备节点，比如手机、桌面、远程机器 |

operator 更像“管理员入口”。node 更像“被管理的设备”。

---

## 常见 scope

| Scope | 可以做什么 |
|-------|------------|
| `operator.read` | 查看状态、列表、配置摘要 |
| `operator.write` | 修改普通配置或执行一般操作 |
| `operator.admin` | 管理级操作，权限更大 |
| `operator.pairing` | 处理配对和批准请求 |
| `operator.approvals` | 审批敏感操作 |
| `operator.talk.secrets` | 访问和语音/对话相关的敏感能力 |

具体版本可能会增加新的 scope。记住原则即可：只给需要的权限。

---

## 最小权限原则

不要为了省事把所有 token 都设成管理员。

更稳的做法：

- 只看仪表盘的 token 给 `operator.read`。
- 自动化脚本只给它需要的写权限。
- 配对审批单独给 `operator.pairing`。
- 真正管理 Gateway 的入口才给 `operator.admin`。

权限越小，出错后的影响越小。

---

## Scope 不是魔法隔离墙

Scope 能限制“同一个 Gateway 内的能力”，但它不能替代真正的环境隔离。

如果你需要严格隔离，比如：

- 家庭 OpenClaw 和公司 OpenClaw 分开。
- 测试环境和生产环境分开。
- 不同团队完全互不信任。

更推荐使用不同 Gateway、不同机器、不同网络或不同部署环境。

---

## 新手怎么用？

如果你只是个人使用：

1. 先使用官方向导默认配置。
2. 不把 Gateway 暴露公网。
3. 远程访问走 Tailscale、VPN 或 SSH 隧道。
4. 有自动化脚本时，再学习 scope。

如果你是团队管理员：

1. 给人和脚本分别发 token。
2. 每个 token 只给必要 scope。
3. 定期清理不用的 token。
4. 记录谁拥有审批权限。

---

## 继续阅读

- [认证与远程访问](/tutorials/gateway/authentication)
- [Gateway 安全说明](/tutorials/gateway/security)
- [设备配对](/tutorials/gateway/pairing)

