from dataclasses import dataclass


@dataclass
class AgentGoal:
    objective: str
    input: str
    input_description: str

    def __str__(self):
        return f"Objective:\n{self.objective}\n\nInputs:\n{self.input}\n\nInput Description:\n{self.input_description}"
