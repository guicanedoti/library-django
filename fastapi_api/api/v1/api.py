from fastapi import APIRouter
from api.v1.endpoints import authors, books, categories, publishers, loans, utilities

api_router = APIRouter()

api_router.include_router(authors.router, prefix="/authors", tags=["Authors"])
api_router.include_router(books.router, prefix="/books", tags=["Books"])
api_router.include_router(categories.router, prefix="/categories", tags=["Categories"])
api_router.include_router(publishers.router, prefix="/publishers", tags=["Publishers"])
api_router.include_router(loans.router, prefix="/loans", tags=["Loans"])
api_router.include_router(utilities.router, prefix="/utilities", tags=["Utilities"])