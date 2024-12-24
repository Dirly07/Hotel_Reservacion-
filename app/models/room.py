from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String, unique=True, index=True)
    is_available = Column(Boolean, default=True)
    room_type = Column(String)
    price_per_night = Column(Integer)
