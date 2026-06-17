# 🐬 Porpoise Agent

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge) ![Version](https://img.shields.io/badge/Version-v0.2.0-blueviolet?style=for-the-badge) ![Agents](https://img.shields.io/badge/Agents-7-agent%20MAS-success?style=for-the-badge) ![Architecture](https://img.shields.io/badge/Architecture-5-layer-orange?style=for-the-badge) ![BDI](https://img.shields.io/badge/BDI-ReAct%2BReflexion-red?style=for-the-badge) ![GoT](https://img.shields.io/badge/GoT-MCTS-yellow?style=for-the-badge) ![SSE](https://img.shields.io/badge/SSE-Streaming-9cf?style=for-the-badge) ![ChromaDB](https://img.shields.io/badge/ChromaDB-RAG-ff69b4?style=for-the-badge) ![StateGraph](https://img.shields.io/badge/StateGraph-LangGraph-important?style=for-the-badge)

> 🎯 Porpoise Domain Expert Engine — 5-layer cognitive architecture with BDI+ReAct+Reflexion, 7-agent MAS, and frontier techniques.
> A porpoise knows the river — an agent knows the domain.

[English](README.md) · [中文](README.zh.md) · [CHANGELOG](CHANGELOG.md)

---

## 📖 Table of Contents

- [Philosophy](#-philosophy)
- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Ecosystem](#-ecosystem)

---

## 🏛️ Philosophy

> The agent does not simulate the porpoise — it embodies porpoise research.

This is **P₁**, the first derived project of SanShengWanWu. It applies a 5-layer cybernetic architecture (Interaction→Cognition→Memory→Mapping→Execution) with formal BDI+ReAct+Reflexion cognitive loops, 7 specialized agents communicating via 6 topology types, and frontier techniques including Tree/Graph of Thoughts, MCTS, and StateGraph orchestration.

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

## 🏗️ Architecture

```
porpoise-agent/
  src/
  ├── interaction/     L1 — NLU intent parser + Markdown renderer
  │   └── sse_emitter.py   SSE streaming output
  ├── cognitive/       L2 — BDI + ReAct + Reflexion + Decomposer (CoT/ToT/GoT)
  │   ├── bdi.py            Formal BDI with MDP correspondence
  │   ├── react_loop.py     Think→Act→Observe→Reflect engine
  │   ├── reflexion.py      Credit assignment + self-critique
  │   ├── decomposer.py     CoT/ToT/GoT task decomposition
  │   ├── search.py         BFS/DFS/Beam/MCTS thought-space search
  │   └── stategraph.py     LangGraph-inspired StateGraph topology
  ├── memory/          L3 — STM + LTM (ChromaDB RAG)
  ├── mapping/         L4 — IntentRouter + Serializer + Validator
  ├── execution/       L5 — Sandbox + ToolRegistry + APIClient
  ├── agents/          7 specialized agents with graph topology
  └── integration/     4 adapters (cognitive-search/Zotero/Obsidian/Neo4j)
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 BDI+ReAct+Reflexion | Formal cognitive loop with MDP correspondence |
| 🌳 CoT/ToT/GoT/MCTS | Multiple task decomposition and search strategies |
| 🕸️ StateGraph | LangGraph-inspired conditional edge routing |
| 🔴 SSE Streaming | Real-time agent output via Server-Sent Events |
| 🗄️ ChromaDB RAG | Vector-backed long-term memory with graceful degradation |
| 🔧 7-Agent MAS | Literature, Acoustic, Ecology, Conservation, Critic... |
| 🔀 6 Topology Types | Sequential, Hierarchical, Star, Debate, DAG, Dynamic |
| 🔒 Subprocess Sandbox | Safe code execution with import whitelist |
| 📚 4 Integrations | cognitive-search, Zotero, Obsidian, Neo4j/KnowledgeGraph |

---

## 📁 Project Structure

```
porpoise-agent/
  (see Architecture section above)
```

---

## 🔗 Ecosystem

This project is the Porpoise Domain Expert Engine (P₁) in the SanShengWanWu ecosystem.

```
Triangle Core (sealed 3):
  📦 fish-ecology-assistant    → Knowledge Supply (V0)
  🔍 cognitive-search-engine   → Search Verification (V1)
  ⚙️ eon-core                  → Coordination Hub (Coord)

Derived Projects (open N):
  🐬 porpoise-agent    → P₁ Porpoise Expert
  🐟 coilia-agent      → P₂ Coilia Expert
  🐟 culter-agent      → P₃ Culter Expert
  🔥 conflict-arbiter  → C  Conflict Arbitration
```

> 🔥 Together infinite power, apart top expert engines.

---
*淡水渔业研究中心 刘凯研究员课题组 · SanShengWanWu Ecosystem · MIT License*
