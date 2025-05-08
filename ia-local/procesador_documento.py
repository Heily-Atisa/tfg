#Transformar documentos heterogéneos en fragmentos procesables para el modelo.

"""
Chunk overlap (superposición): hace que los fragmentos se solapen un poco, evitando que la información se corte a la mitad entre dos chunks. Funciona como un "puente" que conecta un fragmento con el siguiente, asegurando que haya continuidad.
Separators (separadores): las instrucciones sobre dónde preferimos que se divida el texto al crear los chunks. Le dice al sistema: "Intenta cortar por aquí primero, y si no es posible, prueba con esto otro".
"""

# procesador_documento.py
import os
from typing import List, Dict, Any
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

class ProcesadorDocumento:
    """Clase para procesar y fragmentar documentos."""
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ".", " ", ""]
        )
    
    def cargar_documento(self, ruta_archivo: str) -> List[Dict[str, Any]]:
        """Carga un documento según su extensión."""
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo {ruta_archivo} no existe")
            
        # Seleccionar el cargador adecuado según la extensión
        extension = os.path.splitext(ruta_archivo)[1].lower()
        
        if extension == ".pdf":
            loader = PyPDFLoader(ruta_archivo)
        elif extension == ".txt":
            loader = TextLoader(ruta_archivo, encoding="utf-8")
        elif extension == ".docx":
            loader = Docx2txtLoader(ruta_archivo)
        else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")
            
        # Cargar el documento
        documentos = loader.load()
        
        # Añadir metadatos
        for doc in documentos:
            doc.metadata["source"] = os.path.basename(ruta_archivo)
            
        return documentos
    
    def fragmentar_documentos(self, documentos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Divide los documentos en fragmentos."""
        return self.text_splitter.split_documents(documentos)
    
    def procesar_archivo(self, ruta_archivo: str) -> List[Dict[str, Any]]:
        """Procesa un archivo: lo carga y fragmenta."""
        documentos = self.cargar_documento(ruta_archivo)
        fragmentos = self.fragmentar_documentos(documentos)
        
        print(f"Archivo {os.path.basename(ruta_archivo)} procesado: {len(fragmentos)} fragmentos")
        return fragmentos
    
    def procesar_directorio(self, directorio: str) -> List[Dict[str, Any]]:
        """Procesa todos los archivos en un directorio."""
        if not os.path.exists(directorio):
            raise FileNotFoundError(f"El directorio {directorio} no existe")
            
        todos_fragmentos = []
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            if os.path.isfile(ruta_completa):
                try:
                    fragmentos = self.procesar_archivo(ruta_completa)
                    todos_fragmentos.extend(fragmentos)
                except (ValueError, FileNotFoundError) as e:
                    print(f"Error al procesar {archivo}: {e}")
                    
        return todos_fragmentos