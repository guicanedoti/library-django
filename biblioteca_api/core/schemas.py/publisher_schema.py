from pydantic import BaseModel

class PublisherBase(BaseModel):
    name: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(PublisherBase):
    id: int

    class Config:
        from_attributes = True