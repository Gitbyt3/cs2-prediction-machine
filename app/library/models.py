from typing import Optional

from pydantic import BaseModel, Field

from app.models import BaseCS2Model


class Country(BaseCS2Model):
    """Represents a country in the player data."""

    id: int
    code: str
    name: str
    region_id: int


class Player(BaseCS2Model):
    """Represents a BO3.gg player with associated metadata and nested country data.

    Fields are populated from the full CS2 API search_players response.
    """

    # Required fields (always present in API response)
    priority: int = Field(alias="priority", description="Player search priority")
    id: int = Field(description="Unique player identifier")
    slug: str = Field(description="URL-safe player identifier")
    nickname: str = Field(description="Player's display name")
    first_name: Optional[str] = Field(default=None, description="First name (optional)")
    last_name: Optional[str] = Field(default=None, description="Last name (optional)")
    status: int = Field(description="Account status flag")
    image_url: str = Field(description="Player profile image URL")
    rank: int = Field(description="Competitive rank")
    team_id: Optional[int] = Field(default=None, description="Team ID (if applicable)")
    country_id: Optional[int] = Field(default=None, description="Country ID")
    discipline_id: Optional[int] = Field(default=None, description="Discipline ID")

    # Nested country object with full details
    country: Optional[Country] = Field(
        default=None,
        description="Full country information (name, code, region), optional",
    )
