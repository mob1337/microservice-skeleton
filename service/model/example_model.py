from pydantic import BaseModel

class UserDetail(BaseModel):
    first_name: str
    last_name: str