from typing import List
from pydantic import BaseModel

class Player(BaseModel):
    name: str
    id: int

class Event(BaseModel):
    event_type: str
    timestamp: str
    player_id: int

class PlayerList(BaseModel):
    players: List[Player]

class EventList(BaseModel):
    events: List[Event]



# from sqlalchemy import Column, Integer, String  
# from sqlalchemy.orm import relationship
# 
#  jossain kohtaaa hajoaa :(

# from app.database import Base

# class Player(Base):
#     __tablename__ = "players"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)


# class Event(Base):
#     __tablename__ = "events"

#     id = Column(Integer, primary_key=True, index=True)
#     event_type = Column(String)
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())
#     player_id = Column(Integer, ForeignKey("players.id"))

#     player = relationship("Player", back_populates="events")