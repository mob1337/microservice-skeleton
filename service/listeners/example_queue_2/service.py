"""
Module defining the message handling service for the example queue.
"""

from aio_pika.abc import AbstractMessage

# from service.listeners.example_queue_2.config import config
from service.adapters.rabbitmq import RabbitMQClient


async def handler(message: AbstractMessage, message_client: RabbitMQClient) -> None:
    """
    Handle incoming messages from the example queue2.
    """
    print(message_client)
    print("message recevied from test queue", message.body)
