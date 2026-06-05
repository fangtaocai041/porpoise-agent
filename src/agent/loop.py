# Cache-First Loop - Reasonix Adaptation Layer
# Agent loop optimized for DeepSeek prefix-cache

import logging
import re
from typing import Any, Callable, Optional

from src.utils.config import config
from src.prompts.system_prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class PorpoiseLoop:
    """
    Cache-First Loop for porpoise research.

    Core strategies (inspired by Reasonix):
    1. ImmutablePrefix: Domain knowledge + tool specs as immutable prefix
       -> DeepSeek prefix-cache auto-hits 70-95% of requests
    2. Append-Only Log: Each turn appended to log end
       -> Never modify existing content, keep cache valid
    3. R1 Thought Harvesting: Parse reasoning_content
       -> Structured reasoning traces become research logs
    4. Tool-Call Repair: Auto-fix JSON format issues
       -> Scavenge leaked tool calls + repair truncated JSON

    Reasonix library usage:
    from reasonix import CacheFirstLoop, ImmutablePrefix, DeepSeekClient, ToolRegistry
    """

    def __init__(self, model: str = "deepseek-chat"):
        self.model = model
        self.tools: dict[str, Callable] = {}
        self.conversation_log: list[dict] = []
        self.reasoning_traces: list[dict] = []

        # Build immutable prefix
        self.immutable_prefix = self._build_prefix()

        logger.info(f"PorpoiseLoop initialized with model={model}")

    def _build_prefix(self) -> str:
        """Build ImmutablePrefix"""
        return SYSTEM_PROMPT + "\n\n" + self._format_tool_specs()

    def _format_tool_specs(self) -> str:
        """Format tool specs (flattened for DeepSeek compatibility)"""
        if not self.tools:
            return "# Available Tools\n- No tools registered yet"
        specs = ["# Available Tools"]
        for name, fn in self.tools.items():
            doc = fn.__doc__ or "No description"
            specs.append(f"- {name}: {doc}")
        return "\n".join(specs)

    def register_tool(self, name: str, fn: Callable):
        """Register a callable tool"""
        self.tools[name] = fn
        logger.debug(f"Tool registered: {name}")

    async def run(self, user_input: str) -> dict[str, Any]:
        """Execute one conversation turn"""
        logger.info(f"Loop run: {user_input[:100]}...")

        # 1. Append user message to log
        self.conversation_log.append({"role": "user", "content": user_input})

        # 2. Call DeepSeek API
        response = await self._call_model()

        # 3. Append assistant response
        self.conversation_log.append({"role": "assistant", "content": response})

        # 4. Harvest reasoning if enabled
        if config.reasonix.get("harvest_enabled", True):
            trace = self._harvest_reasoning(response)
            if trace:
                self.reasoning_traces.append(trace)

        return {"response": response, "model": self.model}

    async def _call_model(self) -> str:
        """Call DeepSeek API via OpenAI-compatible interface"""
        try:
            from openai import AsyncOpenAI
            client = AsyncOpenAI(
                api_key=config.deepseek_api_key,
                base_url=config.deepseek_base_url,
            )
            messages = [{"role": "system", "content": self.immutable_prefix}]
            messages.extend(self.conversation_log)

            response = await client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=4096,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            logger.error(f"Model call failed: {e}")
            return f"[Error calling model: {e}]"

    def _harvest_reasoning(self, response: str) -> Optional[dict]:
        """Harvest R1 reasoning trace (Python implementation of Reasonix harvest)"""
        reasoning_match = re.search(
            r"<reasoning>(.*?)</reasoning>", response, re.DOTALL
        )
        if not reasoning_match:
            return None

        reasoning_text = reasoning_match.group(1).strip()

        trace = {
            "raw": reasoning_text,
            "subgoals": [],
            "hypotheses": [],
            "uncertainties": [],
            "rejected_paths": [],
        }

        # Heuristic parsing (full version uses Reasonix harvest)
        for line in reasoning_text.split("\n"):
            line = line.strip()
            lower = line.lower()
            if "subgoal" in lower or "step" in lower:
                trace["subgoals"].append(line)
            elif "hypothesis" in lower or "might" in lower:
                trace["hypotheses"].append(line)
            elif "uncertain" in lower or "unclear" in lower:
                trace["uncertainties"].append(line)
            elif "reject" in lower or "alternative" in lower:
                trace["rejected_paths"].append(line)

        return trace
