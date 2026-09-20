---
title: "Provider Plugin SDK"
sidebarTitle: "Provider SDK"
---

# Provider Plugin SDK

Provider 插件负责把模型、语音、媒体或搜索服务注册给 OpenClaw。

它通常要处理：

- API Key。
- base URL。
- 模型列表。
- 请求转换。
- 错误归一化。
- fallback 友好提示。

不要让通道直接依赖某个 vendor。应通过 provider capability 走统一接口。

## 新手怎么理解

Provider 插件像“翻译员”：OpenClaw 说“我要生成文本/图片/语音”，provider 插件把这个请求翻译成某个厂商 API 能懂的格式。

写 provider 插件时，先实现最小模型调用，再补模型列表、错误提示、用量和媒体能力。
