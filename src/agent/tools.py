# Tool Registry - Manages all callable tools for agents

import logging
from typing import Any, Callable

logger = logging.getLogger(__name__)


class ToolRegistry:
    """Tool registry - Similar to Reasonix ToolRegistry"""

    def __init__(self):
        self._tools: dict[str, dict] = {}

    def register(
        self,
        name: str,
        description: str,
        parameters: dict,
        fn: Callable,
        requires_approval: bool = False,
    ):
        """Register a tool"""
        self._tools[name] = {
            "name": name,
            "description": description,
            "parameters": parameters,
            "fn": fn,
            "requires_approval": requires_approval,
        }
        logger.info(f"Tool registered: {name}")

    def get_specs(self) -> list[dict]:
        """Get tool specs for LLM tool choice"""
        return [
            {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["parameters"],
            }
            for t in self._tools.values()
        ]

    def call(self, name: str, **kwargs) -> Any:
        """Call a registered tool"""
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")

        tool = self._tools[name]
        logger.info(f"Tool called: {name}({kwargs})")

        try:
            result = tool["fn"](**kwargs)
            return result
        except Exception as e:
            logger.error(f"Tool {name} failed: {e}")
            raise


# Global tool registry
tools = ToolRegistry()


# ---- Built-in Tools ----

def search_literature(
    query: str, source: str = "semantic_scholar", limit: int = 10
) -> dict:
    """Search scientific literature about cetaceans and porpoises"""
    # Actual implementation calls Scholar MCP
    return {
        "query": query, "source": source, "limit": limit,
        "results": [], "status": "not_implemented"
    }


def load_acoustic_file(path: str) -> dict:
    """Load an acoustic recording (.wav/.flac) and return metadata"""
    # Actual implementation uses librosa/soundfile
    return {"path": path, "status": "not_implemented"}


def detect_clicks(
    audio_path: str, threshold_db: float = -134.0
) -> dict:
    """Detect NBHF clicks using SPL threshold (100-180 kHz band)"""
    return {
        "audio_path": audio_path,
        "threshold_db": threshold_db,
        "status": "not_implemented"
    }


def estimate_abundance(
    detections: list, method: str = "cue_counting"
) -> dict:
    """Estimate porpoise abundance from detection data"""
    return {
        "n_detections": len(detections),
        "method": method,
        "status": "not_implemented"
    }


def query_species_profile(species: str) -> dict:
    """Query structured species profile from knowledge base"""
    return {"species": species, "status": "not_implemented"}


def geocode_location(place_name: str) -> dict:
    """Geocode a location name to coordinates along Yangtze River"""
    return {"place_name": place_name, "status": "not_implemented"}


# Register tools
tools.register(
    "search_literature",
    "Search scientific literature about cetaceans and porpoises",
    {
        "query": {"type": "string", "description": "Search query"},
        "source": {"type": "string", "description": "Data source"},
        "limit": {"type": "integer", "description": "Max results"},
    },
    search_literature,
)

tools.register(
    "load_acoustic_file",
    "Load acoustic recording and return metadata (sr, duration, channels)",
    {"path": {"type": "string", "description": "File path"}},
    load_acoustic_file,
)

tools.register(
    "detect_clicks",
    "Detect NBHF clicks using SPL threshold (100-180 kHz bandpass)",
    {
        "audio_path": {"type": "string"},
        "threshold_db": {"type": "number"},
    },
    detect_clicks,
)

tools.register(
    "estimate_abundance",
    "Estimate porpoise abundance using cue counting or distance sampling",
    {
        "detections": {"type": "array"},
        "method": {"type": "string"},
    },
    estimate_abundance,
)

tools.register(
    "query_species_profile",
    "Query structured species profile from knowledge base",
    {"species": {"type": "string"}},
    query_species_profile,
)

tools.register(
    "geocode_location",
    "Geocode a location name to coordinates (Yangtze River focus)",
    {"place_name": {"type": "string"}},
    geocode_location,
)
