# Porpoise Agent 馃惉

**P鈧?涓囩墿琛嶇敓** 鈥?Yangtze Finless Porpoise Research 路 Multi-Agent System 路 BDI Decision 路 5 Cognitive Layers

> 馃寠 Everything Flows 路 Panta Rhei
>
> The finless porpoise has swum the Yangtze for 25 million years.
> Our code is another language trying to understand them.

[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://python.org)
[![version](https://img.shields.io/badge/version-0.1.0-8b5cf6)]()
[![agents](https://img.shields.io/badge/agents-7-f59e0b)]()

[English](README.md) 路 [涓�枃](README_en.md) 路 [Changelog](CHANGELOG.md)

---

## 馃搵 Introduction

**Porpoise Agent** is an AI Agent framework for Yangtze finless porpoise (*Neophocaena asiaeorientalis asiaeorientalis*) research, built on a **Multi-Agent System (MAS)** with a **BDI cognitive architecture** and **5-layer dimensional evolution engine**. It automates literature search, NBHF acoustic analysis, ecological modeling, and conservation assessment.

### 馃殌 Capabilities

| 馃殌 Capability | 馃摑 Description |
| :-------------- | :--------------- |
| **Multi-Agent System** | 7 specialized agents: Orchestrator, Literature, Acoustic, Ecology, Conservation, Critic + Topology |
| **BDI Decision Engine** | Belief-Desire-Intention state machine — `BDICoordinator` |
| **Three-Tier Memory** | STM (context) + LTM (ChromaDB vector store) + Manager |
| **Dimensional Evolution** | 5-layer cognitive architecture |
| **Quadruple Integration** | cognitive-search-engine, Neo4j, Zotero, Obsidian |
| **Bayesian Analysis** | `bayesian_trend_analysis()`, `bayesian_ab_compare()`, `bayesian_sample_size_plan()` — reproducible seed=42 |
| **Sandbox Execution** | Isolated Python runtime via `SandboxExecutor` |
| **Test Coverage** | BDI state machine + Memory + Serializer + workflow scenarios |

---

## 鈿?Quick Start

### 馃摝 Installation

```bash
git clone https://github.com/FFRC-LiuKai-Lab/porpoise-agent.git
cd porpoise-agent
pip install -e .
```

### 鉁?Verify Installation

```python
from porpoise_agent.src.agents import OrchestratorAgent

orch = OrchestratorAgent()
print(f"Agents registered: {len(orch.list_agents())}")
```

### 馃幃 CLI Usage

```bash
porpoise doctor         # Health check
porpoise topology       # Show MAS topology
porpoise chat           # Interactive chat mode
porpoise run TASK       # Run a single research task
```

---

## 馃殌 Core Features

### 1锔忊儯 Multi-Agent System

```python
from porpoise_agent.src.agents import (
    OrchestratorAgent, LiteratureAgent, AcousticAgent,
    EcologyAgent, ConservationAgent, CriticAgent,
)

orch = OrchestratorAgent()
orch.register_agent(LiteratureAgent())
orch.register_agent(AcousticAgent())
orch.register_agent(EcologyAgent())
orch.register_agent(ConservationAgent())
orch.register_agent(CriticAgent())

result = orch.run("Analyze porpoise population status")
```

### 2锔忊儯 BDI Decision Making

```python
from porpoise_agent.src.cognitive import BDICoordinator, Belief, Desire

bdi = BDICoordinator()
bdi.add_belief(Belief("species", "Neophocaena asiaeorientalis"))
bdi.add_belief(Belief("population", 1200))
bdi.add_desire(Desire("assess_threat", priority=0.9,
                       condition=lambda b: b.get("population", 0) < 1500))
plan = bdi.deliberate()
```

### 3锔忊儯 Memory System

```python
from porpoise_agent.src.memory import MemoryManager

memory = MemoryManager()
memory.stm.store("last_query", "porpoise habitat")
memory.ltm.store_document("paper_001", "Acoustic analysis of finless porpoise")
results = memory.ltm.search("acoustic", top_k=5)
```

### 4锔忊儯 Sandbox Execution

```python
from porpoise_agent.src.execution import execute_safe

result = execute_safe("print(f'Mean: {sum([1,2,3,4,5])/5}')")
print(result.output)
```

---

## 馃幃 CLI Commands

| 馃幃 Command | 馃摑 Description | 馃挕 Example |
|:-----------|:---------------|:-----------|
| `porpoise chat` | Interactive chat (ReAct loop) | `porpoise chat --model deepseek-reasoner` |
| `porpoise run TASK` | Single research task | `porpoise run "Analyze acoustic data"` |
| `porpoise topology` | Show MAS topology | `porpoise topology` |
| `porpoise doctor` | Health check | `porpoise doctor` |

---

## 馃摎 Project Structure

```
porpoise-agent/
鈹溾攢鈹€ src/
鈹?  鈹溾攢鈹€ cli.py                    鈫?CLI 鍏ュ彛 (porpoise doctor/chat/run/topology)
鈹?  鈹溾攢鈹€ agents/                   鈫?Multi-Agent System (7 agents)
鈹?  鈹?  鈹溾攢鈹€ orchestrator.py       鈫?OrchestratorAgent 璋冨害鍣?
鈹?  鈹?  鈹溾攢鈹€ literature.py         鈫?LiteratureAgent 鏂囩尞鎼滅储
鈹?  鈹?  鈹溾攢鈹€ acoustic.py           鈫?AcousticAgent NBHF 澹板�鍒嗘瀽
鈹?  鈹?  鈹溾攢鈹€ ecology.py            鈫?EcologyAgent 鏍栨伅鍦拌瘎浼?
鈹?  鈹?  鈹溾攢鈹€ conservation.py       鈫?ConservationAgent 淇濇姢寤鸿�
鈹?  鈹?  鈹溾攢鈹€ critic.py             鈫?CriticAgent 鑷�弽鎬濆�鏌?
鈹?  鈹?  鈹溾攢鈹€ topology.py           鈫?MAS 鎷撴墤绠＄悊
鈹?  鈹?  鈹斺攢鈹€ base.py               鈫?BaseAgent 鍩虹被
鈹?  鈹溾攢鈹€ agent/                    鈫?5 灞傝�鐭ユ灦鏋?
鈹?  鈹?  鈹溾攢鈹€ orchestrator.py       鈫?棰嗗煙缂栨帓鍣?
鈹?  鈹?  鈹溾攢鈹€ loop.py               鈫?ReAct 寰�幆
鈹?  鈹?  鈹溾攢鈹€ meso_experiment.py    鈫?涓�眰瀹為獙寮曟搸
鈹?  鈹?  鈹溾攢鈹€ resilience_engine.py  鈫?闊ф€у紩鎿?
鈹?  鈹?  鈹溾攢鈹€ stv_core.py           鈫?STV 鏍稿績
鈹?  鈹?  鈹溾攢鈹€ dimensional_evolution.py 鈫?缁村害杩涘寲
鈹?  鈹?  鈹溾攢鈹€ memory.py             鈫?璁板繂绠＄悊
鈹?  鈹?  鈹溾攢鈹€ tools.py              鈫?宸ュ叿娉ㄥ唽
鈹?  鈹?  鈹斺攢鈹€ deepseek_optimizer.py 鈫?DeepSeek 浼樺寲鍣?
鈹?  鈹溾攢鈹€ cognitive/                鈫?BDI + ReAct + TaskDecomposer
鈹?  鈹溾攢鈹€ memory/                   鈫?STM + LTM (ChromaDB) + Manager
鈹?  鈹溾攢鈹€ execution/                鈫?Sandbox + ToolRegistry + APIClient
鈹?  鈹溾攢鈹€ interaction/              鈫?NLU 鎰忓浘璇嗗埆 + Response 娓叉煋
鈹?  鈹溾攢鈹€ mapping/                  鈫?Router + Serializer + Validator
鈹?  鈹溾攢鈹€ integration/              鈫?澶栭儴绯荤粺妗ユ帴
鈹?  鈹溾攢鈹€ knowledge/                鈫?鐭ヨ瘑鍥捐氨
鈹?  鈹溾攢鈹€ prompts/                  鈫?绯荤粺鎻愮ず璇?
鈹?  鈹溾攢鈹€ skills/                   鈫?鎶€鑳芥ā鍧?
鈹?  鈹溾攢鈹€ tools/                    鈫?宸ュ叿闆?
鈹?  鈹斺攢鈹€ utils/                    鈫?Config + logging + types
鈹溾攢鈹€ config/                       鈫?agent.yaml / models.yaml / mcp_servers.yaml
鈹溾攢鈹€ data/                         鈫?鐭ヨ瘑搴撴暟鎹?
鈹溾攢鈹€ docs/                         鈫?鏂囨。
鈹溾攢鈹€ examples/                     鈫?绀轰緥鑴氭湰
鈹溾攢鈹€ external/                     鈫?澶栭儴渚濊禆
鈹溾攢鈹€ scripts/                      鈫?宸ュ叿鑴氭湰
鈹斺攢鈹€ tests/                        鈫?5 娴嬭瘯濂椾欢
```

---

## 馃攲 External Integrations

| 馃枼锔?System | 馃敆 Adapter | 馃幆 Purpose |
|:----------|:-----------|:-----------|
| **cognitive-search-engine** | `CognitiveSearchAdapter` | Multi-engine literature search |
| **Neo4j Knowledge Graph** | `KnowledgeGraph` | Species relationship storage |
| **Zotero** | `ZoteroAdapter` | Research library access |
| **Obsidian** | `ObsidianAdapter` | Personal knowledge base |

---

## 馃敆 Related Projects
```
| 馃彈锔?Project | 馃幆 Role | 馃敆 Relationship |
|:-----------|:--------|:----------------|
| **eon-core** | Coordinator | Vertex V2 鈥?porpoise domain agent |
| **fish-ecology-assistant** | Knowledge V0 | Species knowledge base |
| **cognitive-search-engine** | Search V1 | Literature search and scoring |
| **coilia-agent** | P鈧?Coilia | Sister project |
| **culter-agent** | P鈧?Culter | Sister project |
```

---
```
## 馃摐 License
```
MIT License 漏 2026 Liu Kai Research Group, FFRC-----------|:--------:|:--------|
| [fish-ecology-assistant](../fish-ecology-assistant/) | V0 | 馃摝 Knowledge Supply |
| [cognitive-search-engine](../cognitive-search-engine/) | V1 | 馃攳 Search Verification |
| [eon-core](../eon-core/) | Coord | 鈿欙笍 Coordinator |
| [porpoise-agent](../porpoise-agent/) | P鈧?| 馃惉 Porpoise Research |
| [coilia-agent](../coilia-agent/) | P鈧?| 馃悷 Coilia Research |
| [culter-agent](../culter-agent/) | P鈧?| 馃悷 Culter Research |
| [conflict-arbiter](../conflict-arbiter/) | C | 馃敟 Conflict Arbiter |
```

---
---

```
## 馃敆 Ecosystem
```
> 馃敟 Together infinite power, apart top expert engines.
```
This project is the Porpoise Domain Expert Engine (P1) in the SanShengWanWu ecosystem.
```
```
Triangle Core (sealed 3):
  馃摝 fish-ecology-assistant    鈫?Knowledge Supply (V0)
  馃攳 cognitive-search-engine   鈫?Search Verification (V1)
  鈿欙笍 eon-core                  鈫?Coordinator
```
Derived Projects (open N):
  馃惉 porpoise-agent    鈫?Porpoise Research (P鈧?
  馃悷 coilia-agent      鈫?Coilia Research (P鈧?
  馃悷 culter-agent      鈫?Culter Research (P鈧?
  馃敟 conflict-arbiter  鈫?Conflict Arbitration (C)
```

> 馃寠 Everything Flows 路 Panta Rhei
>
> 馃彌锔?Heraclitus said: No man ever steps in the same river twice.
>
> 馃捇 We say: You can't analyze today's porpoise data with last month's code.
>
> **馃搮 Last updated: 2026-06-17 路 馃枼锔?Reasonix Code 路 鈿?Powered by DeepSeek**

[猬?Back to top](#)
