from typing import TypeVar, Type, Any, List, Optional
from sqlalchemy.orm import Session
from core.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Any)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=Any)

class CRUDBase:
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def get_by_id(self, db: Session, obj_id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == obj_id).first()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.model_dump()) # Use model_dump() para Pydantic v2+
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        # Pydantic v2+ usa model_dump(exclude_unset=True)
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: ModelType) -> ModelType:
        db.delete(db_obj)
        db.commit()
        return db_obj