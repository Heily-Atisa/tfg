# utils/helpers.py
"""
Funciones auxiliares para el sistema RAG.
"""

import re
import json
import time
import logging
import unicodedata
from typing import Any, Dict, List, Optional, Callable
from functools import wraps
from datetime import datetime

def limpiar_texto(texto: str) -> str:
    """
    Limpia un texto eliminando caracteres especiales, espacios duplicados, etc.
    
    Args:
        texto: El texto a limpiar
        
    Returns:
        Texto limpio
    """
    if not texto:
        return ""
        
    # Normalizar caracteres Unicode (acentos, etc.)
    texto = unicodedata.normalize('NFKD', texto)
    
    # Eliminar caracteres especiales y mantener solo letras, números y puntuación básica
    texto = re.sub(r'[^\w\s.,;:¿?¡!()[\]{}"\'"-]', ' ', texto)
    
    # Eliminar espacios duplicados
    texto = re.sub(r'\s+', ' ', texto)
    
    return texto.strip()

def extraer_texto_limpio(html_or_text: str) -> str:
    """
    Extrae texto limpio de un posible contenido HTML.
    Útil para procesar documentos web o emails.
    
    Args:
        html_or_text: Texto que puede contener HTML
        
    Returns:
        Texto limpio sin HTML
    """
    # Eliminar etiquetas HTML si las hay
    texto = re.sub(r'<[^>]+>', ' ', html_or_text)
    
    # Aplicar limpieza general
    return limpiar_texto(texto)

def medir_tiempo(func: Callable) -> Callable:
    """
    Decorador para medir el tiempo de ejecución de una función.
    
    Args:
        func: La función a medir
        
    Returns:
        Función decorada
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tiempo_inicio = time.time()
        resultado = func(*args, **kwargs)
        tiempo_fin = time.time()
        
        print(f"[TIEMPO] {func.__name__} ejecutado en {tiempo_fin - tiempo_inicio:.4f} segundos")
        return resultado
    
    return wrapper

def guardar_json(datos: Any, ruta_archivo: str) -> None:
    """
    Guarda datos en formato JSON.
    
    Args:
        datos: Los datos a guardar
        ruta_archivo: Ruta donde guardar el archivo
    """
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
        
def cargar_json(ruta_archivo: str) -> Any:
    """
    Carga datos desde un archivo JSON.
    
    Args:
        ruta_archivo: Ruta del archivo a cargar
        
    Returns:
        Datos cargados desde el JSON
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_archivo} no contiene JSON válido")
        return None

def configurar_logger(nombre: str, nivel: int = logging.INFO) -> logging.Logger:
    """
    Configura y devuelve un logger personalizado.
    
    Args:
        nombre: Nombre del logger
        nivel: Nivel de logging (por defecto INFO)
        
    Returns:
        Objeto logger configurado
    """
    # Crear logger
    logger = logging.getLogger(nombre)
    logger.setLevel(nivel)
    
    # Evitar duplicación de handlers es decir evitar duplicar metodos que se encargan de manejar a un evento especifco cuando ocurre 
    if not logger.handlers:
        # Crear handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(nivel)
        
        # Formato del log
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        formatter = logging.Formatter(
            f'[{fecha_actual} %(asctime)s] %(name)s - %(levelname)s: %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        
        # Añadir handler al logger
        logger.addHandler(console_handler)
    
    return logger