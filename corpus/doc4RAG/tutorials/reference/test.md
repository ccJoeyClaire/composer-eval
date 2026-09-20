---
title: "Test Reference"
sidebarTitle: "测试参考"
---

# Test Reference

测试参考面向维护者，说明如何验证 OpenClaw 的核心行为、插件、通道和文档。

普通用户排查问题，先跑：

```bash
openclaw doctor
openclaw logs --follow
```

## 维护者常测什么

- Gateway 能否启动、重启、鉴权。
- CLI 命令是否仍然可用。
- 插件 manifest 和 runtime 是否能加载。
- Telegram、Slack、Discord 等通道是否能冒烟。
- 文档能否通过 VitePress 构建。

## 普通用户怎么用这页

你不用跑完整测试矩阵。遇到问题时，先把 `doctor`、`status`、`logs` 的输出收集好，再去 issue 或社区求助。
