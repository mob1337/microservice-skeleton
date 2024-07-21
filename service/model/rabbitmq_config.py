from pydantic import BaseModel

class QueueConfig(BaseModel):
    queue_name: str
    queue_routing_key: str
    on_message_route: str
    
