# rag_system.py
import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from procesador_documento import ProcesadorDocumento
from vector_store import VectorStore
from openai_conector import OpenAIConnector

# Cargar variables de entorno
load_dotenv()

class RAGSystem:
    """Sistema RAG completo que integra procesamiento, vectorización y generación."""
    
    def __init__(self):
        # Cargar configuración desde variables de entorno
        chunk_size = int(os.environ.get("CHUNK_SIZE", 500))
        chunk_overlap = int(os.environ.get("CHUNK_OVERLAP", 50))
        retrieval_k = int(os.environ.get("MAX_RETRIEVAL_DOCS", 5))
        openai_model = os.environ.get("OPENAI_CHAT_MODEL", "gpt-4o-mini")
        embedding_model = os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
        
        # Inicializar componentes
        self.procesador = ProcesadorDocumento(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.vectorstore = VectorStore(embedding_model=embedding_model)
        self.llm = OpenAIConnector(model=openai_model)
        self.retrieval_k = retrieval_k
    
    def indexar_documento(self, ruta_archivo: str) -> None:
        """Procesa e indexa un documento."""
        fragmentos = self.procesador.procesar_archivo(ruta_archivo)
        self.vectorstore.añadir_documentos(fragmentos)
        print(f"Documento {os.path.basename(ruta_archivo)} indexado correctamente.")
    
    def indexar_directorio(self, directorio: str = "documents") -> None:
        """Procesa e indexa todos los documentos en un directorio."""
        fragmentos = self.procesador.procesar_directorio(directorio)
        if fragmentos:
            self.vectorstore.añadir_documentos(fragmentos)
            print(f"Se indexaron {len(fragmentos)} fragmentos de documentos.")
    
    def consultar(self, pregunta: str) -> Dict[str, Any]:
        """Realiza una consulta al sistema RAG."""
        # Buscar documentos relevantes
        contextos = self.vectorstore.buscar_similares(pregunta, k=self.retrieval_k)
        
        if not contextos:
            return {
                "respuesta": "No encontré información relevante para responder tu pregunta.",
                "fuentes": []
            }
        
        # Generar respuesta
        respuesta = self.llm.generar_respuesta(pregunta, contextos)
        
        # Preparar fuentes
        fuentes = []
        for ctx in contextos:
            fuentes.append({
                "documento": ctx["metadata"].get("source", "Desconocido"),
                "relevancia": ctx["score"]
            })
        
        return {
            "respuesta": respuesta,
            "fuentes": fuentes
        }