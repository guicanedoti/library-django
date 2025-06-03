from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from fastapi_api.core.dependencies import get_db
from fastapi_api.schemas.category_schema import Category, CategoryCreate
from fastapi_api.crud.category_crud import category_crud

router = APIRouter()

@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = category_crud.get_by_name(db, category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category with this name already exists")
    return category_crud.create(db=db, obj_in=category)

@router.get("/", response_model=List[Category])
def read_all_categories(db: Session = Depends(get_db)):
    categories = category_crud.get_all(db)
    return categories

@router.get("/{category_id}", response_model=Category)
def read_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = category_crud.get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=Category)
def update_existing_category(category_id: int, category_update: CategoryCreate, db: Session = Depends(get_db)):
    db_category = category_crud.get_by_id(db, category_id)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category_crud.update(db=db, db_obj=db_category, obj_in=category_update)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    db_category = category_crud.get_by_id(db, category_id)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    category_crud.delete(db=db, db_obj=db_category)
    return