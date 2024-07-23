"""
Module defining consumer setup and message handling for example queue.
"""

from aio_pika.abc import AbstractChannel, AbstractIncomingMessage
from service.config import Config
from service.adapters.rabbitmq import RabbitMQClient
from service.listeners.example_queue.config import config
from service.listeners.example_queue.service import handler

message_client = RabbitMQClient()


async def setup(channel: AbstractChannel):
    """
    Set up the queue and exchange for consuming messages.
    """
    queue = await channel.declare_queue(config.queue_name)
    message_client.exchange = await channel.declare_exchange(
        Config.RABBITMQ_EXCHANGE_NAME,
        "direct",
    )
    await queue.bind(message_client.exchange, config.queue_routing_key)
    message_client.channel = channel
    await queue.consume(on_message)


async def on_message(message: AbstractIncomingMessage) -> None:
    """
    Handle incoming message from the queue.
    """
    await handler(message, message_client)
    await message.ack()
