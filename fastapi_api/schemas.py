from pydantic import BaseModel
from typing import Optional
from datetime import date

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        from_attributes = True


class PublisherBase(BaseModel):
    name: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(PublisherBase):
    id: int
    class Config:
        from_attributes = True


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


class LoanBase(BaseModel):
    book_id: int
    borrower: str
    loan_date: date
    return_date: Optional[date]

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    class Config:
        from_attributes = True
