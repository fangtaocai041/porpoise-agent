<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║   🐬  PORPOISE AGENT  ·  P₁ 江豚专研  ·  v2.2.0              ║
║  ─────────────────────────────────────────────────────────  ║
║    NBHF 声学监测 · 栖息地建模 · 种群生存力分析                   ║
║      长江江豚 · Neophocaena asiaeorientalis                    ║
╚══════════════════════════════════════════════════════════════╝
```

<p align="center">
  🇬🇧 <a href="README.md">English</a>  ·  🇨🇳 <a href="README.zh.md">中文</a>
</p>

[![Python 3.11+](https://img.shields.io/badge/Python%203.11%2B-3776AB?style=flat-square)]()
[![v2.2.0](https://img.shields.io/badge/v2.2.0-8A4FCE?style=flat-square)]()
[![17 MCP](https://img.shields.io/badge/17%20MCP-007EC6?style=flat-square)]()
[![18 skills](https://img.shields.io/badge/18%20skills-FE7D37?style=flat-square)]()
[![185 tests](https://img.shields.io/badge/185%2F185%20tests-0EA5E9?style=flat-square)]()
[![BDI+ReAct](https://img.shields.io/badge/BDI%2BReAct-EC4899?style=flat-square)]()

<p align="center">
  <a href="https://github.com/fangtaocai041/porpoise-agent/stargazers"><img src="https://img.shields.io/github/stars/fangtaocai041/porpoise-agent?style=social" alt="Stars"></a>
  <a href="https://github.com/fangtaocai041/porpoise-agent/network/members"><img src="https://img.shields.io/github/forks/fangtaocai041/porpoise-agent?style=social" alt="Forks"></a>
</p>

<div align="center"><h3>🌊 万物皆流。</h3></div>

</div>

---

## 📑 目录

- [🧠 核心哲学](#-核心哲学)
- [🧩 项目定位](#-项目定位)
- [🔺 三角核心 + 衍生角色](#-三角核心--衍生角色)
- [🚀 快速开始](#-快速开始)
- [🏗️ 五层内部架构](#-五层内部架构)
- [✨ 核心特性](#-核心特性)
- [📜 版本历史](#-版本历史)
- [🪞 自我评价](#-自我评价)

---

## 🧠 核心哲学

> 🌍 世界是动态的，📖 知识是暂时的，🌟 涌现是常态。

### 📜 三大信条

**🌍 世界是动态的** — 江豚种群在变，栖息地在变，威胁因素在变。今天的数据不能代表明天。每一次监测都要带时间戳，动态更新。

**📖 知识是暂时的** — 声学检测阈值需要随环境噪声重新校准。分布模型需要随水文数据更新。没有一劳永逸的结论。

**🌟 涌现是常态** — 当多个监测站点独立报告异常时，那不是噪声，那是涌现信号。系统自动触发跨站点交叉验证。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🧩 项目定位

**Porpoise Agent** 是三生万物生态体系中 P₁ 衍生项目。作为江豚领域的专属智能体，它从 S/V0（fish-ecology-assistant）继承知识供给，从 V/V1（cognitive-search-engine）继承搜索验证，从 Coord（eon-core）继承协调能力。

集成 **17 MCP 工具**、**18 领域技能**、**26 知识库文件**、185 测试全覆盖（100% 通过率）。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🔺 三角核心 + 衍生角色

| 项目 | 层级 | 角色 |
|------|:----:|------|
| fish-ecology-assistant | 三角 S/V0 | 知识供给 |
| cognitive-search-engine | 三角 V/V1 | 搜索验证 |
| eon-core | Coord | 协调中枢 |
| **porpoise-agent** | **衍生 P₁** | **江豚专研** |
| coilia-agent | 衍生 P₂ | 刀鲚专研 |
| culter-agent | 衍生 P₃ | 鲌类专研 |
| conflict-arbiter | 衍生 C | 冲突仲裁 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🚀 快速开始

```bash
git clone https://github.com/fangtaocai041/porpoise-agent.git
cd porpoise-agent
pip install -e .
python src/agent/orchestrator.py
```

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🏗️ 五层内部架构

| 层 | 功能 | 模块 |
|:--|------|------|
| **1. 感知** | NBHF 声学检测（100-180kHz），被动声学监测 | `src/acoustics/` |
| **2. 认知** | BDI + ReAct 循环，意图形成 | `src/agent/` |
| **3. 记忆** | 短期 + 长期 + 跨项目共享 | `src/memory/` |
| **4. 推理** | 栖息地建模，种群评估，威胁矩阵 | `src/models/` |
| **5. 执行** | SSE 流式输出，报告生成 | `src/output/` |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## ✨ 核心特性

<details open><summary><b>📋 特性列表</b></summary>

| 特性 | 状态 | 说明 |
|------|:----:|------|
| 🎧 NBHF 声学 | ✅ | 100-180kHz 窄带高频信号检测 |
| 🗺️ 栖息地建模 | ✅ | 长江中下游分布模型 |
| 📊 种群评估 | ✅ | 线样法 + 被动声学双模态 |
| ⚠️ 威胁矩阵 | ✅ | 航运、污染、渔业、水利四维评估 |
| 📡 SSE 流 | ✅ | Server-Sent Events 实时输出 |
| 🧪 测试 | ✅ | 185/185 全通过 |

</details>

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 📜 版本历史

| 版本 | 日期 | 主题 |
|------|------|------|
| **v2.2.0** | 2026-06-18 | 五层架构 + 26 KB 文件 + 185 测试 |
| **v2.1.0** | 2026-06-12 | SSE 流式 + 跨项目验证 |
| **v2.0.0** | 2026-06-07 | 三角核心集成 + 衍生架构 |
| **v1.0.0** | 2026-06-05 | 初始发布 · 江豚声学检测 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🪞 自我评价

**优势**：185/185 测试全覆盖；NBHF 声学模块唯一开源实现；与 eon-core 松耦合，项目可独立运行。

**局限**：依赖长江水文数据更新（非实时）；声学模型需现场校准。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

> **"不要搜索字符串，要重建所指。"**
> Don't search for strings — reconstruct the signified.

---

## 🌱 万物皆变 · Panta Rhei

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 我们说：知识会老去，但人类对世界的追问永不落幕。昨日之真理为今日之基石，今日之未知为明日之征途。我们的目光，从不囿于已知的疆界；我们的脚步，终将踏上那片星光璀璨的浩瀚征途。

这个项目不是一套固定的工具集——它是一个**活的系统**。


> 🔧 Agent 约束: [AGENTS.md](../AGENTS.md) · [core-constitution.md](../.reasonix/core-constitution.md) · [research-first](../skills/research-first.md) · [retro-session](../skills/retro-session.md)

*最后更新: 2026-06-18 | Reasonix Code · DeepSeek 驱动*

---

<div align="center">

### 🏷️ 技术标签

`江豚` `NBHF声学` `栖息地建模` `种群生存力` `BDI智能体` `ReAct循环` `多智能体` `ChromaDB` `SSE流式` `状态图` `长江` `保护生物学` `Reasonix` `MCP`

<br>

<sub>🐬 属于 **三生万物** 生态体系 · P₁ 衍生专研 · 由 [eon-core](https://github.com/fangtaocai041/eon-core) 统一协调</sub>

</div>
