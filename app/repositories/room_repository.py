from sqlalchemy.orm import Session
from app.models.room import Room
from app.schemas.room_schema import RoomCreate

def get_rooms(db: Session):
    return db.query(Room).all()

def create_room(db: Session, room: RoomCreate):
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room
