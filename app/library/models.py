from pydantic import BaseModel


class Country(BaseModel):
    """Represents a country in the player data."""

    id: int
    code: str
    name: str
    region_id: int


class Player(BaseModel):
    """Represents a BO3.gg player with associated metadata."""

    priority: int
    id: int
    slug: str
    nickname: str
    first_name: str | None = None
    last_name: str | None = None
    status: int
    image_url: str
    rank: int
    team_id: int | None = None
    country_id: int | None = None
    discipline_id: int | None = None
    country: Country | None = None
