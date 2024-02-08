from dataclasses import dataclass

from .goal import AgentGoal
from .step import AgentStep


@dataclass
class AgentPlan:
    goal: AgentGoal
    step: list[AgentStep]
