---
title: "Alibaba Model Studio"
sidebarTitle: "Alibaba"
---

# Alibaba Model Studio

Alibaba Model Studio 适合使用通义和阿里系多模态能力的用户。OpenClaw 里常见用途包括文本模型、视频生成或其他厂商能力。

常见 provider id 会按能力区分，模型名也要使用阿里平台实际暴露的名字。不要把 OpenAI、DeepSeek 或其他平台模型名直接搬过来。

配置思路：

```bash
export MODELSTUDIO_API_KEY="..."
openclaw configure --section model
openclaw models status
```

如果你在国内网络环境使用，先确认 API 区域、计费账户和模型名是否匹配。模型名不要从别家 provider 直接搬过来。

## 新手排查

1. 控制台是否已开通对应模型。
2. Key 是否属于同一个地域或项目。
3. Gateway 机器能否访问阿里 endpoint。
4. 模型 ref 是否带正确 provider 前缀。
