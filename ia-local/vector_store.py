# vector_store.py
import os
from typing import List, Dict, Any
import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma



class VectorStore:
    """Gestiona el almacenamiento y recuperación de vectores usando Chroma."""
    
    def __init__(self, persist_directory: str = "./chroma_db", embedding_model: str = "text-embedding-3-small"):
        """Inicializa el almacén de vectores."""
        self.persist_directory = persist_directory
        self.embedding_model = embedding_model
        
        # Crear directorio si no existe
        os.makedirs(persist_directory, exist_ok=True)
        
        # Configurar embeddings de OpenAI
        self.embeddings = OpenAIEmbeddings(model=embedding_model)
        
        # Inicializar Chroma
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings
        )
    
    def añadir_documentos(self, documentos: List[Dict[str, Any]]) -> None:
        """Añade documentos al almacén de vectores."""
        if not documentos:
            print("No hay documentos para añadir.")
            return
            
        # Añadir documentos a Chroma
        self.vectorstore.add_documents(documentos)
        
        # Persistir para guardar cambios
        self.vectorstore.persist()
        print(f"Se añadieron {len(documentos)} documentos al almacén de vectores.")
    
    def buscar_similares(self, consulta: str, k: int = 5) -> List[Dict[str, Any]]:
        """Busca los documentos más similares a la consulta."""
        documentos_similares = self.vectorstore.similarity_search_with_score(
            query=consulta,
            k=k
        )
        
        # Convertir a formato más amigable
        resultados = []
        for doc, score in documentos_similares:
            resultados.append({
                "contenido": doc.page_content,
                "metadata": doc.metadata,
                "score": score
            })
            
        return resultados