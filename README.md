# Vector DB API - Almacenamiento de Vectores

API FastAPI para recibir vectores y almacenarlos en la base de datos Chroma.

## Requisitos

- Python 3.9+
- Dependencias en `requirements.txt`
- Docker (opcional)

## Instalación local

```bash
git clone <repo-vector-db-api>
cd vector-db-api
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8001