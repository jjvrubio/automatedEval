import os
import sys
import json
import logging
from pathlib import Path
from time import time
from ESBS_evaluacion_individual import (
    cargar_configuracion,
    rubrica_a_markdown,
    construir_prompt_desde_config,
    EvaluadorTFM,
    estimate_token_count,
    read_student_text,
    construir_tabla_evaluacion,
    extraer_puntuaciones_tabla_md,
    save_evaluation_result,
)

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


def evaluar_tfm_batch(input_folder, output_folder, base_path, api_key):
    instrucciones = (base_path / "Estructura TFM ESBS y detalles.md").read_text(
        encoding="utf-8"
    )
    rubrica_json = json.loads(
        (base_path / "rubrica_estructurada.json").read_text(encoding="utf-8")
    )
    config = cargar_configuracion(base_path / "configuracion_evaluacion.json")
    evaluador = EvaluadorTFM(api_key=api_key)
    rubrica_md = rubrica_a_markdown(rubrica_json)

    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    archivos = list(input_folder.glob("*.pdf")) + list(input_folder.glob("*.docx"))
    logger.info(f"Se encontraron {len(archivos)} archivos para evaluar.")

    for archivo in archivos:
        logger.info(f"Evaluando: {archivo.name}")
        try:
            texto_completo = read_student_text(str(archivo))
            token_count = estimate_token_count(texto_completo)
            bloques = {}
            if token_count <= evaluador.token_limit:
                bloques = {"TFM completo": texto_completo}
            else:
                tercio = len(texto_completo) // 3
                bloques = {
                    "Bloque 1": texto_completo[:tercio],
                    "Bloque 2": texto_completo[tercio : 2 * tercio],
                    "Bloque 3": texto_completo[2 * tercio :],
                }
            puntuaciones_bloques = []
            for nombre, texto in bloques.items():
                prompt = construir_prompt_desde_config(
                    instrucciones, rubrica_md, texto, config, rubrica_json
                )
                prompt += (
                    "\n\nPor favor, evalúa el texto anterior siguiendo la rúbrica y las normas indicadas. "
                    "Al final de tu respuesta, incluye una tabla Markdown con las puntuaciones numéricas de cada subcriterio en el formato exacto:"
                    "\n| Criterio | Subcriterio | Puntuación |\n|---|---|---|\n...\n"
                    "No uses texto, guiones ni celdas vacías en la columna de puntuación, solo números. Si no puedes puntuar un subcriterio, escribe 1. "
                    "La tabla debe estar al final de la respuesta, sin texto adicional después."
                )
                evaluacion = evaluador.evaluar(prompt)
                tabla_encontrada = None
                import re

                tabla_encontrada = re.search(
                    r"\| *Criterio *\| *Subcriterio *\| *Puntuaci[oó]n? *\|[\s\S]+?(\n\n|$)",
                    evaluacion,
                    re.IGNORECASE,
                )
                if not tabla_encontrada:
                    tabla_encontrada = re.search(
                        r"\|.*criterio.*\|.*subcriterio.*\|.*puntuaci[oó]n?.*\|[\s\S]+?(\n\n|$)",
                        evaluacion,
                        re.IGNORECASE,
                    )
                if tabla_encontrada:
                    puntuaciones_bloques.append(
                        extraer_puntuaciones_tabla_md(tabla_encontrada.group(0))
                    )
                else:
                    puntuaciones_bloques.append({})
            puntuaciones_finales = {}
            for bloque in puntuaciones_bloques:
                for (criterio, subcriterio), valor in bloque.items():
                    clave = (criterio, subcriterio)
                    if clave not in puntuaciones_finales:
                        puntuaciones_finales[clave] = valor
                    else:
                        puntuaciones_finales[clave] = min(
                            puntuaciones_finales[clave], valor
                        )
            tabla_md = construir_tabla_evaluacion(
                rubrica_json, {(k[1]): v for k, v in puntuaciones_finales.items()}
            )
            sintesis = "\n**Síntesis global:**\n\nEl trabajo ha sido evaluado siguiendo criterios ultra-estrictos. Consulta la tabla para ver los puntos fuertes y débiles.\n"
            preguntas = "\n**Preguntas para el autor:**\n1. ¿Cómo justificarías las áreas con menor puntuación?\n2. ¿Qué mejorarías en una futura versión del TFM?\n"
            nombre_base = os.path.splitext(archivo.name)[0]
            fecha = f"{time():.0f}"
            output_md = f"{nombre_base}_evaluacion_{fecha}.md"
            output_path = output_folder / output_md
            contenido_md = f"# Informe de evaluación TFM\n\n{tabla_md}\n\n{sintesis}\n{preguntas}\n"
            save_evaluation_result(contenido_md, str(output_path))
            logger.info(f"✅ Informe guardado: {output_path}")
        except Exception as e:
            logger.error(f"❌ Error evaluando {archivo.name}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python ESBS_evaluacion_batch.py <carpeta_entrada> <carpeta_salida>")
        sys.exit(1)
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    base_path = Path(__file__).parent / "esbs_grader"
    api_key = os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        print("❌ Falta la variable de entorno 'MI_CLAVE_API_OPENAI'")
        sys.exit(1)
    evaluar_tfm_batch(input_folder, output_folder, base_path, api_key)
