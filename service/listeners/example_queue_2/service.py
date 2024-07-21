from aio_pika.abc import AbstractMessage, AbstractChannel
from service.listeners.example_queue_2.config import config
from service.adapters.rabbitmq import RabbitMQClient


async def handler(message: AbstractMessage, message_client: RabbitMQClient) -> None:

    print("message recevied from test queue", message.body)
