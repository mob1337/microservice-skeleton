import aio_pika
import sys
import asyncio
import uvicorn
from fastapi import FastAPI
from service.endpoint import v1
from service.logger_helper import logger
from service.config import Config
from service.listeners.example_queue import consumer as example_consumer
from service.listeners.example_queue_2 import consumer as example_consumer__2

app = FastAPI()
app.include_router(v1.router)

async def rabbit_mq_setup():
    logger.info("setting up connection with rabbitmq")
    connection = await aio_pika.connect(f"amqp://{Config.RABBITMQ_USERNAME}:{Config.RABBITMQ_PASSWORD}@{Config.RABBITMQ_HOST}/"
                        )
    async with connection:
        channel = await connection.channel()
        ###### ADD YOUR QUEUE BELOW #####
        await example_consumer.setup(channel) # example consumer1
        await example_consumer__2.setup(channel) #example consumer2
        ###### ADD YOUR QUEUE ABOVE #####
        try:
            while not connection.is_closed:
                logger.info("connected to rabbitmq client")
                await asyncio.Future()
        except Exception as e:
            connection.close()
            sys.exit()
        
            
async def start_uvicorn():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()

async def start_server_concurrently():
    await asyncio.gather(rabbit_mq_setup(), start_uvicorn())

if __name__ == '__main__':
    asyncio.run(start_server_concurrently())
