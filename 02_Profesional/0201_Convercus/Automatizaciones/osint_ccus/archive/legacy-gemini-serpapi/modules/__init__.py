"""
Paquete de módulos para el Sistema Analista Fantasma.

Arquitectura:
- hunter: Búsqueda de fuentes (SerpAPI)
- collector: Extracción de contenido (HTML + PDF)
- brain: Análisis con Gemini 1.5 Pro
- reporter: Generación de informes estructurados
- macos_dialogs: Diálogos nativos de macOS (AppKit/Cocoa)
- prompt_parser: Parser para system prompt y escenarios desde Markdown
"""

__version__ = "1.0.0"
__author__ = "Sistema Automatizado"

from .hunter import Hunter
from .collector import Collector
from .brain import Brain
from .reporter import Reporter
from .macos_dialogs import MacOSDialogs, request_empresa_escenario, request_scenario_option
from .prompt_parser import load_gems_instruction, extract_system_prompt, extract_scenarios

__all__ = [
    "Hunter", 
    "Collector", 
    "Brain", 
    "Reporter",
    "MacOSDialogs",
    "request_empresa_escenario",
    "request_scenario_option",
    "load_gems_instruction",
    "extract_system_prompt",
    "extract_scenarios"
]
