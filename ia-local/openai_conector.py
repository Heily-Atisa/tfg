# openai_conector.py
import os
from typing import List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class OpenAIConnector:
    """Conector para la API de OpenAI."""
    
    def __init__(self, model: str = "gpt-4o-mini"):
        """Inicializa el conector de OpenAI."""
        # Cargar API key desde variables de entorno
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("No se encontró OPENAI_API_KEY en las variables de entorno")
            
        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        
        # Cargar parámetros de configuración
        self.temperature = float(os.environ.get("TEMPERATURE", 0.7))
        self.top_p = float(os.environ.get("TOP_P", 0.95))
        self.max_tokens = int(os.environ.get("MAX_TOKENS", 1024))
    
    def generar_respuesta(self, consulta: str, contextos: List[Dict[str, Any]]) -> str:
        """Genera una respuesta basada en la consulta y los contextos recuperados."""
        # Construir el prompt
        prompt = self._construir_prompt(consulta, contextos)
        
        # Llamar a la API de OpenAI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Eres un asistente útil que responde preguntas basándose en los documentos proporcionados. Si la información no está en los documentos, indícalo claramente."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens
        )
        
        return response.choices[0].message.content
    
    def _construir_prompt(self, consulta: str, contextos: List[Dict[str, Any]]) -> str:
        """Construye el prompt con la consulta y los contextos."""
        prompt = "Por favor, responde a esta pregunta basándote únicamente en la siguiente información:\n\n"
        
        # Añadir contextos
        prompt += "CONTEXTO:\n"
        for i, ctx in enumerate(contextos, 1):
            source = ctx["metadata"].get("source", f"Documento {i}")
            prompt += f"[{source}]\n{ctx['contenido']}\n\n"
        
        # Añadir consulta
        prompt += f"PREGUNTA: {consulta}\n\n"
        prompt += "RESPUESTA:"
        
        return prompt