---
title: "Code Execution"
sidebarTitle: "远程代码执行"
---

# Code Execution：在远程沙盒里做 Python 分析

`code_execution` 是给分析任务用的远程 Python 沙盒。它由内置 `xai` 插件注册，走 xAI Responses API。

它和本机 `exec` 不一样。

一句话记住：

```text
exec 动你的机器
code_execution 动远程沙盒
```

---

## 适合做什么？

适合：

- 计算。
- 表格统计。
- 小型数据分析。
- 把搜索结果按日期、类别、数量整理。
- 画图前的数据准备。

不适合：

- 读取你的本地文件。
- 修改你的代码仓库。
- 操作你的 shell。
- 控制配对设备。

需要本机能力时，用 [Exec 命令工具](/tutorials/tools/exec)。

---

## 配置 xAI Key

你需要配置 xAI API Key。最简单是把它放到 Gateway 环境变量里：

```bash
export XAI_API_KEY="xai-..."
```

也可以把 key 放到 xAI 插件配置里。这个 key 会同时服务 `code_execution`、`x_search` 等 xAI 工具。

示意配置：

```json5
{
  plugins: {
    entries: {
      xai: {
        config: {
          webSearch: {
            apiKey: "xai-..."
          },
          codeExecution: {
            enabled: true,
            model: "grok-4-1-fast",
            maxTurns: 2,
            timeoutSeconds: 30
          }
        }
      }
    }
  }
}
```

默认模型是 `grok-4-1-fast`，默认超时是 30 秒。

配置完成后重启 Gateway：

```bash
openclaw gateway restart
```

---

## 怎么让 Agent 用它？

直接说明你的分析意图：

```text
用 code_execution 计算这些数字的 7 日移动平均。
```

或者：

```text
先用 web_search 找资料，再用 code_execution 做百分比变化对比。
```

---

## 新手注意

远程沙盒是临时的，不是你的长期 notebook。
不要假设它记得上一次的数据，也不要把它当成本机终端。

如果没有配置 xAI key，工具会返回 `missing_xai_api_key` 这类结构化错误。看到它时，不要去改 Python 代码，先补 `XAI_API_KEY` 或 xAI 插件里的 `webSearch.apiKey`。

---

## 继续阅读

- [Exec 命令工具](/tutorials/tools/exec)
- [Grok Search](/tutorials/tools/grok-search)
- [Web 网络工具](/tutorials/tools/web)
