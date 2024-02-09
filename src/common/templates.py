from src.types.environment import ExecutionEnvironment
from src.types.misc import PlanFormat
from ..types.goal import AgentGoal
from ..types.plan import AgentPlan


class PromptTemplates:
    @classmethod
    def next_step_instructions(cls, plan: AgentPlan) -> str:
        """
        Get an instruction prompt for the next step.
        """
        return NEXT_STEP_INSTRUCTIONS.format(
            objective=plan.goal.objective,
            input_description=plan.goal.input_description,
            input=plan.goal.input,
            steps=plan.steps,
            next_step=plan.next_step,
        )

    @classmethod
    def generate_plan_prompt(cls, goal: AgentGoal) -> str:
        """
        Get an instruction prompt for the next step.
        """
        return NEXT_STEP_INSTRUCTIONS.format(
            objective=goal.objective,
            input_description=goal.input_description,
            input=goal.input,
        )

    @classmethod
    def generate_plan_system_prompt(
        cls, environment: ExecutionEnvironment, format: PlanFormat
    ) -> str:
        """
        Get an instruction prompt for the next step.
        """
        return GENERATE_PLAN_SYSTEM_PROMPT.format(
            environment=environment,
            format=format,
        )


NEXT_STEP_INSTRUCTIONS = """You are a step-by-step plan executor.

Goal :
{objective}

Input Description :
{input_description}}

Input :
{input}

Execution Status:
{steps}

Examine the above information. The next step to be executed is -
{next_step}
"""


GENERATE_PLAN_STEPS = """You are a step-by-step plan executor.

Goal :
{objective}

Input Description :
{input_description}}

Input :
{input}

Execution Status:
{steps}

Examine the above information. The next step to be executed is -
{next_step}
"""

GENERATE_PLAN_SYSTEM_PROMPT = """You are a step-by-step plan executor.

You generate step-by-step plans towards any given objective.

Here are the details about the environement you are executing in - 
{environment}

For any given goal, you need to generate a step-by-step plan in the following format :
{format}
"""
