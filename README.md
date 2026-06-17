![Python 3.11+](https://img.shields.io/badge/Python%203.11%2B-3776AB?style=flat-square)
  ![MIT](https://img.shields.io/badge/MIT-34D058?style=flat-square)
  ![v2.2.0](https://img.shields.io/badge/v2.2.0-8A4FCE?style=flat-square)
  ![17 MCP](https://img.shields.io/badge/17%20MCP-007EC6?style=flat-square)
  ![18 skills](https://img.shields.io/badge/18%20skills-FE7D37?style=flat-square)
  ![26 KB files](https://img.shields.io/badge/26%20KB%20files-D73A4A?style=flat-square)
  ![185 tests](https://img.shields.io/badge/185%2F185%20tests-0EA5E9?style=flat-square)
  ![BDI+ReAct](https://img.shields.io/badge/BDI%2BReAct-EC4899?style=flat-square)
  ![5-layer](https://img.shields.io/badge/5-layer-F59E0B?style=flat-square)
  ![SSE stream](https://img.shields.io/badge/SSE%20stream-6B7280?style=flat-square)
  [![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/porpoise-agent)
</p>

[English](README.md) · [中文](README.zh.md)

<div align="center"><h3>🌊 Everything flows.</h3></div>

The world is dynamic, knowledge is temporary, emergence is the norm.

---

## 📖 Table of Contents

- [Philosophy](#-philosophy)
- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Version History](#-version-history)
- [Self-Assessment](#-self-assessment)
- [Ecosystem](#-ecosystem)

---

## 🏛�?Philosophy

> The river flows, knowledge drifts, emergence patterns.

This is not a slogan. It is the operating system running through every line of code, every search, every analysis.

This project is a **Derived Domain Expert (P�?** in the SanShengWanWu Triangle Core + Derived architecture, coordinated by **eon-core**. It inherits knowledge from S/V0 (fish-ecology-assistant) and verification from V/V1 (cognitive-search-engine), then specializes in Yangtze finless porpoise (*Neophocaena asiaeorientalis*) research.

### 📜 Three Tenets

**🌊 The River Flows** �?Packages update, species migrate, consensus shifts, climate reshapes. Today's certainty is tomorrow's footnote. We place knowledge on a timeline and view it dynamically.

**🍂 Knowledge Drifts** �?The foundation of science is falsifiability (Popper). No discovery is final �?only the best current explanation. We speak in calibrated language: evidence suggests, not proves.

**🌟 Emergence Patterns** �?Life, consciousness, ecosystems, AI reasoning �?all emergent. When three or more independent sources converge on the same unexpected pattern, the system flags emergence �?never dismisses it as noise.

### ⚖️ Why This Matters

| Scenario | Traditional | Dynamic Worldview |
|:---------|:-----------|:-------------------|
| Citations | Studies prove | Smith (2022) found X; Jones (2024) added Y |
| Outliers | Dismiss as noise | Three or more sources �?emergence signal |
| Knowledge Decay | Handbook frozen | Review records include next review date |
| Method | Fixed pipeline | Dynamic selection, dynamic confidence |

> 道生一，一生二，二生三，三生万物�?
From One comes Two, from Two comes Three, from Three come all things.

---

## 🧩 What This Is

**Porpoise Agent** is a specialized AI research agent for Yangtze finless porpoise conservation. It combines:

- **5-layer cybernetic architecture** (Interaction �?Cognitive �?Memory �?Mapping �?Execution)
- **7-agent MAS topology** (Literature, Acoustic, Ecology, Conservation, Critic, +2 support)
- **17 MCP tools** across search, compute, data, and knowledge categories
- **18 skills** for domain-specific analysis workflows
- **185/185 tests passing** with 35 bug fixes applied
- **26 KB files** of curated porpoise research knowledge

---

## 🚀 Quick Start

```bash
# Clone
git clone git@github.com:fangtaocai041/porpoise-agent.git
cd porpoise-agent

# Install
pip install -e .

# Run
python src/cli.py chat "Analyze finless porpoise acoustic data"
```

---

## 🏗�?Architecture

### Triangle Core + Derived Role

```
Triangle Core + Derived Architecture (coordinated by eon-core):

  S/V0  fish-ecology-assistant    �?Knowledge Supply
  V/V1  cognitive-search-engine   �?Search Verification
  Coord  eon-core                  �?Coordination Hub

  P�?   🐬 porpoise-agent         �?Porpoise Expert �?this project
  P�?   🐟 coilia-agent           �?Coilia Expert
  P�?   🐟 culter-agent           �?Culter Expert
  C     🔥 conflict-arbiter       �?Conflict Arbitration
```

### 5-Layer Internal Architecture

```
porpoise-agent/
  src/
  ├── interaction/     L1 �?NLU intent parser + Markdown renderer
  �?  └── sse_emitter.py   SSE streaming output
  ├── cognitive/       L2 �?BDI + ReAct + Reflexion + Decomposer (CoT/ToT/GoT)
  �?  ├── bdi.py            Formal BDI with MDP correspondence
  �?  ├── react_loop.py     Think→Act→Observe→Reflect engine
  �?  ├── reflexion.py      Credit assignment + self-critique
  �?  ├── decomposer.py     CoT/ToT/GoT task decomposition
  �?  ├── search.py         BFS/DFS/Beam/MCTS thought-space search
  �?  └── stategraph.py     LangGraph-inspired StateGraph topology
  ├── memory/          L3 �?STM + LTM (ChromaDB RAG)
  ├── mapping/         L4 �?IntentRouter + Serializer + Validator
  ├── execution/       L5 �?Sandbox + ToolRegistry + APIClient
  ├── agents/          7 specialized agents with graph topology
  └── integration/     4 adapters (cognitive-search/Zotero/Obsidian/Neo4j)
  config/
  ├── agent.yaml             Agent orchestration (v2.2.0)
  ├── mcp_servers.yaml       17 MCP server definitions
  ├── evolution.yaml         Self-evolution parameters
  └── component_registry.yaml Living system component registry
  tests/
  ├── test_bdi.py               BDI cognitive tests
  ├── test_bdi_standalone.py    BDI standalone tests
  ├── test_integration.py       Integration tests
  ├── test_memory.py            Memory system tests
  ├── test_memory_standalone.py Memory standalone tests
  ├── test_search_standalone.py Search strategy tests
  └── test_serializer.py        Serializer tests
```

---

## �?Features

| Feature | Status | Description |
|---------|:------:|-------------|
| 🧠 BDI+ReAct+Reflexion | �?| Full cognitive loop with MDP correspondence |
| 🌳 CoT/ToT/GoT/MCTS | �?| 4 decomposition + 5 search strategies |
| 🕸�?StateGraph | �?| LangGraph-style conditional routing |
| 🔴 SSE Streaming | �?| Real-time agent output |
| 🗄�?ChromaDB RAG | �?| Vector LTM with graceful degradation |
| 🔧 7-Agent MAS | �?| 6 topology types + condition edges |
| 🔒 Subprocess Sandbox | �?| Import whitelist + resource limits |
| 📚 4 Integrations | �?| cognitive-search, Zotero, Obsidian, KG |
| 📦 7 Optional Deps | �?| acoustics/spatial/knowledge/ml/all/dev/gpu |
| 🔄 Self-Evolution | �?| Cross-project parameter propagation |
| ⚠️ Acoustic/Ecology | 🟡 | Framework ready, core methods stub |
| 🐬 Domain Focus | �?| Yangtze finless porpoise research |
| 🧪 Test Suite | �?| 185/185 passing (35 fixes applied) |

---

### Research Pipeline (5 Phases)

| Phase | Name | Description |
|:-----:|------|-------------|
| 1 | Literature Review | Multi-engine search + citation graph |
| 2 | Data Analysis | Signal processing + feature extraction |
| 3 | Field Survey | Route generation + configuration |
| 4 | Conservation Assessment | Indicator calculation + scenario simulation |
| 5 | Output Generation | Draft generation + typesetting |

---

## 📁 Project Structure

```
porpoise-agent/
  (see Architecture section above)
```

---

## 📜 Version History

| Version | Date | Highlights |
|---------|------|------------|
| **v2.2.0** | 2026-06-17 | 17 MCP integration, 18 skills, 26 KB files, 185/185 tests, cross-project evolution |
| v2.1.0 | 2026-06-12 | SSE streaming, StateGraph conditional routing, ChromaDB RAG |
| v2.0.0 | 2026-06-07 | 5-layer architecture, 7-agent MAS, BDI+ReAct+Reflexion loop |
| v1.0.0 | 2026-06-01 | Initial porpoise agent framework |

---

## 🪞 Self-Assessment

### Strengths
- **Full cognitive stack**: BDI (belief modeling) + ReAct (reasoning loop) + Reflexion (self-critique) �?unique in domain-specific agents
- **MAS topology**: 7 agents with 6 topology types, enabling complex research workflows
- **Triangle-powered**: Inherits knowledge from S-layer and verification from V-layer via eon-core
- **Comprehensive testing**: 185/185 tests with 35 bug fixes �?high reliability baseline
- **Graceful degradation**: ChromaDB RAG falls back to keyword search when vector DB unavailable

### Current Limitations
- Acoustic analysis framework is scaffolded but core methods are stubs (requires domain data)
- Ecology agent depends on external R environment for advanced statistics
- Neo4j knowledge graph integration is optional and not yet populated
- Limited to single-species focus (finless porpoise only)

### Roadmap
- [ ] Complete acoustic analysis pipeline (NBHF click detection, whistle classification)
- [ ] Population viability analysis (PVA) module
- [ ] Real-time field survey data ingestion
- [ ] Multi-species extension framework

---

## 🔗 Ecosystem

This project is the **Porpoise Domain Expert (P�?** in the SanShengWanWu ecosystem.

```
Triangle Core + Derived Architecture (coordinated by eon-core):

  S/V0  📦 fish-ecology-assistant    �?Knowledge Supply
  V/V1  🔍 cognitive-search-engine   �?Search Verification
  Coord ⚙️ eon-core                  �?Coordination Hub

  P�?   🐬 porpoise-agent           �?Porpoise Expert �?this project
  P�?   🐟 coilia-agent             �?Coilia Expert
  P�?   🐟 culter-agent             �?Culter Expert
  C     🔥 conflict-arbiter         �?Conflict Arbitration
```

> 🔥 Together infinite power, apart top expert engines.

---

## 📋 README Changelog

| Version | Date | Theme | What Changed |
|---------|------|-------|--------------|
| v8.0 | 2026-06-20 | README Restoration | Restored from historical sessions, added DeepWiki badge, skills/MCP list, 5-phase pipeline details, README Changelog |
| v2.2.0 | 2026-06-17 | Production Release | 17 MCP integration, 18 skills, 26 KB files, 185/185 tests, cross-project evolution |
| v2.1.0 | 2026-06-12 | Streaming & RAG | SSE streaming, StateGraph conditional routing, ChromaDB RAG |
| v2.0.0 | 2026-06-07 | Architecture | 5-layer architecture, 7-agent MAS, BDI+ReAct+Reflexion loop |
| v1.0.0 | 2026-06-01 | Foundation | Initial porpoise agent framework |

---

🌱 **Everything Flows · Panta Rhei**

> Heraclitus said: No man ever steps in the same river twice.
>
> We say: You cannot analyze today's ecological data with last month's code.

This project is not a fixed toolset �?it is a **living system**. Every component has built-in expiration mechanisms, version tracking, and emergence awareness. As your research deepens, packages update, and new methods emerge, it evolves with you.

*Last updated: 2026-06-17　|　Environment: Reasonix Code · DeepSeek Powered*
