"""
Example model defining UserDetail class schema.
"""

from pydantic import BaseModel


class UserDetail(BaseModel):
    """
    UserDetail model schema.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    first_name: str
    last_name: str
