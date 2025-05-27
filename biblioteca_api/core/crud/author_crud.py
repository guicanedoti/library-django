from models.author_model import Author
from schemas.author_schema import AuthorCreate, Author
from crud.base_crud import CRUDBase

class AuthorCRUD(CRUDBase[Author, AuthorCreate, Author]):
    def __init__(self, model: type[Author]):
        super().__init__(model)

author_crud = AuthorCRUD(Author)