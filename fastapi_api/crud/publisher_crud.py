from models.publisher_model import Publisher
from schemas.publisher_schema import PublisherCreate, Publisher
from crud.base_crud import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional

class PublisherCRUD(CRUDBase[Publisher, PublisherCreate, Publisher]):
    def get_by_name(self, db: Session, name: str) -> Optional[Publisher]:
        return db.query(self.model).filter(self.model.name == name).first()

publisher_crud = PublisherCRUD(Publisher)