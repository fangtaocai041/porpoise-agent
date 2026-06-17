# 🐬 江豚智能体

[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-8b5cf6)]()
[![Agents](https://img.shields.io/badge/agents-7-22c55e)]()
[![Frontier](https://img.shields.io/badge/frontier-BDI|ReAct|GoT|MCTS|SSE-orange)]()

> 🎯 江豚领域专家引擎 — 5层认知架构，BDI+ReAct+Reflexion，7智能体MAS，前沿技术。
> 江豚知江河，智能体知领域。

[English](README.md) · [中文](README.zh.md) · [更新日志](CHANGELOG.md)

---

## 📖 目录

- [哲学](#-哲学)
- [快速开始](#-快速开始)
- [架构](#-架构)
- [功能特性](#-功能特性)
- [项目结构](#-项目结构)
- [生态体系](#-生态体系)

---

## 🏛️ 哲学

> 智能体不模拟江豚——它本身就是江豚研究的化身。

这是**P₁**，三生万物的第一个衍生项目。五层控制论架构（交互→认知→记忆→映射→执行），形式化BDI+ReAct+Reflexion认知循环，7个专业智能体通过6种拓扑通信，前沿技术包括Tree/Graph of Thoughts、MCTS、StateGraph编排。

---

## 🚀 快速开始

```bash
git clone git@github.com:fangtaocai041/porpoise-agent.git
cd porpoise-agent
pip install -e .
python src/cli.py chat "分析长江江豚声学数据"
```

---

## 🏗️ 架构

```
porpoise-agent/
  src/
  ├── interaction/     L1 — NLU意图解析 + Markdown渲染
  │   └── sse_emitter.py   SSE 流式输出
  ├── cognitive/       L2 — BDI + ReAct + Reflexion + 任务分解
  │   ├── bdi.py            形式化BDI (MDP对应)
  │   ├── react_loop.py     Think→Act→Observe→Reflect 引擎
  │   ├── reflexion.py      信用分配 + 自我批判
  │   ├── decomposer.py     CoT/ToT/GoT 任务分解
  │   ├── search.py         BFS/DFS/Beam/MCTS 思维空间搜索
  │   └── stategraph.py     LangGraph 风格 StateGraph 拓扑
  ├── memory/          L3 — 短期记忆 + 长期记忆 (ChromaDB RAG)
  ├── mapping/         L4 — 意图路由 + 序列化 + 验证
  ├── execution/       L5 — 沙盒 + 工具注册 + API客户端
  ├── agents/          7 个专业智能体 + 图拓扑
  └── integration/     4 个适配器
```

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🧠 BDI+ReAct+Reflexion | 形式化认知循环 (MDP对应) |
| 🌳 CoT/ToT/GoT/MCTS | 多种任务分解和搜索策略 |
| 🕸️ StateGraph | LangGraph风格条件边路由 |
| 🔴 SSE 流式 | 实时智能体输出 |
| 🗄️ ChromaDB RAG | 向量长期记忆+优雅降级 |
| 🔧 7-Agent MAS | 文献/声学/生态/保护/批判... |
| 🔀 6种拓扑类型 | 顺序/层级/星形/辩论/DAG/动态 |
| 🔒 子进程沙盒 | 安全代码执行 |
| 📚 4项集成 | cognitive-search, Zotero, Obsidian, Neo4j |

---

## 📁 项目结构

```
porpoise-agent/
  (见上方架构图)
```

---

## 🔗 生态体系

本项目是「三生万物」生态的 江豚领域专家引擎 (P₁)。

```
三角核心 (sealed 3):
  📦 fish-ecology-assistant    → 知识供给 (V0)
  🔍 cognitive-search-engine   → 搜索验证 (V1)
  ⚙️ eon-core                  → 协调内核 (Coord)

万物衍生 (open N):
  🐬 porpoise-agent    → P₁ 江豚专研
  🐟 coilia-agent      → P₂ 刀鲚专研
  🐟 culter-agent      → P₃ 鲌类专研
  🔥 conflict-arbiter  → C  冲突仲裁
```

> 🔥 和则无穷力量，分则顶尖专家引擎。

---
*淡水渔业研究中心 刘凯研究员课题组 · SanShengWanWu Ecosystem · MIT License*
