import os
from langchain.vectorstores import Chroma
from langchain.embeddings.base import Embeddings
from langchain.vectorstores.base import Document
from langchain.schema.document import Document as LangchainDocument
from chromadb.config import Settings

# Dummy Embeddings (ya tenemos los vectores, no se usan aquí)
class IdentityEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return texts
    def embed_query(self, text):
        return text

persist_directory = "./chroma_db"

def save_vectors_to_chroma(ids, embeddings, metadatas):
    vectorstore = Chroma(
        collection_name="documents",
        embedding_function=IdentityEmbeddings(),
        persist_directory=persist_directory,
    )

    documents = [LangchainDocument(page_content="vector", metadata=meta) for meta in metadatas]

    vectorstore._collection.add(
        embeddings=embeddings,
        documents=["vector"] * len(embeddings),  # Placeholder text
        metadatas=metadatas,
        ids=ids
    )

    vectorstore.persist()
