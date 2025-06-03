from fastapi_api.models.category_model import Category as CategoryModel
from fastapi_api.schemas.category_schema import CategoryCreate, Category as CategorySchema
from fastapi_api.crud.base_crud import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional

class CategoryCRUD(CRUDBase[CategoryModel, CategoryCreate, CategorySchema]):
    def get_by_name(self, db: Session, name: str) -> Optional[CategoryModel]:
        return db.query(self.model).filter(self.model.name == name).first()

category_crud = CategoryCRUD(CategoryModel)