"""
Module defining an abstract RabbitMQ message client.
"""

import abc
from aio_pika.abc import AbstractMessage


class AbstractMessageClient(abc.ABC):
    """
    Abstract base class defining a message client interface.
    """

    @abc.abstractmethod
    async def send_message(self, message: AbstractMessage, routing_key: str) -> None:
        """
        Abstract method to send a message.
        """
        raise NotImplementedError
