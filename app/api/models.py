from pydantic import Field

from app.library import Player, Transfer
from app.models import BaseCS2Model


class PlayerRequest(BaseCS2Model):
    """API request model for querying player data."""

    name: str


class PlayerResponse(BaseCS2Model):
    """API response model containing validated player data.

    Contains a list of Player models with all fields from the CS2 API,
    including nested country information.
    """

    data: list[Player]


class TransferRequest(BaseCS2Model):
    """API request model for querying player transfers.

    Args:
        player_id: The unique identifier of the player to get transfer history for.
        limit: Maximum number of transfer records to retrieve (default: 10).
    """

    player_id: int = Field(description="Unique player ID from BO3.gg API")
    limit: int = Field(default=10, description="Maximum number of transfers to return")


class TransferResponse(BaseCS2Model):
    """API response model containing validated transfer data.

    Contains a list of Transfer models with all fields from the CS2 API,
    including nested team information (both `team_from` and `team_to`) with
    their IDs, names, slugs, and nested country data.
    """

    data: list[Transfer]
