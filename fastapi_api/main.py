from fastapi import FastAPI
from .routers import authors  # importe o arquivo de rotas que você criou

app = FastAPI()

app.include_router(authors.router, prefix="/authors", tags=["authors"])

@app.get("/")
async def root():
    return {"message": "API de Biblioteca com FastAPI funcionando!"}
