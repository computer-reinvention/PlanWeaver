from dataclasses import dataclass


@dataclass
class AgentGoal:
    objective: str
    input: str
    input_description: str

    def __str__(self):
        return f"Objective: {self.objective}\nInput: {self.input}\nDescription: {self.input_description}"

    def __repr__(self):
        return f"AgentGoal(objective={self.objective!r}, input={self.input!r}, input_description={self.input_description!r})"
