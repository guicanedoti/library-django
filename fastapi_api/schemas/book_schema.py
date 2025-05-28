from pydantic import BaseModel
from typing import Optional
from .enums import BookStatus

class BookBase(BaseModel):
    title: str
    author_id: int
    category_id: int
    publisher_id: int
    publication_year: Optional[int] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    status: BookStatus = BookStatus.available # Adiciona o status padrão

    class Config:
        from_attributes = True