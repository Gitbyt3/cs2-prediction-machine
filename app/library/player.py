from typing import Any

from cs2api import CS2

from app.library.exceptions import PlayerAPIError


async def query_player(name: str) -> list[dict[str, Any]]:
    """
    Fetches matches for a single player using the cs2api client.
    """
    client = CS2()
    try:
        player_data = await client.search_players(name)
        return player_data["results"]
    except Exception as e:
        raise PlayerAPIError(f"Failed to query player '{name}': {e}") from e

    finally:
        await client.close()
