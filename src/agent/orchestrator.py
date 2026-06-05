# Porpoise Agent Orchestrator
# Central coordinator for the five-phase research pipeline

import asyncio
import logging
from typing import Any, Optional

from src.utils.config import config
from src.utils.types import (
    AgentRole,
    ResearchContext,
    ResearchPhase,
    ReasoningTrace,
)
from src.utils.logging import audit

logger = logging.getLogger(__name__)


class Orchestrator:
    """
    Central orchestrator for the five-phase porpoise research pipeline.
    
    Responsibilities:
    1. Accept research questions and determine the current phase
    2. Select appropriate Agents and Skills
    3. Manage context passing and state machine
    4. Request human confirmation at key decision points
    5. Maintain complete audit logs
    """

    def __init__(self):
        self.phase_order = [
            ResearchPhase.LITERATURE_REVIEW,
            ResearchPhase.DATA_ANALYSIS,
            ResearchPhase.FIELD_SURVEY,
            ResearchPhase.CONSERVATION_ASSESSMENT,
            ResearchPhase.REPORT_GENERATION,
        ]
        self.current_phase: Optional[ResearchPhase] = None
        self.context: Optional[ResearchContext] = None
        self.reasoning_traces: list[ReasoningTrace] = []

    async def run(self, question: str) -> dict[str, Any]:
        """Main entry point: accept research question, return results"""
        logger.info(f"Orchestrator started: {question[:100]}...")
        audit.log("session_start", {"question": question})

        # Phase 0: Understand question and route to phase
        self.context = await self._understand_question(question)
        self.current_phase = self.context.phase

        logger.info(f"Routed to phase: {self.current_phase.value}")
        audit.log("phase_routed", {
            "question": question,
            "phase": self.current_phase.value,
        })

        # Execute current phase
        result = await self._execute_phase(self.current_phase)

        # Execute subsequent phases if needed
        phase_idx = self.phase_order.index(self.current_phase)
        for next_phase in self.phase_order[phase_idx + 1:]:
            if await self._should_continue(next_phase):
                self.current_phase = next_phase
                phase_result = await self._execute_phase(next_phase)
                result.update(phase_result)

        audit.log("session_end", {"status": "completed"})
        return result

    async def _understand_question(self, question: str) -> ResearchContext:
        """Phase 0: Understand question, determine research phase"""
        # Keyword-based routing (extensible to LLM classification)
        phase = ResearchPhase.LITERATURE_REVIEW  # default
        q_lower = question.lower()

        if any(kw in q_lower for kw in ["report", "manuscript"]):
            phase = ResearchPhase.REPORT_GENERATION
        elif any(kw in q_lower for kw in ["conservation", "assess", "threat"]):
            phase = ResearchPhase.CONSERVATION_ASSESSMENT
        elif any(kw in q_lower for kw in ["field", "survey", "transect"]):
            phase = ResearchPhase.FIELD_SURVEY
        elif any(kw in q_lower for kw in ["acoustic", "click", "pam", "pulse"]):
            phase = ResearchPhase.DATA_ANALYSIS

        return ResearchContext(
            research_question=question,
            phase=phase,
        )

    async def _execute_phase(self, phase: ResearchPhase) -> dict[str, Any]:
        """Execute specified research phase"""
        logger.info(f"Executing phase: {phase.value}")

        phase_handlers = {
            ResearchPhase.LITERATURE_REVIEW: self._run_literature_review,
            ResearchPhase.DATA_ANALYSIS: self._run_data_analysis,
            ResearchPhase.FIELD_SURVEY: self._run_field_survey,
            ResearchPhase.CONSERVATION_ASSESSMENT: self._run_conservation_assessment,
            ResearchPhase.REPORT_GENERATION: self._run_report_generation,
        }
        handler = phase_handlers.get(phase)
        if handler:
            return await handler()
        return {"error": f"Unknown phase: {phase}"}

    async def _run_literature_review(self) -> dict:
        audit.log("phase_start", {"phase": "literature_review"})
        return {"phase": "literature_review", "status": "pending_implementation"}

    async def _run_data_analysis(self) -> dict:
        audit.log("phase_start", {"phase": "data_analysis"})
        return {"phase": "data_analysis", "status": "pending_implementation"}

    async def _run_field_survey(self) -> dict:
        audit.log("phase_start", {"phase": "field_survey"})
        logger.warning("Field survey requires human approval!")
        return {
            "phase": "field_survey",
            "status": "requires_approval",
            "message": "Field survey plan requires human approval before execution",
        }

    async def _run_conservation_assessment(self) -> dict:
        audit.log("phase_start", {"phase": "conservation_assessment"})
        return {"phase": "conservation_assessment", "status": "pending_implementation"}

    async def _run_report_generation(self) -> dict:
        audit.log("phase_start", {"phase": "report_generation"})
        return {"phase": "report_generation", "status": "pending_implementation"}

    async def _should_continue(self, next_phase: ResearchPhase) -> bool:
        """Ask whether to continue to next phase"""
        # Simplified: always continue. Full version should ask user.
        return True
