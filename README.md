# Porpoise Agent 🐬

**P₁ 万物衍生** — 长江江豚专研 · 多智能体系统 · BDI 决策 · 五层认知架构

> 🌊 万物皆变 · Panta Rhei
>
> 江豚在长江里游了 2500 万年。
> 我们的代码，是试图理解它们的另一种语言。

[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://python.org)
[![version](https://img.shields.io/badge/version-0.1.0-8b5cf6)]()

[English](README_en.md) · [更新日志](CHANGELOG.md)

---

## 📋 简介

**Porpoise Agent** 是面向长江江豚（*Neophocaena asiaeorientalis*）研究的 AI Agent 框架，基于 **多智能体系统 (MAS)** + **BDI 认知架构** + **五层维度演化引擎**。自动化文献检索、NBHF 声学分析、生态建模与保护评估。

长江江豚是长江里唯一的哺乳动物。2017 年种群调查约 1012 头，2022 年约 1249 头——禁渔后第一次止跌回升。本项目追踪它们的声学信号（NBHF，100–180kHz）、建模栖息地分布、评估种群动态。

---

## ⚡ 快速上手

### 安装

```bash
# 最小安装（仅核心功能）
pip install -e .

# 带声学分析支持
pip install -e ".[acoustics]"

# 带空间分析支持
pip install -e ".[spatial]"

# 全功能安装
pip install -e ".[all]"

# 开发安装
pip install -e ".[dev]"
```

### 验证安装

```bash
# 健康检查
porpoise doctor

# 查看拓扑
porpoise topology
```

### CLI 使用

```bash
porpoise doctor              # 健康检查
porpoise topology            # 查看 MAS 拓扑
porpoise chat                # 交互对话
porpoise run "搜索江豚声学监测文献"  # 执行研究任务
```

---

## 🏗️ 架构

基于五层标准智能体分层架构：

```
┌──────────────────────────────────────────┐
│  1. Interaction   — 交互与感知层 (NLU)     │
│  2. Cognitive     — 认知与决策层 (BDI+ReAct)│
│  3. Memory        — 记忆系统层 (STM+LTM)    │
│  4. Mapping       — 逻辑映射与转换层        │
│  5. Execution     — 工具与执行层            │
└──────────────────────────────────────────┘
```

### 多智能体系统

| Agent | 职责 |
|:------|:-----|
| **OrchestratorAgent** | 中央调度器 — 理解意图、构建拓扑、编排执行 |
| **LiteratureAgent** | 文献搜索与分析 — PubMed/CrossRef/Semantic Scholar |
| **AcousticAgent** | NBHF 声学分析 — click 检测、buzz 识别、觅食指数 |
| **EcologyAgent** | 生态建模 — 种群评估、栖息地适宜性 |
| **ConservationAgent** | 保护评估 — IUCN 标准、威胁分析 |
| **CriticAgent** | 批判审查 — 结果验证、方法论评估 |
| **Topology** | 图拓扑引擎 — 节点+边+消息路由 |

### BDI 状态机

```
IDLE → PERCEIVING → DELIBERATING → EXECUTING → REFLECTING → DONE
  ↑                                                          │
  └────────────────── FAILED ←────────────────────────────────┘
```

- **Belief (信念)**: Agent 对环境的客观认知
- **Desire (愿望)**: 持久目标（System Prompt + 用户目标）
- **Intention (意图)**: 当前行动计划（CoT 分解）

---

## 📦 可选依赖组

| 分组 | 安装命令 | 包含 |
|:-----|:---------|:-----|
| `acoustics` | `pip install ".[acoustics]"` | librosa, obspy, pamguide |
| `spatial` | `pip install ".[spatial]"` | geopandas, rasterio, shapely |
| `knowledge` | `pip install ".[knowledge]"` | neo4j, chromadb |
| `ml` | `pip install ".[ml]"` | scikit-learn, torch |
| `all` | `pip install ".[all]"` | 以上全部 |
| `dev` | `pip install ".[dev]"` | pytest, black, ruff, mypy |
| `gpu` | `pip install ".[gpu]"` | torch+torchaudio, tensorflow |

缺失可选依赖时系统会优雅降级——打印 warning 并跳过对应功能，不会崩溃。

---

## 🧪 测试

```bash
# 运行所有测试
pytest

# 仅单元测试
pytest -m unit

# 仅集成测试
pytest -m integration

# 跳过网络测试
pytest -m "not network"
```

---

## 📁 项目结构

```
porpoise-agent/
├── src/
│   ├── agents/          # 多智能体 (Orchestrator, Literature, Acoustic, ...)
│   ├── cognitive/       # 认知层 (BDI, ReAct, Reflexion, Search)
│   ├── execution/       # 工具执行层 (Sandbox, ToolRegistry, API)
│   ├── interaction/     # 交互层 (NLU, Renderer)
│   ├── mapping/         # 映射层 (Router, Serializer, Validator)
│   ├── memory/          # 记忆层 (STM, LTM, Manager)
│   ├── integration/     # 外部集成 (Zotero, Obsidian, Neo4j, cognitive-search)
│   ├── prompts/         # System Prompts
│   ├── skills/          # 可复用技能
│   ├── tools/           # 工具定义
│   └── utils/           # 工具函数
├── tests/               # 测试
├── config/              # 配置文件
├── docs/                # 文档
├── examples/            # 示例
└── pyproject.toml       # 项目配置
```

---

## 🔗 生态体系

本项目是「三生万物」生态的 P₁。

```
三角核心 (sealed 3):
  📦 fish-ecology-assistant    → 知识供给 (V0)
  🔍 cognitive-search-engine   → 搜索验证 (V1)
  ⚙️ eon-core                  → 协调内核 (Coord)

万物衍生 (open N):
  🐬 porpoise-agent    → 江豚专研 (P₁)  ← 你在这里
  🐟 coilia-agent      → 刀鲚专研 (P₂)
  🐟 culter-agent      → 鲌类专研 (P₃)
  🔥 conflict-arbiter  → 冲突仲裁 (C)
```

---

## 🙏 致谢

服务: 无锡渔业学院/淡水渔业研究中心 刘凯研究员课题组

---

> 🌊 万物皆变 · Panta Rhei
>
> 🏛️ 赫拉克利特说：人不能两次踏进同一条河流。
>
> 💻 我们说：你也不能用去年的种群数据预测今年的江豚分布。
>
> **📅 最后更新: 2025-07 · 🖥️ Reasonix Code · ⚡ DeepSeek 驱动**

[⬆ 回到顶部](#)
