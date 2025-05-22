from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Inicializa el cliente persistente
client = PersistentClient(path="./chroma_db")

# Define la función de embedding
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def save_vectors_to_chroma(ids, embeddings, metadatas):
    collection = client.get_or_create_collection(name="documents")
    collection.add(
        embeddings=embeddings,
        documents=["vector"] * len(embeddings),
        metadatas=metadatas,
        ids=ids
    )

def query_chroma(query_text: str, n_results: int = 3):
    # Obtiene o crea la colección con la función de embedding
    collection = client.get_or_create_collection(name="documents", embedding_function=embedding_function)
    
    # Realiza la consulta
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    
    return results
