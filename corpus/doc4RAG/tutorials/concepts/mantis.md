---
title: "Mantis QA"
sidebarTitle: "Mantis QA"
---

# Mantis QA：真实通道问题的前后验证

Mantis 是维护者用于验证真实通道 bug 的 QA 路线。它关注“修复前是什么样、修复后是不是真的好了”。

普通用户可以跳过这一页。

---

## 它适合什么？

适合维护者排查：

- Discord 状态反应是否正确。
- Slack in VNC 是否正常。
- 桌面或浏览器冒烟是否通过。
- 某个 live transport bug 是否复现并修复。

---

## 为什么需要 Mantis？

很多通道问题不是单元测试能完全覆盖的。
真实聊天平台有权限、延迟、消息格式、附件、反应、线程等复杂行为。

Mantis 的价值是把“我感觉修好了”变成“有前后证据”。

---

## 新手理解

它不是普通安装功能。
它是 OpenClaw 维护者的测试工具。

---

## Discord Web 视觉证据

最新版 Mantis 可以给 Discord 线程附件场景补一份“登录后的网页证据”。

原来的 live Discord API 场景仍然是判定标准：它创建真实线程、发送 SUT 的 `thread-reply`，再通过 Discord REST 检查附件是否存在。

当需要额外留证时，可以打开：

```bash
OPENCLAW_QA_DISCORD_CAPTURE_UI_METADATA=1
OPENCLAW_QA_DISCORD_KEEP_THREADS=1
```

这样场景会写出 Discord Web URL，并把线程保留足够久，让浏览器打开并录制。

Mantis 桌面烟测相关参数：

- `--browser-profile-dir <remote-path>`：复用远端 Chrome 用户数据目录，适合长期保持 Discord Web 登录。
- `--browser-profile-archive-env <name>`：从环境变量里的 base64 `.tgz` 恢复 Chrome profile，默认变量是 `OPENCLAW_MANTIS_BROWSER_PROFILE_TGZ_B64`。
- `--video-duration <seconds>`：调长 MP4 捕获时间，给较慢的登录网页留出加载时间。

GitHub workflow 里推荐用：

```text
MANTIS_DISCORD_VIEWER_CHROME_PROFILE_DIR
```

作为持久 viewer profile。
如果 profile 很小，也可以用：

```text
MANTIS_DISCORD_VIEWER_CHROME_PROFILE_TGZ_B64
```

如果两个都没配置，workflow 仍然会发布确定性的 baseline/candidate 附件截图，只是跳过登录后的 Discord Web 见证视频。

---

## 继续阅读

- [QA 自动化](/tutorials/concepts/qa-e2e-automation)
- [Matrix QA](/tutorials/concepts/qa-matrix)
- [QA 测试通道](/tutorials/channels/qa-channel)
