"""
Module defining the message handling service for the example queue.
"""

from aio_pika.abc import AbstractMessage
from service.listeners.example_queue.config import config
from service.adapters.rabbitmq import RabbitMQClient


async def handler(message: AbstractMessage, message_client: RabbitMQClient) -> None:
    """
    Handle incoming messages from the example queue.
    """
    print("Sending message from test queue", message.body)
    await message_client.send_message(
        message=message, routing_key=config.on_message_route
    )
