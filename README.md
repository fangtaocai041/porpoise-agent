# 🐬 Porpoise Agent — 江豚研究智能体

> 适配豚类（江豚为主）研究的 AI Agent 框架
> 基于 [Reasonix](https://github.com/esengine/reasonix) + DeepSeek
> 服务：无锡渔业学院/淡水渔业研究中心 刘凯研究员课题组

---

## 项目愿景

长江江豚 (*Neophocaena asiaeorientalis asiaeorientalis*) 是极度濒危的淡水鲸类，
仅存约1,000-1,200头。保护工作需要高效的数据分析、文献调研和决策支持。

**Porpoise Agent** 是一个 AI 研究助手，帮助江豚研究人员：
- 快速检索和分析全球豚类研究文献
- 自动化被动声学监测 (PAM) 数据处理
- 辅助野外调查规划和数据管理
- 生成研究报告和保护管理建议
- 构建和维护江豚研究知识图谱

---

## 快速开始

### 1. 环境要求
- Python 3.11+
- DeepSeek API Key ([获取](https://platform.deepseek.com))
- Node.js 18+ (Reasonix CLI)

### 2. 安装

```bash
git clone https://github.com/FFRC-LiuKai-Lab/porpoise-agent.git
cd porpoise-agent
pip install -e .
cp .env.example .env
# 编辑 .env 填入 DEEPSEEK_API_KEY
```

### 3. 运行

```bash
# 交互式对话
porpoise chat

# 文献调研
porpoise run "搜索2020年以来关于江豚被动声学监测的文献"

# 声学分析
porpoise run "分析 data/sample.wav 中的江豚 click 脉冲"

# 报告生成
porpoise run "生成2024年XX江段江豚监测报告"
```

---

## 项目结构

```
porpoise-agent/
├── docs/                    # 文档
│   ├── ARCHITECTURE.md      # 架构设计
│   ├── PROMPTS.md           # 提示词工程
│   ├── SKILLS.md            # 技能体系
│   └── WORKFLOWS.md         # 工作流设计
├── src/
│   ├── agent/               # Agent 核心引擎
│   │   ├── orchestrator.py  # 中央编排器
│   │   ├── loop.py          # CacheFirstLoop 适配
│   │   ├── tools.py         # 工具注册
│   │   └── memory.py        # 长期记忆
│   ├── agents/              # 专业子Agent
│   │   ├── literature_agent.py
│   │   ├── acoustic_agent.py
│   │   ├── ecology_agent.py
│   │   ├── conservation_agent.py
│   │   ├── genetics_agent.py
│   │   └── field_agent.py
│   ├── skills/              # 技能模块 (SKILL.md)
│   ├── tools/               # 领域工具
│   ├── knowledge/           # 领域知识库
│   ├── prompts/             # 提示词工程
│   └── utils/               # 工具函数
├── config/                  # 配置文件
├── data/                    # 数据目录
├── tests/                   # 测试
├── scripts/                 # 脚本
└── examples/                # 示例
```

---

## 核心特性

### 🧠 DeepSeek 深度优化
- **Cache-First Loop**: 利用 DeepSeek prefix-cache (70-95% 命中率)，大幅降低成本
- **R1 推理收割**: 自动解析 DeepSeek R1 推理链，生成结构化研究日志
- **Tool-Call Repair**: 自动修复 JSON 格式问题，保证工具调用鲁棒性

### 🔬 江豚研究专用
- **NBHF Click 检测**: 专为江豚 110-150 kHz 窄带高频脉冲设计
- **PAM 数据处理管道**: 支持 SoundTrap、A-tag、C-POD 等设备
- **行为推断**: Buzz 检测、觅食活动指数、昼夜节律分析
- **丰度估计**: Cue counting、Distance Sampling、SECR

### 🤖 多 Agent 协作
- **文献分析 Agent**: 自动搜索、筛选、分析全球豚类论文
- **声学分析 Agent**: 端到端 PAM 数据处理
- **生态分析 Agent**: 栖息地建模、分布预测
- **保护评估 Agent**: IUCN 标准评估、保护优先级
- **野外调查 Agent**: 路线规划、样线优化

### 📊 知识驱动
- **知识图谱**: Neo4j 驱动的江豚研究知识网络
- **向量检索**: ChromaDB 语义搜索文献和数据
- **物种档案**: 结构化江豚及近缘物种知识库

---

## 对标项目

本项目设计和架构受以下优秀项目启发：

| 项目 | 借鉴点 |
|------|--------|
| [Reasonix](https://github.com/esengine/reasonix) | DeepSeek 原生 Agent Loop |
| [Ecology-Harness](https://github.com/ECNU-ICALK/Ecology-Harness) | 生态学 Agent 编排 |
| [AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) | 研究流水线设计 |
| [ecological-agent-skills](https://github.com/baratadiego/ecological-agent-skills) | 技能模块化 |
| [CetusID](https://github.com/Gui-Frainer/CetusID) | 鲸类声学分类 |
| [which.dolphin](https://github.com/tristankleyn/which.dolphin) | 海豚声学识别 |
| [SciToolAgent](https://github.com/hicai-zju/scitoolagent) | 科学工具知识图谱 |

---

## 课题组信息

- **单位**: 无锡渔业学院 / 淡水渔业研究中心 (FFRC)
- **课题组**: 刘凯研究员课题组
- **研究方向**: 长江江豚保护生物学、被动声学监测、栖息地评估

---

## 许可证

MIT License © 2025 无锡渔业学院/淡水渔业研究中心 刘凯研究员课题组