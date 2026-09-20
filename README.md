# composer-agentic-eval

从 sibling 库 [`composer-agentic-rag`](../AgenticRAG) 剥离的端到端评测项目：gold → Agent/RAG infer → extract → RAGChecker score。

运行时依赖 `composer-agentic-rag`（editable install），Cursor 只打开本目录即可。

## 目录结构

```
composer-eval/
├── config/
│   ├── arg_config.yaml          # RAG profile（chunk / retrieve）
│   └── agent_arg_config.yaml    # Agent pattern toggles
├── corpus/doc4RAG/              # 评测语料
├── gold/                        # 完整金标（进 git）
│   └── qa_exports/              # Easy Dataset 导出
├── demo/                        # 只读样例：rag_rerank_hyde 的 2 条 query + scores
├── data/                        # 运行时 infer / ragchecker（不进 git）
├── eval/
│   ├── base.py                  # 类型定义
│   ├── easy_gold/               # LLM 生成金标
│   ├── RAGChecker/              # 打分
│   └── harness/
│       ├── main.py              # 管线入口
│       ├── index.py             # 语料 → Qdrant
│       ├── infer/agent.py
│       └── infer/rag.py
├── pyproject.toml               # 依赖 ../AgenticRAG
└── .env                         # API keys（从 .env.example 复制）
```

Clone 后金标已在 `gold/`。infer / extract / score 写入本地 `data/`。`demo/` 是格式快照，harness 不读写它；其中 `scores.json` 来自全量打分，infer / input / checking_outputs 只保留 `query_001` 与 `query_002`。

## 初始化

前置：与 RAG 库 sibling 放置（`composer-eval` + `AgenticRAG`）。

**uv（推荐）：**

```powershell
cd C:\Users\JoeyC\Projects\composer-eval
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install -e .
```

**pip：**

```powershell
cd C:\Users\JoeyC\Projects\composer-eval
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ..\AgenticRAG -e .
```

```powershell
copy .env.example .env
# 编辑 .env 填入 API key
```

## 运行

前置：

1. Qdrant 运行在 `127.0.0.1:6333`
2. 已索引本仓库语料（默认 collection `openclaw_docs_b`）：

```powershell
python -m eval.harness.index
```

然后：

```powershell
.\.venv\Scripts\Activate.ps1

# 默认：infer → extract → score（使用 gold/openclaw_docs_qa.json）
python -m eval.harness.main --stage all

# 分阶段
python -m eval.harness.main --stage infer
python -m eval.harness.main --stage extract
python -m eval.harness.main --stage score

# 从 Easy Dataset 导出重写金标（可选）
python -m eval.harness.main --stage gold

# 从语料 LLM 生成金标（可选）
python -m eval.easy_gold.generate
```

单独打分也可以：

```powershell
python -m eval.RAGChecker --runner rag_rerank_hyde
```

## 配置

| 文件 | 作用 |
|------|------|
| `config/agent_arg_config.yaml` | pattern 开关（crag / self_rag …） |
| `config/arg_config.yaml` | RAG index / retrieve profile |
| `eval/harness/runners.py` | collection、runner_id、profile |
| `.env` | LLM / embedding / rerank API keys |

infer 阶段会自动：

- Agent：`RequestConfig.config_path` → `config/agent_arg_config.yaml`
- RAG：`get_rag_config(config/arg_config.yaml)`；Agent 内部 RAG 调用通过 `RAG_CONFIG_PATH` 环境变量指向同一文件

## 与 RAG 库的关系

```
composer-eval          AgenticRAG
  eval/harness    →    agent / rag / llm / tools
  config/*.yaml   →    运行时 profile（无需改库源码）
  gold/           →    完整金标
  data/           ←    infer + RAGChecker 产物（本地）
  demo/           ←    少量样例快照（进 git）
```

日后合并：把 `eval/` 移回 RAG 仓库，恢复 `[project.optional-dependencies] eval` 即可。
