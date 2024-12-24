from fastapi import FastAPI
from app.controllers.room_controller import router as room_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(room_router, prefix="/api")
