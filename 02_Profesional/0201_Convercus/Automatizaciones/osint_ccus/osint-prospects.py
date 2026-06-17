#!/usr/bin/env python3
"""
ANALISTA FANTASMA - Pipeline RAG Completo
Sistema automatizado de OSINT con análisis multi-fase usando Gemini 1.5 Pro.

Arquitectura:
1. El Cazador (Hunter)   → Búsqueda de fuentes con SerpAPI
2. El Recolector (Collector) → Scraping y extracción (HTML + PDF)
3. El Cerebro (Brain)     → Análisis secuencial con Gemini
4. El Reportero (Reporter)   → Generación de informes estructurados

Autor: Sistema automatizado
Fecha: 2026-01-11
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import argparse

# Importar módulos del sistema
from modules.hunter import Hunter
from modules.collector import Collector
from modules.brain import Brain
from modules.reporter import Reporter
from modules.macos_dialogs import (
    request_empresa_escenario, 
    request_scenario_option,
    MacOSDialogs
)
from modules.prompt_parser import load_gems_instruction


# --- CONFIGURACIÓN ---

class Config:
    """Configuración centralizada del sistema."""
    
    def __init__(self):
        load_dotenv()
        
        # APIs
        self.serp_key = os.getenv("MI_CLAVE_API_SERPAPI")
        self.gemini_key = os.getenv("MI_CLAVE_API_GEMINI")
        
        # Directorios
        self.base_dir = Path(__file__).parent
        self.prompts_dir = self.base_dir / "prompts"
        self.output_dir = self.base_dir / "reports"
        
        # Ruta al archivo de instrucciones Gems (OneDrive)
        self.gems_instruction_path = Path(
            "/Users/juanjo/Library/CloudStorage/"
            "OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/"
            "The Octavius/Convercus/Prompts/"
            "Instrucción para Gems.md"
        )
        
        # Parámetros de búsqueda
        self.max_sources = 5
        self.scrape_delay = 0.5
        
        # Validar configuración
        self._validate()
    
    def _validate(self):
        """Valida que la configuración esté completa."""
        missing = []
        
        if not self.serp_key:
            missing.append("MI_CLAVE_API_SERPAPI")
        if not self.gemini_key:
            missing.append("MI_CLAVE_API_GEMINI")
        
        if missing:
            print("❌ ERROR: Faltan variables de entorno en .env:")
            for var in missing:
                print(f"   - {var}")
            sys.exit(1)
        
        if not self.prompts_dir.exists():
            print(f"❌ ERROR: Directorio de prompts no encontrado: {self.prompts_dir}")
            sys.exit(1)
        
        # Verificar si existe el archivo de Gems
        if not self.gems_instruction_path.exists():
            print(f"⚠️  AVISO: Archivo de Gems no encontrado: {self.gems_instruction_path}")
            print(f"   Se usarán prompts predeterminados.")


# --- PIPELINE PRINCIPAL ---

class FantasmaAnalyst:
    """Orquestador del pipeline de análisis OSINT."""
    
    def __init__(self, config: Config):
        self.config = config
        
        # Inicializar módulos
        print("🚀 Inicializando Sistema Analista Fantasma...")
        self.hunter = Hunter(config.serp_key)
        self.collector = Collector()
        self.brain = Brain(config.gemini_key, temperature=0.1)
        self.reporter = Reporter(config.output_dir)
        
        print("✅ Todos los módulos cargados\n")
    
    def run_analysis(
        self,
        empresa: str,
        escenario: str,
        keywords: list[str] = None,
        scenario_context: str = None
    ) -> Path:
        """
        Ejecuta el pipeline completo de análisis.
        
        Args:
            empresa: Nombre de la empresa target
            escenario: Escenario de análisis (ej: "Due Diligence", "Expansión")
            keywords: Palabras clave adicionales para búsqueda
            scenario_context: Contexto del escenario seleccionado (OPCIÓN A/B/C/D)
        
        Returns:
            Path al reporte generado
        """
        start_time = time.time()
        
        print(f"\n{'='*70}")
        print(f"🎯 TARGET: {empresa}")
        print(f"📋 ESCENARIO: {escenario}")
        print(f"{'='*70}\n")
        
        # --- FASE 1: BÚSQUEDA ---
        print("🕵️  FASE 1: Búsqueda de Fuentes\n")
        
        if keywords is None:
            keywords = [
                "facturación ebitda",
                "estrategia digital transformación",
                "liderazgo equipo directivo",
                "operaciones logística"
            ]
        
        queries = self.hunter.build_search_queries(
            empresa=empresa,
            keywords=keywords,
            year="2024 2025"
        )
        
        urls = self.hunter.search_multi_query(
            queries=queries,
            max_per_query=self.config.max_sources // len(queries) + 1
        )
        
        if not urls:
            print("❌ No se encontraron fuentes. Abortando análisis.")
            return None
        
        print(f"\n✅ {len(urls)} fuentes identificadas\n")
        
        # --- FASE 2: RECOLECCIÓN ---
        print("📥 FASE 2: Extracción de Contenido\n")
        
        results = self.collector.collect_batch(
            urls=urls[:self.config.max_sources],
            delay=self.config.scrape_delay
        )
        
        # Construir contexto consolidado
        context = self._build_context(results)
        
        # Agregar contexto del escenario si existe
        if scenario_context:
            context = f"--- CONTEXTO ESTRATÉGICO ---\n{scenario_context}\n\n{context}"
        
        if not context.strip():
            print("❌ No se pudo extraer contenido válido. Abortando.")
            return None
        
        print(f"\n✅ Contexto generado: {len(context)} caracteres\n")
        
        # --- FASE 3: ANÁLISIS MULTI-FASE ---
        print("🧠 FASE 3: Análisis Secuencial con Gemini 1.5 Pro\n")
        
        # Cargar prompts secuenciales
        prompts = self.brain.load_prompts_sequence(self.config.prompts_dir)
        print(f"📄 {len(prompts)} prompts cargados\n")
        
        # Variables compartidas entre fases
        variables = {
            "empresa": empresa,
            "escenario": escenario,
            "fecha": datetime.now().strftime("%Y-%m-%d")
        }
        
        # Ejecutar análisis secuencial
        responses = self.brain.sequential_analysis(
            context=context,
            prompts=prompts,
            variables=variables
        )
        
        print(f"\n✅ Análisis completado en {len(responses)} fases\n")
        
        # --- FASE 4: GENERACIÓN DE REPORTE ---
        print("📝 FASE 4: Generación de Reporte\n")
        
        # El último prompt (05_report.md) ya genera el formato final
        final_report = responses[-1]
        
        metadata = {
            "empresa": empresa,
            "escenario": escenario,
            "analista": "Sistema OSINT Automático",
            "fuentes_analizadas": len(results),
            "tiempo_procesamiento": f"{round(time.time() - start_time, 2)}s"
        }
        
        report_path = self.reporter.generate_markdown(
            content=final_report,
            metadata=metadata
        )
        
        # Preview en consola
        self.reporter.print_summary(final_report, max_lines=20)
        
        # --- RESUMEN FINAL ---
        print(f"\n{'='*70}")
        print(f"✅ ANÁLISIS COMPLETADO")
        print(f"{'='*70}")
        print(f"📊 Fuentes procesadas: {len(results)}")
        print(f"⏱️  Tiempo total: {round(time.time() - start_time, 2)}s")
        print(f"📄 Reporte: {report_path}")
        print(f"{'='*70}\n")
        
        return report_path
    
    def _build_context(self, results: list[dict]) -> str:
        """Construye contexto consolidado desde resultados de scraping."""
        context_parts = []
        
        for i, result in enumerate(results, 1):
            if result["status"] == "success" and result["content"]:
                context_parts.append(
                    f"--- FUENTE {i}: {result['url']} ---\n"
                    f"{result['content']}\n"
                )
        
        return "\n".join(context_parts)


# --- ENTRY POINT ---

def main():
    """Función principal con diálogo nativo de macOS."""
    
    # Cargar configuración
    config = Config()

    # Parsear argumentos para modo no interactivo / CLI
    parser = argparse.ArgumentParser(description="Analista Fantasma - OSINT CLI")
    parser.add_argument("--empresa", type=str, help="Nombre de la empresa (modo no interactivo)")
    parser.add_argument("--contexto", type=str, help="Contexto o escenario (modo no interactivo)")
    parser.add_argument("--yes", action="store_true", help="Confirmar automáticamente sin GUI")
    args = parser.parse_args()
    
    # --- FASE 0: CARGAR SYSTEM PROMPT Y ESCENARIOS ---
    print("📚 Cargando system prompt y escenarios desde Gems...\n")
    
    system_prompt_custom = None
    scenarios_dict = {}
    
    if config.gems_instruction_path.exists():
        system_prompt_custom, scenarios_dict = load_gems_instruction(
            config.gems_instruction_path
        )
        
        if system_prompt_custom:
            # Actualizar 01_system.md con el prompt de Gems
            system_file = config.prompts_dir / "01_system.md"
            system_file.write_text(
                f"---\nfase: system\ntipo: contexto_global\n---\n\n{system_prompt_custom}",
                encoding='utf-8'
            )
            print(f"✅ System prompt actualizado en {system_file.name}\n")
    else:
        print("⚠️  Usando prompts predeterminados (Gems no disponible)\n")
    
    # --- FASE 1: SELECCIONAR ESCENARIO ---
    selected_scenario_content = None
    scenario_title = ""

    if scenarios_dict:
        print("💬 Seleccionando escenario estratégico...\n")
        # Si se pasan args desde CLI, evitamos el diálogo GUI
        if args.empresa:
            # si se recibe contexto en args, usarlo como escenario_title
            scenario_title = args.contexto if args.contexto else "Escenario CLI"
            selected_scenario_content = None
            print(f"✅ Modo CLI: Escenario usado: {scenario_title}\n")
        else:
            scenario_result = request_scenario_option(scenarios_dict)
            if scenario_result is None:
                print("❌ Operación cancelada por el usuario.")
                sys.exit(0)

            scenario_key, scenario_title, scenario_content = scenario_result
            selected_scenario_content = scenario_content

            print(f"✅ Escenario seleccionado: OPCIÓN {scenario_key} - {scenario_title}\n")
    
    # --- FASE 2: SOLICITAR EMPRESA Y CONTEXTO ---
    print("💬 Abriendo diálogo de configuración...\n")

    if args.empresa:
        target_empresa = args.empresa
        contexto_adicional = args.contexto if args.contexto else ""
        print("✅ Modo CLI: datos recibidos desde argumentos\n")
    else:
        result = request_empresa_escenario()
        if result is None:
            print("❌ Operación cancelada por el usuario.")
            sys.exit(0)
        target_empresa, contexto_adicional = result
    
    # Construir escenario completo combinando selección + contexto adicional
    if selected_scenario_content:
        escenario_completo = f"{scenario_title}"
        if contexto_adicional:
            escenario_completo += f" - {contexto_adicional}"
    else:
        escenario_completo = contexto_adicional if contexto_adicional else "Análisis General"
    
    print(f"✅ Configuración recibida:")
    print(f"   Empresa: {target_empresa}")
    print(f"   Escenario: {escenario_completo}\n")
    
    # --- FASE 3: CONFIRMACIÓN ---
    confirmar = MacOSDialogs.confirm(
        title="Confirmar Análisis",
        message=f"¿Iniciar análisis OSINT de '{target_empresa}'?\n\nEscenario: {escenario_completo}\n\nEsto consumirá créditos de API.",
        button_yes="Iniciar",
        button_no="Cancelar"
    )
    
    if not confirmar:
        print("❌ Análisis cancelado por el usuario.")
        sys.exit(0)
    
    # --- FASE 4: INICIALIZAR Y EJECUTAR ---
    analyst = FantasmaAnalyst(config)
    
    # Si hay escenario seleccionado, agregarlo como contexto inicial
    if selected_scenario_content:
        print(f"📋 Agregando contexto de escenario al análisis...\n")
    
    report_path = analyst.run_analysis(
        empresa=target_empresa,
        escenario=escenario_completo,
        scenario_context=selected_scenario_content
    )
    
    # --- FASE 5: FINALIZACIÓN ---
    if report_path:
        print(f"🎉 Análisis exitoso. Revisa: {report_path}")
        
        MacOSDialogs.show_info(
            title="Análisis Completado",
            message=f"El reporte ha sido generado exitosamente:\n\n{report_path.name}\n\nRevisa el archivo en la carpeta reports/",
            button_text="Entendido"
        )
    else:
        print("❌ El análisis no pudo completarse.")
        MacOSDialogs.show_info(
            title="Error de Análisis",
            message="No se pudo completar el análisis. Revisa los logs en la terminal.",
            button_text="OK"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
