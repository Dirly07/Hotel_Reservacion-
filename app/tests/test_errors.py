from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_invalid_booking():
    response = client.post("/api/bookings", json={"user_id": 999, "room_id": 999, "start_date": "2024-12-01", "end_date": "2024-12-05", "total_price": 800})
    assert response.status_code == 400  # Esperar un error por usuario o habitación inexistente

def test_invalid_invoice_creation():
    response = client.post("/api/invoices", json={"booking_id": 999, "issue_date": "2024-12-06", "total_amount": 1000})
    assert response.status_code == 400  # Error por reserva no existente
