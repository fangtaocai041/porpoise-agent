"""
认知与决策层 (Cognitive & Decision Layer)

⚠️ v8.0: Canonical source → eon-core/src/shared/cognitive/
This module now re-exports from the shared cognitive engine.
Local copies retained for backward compatibility only.

组件:
- BDI: Belief-Desire-Intention 状态机
- ReActLoop: Reasoning and Acting 闭环反馈系统
- Decomposer: 任务分解 (CoT / ToT / GoT)
- Reflexion: 自我反思 Critic + 信用分配
- Search: 思维树/图搜索 (BFS/DFS/Beam/MCTS)
"""

import sys as _sys
from pathlib import Path as _Path

# Try shared cognitive engine first
_SHARED = str(
    _Path(__file__).resolve().parent.parent.parent.parent
    / "eon-core" / "src" / "shared"
)
if _SHARED not in _sys.path:
    _sys.path.insert(0, _SHARED)

# Import from shared (fallback to local if unavailable)
try:
    from cognitive import (  # noqa: E402
        BDICoordinator, BDIStatus, Belief, Desire, Intention, PlanStep, StepStatus,
        ReActLoop, ReActContext, ReActStep, LoopStatus,
        TaskDecomposer, DecompositionPlan, DecompositionStrategy,
        Critic, CreditAssigner, FeedbackLoop, Reflection, ReflectionType, Severity, CreditNode,
        ThoughtTreeSearch, GraphThoughtSearch, ThoughtNode, GraphThoughtNode,
        SearchConfig, SearchStrategy, SearchResult,
    )
except ImportError:
    from src.cognitive.bdi import (  # noqa: E402
        BDICoordinator, BDIStatus, Belief, Desire, Intention, PlanStep, StepStatus,
    )
    from src.cognitive.react_loop import (  # noqa: E402
        ReActLoop, ReActContext, ReActStep, LoopStatus,
    )
    from src.cognitive.decomposer import (  # noqa: E402
        TaskDecomposer, DecompositionPlan, DecompositionStrategy,
    )
    from src.cognitive.reflexion import (  # noqa: E402
        Critic, CreditAssigner, FeedbackLoop, Reflection, ReflectionType, Severity, CreditNode,
    )
    from src.cognitive.search import (  # noqa: E402
        ThoughtTreeSearch, GraphThoughtSearch, ThoughtNode, GraphThoughtNode,
        SearchConfig, SearchStrategy, SearchResult,
    )

__all__ = [
    "BDICoordinator", "BDIStatus", "Belief", "Desire", "Intention", "PlanStep", "StepStatus",
    "ReActLoop", "ReActContext", "ReActStep", "LoopStatus",
    "TaskDecomposer", "DecompositionPlan", "DecompositionStrategy",
    "Critic", "CreditAssigner", "FeedbackLoop", "Reflection", "ReflectionType", "Severity", "CreditNode",
    "ThoughtTreeSearch", "GraphThoughtSearch", "ThoughtNode", "GraphThoughtNode",
    "SearchConfig", "SearchStrategy", "SearchResult",
]
