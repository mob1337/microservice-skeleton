import aio_pika
from aio_pika.abc import AbstractConnection, AbstractChannel, AbstractMessage, AbstractExchange
from service.config import Config

class RabbitMQClient():
    def __init__(self, channel: AbstractChannel = None, exchange: AbstractExchange = None):
        self.channel = channel
        self.exchange = exchange

    async def send_message(self, message: AbstractMessage, 
                           routing_key: str) -> None:
        await self.exchange.publish(
            message = message,
            routing_key = routing_key
        )
