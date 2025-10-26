#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador TFM Refactorizado - Basado en configuración YAML
=========================================================

Versión simplificada que utiliza los archivos YAML de configuración
para eliminar código redundante y mejorar la mantenibilidad.

Cambios principales:
- Usa configuracion_sistema_tfm.yaml para rutas y configuración
- Usa TFM_Evaluator_Prompt.yaml para lógica de evaluación
- Usa plantillas_preguntas.yaml para generación de preguntas
- Eliminadas funciones redundantes
- Código modular y mantenible
"""
from __future__ import annotations

import os
import sys
import json
import logging
import yaml
import hashlib
import random
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

def cargar_configuracion() -> Dict[str, Any]:
    """
    Carga toda la configuración desde archivos YAML
    """
    base_path = Path(__file__).parent / ".." / ".." / "TFM_Evaluator_Prompt_Package"
    
    config_files = {
        "sistema": base_path / "configuracion_sistema_tfm.yaml",
        "evaluador": base_path / "TFM_Evaluator_Prompt.yaml", 
        "plantillas": base_path / "plantillas_preguntas.yaml",
        "analisis": base_path / "plantillas_analisis_critico.yaml"
    }
    
    config = {}
    for key, file_path in config_files.items():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                config[key] = yaml.safe_load(f)
        except Exception as e:
            print(f"Error cargando {file_path}: {e}")
            config[key] = {}
    
    return config

def configurar_logger(config: Dict[str, Any]) -> logging.Logger:
    """
    Configura logging usando la configuración YAML
    """
    logger = logging.getLogger("evaluador_tfm_refactorizado")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler()
        
        # File handler en la carpeta del evaluador
        log_dir = Path(__file__).parent / "logs"
        log_dir.mkdir(exist_ok=True)
        
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"evaluador_tfm_{timestamp}.log"
        file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        
        # Formato
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger

def seleccionar_archivo_tfm(logger: logging.Logger) -> Optional[str]:
    """
    Selección de archivo TFM usando NSOpenPanel
    """
    try:
        from AppKit import NSOpenPanel, NSModalResponseOK
    except ImportError:
        logger.error("AppKit no disponible. Solo funciona en macOS.")
        return None
    
    panel = NSOpenPanel.openPanel()
    panel.setAllowedFileTypes_(["pdf", "docx"])
    panel.setAllowsMultipleSelection_(False)
    panel.setMessage_("Selecciona el TFM a evaluar")
    
    # DEBUG: Logging detallado de selección
    logger.info("🔍 Iniciando selector de archivos NSOpenPanel...")
    
    if panel.runModal() == NSModalResponseOK:
        url = panel.URLs()[0]
        path = url.path()
        
        # DEBUG CRÍTICO: Verificar selección
        logger.info(f"🔍 ARCHIVO SELECCIONADO: {path}")
        logger.info(f"🔍 RUTA NORMALIZADA: {os.path.abspath(path)}")
        logger.info(f"🔍 EXISTE: {os.path.exists(path)}")
        logger.info(f"🔍 TAMAÑO: {os.path.getsize(path) if os.path.exists(path) else 'NO EXISTE'} bytes")
        
        return path
    
    return None

def leer_contenido_tfm(ruta: str, logger: logging.Logger) -> str:
    """
    Lee el contenido del TFM (PDF o DOCX) con debugging detallado
    """
    if not os.path.exists(ruta):
        logger.error(f"Archivo no existe: {ruta}")
        return ""
    
    # DEBUG CRÍTICO: Información del archivo antes de leer
    logger.info(f"🔍 LEYENDO ARCHIVO: {ruta}")
    logger.info(f"🔍 EXTENSIÓN: {Path(ruta).suffix.lower()}")
    logger.info(f"🔍 TAMAÑO ARCHIVO: {os.path.getsize(ruta)} bytes")
    
    contenido = ""
    
    try:
        if ruta.lower().endswith('.pdf'):
            import pdfplumber
            with pdfplumber.open(ruta) as pdf:
                logger.info(f"🔍 PÁGINAS PDF: {len(pdf.pages)}")
                for i, page in enumerate(pdf.pages, 1):
                    text = page.extract_text() or ""
                    if text.strip():
                        contenido += f"[P{i}] {text}\n"
        
        elif ruta.lower().endswith('.docx'):
            from docx import Document
            doc = Document(ruta)
            logger.info(f"🔍 PÁRRAFOS DOCX: {len(doc.paragraphs)}")
            for paragraph in doc.paragraphs:
                if paragraph.text.strip():
                    contenido += paragraph.text + "\n"
    
    except Exception as e:
        logger.error(f"Error leyendo {ruta}: {e}")
        return ""
    
    # DEBUG CRÍTICO: Verificación del contenido leído
    hash_contenido = hashlib.md5(contenido.encode('utf-8')).hexdigest()
    logger.info(f"🔍 HASH MD5 CONTENIDO: {hash_contenido}")
    logger.info(f"🔍 LONGITUD TEXTO: {len(contenido)} caracteres")
    logger.info(f"🔍 PRIMEROS 200 CHARS: {repr(contenido[:200])}")
    logger.info(f"🔍 ÚLTIMOS 200 CHARS: {repr(contenido[-200:])}")
    
    return contenido

def obtener_respuesta_openai(prompt: str, config: Dict[str, Any], logger: logging.Logger) -> str:
    """
    Obtiene respuesta de OpenAI usando configuración YAML
    """
    try:
        import openai
    except ImportError:
        logger.error("Librería 'openai' no encontrada")
        return ""
    
    # Configuración desde YAML
    openai_config = config.get("sistema", {}).get("openai_config", {})
    modelo = openai_config.get("modelo_por_defecto", "gpt-4o-mini")
    temperatura = openai_config.get("temperatura_por_defecto", 0.3)
    max_tokens = openai_config.get("max_tokens_evaluacion", 2000)
    
    # API Key desde variables de entorno
    api_key = None
    for var in openai_config.get("variables_api_key", ["OPENAI_API_KEY"]):
        api_key = os.getenv(var)
        if api_key:
            break
    
    if not api_key:
        logger.error("No se encontró API key de OpenAI")
        return ""
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        logger.info(f"🤖 Llamando OpenAI - Modelo: {modelo}, Temp: {temperatura}, Tokens: {max_tokens}")
        
        response = client.chat.completions.create(
            model=modelo,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperatura,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        logger.error(f"Error en OpenAI: {e}")
        return ""

def cargar_rubrica(etiquetas: List[str], config: Dict[str, Any], logger: logging.Logger) -> Optional[Any]:
    """
    Carga rúbrica basada en etiquetas Finder usando configuración YAML
    """
    rubricas = config.get("sistema", {}).get("rutas_sistema", {}).get("rubricas", {})
    
    # Buscar rúbrica por etiqueta
    for etiqueta in etiquetas:
        if etiqueta in rubricas:
            ruta_rubrica = rubricas[etiqueta]
            logger.info(f"Usando rúbrica {etiqueta}: {ruta_rubrica}")
            
            try:
                import pandas as pd
                return pd.read_excel(ruta_rubrica)
            except Exception as e:
                logger.error(f"Error cargando rúbrica {ruta_rubrica}: {e}")
                return None
    
    # Si no hay etiquetas, usar la primera disponible
    if rubricas:
        primera_rubrica = list(rubricas.values())[0]
        logger.info(f"Sin etiquetas, usando rúbrica por defecto: {primera_rubrica}")
        try:
            import pandas as pd
            return pd.read_excel(primera_rubrica)
        except Exception as e:
            logger.error(f"Error cargando rúbrica por defecto: {e}")
            return None
    
    return None

def evaluar_tfm_con_yaml(texto_tfm: str, rubrica_df: Any, config: Dict[str, Any], logger: logging.Logger) -> List[Dict[str, Any]]:
    """
    Evalúa TFM usando configuración YAML
    """
    if rubrica_df is None or texto_tfm.strip() == "":
        return []
    
    resultados = []
    
    # Obtener criterios de la rúbrica
    try:
        for _, row in rubrica_df.iterrows():
            criterio = str(row.iloc[0]).strip()
            if not criterio or criterio.lower() in ['nan', 'none', '']:
                continue
            
            # Construir prompt usando configuración del evaluador
            evaluador_config = config.get("evaluador", {})
            principios = evaluador_config.get("principles", {})
            
            prompt = f"""
Rol: {evaluador_config.get('role', 'Academic Evaluator')}
Contexto: {evaluador_config.get('context', 'Evalúa TFM con rigor académico')}

Criterio a evaluar: {criterio}

Principios de evaluación:
- Nivel 4: {principios.get('Level_4', 'Solo si es perfecto')}
- Nivel 3: {principios.get('Level_3', 'Buen trabajo con fallas menores')}
- Tono: {principios.get('Tone', 'Estricto y crítico')}

Texto del TFM (primeros 5000 caracteres):
{texto_tfm[:5000]}

INSTRUCCIONES:
1. Evalúa el criterio "{criterio}" en el texto
2. Asigna nivel (1-4) basado en los principios
3. Justifica la decisión con evidencias específicas
4. Proporciona áreas de mejora concretas

Responde SOLO en formato JSON:
{{
    "criterio": "{criterio}",
    "nivel": [1-4],
    "justificacion": "explicación detallada con evidencias",
    "areas_mejora": ["mejora 1", "mejora 2", "mejora 3"],
    "evidencias": ["evidencia 1", "evidencia 2"]
}}
"""
            
            respuesta = obtener_respuesta_openai(prompt, config, logger)
            
            if respuesta:
                try:
                    # Limpiar respuesta para JSON válido
                    respuesta_limpia = respuesta.strip()
                    if respuesta_limpia.startswith('```json'):
                        respuesta_limpia = respuesta_limpia[7:-3]
                    elif respuesta_limpia.startswith('```'):
                        respuesta_limpia = respuesta_limpia[3:-3]
                    
                    resultado = json.loads(respuesta_limpia)
                    resultados.append(resultado)
                    logger.info(f"✅ Evaluado: {criterio} -> Nivel {resultado.get('nivel', 'N/A')}")
                    
                except json.JSONDecodeError as e:
                    logger.error(f"Error JSON para {criterio}: {e}")
                    logger.error(f"Respuesta: {respuesta}")
                    
                    # Fallback: crear resultado básico
                    resultados.append({
                        "criterio": criterio,
                        "nivel": 2,
                        "justificacion": "Error al procesar respuesta de IA",
                        "areas_mejora": ["Revisar criterio manualmente"],
                        "evidencias": ["Error de procesamiento"]
                    })
            
            # Pausa breve entre llamadas
            time.sleep(0.5)
    
    except Exception as e:
        logger.error(f"Error evaluando TFM: {e}")
    
    return resultados

def exportar_resultados_yaml(resultados: List[Dict[str, Any]], config: Dict[str, Any], logger: logging.Logger) -> None:
    """
    Exporta resultados usando configuración YAML
    """
    # Crear carpeta de resultados
    resultados_dir = Path(__file__).parent / "resultados"
    resultados_dir.mkdir(exist_ok=True)
    
    # Timestamp para archivos únicos
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Exportar CSV
    try:
        import pandas as pd
        csv_path = resultados_dir / f"evaluacion_tfm_{timestamp}.csv"
        pd.DataFrame(resultados).to_csv(csv_path, index=False, encoding='utf-8')
        logger.info(f"✅ CSV exportado: {csv_path}")
    except Exception as e:
        logger.error(f"Error exportando CSV: {e}")
    
    # Exportar JSON
    try:
        json_path = resultados_dir / f"evaluacion_tfm_{timestamp}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ JSON exportado: {json_path}")
    except Exception as e:
        logger.error(f"Error exportando JSON: {e}")

def main() -> int:
    """
    Función principal simplificada
    """
    print("🔄 Evaluador TFM Refactorizado - Iniciando...")
    
    # Reset de variables globales para evitar caché
    import importlib
    if 'pdfplumber' in sys.modules:
        importlib.reload(sys.modules['pdfplumber'])
    if 'docx' in sys.modules:
        importlib.reload(sys.modules['docx'])
    
    # Semilla aleatoria para variabilidad
    seed = int(time.time() * 1000000) % 999999
    random.seed(seed)
    print(f"🎲 Semilla de evaluación: {seed}")
    
    # 1. Cargar configuración YAML
    config = cargar_configuracion()
    logger = configurar_logger(config)
    
    logger.info("=== INICIANDO EVALUACIÓN TFM ===")
    logger.info(f"Semilla: {seed}")
    
    # 2. Seleccionar archivo TFM
    ruta_tfm = seleccionar_archivo_tfm(logger)
    if not ruta_tfm:
        logger.error("No se seleccionó archivo TFM")
        return 1
    
    # 3. Leer contenido TFM
    texto_tfm = leer_contenido_tfm(ruta_tfm, logger)
    if not texto_tfm.strip():
        logger.error("Contenido TFM vacío")
        return 1
    
    # 4. Cargar rúbrica (simplificado - sin etiquetas por ahora)
    rubrica_df = cargar_rubrica([], config, logger)
    if rubrica_df is None:
        logger.error("No se pudo cargar rúbrica")
        return 1
    
    # 5. Evaluar TFM
    logger.info("🔄 Iniciando evaluación...")
    resultados = evaluar_tfm_con_yaml(texto_tfm, rubrica_df, config, logger)
    
    if not resultados:
        logger.error("No se generaron resultados")
        return 1
    
    # 6. Exportar resultados
    exportar_resultados_yaml(resultados, config, logger)
    
    logger.info("✅ Evaluación completada exitosamente")
    print("✅ Evaluación completada. Revisa la carpeta 'resultados' y 'logs'.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())