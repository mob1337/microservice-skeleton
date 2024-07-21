"""
Module defining queue configuration for example queue.
"""

from service.model.rabbitmq_config import QueueConfig

config = QueueConfig(
    queue_name="test2",
    queue_routing_key="test.routingkey2",
    on_message_route="test.routingkey_someother_queue",
)
