from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author_id: int
    category_id: int
    publisher_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True