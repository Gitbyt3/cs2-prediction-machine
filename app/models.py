from pydantic import BaseModel


class PlayerRequest(BaseModel):
    name: str
