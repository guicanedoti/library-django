from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from fastapi_api.core.dependencies import get_db
from fastapi_api.schemas.author_schema import Author, AuthorCreate
from fastapi_api.crud.author_crud import author_crud

router = APIRouter()

@router.post("/", response_model=Author, status_code=status.HTTP_201_CREATED)
def create_new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = author_crud.get_by_name(db, author.name)
    if db_author:
        raise HTTPException(status_code=400, detail="Author with this name already exists")
    return author_crud.create(db=db, obj_in=author)

@router.get("/", response_model=List[Author])
def read_all_authors(db: Session = Depends(get_db)):
    authors = author_crud.get_all(db)
    return authors

@router.get("/{author_id}", response_model=Author)
def read_author_by_id(author_id: int, db: Session = Depends(get_db)):
    author = author_crud.get_by_id(db, author_id)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author

@router.put("/{author_id}", response_model=Author)
def update_existing_author(author_id: int, author_update: AuthorCreate, db: Session = Depends(get_db)):
    db_author = author_crud.get_by_id(db, author_id)
    if not db_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author_crud.update(db=db, db_obj=db_author, obj_in=author_update)

@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_author(author_id: int, db: Session = Depends(get_db)):
    db_author = author_crud.get_by_id(db, author_id)
    if not db_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    author_crud.delete(db=db, db_obj=db_author)
    return