from pydantic import BaseModel


class UserCreate(BaseModel):
    #id: int
    name: str
    task: str