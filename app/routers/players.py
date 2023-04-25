from fastapi import APIRouter

from app.models import Player, PlayerList


router = APIRouter()

# Define a list to store players
players = []

# Create a new player and add them to the list
@router.post("/players", response_model=Player)
def create_player(player: Player):
    player.id = len(players) + 1
    players.append(player)
    return player

# Get a list of all players
@router.get("/players", response_model=PlayerList)
def get_players():
    return {"players": players}

# Get a specific player by ID
@router.get("/players/{player_id}", response_model=Player)
def get_player(player_id: int):
    for player in players:
        if player.id == player_id:
            return player
    return {"error": "Player not found"}
