from typing import Any

from cs2api import CS2


async def query_player(name: str) -> list[dict[str, Any]]:
    """
    Fetches matches for a single player using the cs2api client.
    """
    client = CS2()
    try:
        player_data = await client.search_players(name)
        return player_data
    finally:
        await client.close()
