from models.category_model import Category
from schemas.category_schema import CategoryCreate, Category
from crud.base_crud import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional

class CategoryCRUD(CRUDBase[Category, CategoryCreate, Category]):
    def get_by_name(self, db: Session, name: str) -> Optional[Category]:
        return db.query(self.model).filter(self.model.name == name).first()

category_crud = CategoryCRUD(Category)