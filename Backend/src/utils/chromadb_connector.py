"""
ChromaDB Connector - Funciones CRUD para la base de datos vectorial

---------------------------------------------------------

PEQUEÑO PARENTENSIS

No se crea a partir del crud_base.py porque:

En SQLAlchemy (crud_base.py):

Trabaja con modelos de bases de datos relacionales
Usa sesiones SQL para las transacciones
Maneja entidades que tienen relaciones entre sí
Opera sobre registros con estructura fija (tablas)

En ChromaDB (chromadb_connector.py):

Trabaja con embeddings vectoriales para búsqueda semántica
Opera con "colecciones" de vectores en lugar de tablas
Está optimizado para búsqueda por similitud
No tiene un esquema rígido como SQL

---------------------------------------------------------

SPOILER

En crud_base.py usas: create(), get(), update(), remove()
En chromadb_connector.py usamos: add_document(), search_similar_documents(), update_document(), delete_document()

---------------------------------------------------------

CONCEPTOS PARA ENTENDER CHROMADB
Singleton: Asegura una única instancia compartida
Lazy Initialization:Técnica donde los objetos se crean solo cuando son realmente necesarios, no antes. Esto ahorra recursos al retrasar la creación hasta el momento de uso.
Encapsulación: Oculta detalles de implementación detrás de una interfaz
Búsqueda vectorial: ChromaDB usa embeddings vectoriales para encontrar similitudes semánticas

UTILIZA POR DEFECTO EL EMBEDDING all-MiniLM-L6-v2



---------------------------------------------------------

Un patrón Singleton bien implementado en el método __new__
Inicialización perezosa (lazy) en el método get_client()
Funciones CRUD completas (crear, leer, actualizar, eliminar)
Excelente manejo de errores con bloques try/except
Documentación detallada con docstrings explicativos

"""
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os
import uuid
from typing import List, Dict, Any, Optional
import logging


def load_env_file():
    """Lee el archivo .env manualmente"""
    env_vars = {}
    try:
        with open('.env', 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
        return env_vars
    except FileNotFoundError:
        return {}

class ChromaDBConnector:
    _instance = None
    _client = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChromaDBConnector, cls).__new__(cls)#con esto hace que sea una vez
            # Inicialización lazy - el cliente se creará la primera vez que se use basandose en el patron singleton
            cls._instance._client = None
        return cls._instance
    
    def get_client(self):
        """
        Como no ha sido inicializado la instancia, lo crea utilizando la configuración especificada.Crea el url por asi decirlo
        """
        if self._client is None:
            print(f"Inicializando cliente HTTP de ChromaDB")
            self._client = chromadb.HttpClient(host="10.15.22.81", port=8500)
            
        return self._client
    
#---------------------------------------------------------
    def test_connection(self) -> bool:
        """Prueba la conexión/funcionalidad de ChromaDB"""
        try:
            # Intenta una operación simple para verificar la funcionalidad
            client = self.get_client()
            # Listar colecciones es una operación ligera para probar
            client.list_collections()
            return True
        except Exception as e:
            print(f"Error con ChromaDB: {str(e)}")
            return False

#---------------------------------------------------------
            
    def create_collection(self, collection_name, metadata=None):
        """Crea una colección si no existe"""
        client = self.get_client()
        try:
            # Intenta obtener la colección primero
            return client.get_collection(name=collection_name, embedding_function=None)
        except:
            # Si no existe, créala
            return client.create_collection(
                name=collection_name,
                metadata=metadata or {},
                embedding_function=None
            )
        


#------------------------------------------------------------------        

    def add_documents(self, 
                collection_name: str, 
                document_ids: List[str], 
                chunks: List[str], 
                metadatas: Optional[List[Dict[str, Any]]] = None): #lo que podemos usar para filtrar
        
                collection = self.create_collection(collection_name)
                
                # Si no se proporcionan embeddings, ChromaDB los generará
             
                collection.add(
                    ids=document_ids,
                    documents=chunks,
                    metadatas=metadatas
                )
#--------------------------------------------------
  

    def search_documents(self, 
                    collection_name: str,  # Nombre de la colección donde buscar
                    query_text: str,       # Texto de búsqueda que será convertido a vector
                    n_results: int = 5,    # Número de resultados a devolver
                    where: Optional[Dict[str, Any]] = None):  # Filtros opcionales por metadatos (como SQL WHERE)
        """
        Busca documentos semánticamente similares al texto de consulta.
        
        Funcionamiento:
        1. El texto de consulta 'query_text' se convierte automáticamente en un vector numérico
        usando el modelo de embeddings "all-MiniLM-L6-v2" de Sentence Transformers por defecto,
        que genera vectores de 384 dimensiones que capturan el significado semántico del texto.
        
        2. ChromaDB compara este vector con todos los vectores almacenados usando:
        - Similitud del coseno (predeterminada): Compara la dirección de los vectores 
            ignorando su longitud, detectando textos semánticamente similares.
        - Distancia euclidiana: Mide la distancia directa entre vectores en el espacio.
        - Distancia de Manhattan: Suma las diferencias en cada dimensión.
        
        3. El parámetro 'n_results' controla cuántos documentos más similares se devuelven.
        
        4. El parámetro 'where' permite filtrar resultados por metadatos, similar a SQL:
        Ejemplo: where={"autor": "María"} solo devolverá documentos de ese autor.

        Son como columnas de SQL

        Un "chunk" es un fragmento de texto que:

        Proviene de dividir documentos más grandes en partes manejables
        Tiene un tamaño apropiado para ser procesado eficientemente
        Puede representar párrafos, secciones o divisiones lógicas del texto
        
        """
        client = self.get_client()
        try:
            collection = client.get_collection(name=collection_name)
            results = collection.query(
                query_texts=[query_text],  # Se pasa como lista porque permite consultas múltiples
                n_results=n_results,       # Número máximo de resultados similares
                where=where                # Filtros adicionales por metadatos
            )
            return results
        except Exception as e:
            print(f"Error al buscar documentos: {str(e)}")
            return None
    
#--------------------------------------------------

    def update_document(self,
                   collection_name: str,                     # Nombre de la colección
                   document_id: str,                         # ID único del documento a actualizar
                   chunk: Optional[str] = None,              # Nuevo texto a guardar (opcional)
                   metadata: Optional[Dict[str, Any]] = None): # Nuevos metadatos (opcional
        """Actualiza un documento existente"""
        client = self.get_client()
        try:
            collection = client.get_collection(name=collection_name)
            collection.update(
                ids=[document_id], # ID del documento a actualizar
                documents=[chunk] if chunk else None, # Nuevo contenido del documento enviado a traves de chunk a chroma que ya existe previamente en la base de datos y si es none indica que no quiero actualizar el contenido
                metadatas=[metadata] if metadata else None # los datos por los cuales a traves vas hacer una consulta
            )
            return True
        except Exception as e:
            print(f"Error al actualizar documento: {str(e)}")
            return False


#---------------------------------------------------------

    def delete_documents(self, collection_name: str, document_ids: List[str]):
        """Elimina documentos por ID"""
        client = self.get_client()
        try:
            collection = client.get_collection(name=collection_name)
            collection.delete(ids=document_ids)
            return True
        except Exception as e:
            print(f"Error al eliminar documentos: {str(e)}")
            return False


#---------------------------------------------------------
    def get_document(self, collection_name: str, document_id: str):
        """Obtiene un documento específico por ID"""
        client = self.get_client()
        try:
            collection = client.get_collection(name=collection_name)
            result = collection.get(ids=[document_id])
            return result
        except Exception as e:
            print(f"Error al obtener documento: {str(e)}")
            return None
            
        