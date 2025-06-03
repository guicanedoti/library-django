from fastapi_api.models.publisher_model import Publisher as PublisherModel
from fastapi_api.schemas.publisher_schema import PublisherCreate, Publisher as PublisherSchema
from fastapi_api.crud.base_crud import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional

class PublisherCRUD(CRUDBase[PublisherModel, PublisherCreate, PublisherSchema]):
    def get_by_name(self, db: Session, name: str) -> Optional[PublisherModel]:
        return db.query(self.model).filter(self.model.name == name).first()

publisher_crud = PublisherCRUD(PublisherModel)