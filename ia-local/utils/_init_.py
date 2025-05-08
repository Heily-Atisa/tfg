# utils/__init__.py
"""
Utilidades para el sistema RAG.
Este paquete contiene funciones y clases auxiliares utilizadas por los componentes principales.

¿Qué es __init__.py?
Es un archivo especial que convierte una carpeta en un paquete de Python
Se ejecuta cuando importas el paquete
En este caso, está dentro de la carpeta utils

Primera parte - Importaciones:
El . significa "en esta misma carpeta"
Está importando funciones desde un archivo llamado helpers.py
Cada línea es una función diferente que se está importando

Segunda parte - __all__:
El __all__ es como una lista de control que asegura que solo las funciones que tú quieres sean accesibles cuando alguien importa todo tu paquete con el asterisco (*).
"""

"""
Aquí NO estás importando toda la clase, sino que estás importando específicamente solo las funciones que nombras.
Aquí estás especificando qué funciones estarán disponibles cuando alguien use from utils import *
"""

from .helpers import (
    limpiar_texto,    # Solo importo estas funciones específicas
    medir_tiempo,      # No importo otras funciones que puedan existir en helpers.py
    guardar_json,
    cargar_json,
    configurar_logger,
    extraer_texto_limpio,
)

# Exportar las funciones de helpers para que estén disponibles directamente desde utils
# Defines the public API for the utils package
__all__ = [
    'limpiar_texto',    # Doy permiso para que estas funciones
    'medir_tiempo',      # sean accesibles cuando alguien use from utils import *
    'guardar_json',
    'cargar_json',
    'configurar_logger',
    'extraer_texto_limpio'
]

#Primero seleccionas qué funciones quieres importar de helpers.py
#Luego das permiso para que esas funciones sean visibles cuando otros importen tu paquete