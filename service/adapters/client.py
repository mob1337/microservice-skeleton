from service.adapters.abstract_client import AbstractTestClient
from fastapi.responses import JSONResponse
from service.model.example_model import UserDetail

class SetupClientExample(AbstractTestClient):
    def __init__(self, username: str, lastname: str):
        self.username = username
        self.lastname = lastname
    

    def greet_user(self) -> UserDetail:
        return UserDetail(first_name=self.username, last_name=self.lastname)
