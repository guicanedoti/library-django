from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.dependencies import get_db
from schemas.publisher_schema import Publisher, PublisherCreate
from crud.publisher_crud import publisher_crud

router = APIRouter()

@router.post("/", response_model=Publisher, status_code=status.HTTP_201_CREATED)
def create_new_publisher(publisher: PublisherCreate, db: Session = Depends(get_db)):
    return publisher_crud.create(db=db, obj_in=publisher)

@router.get("/", response_model=List[Publisher])
def read_all_publishers(db: Session = Depends(get_db)):
    publishers = publisher_crud.get_all(db)
    return publishers

@router.get("/{publisher_id}", response_model=Publisher)
def read_publisher_by_id(publisher_id: int, db: Session = Depends(get_db)):
    publisher = publisher_crud.get_by_id(db, publisher_id)
    if not publisher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publisher not found")
    return publisher

@router.put("/{publisher_id}", response_model=Publisher)
def update_existing_publisher(publisher_id: int, publisher_update: PublisherCreate, db: Session = Depends(get_db)):
    db_publisher = publisher_crud.get_by_id(db, publisher_id)
    if not db_publisher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publisher not found")
    return publisher_crud.update(db=db, db_obj=db_publisher, obj_in=publisher_update)

@router.delete("/{publisher_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_publisher(publisher_id: int, db: Session = Depends(get_db)):
    db_publisher = publisher_crud.get_by_id(db, publisher_id)
    if not db_publisher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publisher not found")
    publisher_crud.delete(db=db, db_obj=db_publisher)
    return