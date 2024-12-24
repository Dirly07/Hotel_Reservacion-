from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_booking():
    # Create user and room
    client.post("/api/users", json={"name": "Jane Doe", "email": "jane@example.com", "password": "1234"})
    client.post("/api/rooms", json={"room_number": "101", "is_available": True, "room_type": "Deluxe", "price_per_night": 200})
    
    # Create booking
    response = client.post("/api/bookings", json={"user_id": 1, "room_id": 1, "start_date": "2024-12-01", "end_date": "2024-12-05", "total_price": 800})
    assert response.status_code == 200
    assert response.json()["total_price"] == 800
