---
title: "Control UI"
sidebarTitle: "Control UI"
---

# Control UI：浏览器里的 OpenClaw 控制台

Control UI 是你管理 OpenClaw 的浏览器界面。它可以查看 Gateway、通道、节点、模型、任务和会话状态。

打开方式：

```bash
openclaw dashboard
```

默认地址通常是：

```text
http://127.0.0.1:18789/
```

如果你远程访问，请走 Tailscale、VPN、SSH 隧道或可信反向代理，并配置认证。

继续阅读：[Gateway 认证](/tutorials/gateway/authentication)、[Web 控制 UI](/tutorials/web/)

## 新手提醒

Control UI 很方便，但它也是管理入口。远程访问时一定要保护好：

- 使用 token 或密码。
- 不裸露到公网。
- 不把带 token 的 URL 发给别人。
- 服务器优先用 SSH tunnel 或 Tailscale。

## Chat 和 Talk

Control UI 的聊天仍然通过 Gateway WebSocket 调用：

- `chat.history`
- `chat.send`
- `chat.abort`
- `chat.inject`

Chat history 刷新现在会请求一个有上限的最近窗口，并给单条消息文本设置上限。
人话说：很大的会话不会再逼浏览器一次性渲染完整 transcript，聊天页应该先变得可用，再慢慢补状态。

Talk 走新的 Talk session 合同。

浏览器实时语音分两类：

| 类型 | 谁持有 provider 会话 | 入口 |
| --- | --- | --- |
| OpenAI WebRTC / Google provider WebSocket | 浏览器客户端 | `talk.client.create` |
| Gateway relay / transcription / managed-room | Gateway | `talk.session.create` |

浏览器不会拿到普通 provider API Key。
OpenAI WebRTC 会拿临时 Realtime client secret。
Google Live 会拿一次性的受限 token。
后端 relay provider 的凭据保留在 Gateway，浏览器只把麦克风 PCM 通过 `talk.session.appendAudio` 发给 Gateway。

当 realtime provider 需要咨询更大的 OpenClaw Agent 时，客户端通过：

```text
talk.client.toolCall
```

转发 `openclaw_agent_consult`，由 Gateway 执行策略检查和会话处理。

::: warning 配置字段别写旧了
浏览器 Talk 的实时配置是 `talk.realtime.*`，不是旧的 `talk.provider` 顶层字段。
:::

示例：

```json5
{
  talk: {
    realtime: {
      provider: "openai",
      providers: {
        openai: {
          apiKey: "openai_api_key",
          model: "gpt-realtime",
          voice: "alloy"
        }
      },
      mode: "realtime",
      transport: "webrtc",
      brain: "agent-consult"
    }
  }
}
```

Control UI 里 Talk 按钮通常在聊天输入框旁边。状态从 `Connecting Talk...` 到 `Talk live`，如果 realtime 工具调用正在咨询 OpenClaw，会显示类似 `Asking OpenClaw...` 的状态。

## 慢状态刷新时不会白屏

Control UI 的通道探测、审计、状态刷新可能遇到很慢的 provider。
新版 UI 会尽量保持上一份快照可见，不会因为某个慢检查还没回来就把页面清空。

如果 probe 或 audit 超过 UI 预算，页面会标记 partial snapshot。
这表示“现在看到的是部分结果或旧结果”，不是 Gateway 一定坏了。

调试事件日志里也会记录：

- Control UI refresh/RPC timing。
- 慢 chat/config render timing。
- 浏览器 long animation frame 或 long task（浏览器支持时）。

这些信息可以帮助你判断：是 Gateway 慢、provider 慢，还是浏览器渲染大历史太慢。
