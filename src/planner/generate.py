import openai


from ..common.debug import dprint
from ..common.templates import PromptTemplates
from ..types.goal import AgentGoal
from ..types.environment import ExecutionEnvironment
from ..types.plan import AgentPlan, AgentPlanFormat
from ..types.step import AgentStep


def generate_plan(
    goal: AgentGoal,
    environment: ExecutionEnvironment,
    format: AgentPlanFormat,
    model="gpt-4-1106-preview",
    temperature=0.7,
    top_p=1,
    max_tokens=4000,
    n_completions=1,
):
    """
    Generate a plan for the agent goal.

    Args:
        goal (AgentGoal): The current goal of the agent.
        environment (ExecutionEnvironment): Information about the execution environment that includes the possible actions that can be taken and constraints, if any.
        format (AgentPlanFormat): Container for information about how to format and parse the plan.
        model (str, optional): The model to use for generating plans. Defaults to "gpt-4-1106-preview".
    """
    dprint(
        f"Initializing plan generation with\n"
        f"Goal: {goal}\n"
        f"Environment: {environment}"
    )

    system_prompt = PromptTemplates.generate_plan_system_prompt(
        environment=environment,
        format=format,
    )
    user_prompt = PromptTemplates.generate_plan_prompt(goal)

    dprint(f"System prompt: {system_prompt}")
    dprint(f"User prompt: {user_prompt}")

    completion = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=n_completions,
    )

    dprint(f"Completion received. Processing steps...")

    steps = [
        AgentStep(step)
        for step in format.parser(completion.choices[0].message.content)
    ]

    dprint(f"Generated steps: {steps}")
    dprint(f"Plan generation completed.")

    return AgentPlan(goal=goal, steps=steps)
