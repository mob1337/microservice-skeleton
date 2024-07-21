from service.model.rabbitmq_config import QueueConfig

config = QueueConfig(
                    queue_name = "test",
                    queue_routing_key = "test.routingkey1",
                    on_message_route = "test.routingkey2"
                    )