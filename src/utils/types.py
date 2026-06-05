# Porpoise Agent Core Types

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional


class AgentRole(str, Enum):
    LITERATURE = "literature"
    ACOUSTIC = "acoustic"
    ECOLOGY = "ecology"
    CONSERVATION = "conservation"
    GENETICS = "genetics"
    FIELD = "field"
    ORCHESTRATOR = "orchestrator"


class ResearchPhase(str, Enum):
    LITERATURE_REVIEW = "literature_review"
    DATA_ANALYSIS = "data_analysis"
    FIELD_SURVEY = "field_survey"
    CONSERVATION_ASSESSMENT = "conservation_assessment"
    REPORT_GENERATION = "report_generation"


class ClickType(str, Enum):
    REGULAR_CLICK = "regular_click"
    BUZZ = "buzz"
    BURST_PULSE = "burst_pulse"
    WHISTLE = "whistle"


@dataclass
class ClickEvent:
    timestamp: float
    peak_frequency: float
    center_frequency: float
    bandwidth_3db: float
    duration: float
    spl_peak: float
    click_type: ClickType = ClickType.REGULAR_CLICK


@dataclass
class ClickTrain:
    clicks: list = field(default_factory=list)
    start_time: float = 0.0
    end_time: float = 0.0
    mean_ici: float = 0.0
    buzz_ratio: float = 0.0
    n_clicks: int = 0


@dataclass
class AcousticFeatures:
    ici_mean: float = 0.0
    ici_std: float = 0.0
    duration: float = 0.0
    buzz_check: float = 0.0
    peak_freq: float = 0.0
    center_freq: float = 0.0
    bandwidth_3db: float = 0.0
    spl_mean: float = 0.0
    spl_std: float = 0.0
    av_splr: float = 0.0
    sd_pi: float = 0.0
    start_freq: float = 0.0
    end_freq: float = 0.0


@dataclass
class PorpoiseObservation:
    timestamp: datetime
    latitude: float
    longitude: float
    group_size: int = 1
    calves: int = 0
    behavior: str = ""
    detection_method: str = ""
    confidence: float = 1.0
    notes: str = ""


@dataclass
class ResearchContext:
    research_question: str
    phase: ResearchPhase = ResearchPhase.LITERATURE_REVIEW
    target_species: str = "Neophocaena asiaeorientalis asiaeorientalis"
    study_area: str = ""
    time_range: tuple = ("", "")
    constraints: list = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


@dataclass
class ReasoningTrace:
    subgoals: list = field(default_factory=list)
    hypotheses: list = field(default_factory=list)
    uncertainties: list = field(default_factory=list)
    rejected_paths: list = field(default_factory=list)
    raw_reasoning: str = ""
