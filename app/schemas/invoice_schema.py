from pydantic import BaseModel
from datetime import datetime

class InvoiceBase(BaseModel):
    booking_id: int
    issue_date: datetime
    total_amount: int

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
