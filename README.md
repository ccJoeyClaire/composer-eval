# composer-agentic-eval

从 [`composer-agentic_rag`](../composer-agentic_rag) 剥离的端到端评测项目：Easy Dataset QA → gold → Agent/RAG infer → RAGChecker input。

运行时依赖 sibling 库 `composer-agentic-rag`（editable install），Cursor 只打开本目录即可。

## 目录结构

```
composer-eval/
├── config/
│   ├── arg_config.yaml          # RAG profile（chunk / retrieve）
│   └── agent_arg_config.yaml    # Agent pattern toggles
├── eval/
│   ├── base.py                  # 类型定义
│   ├── data/                    # gold / infer / ragchecker 产物
│   └── harness/
│       ├── main.py              # 管线入口
│       ├── infer/agent.py       # Agent graph infer
│       └── infer/rag.py         # 直连 RAG + LLM infer
├── pyproject.toml               # 依赖 ../composer-agentic_rag
└── .env                         # API keys（从 .env.example 复制）
```

## 初始化

前置：与 RAG 库 sibling 放置（`Desktop/composer-eval` + `Desktop/composer-agentic_rag`）。

**uv（推荐）：**

```powershell
cd C:\Users\JoeyC\Desktop\composer-eval
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install -e .
```

**pip：**

```powershell
cd C:\Users\JoeyC\Desktop\composer-eval
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ..\composer-agentic_rag -e .
```

```powershell
copy .env.example .env
# 编辑 .env 填入 API key
```

## 运行

前置：

1. Qdrant 运行在 `127.0.0.1:6333`
2. 已在 RAG 库里建好 collection（默认 `getstart_codex_baseline`）：

```powershell
cd ..\composer-agentic_rag
python -m get_start.index_example
```

回到 eval 项目：

```powershell
cd ..\composer-eval
.\.venv\Scripts\Activate.ps1

# 全流程：gold → infer → extract
python -m eval.harness.main --stage all

# 分阶段
python -m eval.harness.main --stage gold
python -m eval.harness.main --stage infer
python -m eval.harness.main --stage extract
```

RAGChecker 打分（score 阶段尚未封装进 harness）：

```powershell
ragchecker-cli `
  --input eval/data/ragchecker/agent_self_rag_hyde/input.json `
  --output eval/data/ragchecker/agent_self_rag_hyde/scores.json
```

## 配置

| 文件 | 作用 |
|------|------|
| `config/agent_arg_config.yaml` | pattern 开关（crag / self_rag …） |
| `config/arg_config.yaml` | RAG index / retrieve profile |
| `eval/harness/main.py` → `DEFAULT_RUNNERS` | collection、runner_id、profile |
| `.env` | LLM / embedding / rerank API keys |

infer 阶段会自动：

- Agent：`RequestConfig.config_path` → `config/agent_arg_config.yaml`
- RAG：`get_rag_config(config/arg_config.yaml)`；Agent 内部 RAG 调用通过 `RAG_CONFIG_PATH` 环境变量指向同一文件

## 与 RAG 库的关系

```
composer-eval          composer-agentic_rag
  eval/harness    →    agent / rag / llm / tools
  config/*.yaml   →    运行时 profile（无需改库源码）
  eval/data/      ←    infer + RAGChecker 产物
```

日后合并：把 `eval/` 移回 RAG 仓库，恢复 `[project.optional-dependencies] eval` 即可。
