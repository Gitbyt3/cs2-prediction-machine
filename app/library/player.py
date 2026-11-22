from cs2api import CS2

from app.library.exceptions import PlayerAPIError
from app.library.models import Player


async def query_player(name: str) -> list[Player]:
    """Fetches match and player data for a single player using the CS2 API client.

    The full API response is parsed and validated into Player model objects,
    including nested country data.

    Args:
        name: The player's display name or partial name to search for.

    Returns:
        A list of Player model instances containing validated player match data.

    Raises:
        PlayerAPIError: If the API call fails or player data cannot be retrieved.
    """
    client = CS2()
    try:
        player_data = await client.search_players(name)
        results = player_data["results"]

        # Convert raw dicts to validated Player models
        return [Player.model_validate(player_data) for player_data in results]

    except Exception as e:
        raise PlayerAPIError(f"Failed to query player '{name}': {e}") from e

    finally:
        await client.close()
