from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    event_type: str
    timestamp: Optional[datetime] = None
    player_id: int


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
