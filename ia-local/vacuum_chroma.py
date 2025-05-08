"""
vacuum_chroma.py - Script de mantenimiento para bases de datos ChromaDB

Este script resuelve el siguiente problema:
"It looks like you upgraded from a version below 0.5.6 and could benefit from vacuuming your database"

PROBLEMA:
Cuando se actualiza ChromaDB desde una versión anterior a la 0.5.6, la estructura interna
de la base de datos puede contener datos que ya no son necesarios en la nueva versión.
Esto puede provocar advertencias, uso ineficiente del almacenamiento y potencialmente 
afectar al rendimiento.

SOLUCIÓN:
La operación "vacuum" limpia la base de datos eliminando datos obsoletos, 
reorganizando el almacenamiento y optimizando la estructura, similar a cómo 
funciona VACUUM en SQLite o ANALYZE TABLE en otras bases de datos.

BENEFICIOS:
- Elimina el mensaje de advertencia
- Recupera espacio en disco
- Mejora el rendimiento de las consultas
- Mantiene la integridad de los datos
"""

import chromadb
import os
import sys

def vacuum_chroma_db(db_path="./chroma_db"):
    """
    Ejecuta la operación de vacuum en una base de datos ChromaDB.
    
    Args:
        db_path (str): Ruta a la carpeta de la base de datos ChromaDB.
                       Por defecto busca en ./chroma_db
    """
    # Verificar si la carpeta existe
    if not os.path.exists(db_path):
        print(f"Error: No se encontró la base de datos en {db_path}")
        print("Posibles ubicaciones de la base de datos:")
        print("  - ./chroma_db")
        print("  - ./.chroma")
        print("  - ./db")
        return False
    
    try:
        print(f"Conectando a la base de datos ChromaDB en: {db_path}")
        client = chromadb.PersistentClient(db_path)
        
        print("Ejecutando operación de vacuum...")
        print("Esto puede tardar un momento dependiendo del tamaño de la base de datos.")
        client.maintenance.vacuum()
        
        print("\n✅ Operación de vacuum completada exitosamente.")
        print("El mensaje de advertencia no debería aparecer en futuras ejecuciones.")
        return True
    
    except Exception as e:
        print(f"\n❌ Error durante la operación de vacuum: {str(e)}")
        print("\nSi el error persiste, considera estas alternativas:")
        print("1. Actualizar chromadb a la última versión: pip install -U chromadb")
        print("2. Recrear la base de datos (implica reindexar documentos)")
        return False

if __name__ == "__main__":
    # Permitir especificar una ruta personalizada como argumento
    db_path = sys.argv[1] if len(sys.argv) > 1 else "./chroma_db"
    vacuum_chroma_db(db_path)