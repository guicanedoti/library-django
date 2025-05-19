from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/authors", tags=["Authors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Author)

@router.post("/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, models.Author, author)
