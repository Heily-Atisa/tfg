# Carpeta de documentos

Coloca en esta carpeta los documentos que deseas indexar y consultar con el sistema RAG local.

## Formatos soportados

El sistema actualmente soporta los siguientes formatos de archivo:

- **Archivos de texto (.txt)**
- **Documentos PDF (.pdf)**

## Recomendaciones

Para obtener los mejores resultados:

1. **Estructura clara**: Utiliza documentos bien estructurados con títulos, subtítulos y párrafos claros.

2. **Contenido relevante**: Incluye documentos que contengan la información que deseas consultar.

3. **Tamaño adecuado**: Archivos demasiado grandes pueden ralentizar el procesamiento.

4. **Nombres descriptivos**: Usa nombres de archivo significativos para facilitar la identificación de fuentes.

5. **Texto legible**: Asegúrate de que los PDF contengan texto legible por computadora (no escaneos sin OCR).

6. **Organización**: Considera crear subcarpetas para organizar documentos por tema o categoría.

## Procesamiento

Cuando ejecutes `python indexer.py` o inicies el sistema completo, estos documentos serán:

1. Leídos y procesados para extraer su texto
2. Divididos en fragmentos más pequeños
3. Convertidos a embeddings vectoriales
4. Almacenados en un índice para búsqueda eficiente

## Documento de ejemplo

Se ha incluido un documento de ejemplo (`documento_ejemplo.txt`) para que puedas probar el sistema inmediatamente. 

Para agregar tus propios documentos, simplemente colócalos en esta carpeta y ejecuta nuevamente el indexador.
