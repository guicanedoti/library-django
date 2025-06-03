from sqlalchemy.orm import Session
from fastapi_api.core.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()