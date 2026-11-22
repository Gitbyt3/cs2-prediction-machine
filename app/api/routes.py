from fastapi import APIRouter

from app.api.models import PlayerRequest, PlayerResponse
from app.library.player import query_player

router = APIRouter()


@router.post("/player", response_model=PlayerResponse)
async def get_player_matches(request: PlayerRequest) -> PlayerResponse:
    result = await query_player(request.name)
    return PlayerResponse(data=result)
