from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/reports/occupancy")
def occupancy_report(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    # Consulta para ocupación de habitaciones
    query = """
    SELECT room_id, COUNT(*) as reservations
    FROM bookings
    WHERE start_date >= :start_date AND end_date <= :end_date
    GROUP BY room_id
    """
    result = db.execute(query, {"start_date": start_date, "end_date": end_date}).fetchall()
    return {"data": [dict(row) for row in result]}

@router.get("/reports/revenue")
def revenue_report(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    # Consulta para ingresos por reservas
    query = """
    SELECT SUM(total_amount) as total_revenue
    FROM invoices
    WHERE issue_date >= :start_date AND issue_date <= :end_date
    """
    result = db.execute(query, {"start_date": start_date, "end_date": end_date}).scalar()
    return {"total_revenue": result or 0}
