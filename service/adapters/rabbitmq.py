"""
Module defining a RabbitMQ client implementation.
"""

from aio_pika.abc import AbstractChannel, AbstractMessage, AbstractExchange
from service.adapters.abstract_rabbitmq import AbstractMessageClient


class RabbitMQClient(AbstractMessageClient):
    """
    Implementation of RabbitMQ client using aio-pika.
    """

    def __init__(
        self, channel: AbstractChannel = None, exchange: AbstractExchange = None
    ):
        self.channel = channel
        self.exchange = exchange

    async def send_message(self, message: AbstractMessage, routing_key: str) -> None:
        """
        Send a message to RabbitMQ exchange with specified routing key.
        """
        await self.exchange.publish(message=message, routing_key=routing_key)
