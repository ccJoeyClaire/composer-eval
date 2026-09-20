---
title: "诊断 Flags"
sidebarTitle: "诊断 Flags"
---

# 诊断 Flags：只打开你需要的调试日志

诊断 flags 可以打开某个子系统的 debug 日志，而不是把全局日志全部调到很吵。

示意：

```json
{
  "diagnostics": {
    "flags": ["telegram.http", "gateway.*"]
  }
}
```

一次性环境变量：

```bash
OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload openclaw gateway run
```

时间线文件：

```bash
OPENCLAW_DIAGNOSTICS=timeline \
OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \
openclaw gateway run
```

分享日志前先检查敏感信息。

## 新手怎么用

平时不要打开一大堆 flag。日志太吵，反而看不出重点。

建议只围绕一个问题打开：

- Telegram 不回：开 `telegram.http`。
- Gateway 事件顺序不清楚：开 `timeline`。
- 插件加载异常：先看 `openclaw plugins doctor`，再决定是否加插件相关 flag。

问题复现完就关掉，避免长期写大量日志。
