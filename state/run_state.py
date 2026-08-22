from dataclasses import dataclass, field


@dataclass
class RunState:
    phase: str = "routine"
    artifacts: dict = field(default_factory=dict)
