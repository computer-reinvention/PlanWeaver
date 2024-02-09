from dataclasses import dataclass
from typing import Callable

from .goal import AgentGoal
from .step import AgentStep
from ..common.debug import dprint
from ..common.exceptions import EndOfPlan


@dataclass
class AgentPlan:
    """
    A data class that represents the generated plan of execution.

    Args:
        goal (AgentGoal): The goal of the agent, containing the input and input description.
        steps (list[AgentStep]): The list of steps in the plan. Each step can contain the result and whether it has been completed.
        current_step_index (int, optional): The index of the current step in the plan. Defaults to 0.
    """

    goal: AgentGoal
    steps: list[AgentStep]
    current_step_index: int = 0

    @property
    def current_step(self):
        """
        The current step in this plan. That is, the step that is being / should be executed right now.
        """
        dprint(
            f"Accessing current_step property for Step {self.current_step_index + 1}"
        )
        return self.steps[self.current_step_index]

    @property
    def next_step(self):
        """
        The next step in this plan. Is None if there is no next step.
        """
        if self.current_step_index >= len(self.steps) - 1:
            dprint(
                "Accessing next_step property: No next step available. End of plan."
            )
            return None

        dprint(
            f"Accessing next_step property: Moving to next step: Step {self.current_step_index + 2}"
        )
        return self.steps[self.current_step_index + 1]

    def next(self, result: str | None = None):
        """
        Mark the current step as completed and proceed to the next step.
        """
        dprint(
            f"Executing next method: Completing current step: Step {self.current_step_index + 1} with result: {result}"
        )
        self.current_step.complete(result)

        if self.current_step_index >= len(self.steps) - 1:
            dprint(
                "Executing next method: End of plan reached. No more steps to proceed."
            )
            raise EndOfPlan

        self.current_step_index += 1
        dprint(
            f"Executing next method: Proceeding to next step: Step {self.current_step_index + 1}"
        )
        return self.current_step

    def __str__(self):
        goal_str = str(self.goal)
        current_step_str = f"Current Step ({self.current_step_index + 1}): {self.current_step}"
        steps_str = "\n".join(
            [f"Step {idx + 1}: {step}" for idx, step in enumerate(self.steps)]
        )

        plan_str = (
            f"Goal:\n{goal_str}\n\nSteps:\n{steps_str}\n\n{current_step_str}"
        )
        return plan_str

    def __repr__(self):
        repr_str = f"AgentPlan(goal={self.goal!r}, steps={self.steps!r}, current_step_index={self.current_step_index})"

        return repr_str


@dataclass
class AgentPlanFormat:
    """
    The formatting info required to generate and parse the plan of the plan.

    Args:
        instruction (str): The instruction prompt that tells the LLM how the generated plan should be formatted.
        example (str): An example of a generated plan showcasing ideal formatting.
        parser (Callable): A function that parses the generated plan into a list of steps (str).
    """

    instructions: str
    example: str
    parser: Callable

    def __repr__(self):
        return (
            f"PlanFormat(instruction={self.instructions!r}, "
            f"example={self.example!r}, "
            f"parser={self.parser.__name__!r})"
        )

    def __str__(self):
        return (
            f"Plan Format:\n"
            f"Instructions: {self.instructions}\n"
            f"Example: {self.example}\n"
        )
