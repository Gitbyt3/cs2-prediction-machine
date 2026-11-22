"""Player data fetching using CS2 API client."""

from typing import Any

from cs2api import CS2

from app.library.exceptions import PlayerAPIError


async def query_player(name: str) -> list[dict[str, Any]]:
    """Fetches match and player data for a single player using the CS2 API client.

    Args:
        name: The player's display name or partial name to search for.

    Returns:
        A list of dictionaries containing player match data.

    Raises:
        PlayerAPIError: If the API call fails or player data cannot be retrieved.
    """
    client = CS2()
    try:
        player_data = await client.search_players(name)
        return player_data["results"]
    except Exception as e:
        raise PlayerAPIError(f"Failed to query player '{name}': {e}") from e

    finally:
        await client.close()
