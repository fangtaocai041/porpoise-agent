![Python 3.11+](https://img.shields.io/badge/Python%203.11%2B-3776AB?style=flat-square)
  ![MIT](https://img.shields.io/badge/MIT-34D058?style=flat-square)
  ![v2.2.0](https://img.shields.io/badge/v2.2.0-8A4FCE?style=flat-square)
  ![17 MCP](https://img.shields.io/badge/17%20MCP-007EC6?style=flat-square)
  ![18 skills](https://img.shields.io/badge/18%20技?FE7D37?style=flat-square)
  ![26 KB files](https://img.shields.io/badge/26%20知识文件-D73A4A?style=flat-square)
  ![185 tests](https://img.shields.io/badge/185%2F185%20测试-0EA5E9?style=flat-square)
  ![BDI+ReAct](https://img.shields.io/badge/BDI%2BReAct-EC4899?style=flat-square)
  ![5-layer](https://img.shields.io/badge/5层架?F59E0B?style=flat-square)
  ![SSE stream](https://img.shields.io/badge/SSE%20?6B7280?style=flat-square)
  [![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/porpoise-agent)
</p>

[English](README.md) · [中文](README.zh.md)

<div align="center"><h3>🌊 万物皆流?/h3></div>

世界是动态的，知识是暂时的，涌现是常态?
---

## 📖 目录

- [哲学](#-哲学)
- [快速开始](#-快速开?
- [架构](#-架构)
- [功能特性](#-功能特?
- [项目结构](#-项目结构)
- [版本历史](#-版本历史)
- [自我评估](#-自我评估)
- [生态体系](#-生态体?

---

## 🏛?哲学

> 万象流转，真知若寄，涌现成章?
此非口号。乃贯穿每一行代码、每一次检索、每一份分析之操作系统?
本项目是三生万物三角核心 + 衍生架构中的**衍生领域专家（P₁）**，由 **eon-core** 统一协调。它?S/V0（fish-ecology-assistant）继承知识，?V/V1（cognitive-search-engine）继承验证能力，专注于长江江豚（*Neophocaena asiaeorientalis*）研究?
### 📜 三谛

**🌊 万象流转** ?R包迭代，物种迁徙，共识更迭，气候重塑生态。今日之确论，半载后或为陈迹。吾辈不视任何知识为永恒真理，而将其置于时间轴上，以动态眼光审之?
**🍂 真知若寄** ?科学之基石，在于可证伪（波普尔）。无发现乃终极真理——唯有「当下最佳解释」。吾辈用校准之语：「证据提示」而非「证明」，「Smith (2022) 发现」而非「研究表明」。每一条输出，皆镌刻时间之锚?
**🌟 涌现成章** ?生命、意识、生态、AI推理——莫非涌现。不可执一隅以窥全豹。当?个独立来源指向同一意外模式，系统不以其为噪声而弃之，乃标记为涌现信号而追踪之?
### ⚖ 何以重要

| 事境 | 旧习 | 新观 |
|:-----|:----|:----|
| 引用 | 「研究证明?| 「Smith(2022) 发现 X，Jones(2024) ?Y?|
| 异常 | 视为噪声弃之 | ? 来源 ?涌现信号，持续追?|
| 知识衰减 | 手册尘封不更 | 审查记录含「下次审查日期?|
| 方法选择 | 流水线一成不?| 择法动态，信心动?|

> 道生一，一生二，二生三，三生万物?
---

## 🧩 这个项目是什?
**Porpoise Agent** 是一个专注于长江江豚保护的专?AI 研究智能体。它结合了：

- **5层控制论架构**（交??认知 ?记忆 ?映射 ?执行?- **7智能?MAS 拓扑**（文献、声学、生态、保护、批?+ 2 辅助?- **17 ?MCP 工具**涵盖搜索、计算、数据和知识类别
- **18 个技?*用于领域分析工作?- **185/185 项测试通过**?5 个缺陷修?- **26 个知识文?*精选江豚研究知?
---

## 🚀 快速开?
```bash
git clone git@github.com:fangtaocai041/porpoise-agent.git
cd porpoise-agent
pip install -e .
python src/cli.py chat "分析长江江豚声学数据"
```

---

## 🏗?架构

### 三角核心 + 衍生角色

```
三角核心 + 衍生架构（由 eon-core 协调）：

  S/V0  fish-ecology-assistant    ?知识供给
  V/V1  cognitive-search-engine   ?搜索验证
  Coord  eon-core                  ?协调内核

  P?   🐬 porpoise-agent         ?江豚专家 ?本项?  P?   🐟 coilia-agent           ?刀鲚专?  P?   🐟 culter-agent           ?鲌类专家
  C     🔥 conflict-arbiter       ?冲突仲裁
```

### 五层内部架构

```
porpoise-agent/
  src/
  ├── interaction/     L1 ?NLU意图解析 + Markdown渲染
  ?  └── sse_emitter.py   SSE 流式输出
  ├── cognitive/       L2 ?BDI + ReAct + Reflexion + 任务分解
  ?  ├── bdi.py            形式化BDI (MDP对应)
  ?  ├── react_loop.py     Think→Act→Observe→Reflect 引擎
  ?  ├── reflexion.py      信用分配 + 自我批判
  ?  ├── decomposer.py     CoT/ToT/GoT 任务分解
  ?  ├── search.py         BFS/DFS/Beam/MCTS 思维空间搜索
  ?  └── stategraph.py     LangGraph 风格 StateGraph 拓扑
  ├── memory/          L3 ?短期记忆 + 长期记忆 (ChromaDB RAG)
  ├── mapping/         L4 ?意图路由 + 序列?+ 验证
  ├── execution/       L5 ?沙盒 + 工具注册 + API客户?  ├── agents/          7 个专业智能体 + 图拓?  └── integration/     4 个适配?(cognitive-search/Zotero/Obsidian/Neo4j)
  config/
  ├── agent.yaml             智能体编?(v2.2.0)
  ├── mcp_servers.yaml       17 ?MCP 服务器定?  ├── evolution.yaml         自进化参?  └── component_registry.yaml 活系统组件注册表
  tests/
  ├── test_bdi.py               BDI 认知测试
  ├── test_bdi_standalone.py    BDI 独立测试
  ├── test_integration.py       集成测试
  ├── test_memory.py            记忆系统测试
  ├── test_memory_standalone.py 记忆独立测试
  ├── test_search_standalone.py 搜索策略测试
  └── test_serializer.py        序列化器测试
```

---

## ?功能特?
| 功能 | 状?| 说明 |
|------|:--:|------|
| 🧠 BDI+ReAct+Reflexion | ?| 完整 MDP 认知循环 |
| 🌳 CoT/ToT/GoT/MCTS | ?| 4 分解 + 5 搜索策略 |
| 🕸?StateGraph | ?| LangGraph 风格条件路由 |
| 🔴 SSE 流式 | ?| 实时智能体输?|
| 🗄?ChromaDB RAG | ?| 向量长期记忆 + 优雅降级 |
| 🔧 7 ?MAS | ?| 6 种拓?+ 条件?|
| 🔒 子进程沙?| ?| 导入白名?+ 资源限制 |
| 📚 4 项集?| ?| cognitive-search, Zotero, Obsidian, KG |
| 📦 7 可选依?| ?| acoustics/spatial/knowledge/ml/all/dev/gpu |
| 🔄 自进?| ?| 跨项目参数传?|
| ⚠ 声学/生?Agent | 🟡 | 框架就绪，核心方法存?|
| 🐬 领域聚焦 | ?| 长江江豚研究 |
| 🧪 测试套件 | ?| 185/185 通过?5 个修复） |

---

### 研究流水线（5 阶段?
| 阶段 | 名称 | 说明 |
|:---:|------|------|
| 1 | 文献综述 | 多引擎搜?+ 引用图谱 |
| 2 | 数据分析 | 信号处理 + 特征提取 |
| 3 | 野外调查 | 路线生成 + 配置 |
| 4 | 保护评估 | 指标计算 + 情景模拟 |
| 5 | 输出生成 | 草稿生成 + 排版 |

---

## 📁 项目结构

```
porpoise-agent/
  （见上方架构图）
```

---

## 📜 版本历史

| 版本 | 日期 | 重要更新 |
|------|------|----------|
| **v2.2.0** | 2026-06-17 | 17 MCP 集成?8 技能，26 KB 文件?85/185 测试，跨项目进化 |
| v2.1.0 | 2026-06-12 | SSE 流式输出，StateGraph 条件路由，ChromaDB RAG |
| v2.0.0 | 2026-06-07 | 5层架构，7智能?MAS，BDI+ReAct+Reflexion 循环 |
| v1.0.0 | 2026-06-01 | 初始江豚智能体框?|

---

## 🪞 自我评估

### 优势
- **完整认知?*：BDI（信念建模）+ ReAct（推理循环）+ Reflexion（自我批判）——领域智能体中独树一?- **MAS 拓扑**? 智能体配 6 种拓扑类型，支持复杂研究工作?- **三角赋能**：通过 eon-core ?S 层继承知识、从 V 层继承验证能?- **全面测试**?85/185 测试通过?5 个缺陷修复——高可靠性基?- **优雅降级**：ChromaDB RAG 在向量数据库不可用时回退到关键词搜索

### 当前局?- 声学分析框架已搭建但核心方法为存根（需领域数据?- 生态智能体依赖外部 R 环境进行高级统计
- Neo4j 知识图谱集成可选且尚未填充数据
- 仅限单物种聚焦（仅长江江豚）

### 路线?- [ ] 完善声学分析流水线（NBHF 点击检测、哨声分类）
- [ ] 种群生存力分析（PVA）模?- [ ] 实时野外调查数据接入
- [ ] 多物种扩展框?
---

## 🔗 生态体?
本项目是「三生万物」生态的 **江豚领域专家（P₁）**?
```
三角核心 + 衍生架构（由 eon-core 协调）：

  S/V0  📦 fish-ecology-assistant    ?知识供给
  V/V1  🔍 cognitive-search-engine   ?搜索验证
  Coord ⚙ eon-core                  ?协调内核

  P?   🐬 porpoise-agent           ?江豚专家 ?本项?  P?   🐟 coilia-agent             ?刀鲚专?  P?   🐟 culter-agent             ?鲌类专家
  C     🔥 conflict-arbiter         ?冲突仲裁
```

> 🔥 和则无穷力量，分则顶尖专家引擎?
---

## 📋 README 更新日志

| 版本 | 日期 | 主题 | 更新内容 |
|------|------|------|----------|
| v8.0 | 2026-06-20 | README 恢复 | 从历史会话恢复，新增 DeepWiki 徽章、技?MCP 列表? 阶段流水线详情、README 更新日志 |
| v2.2.0 | 2026-06-17 | 生产发布 | 17 MCP 集成?8 技能，26 KB 文件?85/185 测试，跨项目进化 |
| v2.1.0 | 2026-06-12 | 流式?RAG | SSE 流式输出，StateGraph 条件路由，ChromaDB RAG |
| v2.0.0 | 2026-06-07 | 架构搭建 | 5层架构，7智能?MAS，BDI+ReAct+Reflexion 循环 |
| v1.0.0 | 2026-06-01 | 奠基 | 初始江豚智能体框?|

---

🌱 **万物皆变 · Panta Rhei**

> > > 我们说：知识会老去，但人类对世界的追问永不落幕。昨日之真理为今日之基石，今日之未知为明日之征途。我们的目光，从不囿于已知的疆界；我们的脚步，终将踏上那片星光璀璨的浩瀚征途。

这个项目不是一套固定的工具集——它是一?*活的系统**。每个组件都内置了过期机制、版本追踪和涌现感知。随着你的研究深入、R包更新、新方法涌现，它会和你一起进化?
*最后更新：2026-06-20　|　适用环境：Reasonix Code · DeepSeek 驱动*
