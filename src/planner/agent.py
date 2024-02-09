import openai

from ..common.templates import PromptTemplates
from ..types.goal import AgentGoal


class Planner:
    def __init__(self, goal: AgentGoal):
        """
        Initialize the planner with an agent goal.
        """
        self.goal = goal

    def plan(self, model="gpt-4"):
        """
        Generate a plan for the agent goal.
        """
        completion = openai.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": PromptTemplates.generate_plan_system_prompt(),
                },
                {
                    "role": "user",
                    "content": PromptTemplates.generate_plan_prompt(self.goal),
                },
            ],
        )
