---
title: "Matrix 通道迁移"
sidebarTitle: "Matrix 迁移"
---

# Matrix 通道迁移：从旧配置平稳走到新版插件

Matrix 是一个开放聊天协议。OpenClaw 的 Matrix 通道已经进入插件化架构，升级时重点是保留账号、凭据、房间和加密相关数据。

如果你没有用 Matrix，可以跳过这一页。

---

## 先备份，再升级

升级前先备份 OpenClaw 数据目录。常见位置是：

```text
~/.openclaw/
```

重点关注：

```text
~/.openclaw/credentials/matrix/
~/.openclaw/matrix/
```

如果你不确定目录在哪里，先运行：

```bash
openclaw doctor
```

---

## 推荐升级流程

```bash
openclaw update
openclaw doctor --fix
openclaw gateway restart
openclaw channels status --probe
```

解释一下：

| 命令 | 作用 |
|------|------|
| `openclaw update` | 更新 OpenClaw |
| `openclaw doctor --fix` | 检查并修复常见配置问题 |
| `openclaw gateway restart` | 让新配置生效 |
| `openclaw channels status --probe` | 确认 Matrix 是否在线 |

---

## 插件名称和配置位置

新版 Matrix 通道仍然围绕 `@openclaw/matrix` 插件工作，配置通常在 `channels.matrix` 下。

你要检查的是：

- 插件是否存在。
- Matrix 账号凭据是否还在。
- homeserver 地址是否正确。
- 房间或群组映射是否仍然匹配。
- 加密房间需要的本地状态是否完整。

查看插件：

```bash
openclaw plugins list
```

查看通道：

```bash
openclaw channels status --probe
```

---

## 加密房间要格外小心

Matrix 加密房间依赖本地密钥和设备状态。
如果这些数据丢了，OpenClaw 可能还能登录，但看不懂旧消息。

升级前请确认：

1. 你有 OpenClaw 数据目录备份。
2. 你知道 Matrix 账号如何恢复。
3. 你理解 homeserver 的密钥备份策略。

不要在没有备份的情况下直接删除 `~/.openclaw/matrix/`。

---

## 迁移后检查

给 Matrix 里允许的房间发一条测试消息，然后看：

```bash
openclaw logs --follow
openclaw channels status --probe
```

如果没有回复，按顺序检查：

1. 通道是否在线。
2. 发送者是否在 allowlist 或访问组里。
3. 房间 ID 是否改变。
4. 加密房间是否解密失败。
5. 插件是否加载成功。

---

## 继续阅读

- [Matrix 通道](/tutorials/channels/matrix)
- [Matrix Push Rules](/tutorials/channels/matrix-push-rules)
- [访问组](/tutorials/channels/access-groups)

