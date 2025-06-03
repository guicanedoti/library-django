from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_api.core.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    publication_year = Column(Integer, nullable=True)

    author = relationship("Author", back_populates="books")
    category = relationship("Category", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")
    loans = relationship("Loan", back_populates="book")