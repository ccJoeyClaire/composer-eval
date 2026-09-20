---
title: "Tencent"
sidebarTitle: "Tencent"
---

# Tencent

Tencent 相关 provider 适合已经在腾讯云或腾讯模型服务里管理账号、密钥和模型的用户。

最新版官方文档重点提到 Tencent Cloud TokenHub provider，provider id 是 `tencent-tokenhub`，默认模型 ref 类似 `tencent-tokenhub/hy3-preview`。

使用前确认：

- 云账号权限。
- API Key 或 SecretId/SecretKey。
- 区域和模型名。
- 网络能访问对应 endpoint。

国内团队如果已有腾讯云基础设施，用统一 provider 管理会更方便。

## 新手验证

```bash
openclaw configure --section model
openclaw models list --provider tencent-tokenhub
openclaw models status
```

不要把 Hy3 chat 模型和腾讯 3D 生成类 API 混在一起，它们不是同一个能力面。
