from dataclasses import dataclass


@dataclass
class AgentAction:
    """
    An action that can be performed in the environment.
    This is just a high level representation of the action to be used while creating the plan.
    The actual action is executed using Tools by the executor.
    The action will usually correspond to a Tool that can be used by the executor.

    Args:
        name (str): The name of the action.
        description (str): A description of the action.
    """

    name: str
    description: str

    def __repr__(self):
        """
        Returns an unambiguous string representation of the action,
        which could be used to recreate the object.
        """
        return f"AgentAction(name={self.name!r}, description={self.description!r})"

    def __str__(self):
        """
        Returns a readable string representation of the action,
        highlighting its name and description.
        """
        return f"Action: {self.name} - {self.description}"
