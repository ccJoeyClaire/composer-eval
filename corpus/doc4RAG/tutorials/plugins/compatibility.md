---
title: "插件兼容性"
sidebarTitle: "兼容性"
---

# 插件兼容性

插件兼容性主要看三件事：

1. manifest 格式是否被当前 OpenClaw 支持。
2. SDK API 是否匹配。
3. 插件声明的能力是否在当前 Gateway 版本可用。

升级 OpenClaw 后，如果插件突然不可用，先跑：

```bash
openclaw plugins list
openclaw doctor
openclaw logs --follow
```

## 升级前后怎么做

升级前：

```bash
openclaw plugins list --verbose
openclaw backup create --verify
```

升级后：

```bash
openclaw plugins doctor
openclaw doctor
```

如果插件来自第三方，确认它声明的最低 OpenClaw/Gateway 版本。

兼容性问题通常不是“重装一次就好”。它可能需要更新插件、调整 manifest、升级 Gateway，或者临时禁用某个旧能力。先在测试环境验证，再动生产环境。
