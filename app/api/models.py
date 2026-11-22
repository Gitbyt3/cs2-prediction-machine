from pydantic import BaseModel

from app.library import Player


class PlayerRequest(BaseModel):
    name: str


class PlayerResponse(BaseModel):
    data: list[Player]
