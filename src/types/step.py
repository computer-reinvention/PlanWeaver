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
        dprint(f"Step completed: {self.step}, Result: {self.result}")

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        result_str = (
            f"Result: {self.result}"
            if self.result is not None
            else "No result yet."
        )
        debug_str = f"Step: {self.step}, Status: {status}, {result_str}"
        dprint(f"__str__ called: {debug_str}")

        return f"Step: {self.step}\nStatus: {status}\n{result_str}"

    def __repr__(self):
        repr_str = f"AgentStep(step={self.step!r}, completed={self.completed}, result={self.result!r})"
        dprint(f"__repr__ called: {repr_str}")

        return repr_str
