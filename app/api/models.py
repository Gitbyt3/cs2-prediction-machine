from pydantic import BaseModel

from app.library.models import Player


class PlayerRequest(BaseModel):
    name: str


class PlayerResponse(BaseModel):
    data: list[Player]
