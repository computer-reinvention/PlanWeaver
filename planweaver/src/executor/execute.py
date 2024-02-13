from collections.abc import Callable

from ..types.goal import AgentGoal

from .utils import dprint
from ..common.templates import PromptTemplates
from ..common.debug import dprint
from ..common.exceptions import EndOfPlan
from ..types.plan import AgentPlan
from ..types.environment import ExecutionEnvironment


def execute_plan(plan: AgentPlan, delegate: Callable):
    """
    Execute the given plan in a step-by-step manner using the given delegate.

    Args:
        plan (AgentPlan): The plan to execute.
        delegate (Callable): The delegate to use for executing the plan.
    Returns:
        result (dict): The result of the execution.
    """

    while not plan.finished:
        try:
            result = delegate(PromptTemplates.current_step_instructions(plan))
            plan.next(result)
        except EndOfPlan:
            dprint("EoP Reached.")
            break
