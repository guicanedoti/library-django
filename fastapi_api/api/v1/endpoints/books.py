from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from core.dependencies import get_db
from schemas.book_schema import Book, BookCreate
from crud.book_crud import book_crud
from schemas.enums import BookStatus

router = APIRouter()

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_crud.create(db=db, obj_in=book)

@router.get("/", response_model=List[Book])
def read_all_books(
    db: Session = Depends(get_db),
    title: Optional[str] = Query(None, description="Filtrar por título do livro"),
    author_id: Optional[int] = Query(None, description="Filtrar por ID do autor")
):
    books = book_crud.get_books_by_filters(db, title=title, author_id=author_id)
    return books

@router.get("/{book_id}", response_model=Book)
def read_book_by_id(book_id: int, db: Session = Depends(get_db)):
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

@router.get("/status/{book_id}/{status_enum}", response_model=Book)
def update_book_status(book_id: int, status_enum: BookStatus, db: Session = Depends(get_db)):
    db_book = book_crud.get_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    # Para demonstração: Cria um Book schema com o status atualizado
    # IMPORTANTE: Se você quiser PERSISTIR o status, adicione uma coluna 'status' ao Book model (models/book_model.py)
    # e salve no banco de dados.
    book_response = Book.model_validate(db_book) # Cria um Pydantic model a partir do SQLAlchemy model
    book_response.status = status_enum # Define o status no objeto de resposta
    return book_response