"""
Main file for starting the uvicorn server and setting up RabbitMQ consumers.
"""

import asyncio
import sys

import uvicorn

import aio_pika
from aio_pika.abc import AbstractRobustChannel, AbstractRobustConnection

from fastapi import FastAPI
from service.endpoint import v1
from service.logger_helper import logger
from service.config import Config
from service.listeners.example_queue import consumer as example_consumer
from service.listeners.example_queue_2 import consumer as example_consumer_2

app = FastAPI()
app.include_router(v1.router)


async def rabbit_mq_setup() -> None:
    """
    Set up connection with RabbitMQ and start consumers.
    """
    logger.info("Setting up connection with RabbitMQ")
    connection: AbstractRobustConnection = await aio_pika.connect_robust(
        f"amqp://{Config.RABBITMQ_USERNAME}:{Config.RABBITMQ_PASSWORD}@{Config.RABBITMQ_HOST}/"
    )
    async with connection:
        channel: AbstractRobustChannel = await connection.channel()
        await example_consumer.setup(channel)  # Example consumer 1
        await example_consumer_2.setup(channel)  # Example consumer 2
        try:
            while not connection.is_closed:
                logger.info("Connected to RabbitMQ client")
                await asyncio.Future()
        except Exception as e:  # pylint: disable=W0703
            logger.error(e)
            connection.close()
            sys.exit()


async def start_uvicorn() -> None:
    """
    Start uvicorn server with FastAPI.
    """
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


async def start_server_concurrently() -> None:
    """
    Start RabbitMQ setup and uvicorn server concurrently.
    """
    await asyncio.gather(rabbit_mq_setup(), start_uvicorn())


if __name__ == "__main__":
    asyncio.run(start_server_concurrently())
