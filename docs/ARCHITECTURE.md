# 🏗️ Porpoise Agent 架构设计

> 每一层抽象都由江豚研究的具体需求和 DeepSeek 的特性驱动。

## 1. 设计哲学

### 三条铁律

| # | 原则 | 说明 |
|---|------|------|
| I | DeepSeek 原生 | 深度利用 prefix-cache、R1 推理链、廉价 token |
| II | 领域可解释 | 每一步推理留有可审计的痕迹 |
| III | 人机协作 | Agent 是副驾驶，关键决策保留人工审批 |

### 对标项目借鉴

| 借鉴来源 | 借鉴内容 | 适配方式 |
|-----------|----------|----------|
| Reasonix (esengine) | Cache-First Loop, R1 Harvesting | 直接复用核心 Loop |
| Ecology-Harness (ECNU) | Skill Hub, MCP 编排 | 适配为江豚 Skill Pack |
| AgentLaboratory | 三阶段流水线 | 扩展为五阶段 |
| ecological-agent-skills | SKILL.md 格式 | 豚类专用 Skills |
| CetusID / which.dolphin | CNN 声学分类 | 集成 NBHF click 检测 |
| SciToolAgent (ZJU) | 工具知识图谱 | 江豚研究工具 KG |

## 2. 总体架构

三层架构：用户界面层 → Orchestrator (CacheFirstLoop + ToolCallRepair) → 专业Agent层/Skill Hub层/工具知识层

## 3. 五阶段研究流水线

Phase 1 文献调研 → Phase 2 数据分析 → Phase 3 野外调查 → Phase 4 保护评估 → Phase 5 成果产出

| 阶段 | AI 自主 | 需人工确认 |
|------|---------|-------------|
| 文献调研 | 搜索、摘要、分类 | 纳入标准、方向校准 |
| 数据分析 | 信号处理、特征提取 | 模型选择、异常值 |
| 野外调查 | 路线生成、配置建议 | 方案审批、安全决策 |
| 保护评估 | 指标计算、情景模拟 | 管理建议审核 |
| 成果产出 | 草稿生成、排版 | 内容审核、学术判断 |

## 4. Reasonix 适配

CacheFirstLoop + ImmutablePrefix → 最大化 DeepSeek prefix-cache 命中率 (70-95%)
R1 Thought Harvesting → 结构化推理追踪 (subgoals/hypotheses/uncertainties)
ToolCallRepair → 自动修复 DeepSeek 的 JSON 格式问题

## 5. 数据流

原始声学数据 → PAM预处理 (带通滤波100-180kHz/脉冲检测/Click Train提取/特征工程) → 分析Agent (物种识别/行为分类/丰度估计) → 知识图谱 → 报告生成

## 6. MCP 集成

| MCP 服务器 | 用途 |
|------------|------|
| Scholar MCP | 文献搜索与全文 |
| Article MCP | PMC 全文 + 期刊评估 |
| Filesystem MCP | 数据管理 |
| Memory MCP | 知识图谱持久化 |
| Echarts MCP | 可视化 |

## 7. 关键设计决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 语言 | Python 3.11+ | 生态/声学工具链 |
| Agent框架 | Reasonix + Python bridge | DeepSeek优化 + 领域计算 |
| 模型 | DeepSeek V3+R1 | 廉价token + cache + 中文 |
| 知识图谱 | Neo4j + ChromaDB | 结构关系 + 语义检索 |
| 声学分析 | librosa + obspy | 成熟生态 |
| 技能格式 | SKILL.md | 可读、版本可控 |

## 8. 安全与治理

- 沙箱执行：代码隔离运行
- 数据脱敏：GPS 自动模糊化
- 审计日志：JSONL 决策记录
- 人工关卡：野外方案须审批
- 引用验证：自动验证文献存在性