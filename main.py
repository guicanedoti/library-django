from fastapi_api.routers import authors, books

app = FastAPI()

app.include_router(authors.router)
app.include_router(categories.router)
app.include_router(books.router)
app.include_router(publishers.router)  
app.include_router(loans.router)
