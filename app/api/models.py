from typing import List

from pydantic import BaseModel

from app.models import BaseCS2Model
from app.library.models import Player


class PlayerRequest(BaseCS2Model):
    """API request model for querying player data."""

    name: str


class PlayerResponse(BaseCS2Model):
    """API response model containing validated player data.

    Contains a list of Player models with all fields from the CS2 API,
    including nested country information.
    """

    data: List[Player]
