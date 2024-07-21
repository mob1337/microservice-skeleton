"""
Module defining QueueConfig model schema.
"""

from pydantic import BaseModel


class QueueConfig(BaseModel):
    """
    QueueConfig model schema.

    Attributes:
        queue_name (str): The name of the queue.
        queue_routing_key (str): The routing key for the queue.
        on_message_route (str): The route for handling incoming messages.
    """

    queue_name: str
    queue_routing_key: str
    on_message_route: str
