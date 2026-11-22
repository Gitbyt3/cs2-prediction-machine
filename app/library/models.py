from pydantic import ConfigDict, Field

from app.models import BaseCS2Model


class Country(BaseCS2Model):
    """Represents a country in the player/team data.

    Fields are populated from the CS2 API nested country object.
    The API also includes `region` as a nested object within country.
    """

    id: int
    code: str
    name: str
    region_id: int
    region: dict | None = Field(
        default=None, description="Region information (id, slug, name, flag)"
    )


class Team(BaseCS2Model):
    """Represents a CS2 team.

    This model matches the nested `team_to` and `team_from` objects
    from the player_transfers API response.
    The API also includes extra fields like `discipline_id` at top level.
    """

    # Use relaxed validation for team models since API may include extra fields
    model_config = ConfigDict(
        strict=False,
        extra="allow",
        frozen=True,
    )

    id: int = Field(alias="id", description="Team unique identifier")
    slug: str = Field(alias="slug", description="URL-safe team identifier")
    name: str = Field(alias="name", description="Team display name")
    image_url: str | None = Field(
        default=None, alias="image_url", description="Team logo URL"
    )


class Player(BaseCS2Model):
    """Represents a BO3.gg player with associated metadata.

    This model matches the nested `player` object from the player_transfers API response.
    The country field contains nested region information.
    The API also includes extra fields at top level (discipline_id, is_coach, etc.)
    """

    # Use relaxed validation for player models since API may include extra fields
    model_config = ConfigDict(
        strict=False,
        extra="allow",
        frozen=True,
    )

    id: int = Field(alias="id", description="Unique player identifier")
    slug: str = Field(alias="slug", description="URL-safe player identifier")
    nickname: str = Field(alias="nickname", description="Player's display name")
    first_name: str | None = Field(
        default=None, alias="first_name", description="First name (optional)"
    )
    last_name: str | None = Field(
        default=None, alias="last_name", description="Last name (optional)"
    )
    image_url: str | None = Field(
        default=None, alias="image_url", description="Player profile image URL"
    )
    is_coach: bool = Field(
        alias="is_coach", default=False, description="Whether player is a coach"
    )
    coach_status: str | None = Field(
        default=None, alias="coach_status", description="Coach status (optional)"
    )
    country_id: int | None = Field(
        default=None, alias="country_id", description="Country ID"
    )

    # Nested country object with region information
    country: Country | None = Field(
        default=None,
        description="Full country information including nested region data (name, code)",
    )


class Transfer(BaseCS2Model):
    """Represents a player transfer event.

    Fields are populated from the CS2 API player_transfers endpoint response.
    The API returns both flat fields at top level AND nested team/player objects.
    This model accepts all fields including extra ones for compatibility.
    """

    # Configure to allow extra fields (API returns more than just our schema)
    model_config = ConfigDict(
        strict=False,
        extra="allow",
        frozen=True,
    )

    # Top-level flat fields from API response
    id: int = Field(description="Transfer unique identifier")
    created_at: str | None = Field(
        default=None, description="Transfer record creation timestamp"
    )
    updated_at: str | None = Field(
        default=None, description="Transfer record update timestamp"
    )
    player_id: int = Field(description="Associated player ID")

    # Team IDs (from nested objects, also available flat)
    team_to_id: int | None = Field(
        default=None, description="Team to ID from nested object"
    )
    team_from_id: int | None = Field(
        default=None, description="Team from ID from nested object"
    )

    # Team names (from nested objects, also available flat)
    team_to_name: str | None = Field(
        default=None, description="Team to name from nested object"
    )
    team_from_name: str | None = Field(
        default=None, description="Team from name from nested object"
    )

    # Core transfer information
    action_date: str = Field(description="Date of transfer in YYYY-MM-DD format")
    action_type: int = Field(description="Action type (1=Signed to, 2=Released, etc.)")
    compensation: int | None = Field(
        default=None, description="Compensation amount (if applicable)"
    )

    # Nested objects from API response
    team_to: Team | None = Field(
        default=None,
        description="Team to with nested country data (optional)",
    )
    team_from: Team | None = Field(
        default=None,
        description="Team from with nested country data (optional)",
    )
    player: Player | None = Field(
        default=None,
        description="Player information at time of transfer",
    )
