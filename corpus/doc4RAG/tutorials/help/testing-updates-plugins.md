---
title: "测试更新和插件"
sidebarTitle: "测试更新插件"
---

# 测试更新和插件

升级 OpenClaw 或插件前，建议先做一个小检查：

```bash
openclaw doctor
openclaw plugins list
openclaw channels status --probe
openclaw backup create
```

升级后再跑同样的检查。
如果通道、工具或模型行为变化，先看插件是否启用、配置是否迁移、密钥是否还能读取。

继续阅读：[插件专题](/tutorials/plugins/)、[更新 OpenClaw](/tutorials/installation/updating)。

## 新手安全做法

升级前不要只记“版本号”。也要记当前插件列表和通道状态：

```bash
openclaw plugins list --verbose
openclaw channels status --probe
```

升级后对比一次。差异越早发现，越容易回滚或修复。
