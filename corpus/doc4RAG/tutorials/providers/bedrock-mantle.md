---
title: "Bedrock Mantle"
sidebarTitle: "Bedrock Mantle"
---

# Bedrock Mantle

Bedrock Mantle 是围绕 AWS Bedrock 的接入路线。适合已经在 AWS 里统一管理模型权限和网络的团队。

你需要先准备 AWS 凭据、区域和 Bedrock 模型访问权限。它的 provider id 是 `amazon-bedrock-mantle`，可通过显式 bearer token 或 AWS 凭据链获取访问能力。

新手先看 [Amazon Bedrock](/tutorials/providers/bedrock)。如果只是想快速跑通 OpenClaw，Bedrock 不是最省事的第一站。

## 新手排查

Bedrock 相关问题通常在 OpenClaw 之外：

- IAM 权限不够。
- 区域没有开通模型。
- 组织策略挡住 Bedrock。
- 服务器没有正确加载 AWS profile。

先用 AWS 自己的命令或控制台确认模型可用，再接入 OpenClaw。
