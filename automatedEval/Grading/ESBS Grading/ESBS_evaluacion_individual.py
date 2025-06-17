import os
import sys
import json
import logging
import re
from time import time
from pathlib import Path
import docx
import PyPDF2
import openai
import tiktoken
from typing import Literal
from AppKit import NSOpenPanel, NSApplication

# === CONFIGURACIÓN LOGGING ===
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# === TOKENIZACIÓN - contar los tokens para adoptar la estrategia de entrega al LLM===
def get_token_encoder(model: str = "gpt-4o"):
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        return tiktoken.get_encoding("cl100k_base")

def estimate_token_count(text: str, model: str = "gpt-4o") -> int:
    return len(get_token_encoder(model).encode(text))

# === RATE LIMITER ===
class TokenRateLimiter:
    def __init__(self, max_tokens_per_minute=30000):
        self.max_tokens_per_minute = max_tokens_per_minute
        self.token_window = []

    def wait_if_needed(self, token_count: int):
        now = time()
        self.token_window = [t for t in self.token_window if now - t[0] < 60]
        total = sum(t[1] for t in self.token_window)
        if total + token_count > self.max_tokens_per_minute:
            logger.warning("❌ Límite de tokens por minuto superado.")
            sys.exit(1)
        self.token_window.append((now, token_count))

# === UTILIDADES I/O Y EXTRACCIÓN ===
def read_pdf_text(file_path: str) -> str:
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return "\n".join(p.extract_text() or "" for p in reader.pages)

def dividir_tfm_en_bloques_por_paginas(file_path: str) -> dict:
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        total = len(reader.pages)
        if total < 40:
            texto = "".join(p.extract_text() or "" for p in reader.pages)
            return {f"TFM completo (1-{total} páginas)": texto}
        tercios = [total // 3 + (1 if i < total % 3 else 0) for i in range(3)]
        bloques, start = {}, 0
        for i, n in enumerate(tercios):
            texto = "".join(reader.pages[p].extract_text() or "" for p in range(start, start + n))
            bloques[f"Bloque {i+1} (páginas {start+1}-{start+n})"] = texto
            start += n
        return bloques

def save_evaluation_result(content: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def select_student_file() -> str:
    NSApplication.sharedApplication()
    panel = NSOpenPanel.alloc().init()
    panel.setTitle_("Selecciona el archivo PDF del estudiante")
    panel.setCanChooseFiles_(True)
    panel.setAllowedFileTypes_(["pdf"])
    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None

# === EVALUADOR OPENAI ===
class EvaluadorTFM:
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = "gpt-4o"
        self.token_limit = 128000

    def count_tokens(self, *args) -> int:
        return sum(len(t.split()) for t in args if t)

    def evaluar(self, prompt: str):
        input_tokens = self.count_tokens(prompt)
        max_output = 4000
        if input_tokens + max_output > self.token_limit:
            raise ValueError("Superado el límite de tokens")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": "Eres un corrector académico riguroso."},
                      {"role": "user", "content": prompt}],
            max_tokens=max_output,
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()

# === PROMPT ===
def cargar_configuracion(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def construir_prompt_desde_config(instrucciones: str, rubrica_md: str, texto_estudiante: str, config: dict, rubrica_json: dict) -> str:
    titulo = config.get("titulo", "Instrucciones")
    normas = "\n".join(f"- {n}" for n in config.get("normas", []))
    ejemplos = "\n".join(f"- {e}" for e in config.get("ejemplos", []))
    # Extraer secciones del .md (instrucciones)
    secciones = re.findall(r"^\d+\.\s+([A-Za-z &]+)|^#\s+([A-Za-z &]+)", instrucciones, re.MULTILINE)
    secciones = [s[0] or s[1] for s in secciones if s[0] or s[1]]
    # Para cada sección, pide evaluación guiada por subcriterios
    instrucciones_secciones = ""
    for seccion in secciones:
        instrucciones_secciones += (
            f"\n### Evalúa la sección '{seccion}'\n"
            f"- Usa los subcriterios de la rúbrica que correspondan a esta sección.\n"
            f"- Para cada subcriterio, indica la puntuación, la justificación literal y cita textual.\n"
            f"- Indica explícitamente qué norma(s) y ejemplo(s) del bloque de configuración aplicas.\n"
            f"- Si la sección es deficiente o falta, asigna la puntuación mínima y explica por qué, citando la norma correspondiente.\n"
            f"- No asignes puntuaciones altas si no puedes citar evidencia textual clara y completa para ese subcriterio.\n"
        )
    return (
        f"{instrucciones}\n\n"
        f"### Rúbrica de evaluación estructurada:\n{rubrica_md}\n\n"
        f"### Texto del estudiante a evaluar:\n{texto_estudiante}\n\n"
        f"{titulo}\n{normas}\n\n"
        f"EJEMPLOS DE RAZONAMIENTO PASO A PASO:\n{ejemplos}\n\n"
        f"INSTRUCCIONES ESPECÍFICAS POR SECCIÓN:\n{instrucciones_secciones}"
    )

def rubrica_a_markdown(rubrica: dict) -> str:
    md = ""
    for criterio, datos in rubrica.items():
        md += f"## {criterio.strip()}\n"
        for item in datos["items"]:
            md += f"- **{item['detalle']}** (Peso: {item.get('contribucion', 'N/A')})\n"
            escala = ', '.join(f"{k}: {v}" for k, v in item["escala"].items())
            md += f"  - Escala: {escala}\n"
    return md

def construir_tabla_evaluacion(rubrica, resultados):
    tabla = "| Criterio | Subcriterio | Puntuación |\n|---|---|---|\n"
    for criterio, datos in rubrica.items():
        for item in datos["items"]:
            detalle = item["detalle"]
            valor = resultados.get(detalle, "-")
            tabla += f"| {criterio.strip()} | {detalle} | {valor} |\n"
    return tabla

def extraer_puntuaciones_tabla_md(tabla_md):
    # Extrae las puntuaciones de una tabla Markdown generada por la IA
    # Devuelve un dict: {(criterio, subcriterio): puntuacion}
    resultados = {}
    for line in tabla_md.splitlines():
        if line.startswith('|') and not line.startswith('|---'):
            partes = [x.strip() for x in line.strip('|').split('|')]
            if len(partes) == 3:
                # Acepta números enteros, decimales, y guiones como vacío
                valor = partes[2].replace(',', '.').replace('-', '').strip()
                try:
                    if valor:
                        resultados[(partes[0], partes[1])] = float(valor)
                except ValueError:
                    continue
    return resultados

# === BLOQUE PRINCIPAL ===
def main():
    api_key = os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        print("❌ Falta la variable de entorno 'MI_CLAVE_API_OPENAI'")
        return

    student_file = select_student_file()
    if not student_file:
        print("❌ No se seleccionó ningún archivo")
        return

    base_path = Path("/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/Grading/ESBS Grading/esbs_grader")
    instrucciones = (base_path / "Estructura TFM ESBS y detalles.md").read_text(encoding="utf-8")
    rubrica_json = json.loads((base_path / "rubrica_estructurada.json").read_text(encoding="utf-8"))
    config = cargar_configuracion(base_path / "configuracion_evaluacion.json")

    evaluador = EvaluadorTFM(api_key=api_key)
    rubrica_md = rubrica_a_markdown(rubrica_json)

    # Leer texto del PDF según discriminante de 40 páginas
    with open(student_file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        total = len(reader.pages)
        if total < 40:
            bloques = {f"TFM completo (1-{total} páginas)": "".join(p.extract_text() or "" for p in reader.pages)}
        else:
            tercios = [total // 3 + (1 if i < total % 3 else 0) for i in range(3)]
            bloques, start = {}, 0
            for i, n in enumerate(tercios):
                texto = "".join(reader.pages[p].extract_text() or "" for p in range(start, start + n))
                bloques[f"Bloque {i+1} (páginas {start+1}-{start+n})"] = texto
                start += n

    evaluaciones = {}
    puntuaciones_bloques = []
    for nombre, texto in bloques.items():
        print(f"\nEvaluando: {nombre}")
        # Refuerza el prompt para exigir tabla Markdown clara
        prompt = construir_prompt_desde_config(instrucciones, rubrica_md, texto, config, rubrica_json)
        prompt += ("\n\nIMPORTANTE: Al final de tu respuesta, incluye SIEMPRE una tabla Markdown con las puntuaciones numéricas de cada subcriterio, en el formato:"
                  "\n| Criterio | Subcriterio | Puntuación |\n|---|---|---|\n...\n. No uses texto, guiones ni celdas vacías en la columna de puntuación, solo números.")
        evaluacion = evaluador.evaluar(prompt)
        resultados = {}  # Extraer después
        tabla = construir_tabla_evaluacion(rubrica_json, resultados)
        contenido = f"{evaluacion}\n\n## Tabla resumen de evaluación\n\n{tabla}"
        base_name = os.path.splitext(os.path.basename(student_file))[0]
        output_dir = os.path.dirname(student_file)
        out = os.path.join(output_dir, f"{base_name}_{nombre.replace(' ', '_').replace('(', '').replace(')', '')}.md")
        save_evaluation_result(contenido, out)
        evaluaciones[nombre] = contenido
        # Extrae puntuaciones de la tabla Markdown generada
        # Busca la tabla real en el texto generado por la IA
        tabla_encontrada = re.search(r"\| *Criterio *\| *Subcriterio *\| *Puntuaci[oó]n *\|[\s\S]+?\n\n", evaluacion)
        if tabla_encontrada:
            puntuaciones_bloques.append(extraer_puntuaciones_tabla_md(tabla_encontrada.group(0)))
        else:
            puntuaciones_bloques.append({})
        print(f"✅ Evaluación de '{nombre}' guardada en: {out}")

    # Calcula la tabla resumen global
    from collections import defaultdict
    suma = defaultdict(list)
    for bloque in puntuaciones_bloques:
        for clave, valor in bloque.items():
            suma[clave].append(valor)
    resumen_global = "| Criterio | Subcriterio | Media |\n|---|---|---|\n"
    for (criterio, subcriterio), valores in suma.items():
        media = round(sum(valores)/len(valores),2)
        resumen_global += f"| {criterio} | {subcriterio} | {media} |\n"

    # Síntesis global ultra-estricta
    print("\nGenerando síntesis global ultra-estricta...")
    resumenes = '\n\n'.join([f"{k}:\n{v[:2000]}..." for k,v in evaluaciones.items()])  # Limita cada bloque a 2000 chars para el prompt
    prompt_sintesis = (
        "A continuación tienes los informes de evaluación ultra-estricta de los bloques de un TFM. "
        "Elabora una síntesis global crítica e INTEGRADA, analizando la coherencia, congruencia y el flujo entre bloques. "
        "Detecta contradicciones, repeticiones o saltos argumentales entre partes. "
        "Integra las justificaciones y puntuaciones de cada bloque en una visión global, penalizando incoherencias. "
        "Emite recomendaciones finales. "
        "No repitas texto, razona sobre la integración y la calidad global del TFM.\n\n"
        f"{resumenes}"
    )
    sintesis = evaluador.evaluar(prompt_sintesis)
    out_sintesis = os.path.join(output_dir, f"{base_name}_sintesis_global.md")
    # Incluye la tabla resumen global al principio de la síntesis
    save_evaluation_result(f"## Tabla resumen global de puntuaciones\n\n{resumen_global}\n\n{sintesis}", out_sintesis)
    print(f"\n✅ Síntesis global guardada en: {out_sintesis}")

# === EJECUCIÓN ===
if __name__ == "__main__":
    main()
