from fastapi_api.models.book_model import Book as BookModel
from fastapi_api.schemas.book_schema import BookCreate, Book as BookSchema
from fastapi_api.crud.base_crud import CRUDBase
from typing import List, Optional
from sqlalchemy.orm import Session

class BookCRUD(CRUDBase[BookModel, BookCreate, BookSchema]):
    def get_books_by_filters(self, db: Session, title: Optional[str] = None, author_id: Optional[int] = None) -> List[BookModel]:
        query = db.query(self.model)
        if title:
            query = query.filter(self.model.title.contains(title))
        if author_id:
            query = query.filter(self.model.author_id == author_id)
        return query.all()

book_crud = BookCRUD(BookModel)
