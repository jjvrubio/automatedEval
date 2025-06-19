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
        self.token_limit = 128000  # Updated context window for GPT-4o

    def count_tokens(self, *args) -> int:
        return sum(len(t.split()) for t in args if t)

    def evaluar(self, prompt: str):
        input_tokens = self.count_tokens(prompt)
        max_output = 4000
        if input_tokens + max_output > self.token_limit:
            raise ValueError("Superado el límite de tokens")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": (
                "Eres un evaluador académico ultra-estricto. Debes penalizar cualquier superficialidad, falta de método, justificación genérica o ausencia de aplicación real. "
                "No asignes un 5 salvo que se cumplan absolutamente todos los requisitos, con justificación literal, exhaustiva y alineada con los ejemplos positivos. "
                "Si hay la más mínima duda, la puntuación debe ser menor. "
                "Si la justificación es parcial, superficial, genérica o no se citan todos los elementos requeridos, la puntuación máxima permitida es 3. "
                "Si la justificación se parece a los ejemplos negativos, la puntuación debe ser menor. "
                "Si no se identifica, justifica y aplica explícitamente un método o técnica, la puntuación máxima no puede asignarse bajo ningún concepto."
            )},
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
    normas_globales = "\n".join(f"- {n}" for n in config.get("normas", []))
    ejemplos_globales = "\n".join(f"- {e}" for e in config.get("ejemplos", []))
    criterios_cfg = config.get("criterios", {})
    instrucciones_por_seccion = config.get("instrucciones_por_seccion", [])
    instrucciones_por_capitulo = config.get("instrucciones_por_capitulo", {})
    claves_puntuacion = config.get("claves_puntuacion", {})
    instrucciones_seccion_str = "\n".join(f"- {line}" for line in instrucciones_por_seccion)
    # Añade normas, ejemplos y claves de puntuación específicos por criterio y subcriterio
    normas_por_criterio = ""
    for criterio, datos in rubrica_json.items():
        normas = criterios_cfg.get(criterio, {}).get("normas", [])
        ejemplos = criterios_cfg.get(criterio, {}).get("ejemplos", [])
        if normas or ejemplos:
            normas_por_criterio += f"\n#### {criterio}\n"
            if normas:
                normas_por_criterio += "Normas específicas:\n" + "\n".join(f"- {n}" for n in normas) + "\n"
            if ejemplos:
                normas_por_criterio += "Ejemplos específicos:\n" + "\n".join(f"- {e}" for e in ejemplos) + "\n"
        # Añade claves de puntuación y ejemplos por subcriterio
        for item in datos.get("items", []):
            detalle = item.get("detalle")
            claves = claves_puntuacion.get(detalle, [])
            if claves:
                normas_por_criterio += f"Claves y ejemplos para '{detalle}':\n" + "\n".join(f"- {c}" for c in claves) + "\n"
    # Extraer secciones del .md (instrucciones)
    secciones = re.findall(r"^\d+\.\s+([A-Za-z &]+)|^#\s+([A-Za-z &]+)", instrucciones, re.MULTILINE)
    secciones = [s[0] or s[1] for s in secciones if s[0] or s[1]]
    instrucciones_secciones = ""
    for seccion in secciones:
        instrucciones_cap = instrucciones_por_capitulo.get(seccion, [])
        if instrucciones_cap:
            instrucciones_cap_str = "\n".join(f"- {line}" for line in instrucciones_cap)
            instrucciones_secciones += f"\n### Evalúa la sección '{seccion}'\n{instrucciones_cap_str}\n"
        else:
            instrucciones_secciones += f"\n### Evalúa la sección '{seccion}'\n{instrucciones_seccion_str}\n"
    return (
        f"{instrucciones}\n\n"
        f"### Rúbrica de evaluación estructurada:\n{rubrica_md}\n\n"
        f"### Texto del estudiante a evaluar:\n{texto_estudiante}\n\n"
        f"{titulo}\n{normas_globales}\n\n"
        f"EJEMPLOS DE RAZONAMIENTO PASO A PASO:\n{ejemplos_globales}\n\n"
        f"NORMAS, EJEMPLOS Y CLAVES DE PUNTUACIÓN POR CRITERIO Y SUBCRITERIO:\n{normas_por_criterio}\n\n"
        f"INSTRUCCIONES ESPECÍFICAS POR SECCIÓN:\n{instrucciones_secciones}\n\n"
        f"IMPORTANTE: Evalúa el TFM EXCLUSIVAMENTE según los criterios y subcriterios de la rúbrica proporcionada, aunque la estructura del documento del alumno sea diferente. "
        f"Para cada subcriterio de la rúbrica, busca el contenido más asimilable o equivalente en el TFM, aunque esté en otro capítulo o con otro nombre. "
        f"La tabla de puntuaciones debe seguir exactamente la rúbrica, en el mismo orden y con los mismos nombres de criterio y subcriterio. "
        f"Si no encuentras un apartado asimilable, puntúa bajo y justifícalo."
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
            valor = resultados.get(detalle)
            if valor is None or valor == "-":
                valor = 1
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
                valor = partes[2].replace(',', '.').strip()
                # Si la celda está vacía o es un guion, asigna 1
                if valor == '' or valor == '-' or valor == '--':
                    valor = '1'
                else:
                    valor = valor.replace('-', '')
                try:
                    resultados[(partes[0], partes[1])] = float(valor)
                except ValueError:
                    resultados[(partes[0], partes[1])] = 1.0
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
    # Cambia aquí para usar el JSON minimalista
    config = cargar_configuracion(base_path / "configuracion_evaluacion.json")

    evaluador = EvaluadorTFM(api_key=api_key)
    rubrica_md = rubrica_a_markdown(rubrica_json)

    # Leer texto del PDF según discriminante de tokens (ventana de contexto)
    with open(student_file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        textos_paginas = [p.extract_text() or "" for p in reader.pages]
        texto_completo = "".join(textos_paginas)
        token_count = estimate_token_count(texto_completo)
        if token_count <= evaluador.token_limit:
            bloques = {f"TFM completo (1-{len(reader.pages)} páginas)": texto_completo}
        else:
            # Si excede el límite, divide en tercios de páginas como fallback
            total = len(reader.pages)
            tercios = [total // 3 + (1 if i < total % 3 else 0) for i in range(3)]
            bloques, start = {}, 0
            for i, n in enumerate(tercios):
                texto = "".join(textos_paginas[start:start + n])
                bloques[f"Bloque {i+1} (páginas {start+1}-{start+n})"] = texto
                start += n

    evaluaciones = {}
    puntuaciones_bloques = []
    for nombre, texto in bloques.items():
        print(f"\nEvaluando: {nombre}")
        prompt = construir_prompt_desde_config(instrucciones, rubrica_md, texto, config, rubrica_json)
        prompt += ("\n\nPor favor, evalúa el texto anterior siguiendo la rúbrica y las normas indicadas. "
            "Al final de tu respuesta, incluye una tabla Markdown con las puntuaciones numéricas de cada subcriterio en el formato exacto:"
            "\n| Criterio | Subcriterio | Puntuación |\n|---|---|---|\n...\n"
            "No uses texto, guiones ni celdas vacías en la columna de puntuación, solo números. Si no puedes puntuar un subcriterio, escribe 1. "
            "La tabla debe estar al final de la respuesta, sin texto adicional después.")
        evaluacion = evaluador.evaluar(prompt)
        print(f"[DEBUG] Respuesta completa del LLM para el bloque '{nombre}':\n{evaluacion}\n{'='*80}")
        # Busca la tabla real en el texto generado por la IA (más tolerante)
        tabla_encontrada = re.search(r"\| *Criterio *\| *Subcriterio *\| *Puntuaci[oó]n? *\|[\s\S]+?(\n\n|$)", evaluacion, re.IGNORECASE)
        if not tabla_encontrada:
            # Intenta detectar variantes del encabezado (por ejemplo, sin acento, con espacios, etc.)
            tabla_encontrada = re.search(r"\|.*criterio.*\|.*subcriterio.*\|.*puntuaci[oó]n?.*\|[\s\S]+?(\n\n|$)", evaluacion, re.IGNORECASE)
        if tabla_encontrada:
            print(f"[DEBUG] Tabla encontrada en bloque '{nombre}':\n{tabla_encontrada.group(0)}")
            puntuaciones_bloques.append(extraer_puntuaciones_tabla_md(tabla_encontrada.group(0)))
        else:
            print(f"[ADVERTENCIA] No se encontró tabla de puntuaciones en el bloque '{nombre}'.")
            puntuaciones_bloques.append({})
    # === AGREGACIÓN Y GUARDADO DEL INFORME FINAL ===
    # Fusionar puntuaciones de todos los bloques (si hay más de uno, tomar el mínimo por subcriterio para máxima severidad)
    puntuaciones_finales = {}
    for bloque in puntuaciones_bloques:
        for (criterio, subcriterio), valor in bloque.items():
            clave = (criterio, subcriterio)
            if clave not in puntuaciones_finales:
                puntuaciones_finales[clave] = valor
            else:
                puntuaciones_finales[clave] = min(puntuaciones_finales[clave], valor)

    # Construir tabla global de evaluación
    tabla_md = construir_tabla_evaluacion(rubrica_json, {(k[1]): v for k, v in puntuaciones_finales.items()})

    # Síntesis global y preguntas al autor (puedes mejorar el prompt si quieres que sea más detallado)
    sintesis = "\n**Síntesis global:**\n\nEl trabajo ha sido evaluado siguiendo criterios ultra-estrictos. Consulta la tabla para ver los puntos fuertes y débiles.\n"
    preguntas = "\n**Preguntas para el autor:**\n1. ¿Cómo justificarías las áreas con menor puntuación?\n2. ¿Qué mejorarías en una futura versión del TFM?\n"

    # Construir el contenido Markdown final
    nombre_pdf = os.path.splitext(os.path.basename(student_file))[0]
    fecha = f"{time():.0f}"
    output_md = f"{nombre_pdf}_evaluacion_{fecha}.md"
    output_path = str(Path(student_file).parent / output_md)
    contenido_md = f"# Informe de evaluación TFM\n\n{tabla_md}\n\n{sintesis}\n{preguntas}\n"
    save_evaluation_result(contenido_md, output_path)
    print(f"\n✅ Informe de evaluación guardado en: {output_path}\n")

# === EJECUCIÓN ===
if __name__ == "__main__":
    main()
