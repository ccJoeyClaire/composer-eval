---
title: "DeepInfra"
sidebarTitle: "DeepInfra"
---

# DeepInfra

DeepInfra 提供多种模型和媒体能力，适合想通过托管 API 使用开源模型的用户。

它的 API 通常是统一入口，provider id 是 `deepinfra`，环境变量是 `DEEPINFRA_API_KEY`。

配置：

```bash
export DEEPINFRA_API_KEY="..."
openclaw configure --section model
openclaw models list --provider deepinfra
```

它也可能用于图像、视频、TTS、STT 或媒体理解，具体看你启用的模型和插件能力。

## 新手怎么选模型

DeepInfra 的模型名经常带上组织名，例如 `deepinfra/<owner>/<model>`。复制模型名时要保留完整路径。
如果只写最后一段模型名，OpenClaw 可能找不到。

排查时先跑：

```bash
openclaw models status
openclaw models list --provider deepinfra
```
