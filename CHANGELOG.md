# Changelog

## v2.2.0 — 2026-06-27

### 🧪 测试修复 + 依赖瘦身

- 🧪 **35 测试修复**: 全量 185/185 通过 (修复导入路径/API 签名/异步 fixture 等)
- 📦 **依赖瘦身 7 可选分组**: acoustics / spatial / knowledge / ml / all / dev / gpu
  - 核心依赖仅保留 14 个必需包, 可选依赖按需 `pip install -e ".[acoustics]"`
- 🧪 测试文件 7→8 (新增 `robustness_test.py` 7 层稳健性测试)

---

## v2.1.0 — 2026-06-16
- 项目结构标准化：补齐 docs/、scripts/
- CLI 入口 src/cli.py

## v2.0.0 — 2026-06-07
- 五层标准智能体分层架构
- 三重外部集成
