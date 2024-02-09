from collections.abc import Callable

from .utils import dprint
from ..common.templates import PromptTemplates
from ..common.debug import dprint
from ..types.plan import AgentPlan
from ..types.environment import ExecutionEnvironment


class PlanExecutor:
    def __init__(
        self,
        func: Callable,
        plan: AgentPlan,
        environment: ExecutionEnvironment,
    ):
        """
        Initialize the executor with a function and a plan.
        The function should be a callable that takes a string as input and returns a string as output.
        It has to be a function capable of executing each step just by an input prompt.

        Args:
            func (Callable): The function to execute the plan.
            plan (AgentPlan): The plan to execute.
        """
        self.func = func
        self.plan = plan
        self.environment = environment

    def run(self):
        """
        Execute the plan in a step-by-step manner.
        """
        for i, step in enumerate(self.plan.steps):
            result = self.func(
                PromptTemplates.next_step_instructions(self.plan)
            )

            self.plan.next(result)
