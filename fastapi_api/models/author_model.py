from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from fastapi_api.core.database import Base

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)

    books = relationship("Book", back_populates="author")