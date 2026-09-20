---
title: "StepFun"
sidebarTitle: "StepFun"
---

# StepFun

StepFun 阶跃星辰是国内模型 provider 之一，适合中文和国内网络环境。

最新版 OpenClaw 内置两个 provider：

- `stepfun`：标准接口。
- `stepfun-plan`：Step Plan 接口。

它们的 endpoint 和模型前缀不同，不要混着写。中国区通常使用 `.com` endpoint，国际区通常使用 `.ai` endpoint。

配置：

```bash
export STEPFUN_API_KEY="..."
openclaw configure --section model
openclaw models list --provider stepfun
```

## 新手排查

1. API Key 是中国区还是国际区。
2. provider 前缀是 `stepfun/...` 还是 `stepfun-plan/...`。
3. base URL 是否和账号区域匹配。
4. 模型名是否属于 StepFun。
5. 账户是否还有额度。
