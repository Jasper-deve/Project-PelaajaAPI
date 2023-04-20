from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Define a data model for Player
class Player(BaseModel):
    name: str
    id: int

# Define a data model for an Event
class Event(BaseModel):
    event_type: str
    timestamp: str
    player_id: int

# Define a list to store players and events
players = []
events = []

# Create a new player and add them to the list
@app.post("/players")
def create_player(player: Player):
    player.id = len(players) + 1
    players.append(player)
    return player

# Get a list of all players
@app.get("/players")
def get_players():
    return players

# Get a specific player by ID
@app.get("/players/{player_id}")
def get_player(player_id: int):
    for player in players:
        if player.id == player_id:
            return player
    return {"error": "Player not found"}

# Create a new event and add it to the list
@app.post("/events")
def create_event(event: Event):
    event.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    events.append(event)
    return event

# Get a list of all events
@app.get("/events")
def get_events():
    return events

# Get all events for a specific player
@app.get("/players/{player_id}/events")
def get_player_events(player_id: int):
    player_events = []
    for event in events:
        if event.player_id == player_id:
            player_events.append(event)
    return player_events

# Get all events of a specific type for a specific player
@app.get("/players/{player_id}/events/{event_type}")
def get_player_events_by_type(player_id: int, event_type: str):
    player_events = []
    for event in events:
        if event.player_id == player_id and event.event_type == event_type:
            player_events.append(event)
    return player_events

# Get all events of a specific type
@app.get("/events/{event_type}")
def get_events_by_type(event_type: str):
    type_events = []
    for event in events:
        if event.event_type == event_type:
            type_events.append(event)
    return type_events
