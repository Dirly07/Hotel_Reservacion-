from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.invoice_schema import InvoiceCreate, InvoiceResponse
from app.repositories.invoice_repository import create_invoice, get_invoices
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/invoices", response_model=InvoiceResponse)
def add_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db, invoice)

@router.get("/invoices", response_model=list[InvoiceResponse])
def read_invoices(db: Session = Depends(get_db)):
    return get_invoices(db)
