import json

from .src.types.plan import AgentPlanFormat


def get_default_format():
    """
    Get the default AgentPlanFormat
    """

    FORMAT = (
        "```"
        + json.dumps(
            {
                "plan_overview": "A short overview of overall strategy.",
                "steps": [
                    "instructions for step 1",
                    "instructions for step 2",
                    "instructions for step 3",
                    "instructions for step 4",
                ],
            }
        )
        + "```"
    )

    FORMAT_EXAMPLE = (
        "```"
        + json.dumps(
            {
                "plan_overview": "I will first check if the 03:00 PM Thursday , February 28th is available. If it is, I shall create a meeting with person@example.com and person2@example.com.",
                "steps": [
                    "Use the check_if_free action to check if the 03:00 PM Thursday , February 28th is available.",
                    "Use the create_event action to create a meeting with person@example.com and person2@example.com.",
                    "Generate an email reply with confirmation.",
                ],
            }
        )
        + "```"
    )

    def plan_parser(plan):
        plan = plan.strip("\n").strip(" ")
        plan = plan.replace("```", "")
        plan = plan.replace("json", "")

        print("============")
        print(plan)
        print("============")

        plan = json.loads(plan)

        steps = plan.get("steps")

        if not steps:
            return None

        return steps

    format = AgentPlanFormat(
        instructions=f"""Create a series of steps required to achieve the goal according the format given below.\n

Here's the format which the plan should be generated in. It should always be in the following format.\n

{FORMAT}""",
        example=FORMAT_EXAMPLE,
        parser=plan_parser,
    )

    return format
