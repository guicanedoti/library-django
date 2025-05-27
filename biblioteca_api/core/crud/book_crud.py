from models.book_model import Book
from schemas.book_schema import BookCreate, Book
from crud.base_crud import CRUDBase

class BookCRUD(CRUDBase[Book, BookCreate, Book]):
    def __init__(self, model: type[Book]):
        super().__init__(model)

book_crud = BookCRUD(Book)