from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.room_schema import RoomCreate, RoomResponse
from app.repositories.room_repository import get_rooms, create_room
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/rooms", response_model=list[RoomResponse])
def read_rooms(db: Session = Depends(get_db)):
    return get_rooms(db)

@router.post("/rooms", response_model=RoomResponse)
def add_room(room: RoomCreate, db: Session = Depends(get_db)):
    return create_room(db, room)
