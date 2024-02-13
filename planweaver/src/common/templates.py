from ..types.environment import ExecutionEnvironment
from ..types.plan import AgentPlanFormat
from ..types.goal import AgentGoal
from ..types.plan import AgentPlan


class PromptTemplates:
    @classmethod
    def current_step_instructions(cls, plan: AgentPlan) -> str:
        """
        Get an instruction prompt for the next step.
        """

        completed_steps = "Progress so far in the plan - "

        for step in plan.steps:
            if step.completed:
                completed_steps += "\n\n" + str(step)

        current_step = plan.current_step

        if len(completed_steps) > 0:
            return CURRENT_STEP_INSTRUCTIONS.format(
                # goal=plan.goal,
                steps=completed_steps,
                current_step=current_step,
            )
        else:
            return CURRENT_STEP_INSTRUCTIONS.format(
                # goal=plan.goal,
                steps="This is the first step.",
                current_step=current_step,
            )

    @classmethod
    def generate_plan_prompt(cls, goal: AgentGoal) -> str:
        """
        Get an instruction prompt for the next step.
        """
        return GENERATE_PLAN_STEPS.format(goal=goal)

    @classmethod
    def generate_plan_system_prompt(
        cls, environment: ExecutionEnvironment, format: AgentPlanFormat
    ) -> str:
        """
        Get an instruction prompt for the next step.
        """
        return GENERATE_PLAN_SYSTEM_PROMPT.format(
            environment=environment,
            format=format,
        )


CURRENT_STEP_INSTRUCTIONS = """You are the executor component of a Planner-Executor agent. 

{steps}

Complete the current step -
{current_step}

Remember, ONLY complete the current step and return ONLY the required information.
"""


GENERATE_PLAN_STEPS = """Generate a well-formatted step-by-step plan to achieve the following objective.

{goal}

"""

GENERATE_PLAN_SYSTEM_PROMPT = """You are a step-by-step plan executor.

You generate step-by-step plans towards any given objective.

Here are the details about the environement you are executing in - 
{environment}

For any given goal, you need to generate a step-by-step plan in the following format :
{format}"""
