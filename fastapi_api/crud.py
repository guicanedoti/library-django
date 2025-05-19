from sqlalchemy.orm import Session
import models, schemas

def get_all(db: Session, model):
    return db.query(model).all()

def create_item(db: Session, model, schema):
    db_item = model(**schema.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
