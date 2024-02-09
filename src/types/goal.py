from dataclasses import dataclass


@dataclass
class AgentGoal:
    objective: str
    input: str
    input_description: str
