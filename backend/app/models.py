from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Fan(Base):
    __tablename__ = "fans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    favorite_player = Column(String)
    join_date = Column(TIMESTAMP)

    interactions = relationship("Interaction", back_populates="fan")
    scores = relationship("Score", back_populates="fan")


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    fan_id = Column(Integer, ForeignKey("fans.id"))
    interaction_type = Column(String, nullable=False)
    timestamp = Column(TIMESTAMP)

    fan = relationship("Fan", back_populates="interactions")


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    fan_id = Column(Integer, ForeignKey("fans.id"))
    points = Column(Integer, nullable=False)
    updated_at = Column(TIMESTAMP)

    fan = relationship("Fan", back_populates="scores")
