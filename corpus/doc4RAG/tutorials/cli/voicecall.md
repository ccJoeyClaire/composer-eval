---
title: "openclaw voicecall"
sidebarTitle: "voicecall"
---

# `openclaw voicecall`

`voicecall` 是语音通话相关命令，适合 Voice Call、实时语音和通话调试。

```bash
openclaw voicecall --help
openclaw plugins list | grep voice
```

## 什么时候用

- 接入实时语音通话插件。
- 调试通话状态、音频路由或 provider。
- 语音通话能接通但没有声音。

## 新手排查

先确认插件和 provider：

```bash
openclaw plugins list
openclaw doctor
openclaw logs --follow
```

继续阅读：[Voice Call 插件](/tutorials/plugins/voice-call)。

## 常见命令

```bash
openclaw voicecall setup
openclaw voicecall smoke
openclaw voicecall status --json
```

先 smoke test，再接真实号码或正式通道。
