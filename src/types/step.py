from dataclasses import dataclass


@dataclass
class AgentStep:
    step: str
    completed: bool = False
    result: str | None = None
