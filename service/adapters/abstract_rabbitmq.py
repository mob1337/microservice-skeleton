import abc
from fastapi.responses import JSONResponse

class AbstractMessageClient(abc.ABC): 

    @abc.abstractmethod
    def send_message(self) -> JSONResponse:
        raise NotImplementedError