import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    RABBITMQ_USERNAME=os.getenv("RABBITMQ_USERNAME","guest")
    RABBITMQ_PASSWORD=os.getenv("RABBITMQ_PASSWORD","guest")
    RABBITMQ_HOST=os.getenv("RABBITMQ_HOST","localhost")
    RABBITMQ_EXCHANGE_NAME="TEST_EXCHANGE"


Config()
