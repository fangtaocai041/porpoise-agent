"""
Porpoise Agent v2.0 — 江豚研究智能体
─────────────────────────────────────
基于五层标准智能体分层架构模型:
  1. Interaction  — 交互与感知层
  2. Cognitive    — 认知与决策层 (BDI + ReAct)
  3. Memory       — 记忆系统层 (STM + LTM)
  4. Mapping      — 逻辑映射与转换层
  5. Execution    — 工具与执行层

服务: 无锡渔业学院/淡水渔业研究中心 刘凯研究员课题组
"""

import sys as _sys
from pathlib import Path as _Path
_PROJECT_ROOT = str(_Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in _sys.path:
    _sys.path.insert(0, _PROJECT_ROOT)

def _load_version():
    """Read version from VERSION.yaml — single source of truth."""
    try:
        import yaml
        _vpath = _Path(__file__).resolve().parent.parent.parent / "VERSION.yaml"
        with open(_vpath, encoding="utf-8") as _f:
            _data = yaml.safe_load(_f)
        _key = _Path(__file__).resolve().parent.parent.name
        return _data.get("projects", {}).get(_key, {}).get("version", "0.0.0")
    except Exception:
        return "0.0.0"

__version__ = _load_version()
__architecture__ = "five_layer_cybernetic"
