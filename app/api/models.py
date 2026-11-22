from pydantic import BaseModel

from app.library.models import Player


class PlayerRequest(BaseModel):
    """API request model for querying player data."""

    name: str


class PlayerResponse(BaseModel):
    """API response model containing validated player data.

    Contains a list of Player models with all fields from the CS2 API,
    including nested country information.
    """

    data: list[Player]
