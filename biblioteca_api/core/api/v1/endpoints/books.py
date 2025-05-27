from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importações corrigidas:
from core.dependencies import get_db # A dependência get_db está em core/dependencies
from schemas.book_schema import Book, BookCreate # Os schemas estão em schemas/ e o arquivo é book_schema.py
from crud.book_crud import book_crud # O crud específico está em crud/ e o arquivo é book_crud.py

router = APIRouter() # Removi o prefixo daqui, pois ele será incluído em api/v1/api.py

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    # Certifique-se de que book_crud está sendo importado corretamente
    return book_crud.create(db=db, obj_in=book)

@router.get("/", response_model=List[Book])
def read_all_books(db: Session = Depends(get_db)):
    books = book_crud.get_all(db)
    return books

@router.get("/{book_id}", response_model=Book)
def read_book_by_id(book_id: int, db: Session = Depends(get_db)):
    # Use o método do CRUD
    book = book_crud.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book)
def update_existing_book(book_id: int, book_update: BookCreate, db: Session = Depends(get_db)):
    db_book = book_crud.get_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book_crud.update(db=db, db_obj=db_book, obj_in=book_update)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_crud.get_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    book_crud.delete(db=db, db_obj=db_book)
    return