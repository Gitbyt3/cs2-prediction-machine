from cs2api import CS2

from app.library.exceptions import PlayerAPIError
from app.library.models import Player, Transfer


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


async def player_transfers(player_id: int, limit: int = 10) -> list[Transfer]:
    client = CS2()
    try:
        transfer_data = await client.get_player_transfers(player_id, limit)

        # Validate and extract transfers from results list
        if "results" not in transfer_data:
            raise PlayerAPIError(f"No results found for player_id={player_id}")

        transfer_list = transfer_data["results"]

        # Convert raw dicts to validated Transfer models
        return [Transfer.model_validate(transfer) for transfer in transfer_list]

    except Exception as e:
        raise PlayerAPIError(
            f"Failed to query transfers for player {player_id}: {e}"
        ) from e

    finally:
        await client.close()
