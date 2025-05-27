from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.dependencies import get_db
from schemas.loan_schema import Loan, LoanCreate
from crud.loan_crud import loan_crud

router = APIRouter()

@router.post("/", response_model=Loan, status_code=status.HTTP_201_CREATED)
def create_new_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    return loan_crud.create(db=db, obj_in=loan)

@router.get("/", response_model=List[Loan])
def read_all_loans(db: Session = Depends(get_db)):
    loans = loan_crud.get_all(db)
    return loans

@router.get("/{loan_id}", response_model=Loan)
def read_loan_by_id(loan_id: int, db: Session = Depends(get_db)):
    loan = loan_crud.get_by_id(db, loan_id)
    if not loan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    return loan

@router.put("/{loan_id}", response_model=Loan)
def update_existing_loan(loan_id: int, loan_update: LoanCreate, db: Session = Depends(get_db)):
    db_loan = loan_crud.get_by_id(db, loan_id)
    if not db_loan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    return loan_crud.update(db=db, db_obj=db_loan, obj_in=loan_update)

@router.delete("/{loan_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = loan_crud.get_by_id(db, loan_id)
    if not db_loan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    loan_crud.delete(db=db, db_obj=db_loan)
    return