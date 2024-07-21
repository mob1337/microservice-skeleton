import abc
from fastapi.responses import JSONResponse
from aio_pika.abc import AbstractConnection, AbstractChannel, AbstractMessage, AbstractExchange

class AbstractMessageClient(abc.ABC): 

    @abc.abstractmethod
    def send_message(self, message: AbstractMessage, 
                           routing_key: str) -> None:
        raise NotImplementedError