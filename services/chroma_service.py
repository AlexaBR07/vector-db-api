from chromadb import PersistentClient

def save_vectors_to_chroma(ids, embeddings, metadatas):
    client = PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(name="documents")

    collection.add(
        embeddings=embeddings,
        documents=["vector"] * len(embeddings),
        metadatas=metadatas,
        ids=ids
    )
