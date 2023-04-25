from fastapi import APIRouter
from datetime import datetime

from app.models import Event, EventList

router = APIRouter()

# Define a list to store events
events = []

# Create a new event and add it to the list
@router.post("/events", response_model=Event)
def create_event(event: Event):
    event.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    events.append(event)
    return event

# Get a list of all events
@router.get("/events", response_model=EventList)
def get_events():
    return {"events": events}

# Get all events for a specific player
@router.get("/players/{player_id}/events", response_model=EventList)
def get_player_events(player_id: int):
    player_events = []
    for event in events:
        if event.player_id == player_id:
            player_events.append(event)
    return {"events": player_events}

# Get all events of a specific type for a specific player
@router.get("/players/{player_id}/events/{event_type}", response_model=EventList)
def get_player_events_by_type(player_id: int, event_type: str):
    player_events = []
    for event in events:
        if event.player_id == player_id and event.event_type == event_type:
            player_events.append(event)
    return {"events": player_events}

# Get all events of a specific type
@router.get("/events/{event_type}", response_model=EventList)
def get_events_by_type(event_type: str):
    type_events = []
    for event in events:
        if event.event_type == event_type:
            type_events.append(event)
    return {"events": type_events}
