from dataclasses import dataclass

from .goal import AgentGoal
from .step import AgentStep


class EndOfPlan(Exception):
    """Raised when trying to move beyond the last step of the plan."""


@dataclass
class AgentPlan:
    goal: AgentGoal
    steps: list[AgentStep]
    current_step_index: int = 0

    @property
    def current_step(self):
        """
        The current step in this plan. That is, the step that is being / should be executed right now.
        """
        return self.steps[self.current_step_index]

    @property
    def next_step(self):
        """
        The next step in this plan. Is None if there is no next step.
        """
        if self.current_step_index >= len(self.steps) - 1:
            return None

        return self.steps[self.current_step_index + 1]

    def next(self, result: str | None = None):
        """
        Mark the current step as completed and proceed to the next step.
        """
        self.current_step.complete(result)

        if self.current_step_index >= len(self.steps) - 1:
            raise EndOfPlan

        self.current_step_index += 1

        return self.current_step

    def __str__(self):
        goal_str = str(self.goal)
        current_step_str = f"Current Step ({self.current_step_index + 1}): {self.current_step}"
        steps_str = "\n".join(
            [f"Step {idx + 1}: {step}" for idx, step in enumerate(self.steps)]
        )

        return (
            f"Goal:\n{goal_str}\n\n{current_step_str}\n\nSteps:\n{steps_str}"
        )

    def __repr__(self):
        return f"AgentPlan(goal={self.goal!r}, steps={self.steps!r}, current_step_index={self.current_step_index})"
