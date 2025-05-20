from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from services.chroma_service import save_vectors_to_chroma

app = FastAPI()

class VectorData(BaseModel):
    ids: List[str]
    embeddings: List[List[float]]
    metadatas: List[Dict[str, Any]]

@app.post("/store-vectors")
def store_vectors(data: VectorData):
    try:
        save_vectors_to_chroma(data.ids, data.embeddings, data.metadatas)
        return {"message": "Vectores almacenados exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
