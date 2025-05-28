from models.author_model import Author
from schemas.author_schema import AuthorCreate, Author
from crud.base_crud import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional

class AuthorCRUD(CRUDBase[Author, AuthorCreate, Author]):
    def get_by_name(self, db: Session, name: str) -> Optional[Author]:
        return db.query(self.model).filter(self.model.name == name).first()

author_crud = AuthorCRUD(Author)