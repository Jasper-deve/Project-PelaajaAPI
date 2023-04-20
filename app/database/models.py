from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)

    events = relationship("Event", back_populates="player")


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String(50), index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    player_id = Column(Integer, ForeignKey("players.id"))
    player = relationship("Player", back_populates="events")
