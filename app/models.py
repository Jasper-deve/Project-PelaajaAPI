from typing import List
from pydantic import BaseModel


# Define a data model for Player
class Player(BaseModel):
    name: str
    id: int


# Define a data model for an Event
class Event(BaseModel):
    event_type: str
    timestamp: str
    player_id: int


# Define a data model for a list of players
class PlayerList(BaseModel):
    players: List[Player]


# Define a data model for a list of events
class EventList(BaseModel):
    events: List[Event]
