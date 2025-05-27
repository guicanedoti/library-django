from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from core.database import Base

class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    borrower = Column(String, index=True)
    loan_date = Column(Date)
    return_date = Column(Date, nullable=True)

    book = relationship("Book", back_populates="loans")