#!/usr/bin/env python3
"""
Parser para extraer system prompt y escenarios desde archivo Markdown.
Específico para 'Instrucción para Gems.md'.
"""

import re
from pathlib import Path
from typing import Dict, Optional, Tuple


def extract_system_prompt(markdown_content: str) -> Optional[str]:
    """
    Extrae el contenido del epígrafe '# System instruction'.
    
    Args:
        markdown_content: Contenido completo del archivo Markdown
    
    Returns:
        Texto del system prompt o None si no se encuentra
    """
    # Buscar desde '# System instruction' hasta el siguiente '# ' o '---'
    pattern = r'# System instruction\s*\n(.*?)(?=\n#\s|\n---|\Z)'
    match = re.search(pattern, markdown_content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    return None


def extract_scenarios(markdown_content: str) -> Dict[str, str]:
    """
    Extrae los 4 escenarios (OPCIÓN A, B, C, D).
    
    Args:
        markdown_content: Contenido completo del archivo Markdown
    
    Returns:
        Dict con keys 'A', 'B', 'C', 'D' y sus contenidos
    """
    scenarios = {}
    
    # Patrón para cada opción
    pattern = r'## OPCIÓN ([A-D]):\s*([^\n]+)\n(.*?)(?=\n## OPCIÓN|\Z)'
    matches = re.finditer(pattern, markdown_content, re.DOTALL)
    
    for match in matches:
        option_letter = match.group(1)  # A, B, C, D
        option_title = match.group(2).strip()  # Título del escenario
        option_content = match.group(3).strip()  # Contenido completo
        
        scenarios[option_letter] = {
            'title': option_title,
            'content': option_content
        }
    
    return scenarios


def load_gems_instruction(file_path: Path) -> Tuple[Optional[str], Dict[str, str]]:
    """
    Carga el archivo completo y extrae system prompt + escenarios.
    
    Args:
        file_path: Ruta al archivo 'Instrucción para Gems.md'
    
    Returns:
        Tupla (system_prompt, scenarios_dict)
    """
    if not file_path.exists():
        print(f"❌ Archivo no encontrado: {file_path}")
        return None, {}
    
    try:
        content = file_path.read_text(encoding='utf-8')
        
        system_prompt = extract_system_prompt(content)
        scenarios = extract_scenarios(content)
        
        if system_prompt:
            print(f"✅ System prompt extraído: {len(system_prompt)} caracteres")
        else:
            print("⚠️  System prompt no encontrado")
        
        print(f"✅ Escenarios extraídos: {len(scenarios)}")
        
        return system_prompt, scenarios
        
    except Exception as e:
        print(f"❌ Error leyendo archivo: {e}")
        return None, {}


if __name__ == "__main__":
    # Test con archivo adjunto
    test_content = """
# System instruction

**Rol:** Actúa como Socio Senior de Bain & Company.

**Tu Objetivo:** Preparar a la compañía.

---

# Petición inicial de Activación

## OPCIÓN A: Escenario de Expansión

_Descripción del escenario A_

> **Contexto:** Expansión geográfica
> Detalles...

## OPCIÓN B: Escenario de Consolidación

_Descripción del escenario B_

> **Contexto:** Consolidación
> Detalles...
"""
    
    system = extract_system_prompt(test_content)
    scenarios = extract_scenarios(test_content)
    
    print("\n=== SYSTEM PROMPT ===")
    print(system[:200] if system else "No encontrado")
    
    print("\n=== ESCENARIOS ===")
    for key, value in scenarios.items():
        print(f"Opción {key}: {value['title']}")
