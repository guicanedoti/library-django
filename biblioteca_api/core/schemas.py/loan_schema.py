from pydantic import BaseModel
from typing import Optional
from datetime import date

class LoanBase(BaseModel):
    book_id: int
    borrower: str
    loan_date: date
    return_date: Optional[date] = None

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int

    class Config:
        from_attributes = True