import abc
from fastapi.responses import JSONResponse

class AbstractTestClient(abc.ABC): 

    @abc.abstractmethod
    def greet_user(self) -> JSONResponse:
        raise NotImplementedError
