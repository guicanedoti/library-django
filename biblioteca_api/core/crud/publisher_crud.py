from models.publisher_model import Publisher
from schemas.publisher_schema import PublisherCreate, Publisher
from crud.base_crud import CRUDBase

class PublisherCRUD(CRUDBase[Publisher, PublisherCreate, Publisher]):
    def __init__(self, model: type[Publisher]):
        super().__init__(model)

publisher_crud = PublisherCRUD(Publisher)