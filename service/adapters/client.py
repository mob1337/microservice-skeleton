"""
Module defining a setup client example using AbstractTestClient.
"""

from service.adapters.abstract_client import (
    AbstractClient,
)  # Import from same package together
from service.model.example_model import UserDetail  # Import from same package together


class SetupClientExample(AbstractClient):
    """
    Example client setup implementing AbstractTestClient.
    """

    def __init__(self, username: str, lastname: str):
        self.username = username
        self.lastname = lastname

    def greet_user(self) -> UserDetail:
        """
        Greet the user with provided username and lastname.
        """
        return UserDetail(first_name=self.username, last_name=self.lastname)
