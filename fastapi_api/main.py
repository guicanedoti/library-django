from fastapi import FastAPI
from core.database import Base, engine

from models import author_model, book_model, category_model, loan_model, publisher_model
from api.v1.api import api_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Biblioteca",
    description="Uma API completa para gerenciamento de biblioteca com FastAPI, SQLAlchemy e Pydantic.",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)


app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "API de Biblioteca com FastAPI funcionando!"}