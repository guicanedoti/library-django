from models.book_model import Book
from schemas.book_schema import BookCreate, Book
from crud.base_crud import CRUDBase
from typing import List, Optional
from sqlalchemy.orm import Session

class BookCRUD(CRUDBase[Book, BookCreate, Book]):
    def get_books_by_filters(self, db: Session, title: Optional[str] = None, author_id: Optional[int] = None) -> List[Book]:
        query = db.query(self.model)
        if title:
            query = query.filter(self.model.title.contains(title))
        if author_id:
            query = query.filter(self.model.author_id == author_id)
        return query.all()

book_crud = BookCRUD(Book)