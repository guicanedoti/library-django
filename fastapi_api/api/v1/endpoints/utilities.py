from fastapi import APIRouter, Path, Query
from typing import Optional, List # Importar List para o Query Parameter com lista

router = APIRouter()

# Endpoint com Path Parameter com Path
@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    Simula a leitura de um arquivo, demonstrando um Path Parameter com Path.
    O 'file_path' pode conter barras, por exemplo: /utilities/files/docs/my_book.pdf
    """
    return {"file_path": file_path, "message": f"Conteúdo do arquivo em {file_path} seria lido aqui."}

# Endpoint com Path Parameters opcionais e Múltiplos Query Parameters
@router.get("/search/{item_id}")
async def search_item(
    item_id: int,
    q: Optional[str] = Query(None, min_length=3, max_length=50, description="Termo de busca opcional"),
    is_active: bool = Query(True, description="Filtrar por itens ativos (true por padrão)"),
    # Exemplo de Query Parameter com lista
    tags: Optional[List[str]] = Query(None, description="Lista de tags para filtrar")
):
    """
    Demonstra Path Parameter (item_id), Query Parameter opcional (q),
    e Múltiplos Query Parameters (q, is_active, tags).
    """
    results = {"item_id": item_id, "is_active": is_active}
    if q:
        results.update({"query": q})
    if tags:
        results.update({"tags": tags})

    return results