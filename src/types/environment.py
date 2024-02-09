from dataclasses import dataclass

from .actions import AgentAction


@dataclass
class ExecutionEnvironment:
    """
    The environment in which the plan is executed.
    This provides context for the plan formulation and highlights the possible actions that can be taken.
    Args:
        name (str): The name of the environment.
        description (str): A description of the environment.
        actions (list[AgentAction]): A list of actions that can be performed in the environment.
        constraints (list[str] | None, optional): A list of constraints specific to this environment. Defaults to None.
    """

    name: str
    description: str
    actions: list[AgentAction]
    constraints: list[str] | None = None

    def __repr__(self):
        """
        Returns an unambiguous string representation of the environment,
        which could be used to recreate the object.
        """
        return (
            f"ExecutionEnvironment(name={self.name!r}, description={self.description!r}, "
            f"actions={self.actions!r}, constraints={self.constraints!r})"
        )

    def __str__(self):
        """
        Returns a readable string representation of the environment,
        highlighting its name, description, and key attributes.
        """
        actions_str = "\n ".join(str(self.actions))
        constraints_str = (
            "\n -".join(self.constraints)
            if self.constraints
            else "No constraints"
        )
        return (
            f"ExecutionEnvironment: {self.name} - {self.description}\n\n"
            f"Actions available: {actions_str}\n\n"
            f"Constraints: {constraints_str}"
        )
