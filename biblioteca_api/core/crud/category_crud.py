from models.category_model import Category
from schemas.category_schema import CategoryCreate, Category
from crud.base_crud import CRUDBase

class CategoryCRUD(CRUDBase[Category, CategoryCreate, Category]):
    def __init__(self, model: type[Category]):
        super().__init__(model)

category_crud = CategoryCRUD(Category)