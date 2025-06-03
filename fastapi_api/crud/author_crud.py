from fastapi_api.models.author_model import Author as AuthorModel
from fastapi_api.schemas.author_schema import AuthorCreate, Author as AuthorSchema
from fastapi_api.crud.base_crud import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional

class AuthorCRUD(CRUDBase[AuthorModel, AuthorCreate, AuthorSchema]):
    def get_by_name(self, db: Session, name: str) -> Optional[AuthorModel]:
        return db.query(self.model).filter(self.model.name == name).first()

author_crud = AuthorCRUD(AuthorModel)
