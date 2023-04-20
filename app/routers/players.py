from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from ..database import SessionLocal, engine, Player, Event
from pydantic import BaseModel

router = APIRouter()

class PlayerIn(BaseModel):
    name: str

class PlayerOut(BaseModel):
    id: int
    name: str

# Dependency to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/players", response_model=PlayerOut)
def create_player(player: PlayerIn, db: Session = Depends(get_db)):
    db_player = Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

@router.get("/players", response_model=List[PlayerOut])
def get_players(db: Session = Depends(get_db)):
    players = db.query(Player).all()
    return players

@router.get("/players/{player_id}", response_model=PlayerOut)
def get_player(player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(Player).filter(Player.id == player_id).first()
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@router.get("/players/{player_id}/events")
def get_player_events(player_id: int, db: Session = Depends(get_db)):
    db_events = db.query(Event).filter(Event.player_id == player_id).all()
    return db_events
