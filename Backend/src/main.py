# Importar FastAPI desde fastapi directamente
from fastapi import FastAPI

#http://10.15.22.81:8500/docs todos los endpoints de ChromaDB 




# Importar modelos específicos según los necesites
from src.models.schemas.user import UserCreate, UserResponse
from src.models.schemas.document import DocumentBase, DocumentResponse
from src.models.schemas.chat import ChatMessage

# Importar el conector de ChromaDB 
from src.utils.chromadb_connector import ChromaDBConnector

# Crear la aplicación
app = FastAPI()

# Inicializar el conector ChromaDB una sola vez al inicio de la aplicación
chroma_db = ChromaDBConnector()

# Endpoint para verificar el estado de ChromaDB
@app.get("/chroma-status")
def chroma_status():
    is_connected = chroma_db.test_connection()
    if is_connected:
        collections = chroma_db.get_client().list_collections()
        return {"status": "ChromaDB funcionando correctamente", "collections": len(collections)}
    else:
        return {"status": "Error en ChromaDB"}

# Ejecutar la app con uvicorn con uvicorn src.main:app --host localhost --port 2691
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=2691, reload=True)