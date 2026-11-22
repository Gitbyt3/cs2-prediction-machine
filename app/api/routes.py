from fastapi import APIRouter

from app.library.player import query_player
from app.models import PlayerRequest

router = APIRouter()


@router.post("/player")
async def get_player_matches(request: PlayerRequest):
    return await query_player(request.name)
