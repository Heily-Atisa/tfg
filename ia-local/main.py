# main.py

import os
import sys
from ragsystem import RAGSystem

"""
os.getcwd() es una función en Python que devuelve el directorio de trabajo actual (CWD - Current Working Directory) como una cadena de texto. El nombre es una abreviatura de "get current working directory".
Esta función es muy útil para:

Saber exactamente desde qué directorio está operando tu programa
Construir rutas absolutas basadas en la ubicación actual
Diagnosticar problemas de rutas relativas

"""
def main():
    """Función principal para ejecutar el sistema RAG."""
   
    # Crear instancia del sistema RAG
    rag = RAGSystem()

    # Variable para rastrear si se ha indexado algo
    documentos_indexados = False

    # Menú principal
    while True:
        print("\n=== SISTEMA RAG ===")
        
        print("0. Ver todos los documentos")
        print("1. Indexar documento")
        print("2. Indexar directorio completo")
        print("3. Hacer consulta")
        print("4. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "0":
            # Mostrar todos los documentos en el directorio "documents" no usar rutas relativas como directorio = "documents" mejor usar rutas absolutas y luego lo añades con join asi evitas el posible error de usar distintas rutas para referirse a la misma carpeta
            directorio = os.path.join(os.getcwd(), "documents")

            if os.path.exists(directorio) and os.path.isdir(directorio):
                print("\nDocumentos en el directorio 'documents':")
                for archivo in os.listdir(directorio):
                    ruta_archivo = os.path.join(directorio, archivo)
                    if os.path.isfile(ruta_archivo):
                        print(f"- {archivo}")
            else:
                print(f"Error: El directorio {directorio} no existe.")
        
        elif opcion == "1":
            # Indexar documento individual
            ruta = input("Ruta del documento a indexar: ")
            if os.path.exists(ruta) and os.path.isfile(ruta):
                rag.indexar_documento(ruta)
                documentos_indexados = True
            else:
                print(f"Error: El archivo {ruta} no existe.")
        elif opcion == "2":
            # Indexar directorio completo
            directorio = input("Directorio a indexar (default: documents): ") or "documents"
            if os.path.exists(directorio) and os.path.isdir(directorio):
                rag.indexar_directorio(directorio)
                documentos_indexados = True
            else:
                print(f"Error: El directorio {directorio} no existe.")
        elif opcion == "3":

            if not documentos_indexados:
                print("\nError: Debes indexar al menos un documento antes de hacer consultas.")
                print("Utiliza la opción 1 o 2 para indexar documentos primero.")
                continue
                
            # Hacer consulta
            pregunta = input("\nEscribe tu pregunta: ")
            if pregunta:
                print("\nBuscando respuesta...")
                resultado = rag.consultar(pregunta)
                
                print("\nRespuesta:")
                print(resultado["respuesta"]) #Imprimes la respuesta en un diccionario
                """
                    Este código asume que:

                    resultado["fuentes"] es una lista de diccionarios
                    Cada diccionario tiene al menos dos claves: 'documento' y 'relevancia'
                    La relevancia es un valor numérico (probablemente entre 0 y 1)

                    El objetivo de mostrar estas fuentes es proporcionar transparencia sobre:

                    De dónde vino la información
                    Qué tan relevante fue cada documento para la consulta (mediante el puntaje de relevancia)
                    Ayudar al usuario a verificar la calidad y confiabilidad de la respuesta
                """
                
                if resultado["fuentes"]:  # Verifica si hay fuentes disponibles
                    print("\nFuentes:")   # Imprime un encabezado
                    # Recorre cada fuente en la lista, empezando a enumerar desde 1
                    for i, fuente in enumerate(resultado["fuentes"], 1):
                        # Imprime cada fuente con formato: número, nombre del documento y relevancia
                        print(f"{i}. {fuente['documento']} (Relevancia: {fuente['relevancia']:.4f})")
            else:
                print("Debes escribir una pregunta.")
                
        elif opcion == "4":
            # Salir
            print("¡Hasta luego!")
            sys.exit(0)
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()