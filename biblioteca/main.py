from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Olá, essa é a API do projeto Library!"}
