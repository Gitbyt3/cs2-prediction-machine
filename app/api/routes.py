from fastapi import APIRouter

from app.api.models import (
    PlayerRequest,
    PlayerResponse,
    TransferRequest,
    TransferResponse,
)
from app.library.player import CS2Player

router = APIRouter()


@router.post("/player", response_model=PlayerResponse)
async def get_player_matches(request: PlayerRequest) -> PlayerResponse:
    async with CS2Player() as player:
        result = await player.query_player(request.name)
    return PlayerResponse(data=result)


@router.post("/player/transfers", response_model=TransferResponse)
async def get_player_transfers(request: TransferRequest) -> TransferResponse:
    async with CS2Player() as player:
        result = await player.player_transfers(request.player_id, request.limit)
    return TransferResponse(data=result)
