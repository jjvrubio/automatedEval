#!/usr/bin/env python3
"""
Módulo 3: EL CEREBRO (Gemini 1.5 Pro API)
Analiza contenido recolectado usando prompts secuenciales.
"""

import google.genai as genai
from pathlib import Path
from typing import List, Dict, Optional


class Brain:
    """Motor de análisis con Gemini 1.5 Pro."""
    
    def __init__(
        self, 
        api_key: str,
        model_name: str = "gemini-1.5-pro-latest",
        temperature: float = 0.1
    ):
        genai.configure(api_key=api_key)
        config = genai.GenerationConfig(
            temperature=temperature,
            top_p=0.95,
            top_k=64,
            max_output_tokens=8192,
        )
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=config
        )
        
        self.prompts_cache: Dict[str, str] = {}
    
    def load_prompt(self, prompt_file: Path) -> str:
        """
        Carga un prompt desde archivo Markdown.
        
        Args:
            prompt_file: Ruta al archivo de prompt
        
        Returns:
            Contenido del prompt
        """
        if not prompt_file.exists():
            raise FileNotFoundError(f"Prompt no encontrado: {prompt_file}")
        
        # Usar cache para evitar lecturas repetidas
        cache_key = str(prompt_file)
        if cache_key not in self.prompts_cache:
            self.prompts_cache[cache_key] = prompt_file.read_text(encoding='utf-8')
        
        return self.prompts_cache[cache_key]
    
    def load_prompts_sequence(self, prompts_dir: Path) -> List[str]:
        """
        Carga secuencia de prompts numerados.
        
        Args:
            prompts_dir: Directorio con archivos 01_system.md, 02_trigger.md, etc.
        
        Returns:
            Lista ordenada de prompts
        """
        if not prompts_dir.exists():
            raise FileNotFoundError(f"Directorio de prompts no encontrado: {prompts_dir}")
        
        prompt_files = sorted(prompts_dir.glob("*.md"))
        
        if not prompt_files:
            raise ValueError(f"No se encontraron archivos .md en {prompts_dir}")
        
        prompts = []
        for pf in prompt_files:
            print(f"📄 Cargando: {pf.name}")
            prompts.append(self.load_prompt(pf))
        
        return prompts
    
    def analyze_with_context(
        self, 
        context: str,
        prompt_template: str,
        variables: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Ejecuta análisis con contexto y variables.
        
        Args:
            context: Contenido recolectado (texto de fuentes)
            prompt_template: Prompt con placeholders {variable}
            variables: Dict con valores para reemplazar en template
        
        Returns:
            Respuesta generada por el modelo
        """
        # Preparar prompt final
        if variables:
            prompt = prompt_template.format(**variables)
        else:
            prompt = prompt_template
        
        # Agregar contexto
        full_prompt = f"{prompt}\n\n--- DATOS RECUPERADOS ---\n{context}"
        
        print(f"🧠 Analizando ({len(full_prompt)} caracteres)...")
        
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"❌ Error generando contenido: {e}"
    
    def sequential_analysis(
        self,
        context: str,
        prompts: List[str],
        variables: Optional[Dict[str, str]] = None
    ) -> List[str]:
        """
        Ejecuta análisis secuencial con múltiples prompts.
        
        Cada prompt puede usar el resultado del anterior como input adicional.
        
        Args:
            context: Contenido base
            prompts: Lista de prompts a ejecutar en orden
            variables: Variables compartidas entre prompts
        
        Returns:
            Lista de respuestas por prompt
        """
        responses = []
        accumulated_context = context
        
        for i, prompt in enumerate(prompts, 1):
            print(f"\n🔄 Fase {i}/{len(prompts)}")
            
            response = self.analyze_with_context(
                context=accumulated_context,
                prompt_template=prompt,
                variables=variables
            )
            
            responses.append(response)
            
            # Acumular respuestas previas para siguiente fase
            accumulated_context += f"\n\n--- ANÁLISIS FASE {i} ---\n{response}"
        
        return responses
    
    def simple_query(self, question: str) -> str:
        """
        Query simple sin contexto adicional.
        
        Args:
            question: Pregunta directa al modelo
        
        Returns:
            Respuesta generada
        """
        try:
            response = self.model.generate_content(question)
            return response.text
        except Exception as e:
            return f"❌ Error: {e}"


if __name__ == "__main__":
    # Test básico
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("MI_CLAVE_API_GEMINI")
    
    if api_key:
        brain = Brain(api_key)
        
        # Test simple
        response = brain.simple_query("¿Cuál es la capital de España?")
        print(response)
    else:
        print("❌ Configura MI_CLAVE_API_GEMINI en .env")
