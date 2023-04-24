from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database.database import SessionLocal, engine
from .database.models import Base, Player, Event
from .database.schemas import PlayerCreate, Player, EventCreate, Event

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/players", response_model=Player)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


@app.get("/players", response_model=List[Player])
def get_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = db.query(Player).offset(skip).limit(limit).all()
    return players


@app.get("/players/{player_id}", response_model=Player)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.post("/events", response_model=Event)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_player = db.query(Player).filter(Player.id == event.player_id).first()
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    db_event = Event(event_type=event.event_type, player_id=event.player_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@app.get("/events", response_model=List[Event])
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events


@app.get("/players/{player_id}/events", response_model=List[Event])
def get_player_events(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    events = db.query(Event).filter(Event.player_id == player_id).all()
    return events


@app.get("/players/{player_id}/events/{event_type}", response_model=List[Event])
def get_player_events_by_type(player_id: int, event_type: str, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    events = db.query(Event).filter(Event.player_id == player_id, Event.event_type == event_type).all()
    return events


@app.get("/events/{event_type}", response_model=List[Event])
def get_events_by_type(event_type: str, db: Session = Depends(get_db)):
    events = db.query(Event).filter(Event.event_type == event_type).all()
    return events
