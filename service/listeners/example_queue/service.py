from aio_pika.abc import AbstractMessage, AbstractChannel
from service.listeners.example_queue.config import config
from service.adapters.rabbitmq import RabbitMQClient


async def handler(message: AbstractMessage, message_client: RabbitMQClient) -> None:

    print("sending message from test queue", message.body)
    await message_client.send_message(
        message= message,
        routing_key = config.on_message_route
    )
