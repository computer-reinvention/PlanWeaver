from dataclasses import dataclass


@dataclass
class AgentStep:
    step: str
    completed: bool = False
    result: str | None = None

    def complete(self, result: str | None = None):
        self.result = result
        self.completed = True
