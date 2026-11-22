from cs2api import CS2

from app.library.exceptions import PlayerAPIError
from app.library.models import Player, Transfer


class CS2Player:
    def __init__(self):
        """Initialize the API client."""
        self._client = CS2()

    async def __aenter__(self):
        """Enter async context manager - returns self."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context manager - ensures client is closed."""
        await self._client.close()

    async def close(self):
        """Explicitly close the underlying client.

        This method can be called directly or via the context manager's `__aexit__`.
        """
        await self._client.close()

    async def query_player(self, name: str) -> list[Player]:
        try:
            player_data = await self._client.search_players(name)
            results = player_data["results"]

            # Convert raw dicts to validated Player models
            return [Player.model_validate(player_data) for player_data in results]

        except Exception as e:
            raise PlayerAPIError(f"Failed to query player '{name}': {e}") from e

    async def player_transfers(self, player_id: int, limit: int = 10) -> list[Transfer]:
        try:
            transfer_data = await self._client.get_player_transfers(player_id, limit)

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
