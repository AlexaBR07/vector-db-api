from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from services.chroma_service import save_vectors_to_chroma, query_chroma

app = FastAPI()

class VectorData(BaseModel):
    ids: List[str]
    embeddings: List[List[float]]
    metadatas: List[Dict[str, Any]]

class QueryRequest(BaseModel):
    query: str
    n_results: int = 3

@app.post("/save-vectors")
def store_vectors(data: VectorData):
    try:
        save_vectors_to_chroma(data.ids, data.embeddings, data.metadatas)
        return {"message": "Vectores almacenados exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query-vectors")
def query_vectors(request: QueryRequest):
    try:
        results = query_chroma(request.query, request.n_results)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
