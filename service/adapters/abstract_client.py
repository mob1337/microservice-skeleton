"""
Module defining an abstract client interface.
"""

import abc
from fastapi.responses import JSONResponse


class AbstractClient(abc.ABC):
    """
    Abstract base class for defining a interface.
    """

    @abc.abstractmethod
    def greet_user(self) -> JSONResponse:
        """
        Abstract method to greet the user.
        """
        raise NotImplementedError
