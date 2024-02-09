from dataclasses import dataclass

from ..common.debug import dprint


@dataclass
class AgentStep:
    step: str
    completed: bool = False
    result: str | None = None

    def complete(self, result: str | None = None):
        dprint(f"Marking as complete: {self.step}")
        self.result = result
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        result_str = (
            f"Result: {self.result}"
            if self.result is not None
            else "No result yet."
        )

        return f"Step: {self.step}\nStatus: {status}\n{result_str}"

    def __repr__(self):
        return f"AgentStep(step={self.step!r}, completed={self.completed}, result={self.result!r})"
