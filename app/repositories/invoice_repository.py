from sqlalchemy.orm import Session
from app.models.invoice import Invoice
from app.schemas.invoice_schema import InvoiceCreate

def create_invoice(db: Session, invoice: InvoiceCreate):
    db_invoice = Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoices(db: Session):
    return db.query(Invoice).all()
