from pydantic import BaseModel

class RoomBase(BaseModel):
    room_number: str
    is_available: bool
    room_type: str
    price_per_night: int

class RoomCreate(RoomBase):
    pass

class RoomResponse(RoomBase):
    id: int

    class Config:
        orm_mode = True
