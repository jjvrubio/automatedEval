# Sistema de Evaluación Automatizada de TFMs – Diseño de Despliegue y Orquestación

> **Objetivo**: Reutilizar el repositorio/proyecto existente (aunque esté vacío) para construir una **capa de ejecución** (CLI/servicio), una **capa de orquestación** (jobs programados y colas) y un **pipeline reproducible** que procese PDFs de TFM, aplique una **rúbrica JSON** e **instrucciones Markdown**, y genere **informes en PDF/Markdown** con plena **trazabilidad y auditabilidad académica**.

---

## 1. Arquitectura objetivo (capas y responsabilidades)

Para escalar sin comprometer la gobernanza académica, se proponen capas bien separadas:

1. **Dominio (core)**  
   - `evaluator/` con la lógica de evaluación: carga/validación de rúbrica (JSON), parsing de instrucciones (Markdown), extracción de texto e imágenes desde PDF (OCR cuando aplique), prompts y parámetros del modelo, cálculo de puntuaciones con ponderaciones, verificación de evidencias y generación de justificantes.  
   - Sin dependencias de interfaz (HTTP/CLI). Solo Python tipado (pydantic), utilidades puras y tests.

2. **Interfaces de ejecución**  
   - **CLI** (Typer/Click): comandos para *evaluar un TFM*, *evaluar un lote*, *validar rúbricas*, *generar informes*.  
   - **Servicio HTTP** (FastAPI): endpoints para subida de PDF, consulta de resultados y webhooks de finalización.  
   - (Opcional) **Worker de colas** (Celery/RQ) si se prevén picos de carga al cierre de convocatoria.

3. **Orquestación y automatización**  
   - **Makefile/Taskfile** para reproducibilidad local.  
   - **Docker** + `docker-compose.yml` para empaquetar dependencias (OCR, Poppler).  
   - **CI/CD (GitHub Actions)**: lint, tests, build, escaneo de seguridad, publicación de imágenes, y *cron* para lotes/QA.  
   - (Opcional) **Prefect/Airflow** para pipelines por cohortes con trazabilidad avanzada.

4. **Observabilidad y cumplimiento**  
   - Logging estructurado, trazas por expediente (ID de estudiante y hash de archivo).  
   - Validación de esquemas (JSON Schema/pydantic) para rúbricas y salidas.  
   - Cifrado en reposo de ficheros sensibles y **data minimization** (GDPR).

---

## 2. Estructura propuesta de proyecto (reutilizando el repo)

```
tfm-eval/
  pyproject.toml            # Poetry/uv/pip-tools; dependencias y entry points
  README.md
  LICENSE
  .env.example              # variables de entorno (API keys, rutas)
  .gitignore
  Makefile
  docker/
    Dockerfile              # imagen para CLI/servicio
    docker-compose.yml      # servicio + redis (si usas colas)
  configs/
    rubric.schema.json      # contrato de rúbrica (JSON Schema)
    rubric.example.json
    instructions.md         # instrucciones base del documento (plantilla)
    model.yaml              # proveedor LLM y parámetros
  data/
    inputs/
      sample/
        demo_tfm.pdf
    outputs/
      reports/              # PDF/MD generados
      traces/               # JSON con prompts, respuestas y hashes
      scores/               # CSV/JSON con puntuaciones agregadas
  evaluator/                # núcleo de dominio
    __init__.py
    rubric.py               # carga/validaciones de rúbrica
    extractor.py            # parsing PDF, OCR opcional
    prompts.py              # plantillas y parametrización
    scoring.py              # cálculo de notas con ponderaciones
    reporting/
      __init__.py
      jinja/
        report.md.j2        # plantilla de informe
      renderer.py           # MD -> PDF (Pandoc/WeasyPrint)
    pipeline.py             # run_evaluation(file, rubric, cfg)
  interfaces/
    cli.py                  # Typer CLI
    api.py                  # FastAPI (submit, status, download)
    workers.py              # Celery/RQ tasks (opcional)
  tests/
    test_rubric.py
    test_scoring.py
    test_pipeline.py
  .github/
    workflows/
      ci.yml                # lint+tests
      release.yml           # build/push docker image
      scheduled-batch.yml   # (opcional) ejecuciones programadas
```

Esta organización permite aislar el núcleo, intercambiar LLMs sin tocar el dominio y estandarizar entradas/salidas con reproducibilidad.

---

## 3. Gestión de configuración y secretos

- **Variables de entorno** (.env): `OPENAI_API_KEY` (u otro proveedor), `DATA_DIR`, `MODEL_NAME`, `TEMPERATURE`, etc.  
- **`configs/model.yaml`** (pydantic-settings): parámetros de inferencia por defecto y *overrides* por entorno.  
- **Secretos en CI**: `GitHub Encrypted Secrets`.  
- **Separación de datos**: PDFs y resultados en `data/` (fuera de la imagen Docker) para facilitar borrado/retención.

---

## 4. Contratos de datos (esquemas) para gobernanza

### 4.1 Rúbrica (JSON Schema)

`configs/rubric.schema.json` (esbozo):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "TFM Rubric",
  "type": "object",
  "required": ["version", "criteria", "weights"],
  "properties": {
    "version": { "type": "string" },
    "criteria": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "levels"],
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "levels": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["label", "descriptor", "score"],
              "properties": {
                "label": { "type": "string" },
                "descriptor": { "type": "string" },
                "score": { "type": "number" }
              }
            },
            "minItems": 2
          }
        }
      }
    },
    "weights": {
      "type": "object",
      "additionalProperties": { "type": "number" }
    },
    "thresholds": {
      "type": "object",
      "properties": {
        "pass": { "type": "number" },
        "distinction": { "type": "number" }
      }
    }
  }
}
```

### 4.2 Instrucciones (Markdown)

`configs/instructions.md` contendrá la **estructura esperada** (resumen, metodología, resultados, discusión, bibliografía APA 7), con *hints* que el evaluador usará para verificar presencia y calidad de secciones.

### 4.3 Salida de evaluación (JSON + artefactos)

Ejemplo por expediente:

```json
{
  "student_id": "ESBS-2025-00123",
  "file_hash": "sha256:...",
  "rubric_version": "1.2.0",
  "scores": [
    {"criterion_id": "method", "level": "Excelente", "score": 4.0, "weight": 0.25, "evidence_ref": ["p.12-15","fig.2"]}
  ],
  "total": 3.6,
  "decision": "Aprobado con mención",
  "explanations": {
    "method": "La sección describe ... con referencias recientes."
  },
  "trace": {
    "model": "gpt-4o-mini-2025-09",
    "temperature": 0.2,
    "prompt_hash": "sha256:...",
    "timestamp": "2025-09-27T17:05:13Z"
  }
}
```

El JSON se guarda en `data/outputs/traces/ESBS-2025-00123.json`. El informe legible se genera a partir de ahí.

---

## 5. Pipeline de extremo a extremo (E2E)

1. **Ingesta**: recepción de PDFs (*drop folder* o upload API).  
2. **Extracción**: texto + metadatos (título, autores, secciones, figuras). Para PDFs escaneados, OCR (Tesseract).  
3. **Evaluación**:  
   - Enriquecimiento con instrucciones y rúbrica.  
   - Llamadas al LLM por bloque/criterio, con *temperature* baja y *system prompts* que obligan a citar páginas/figuras (*evidence_ref*).  
4. **Scoring**: normalización, agregación ponderada y verificación de *thresholds*.  
5. **QC (controles de calidad)**: presencia de secciones clave; referencias localizables; consistencia entre evidencia y nota.  
6. **Reporting**: Jinja2 → Markdown → PDF (WeasyPrint o Pandoc) + anexos.  
7. **Publicación**: carpeta del expediente con informe, JSON de traza y CSV de cohortes.  
8. **Retención y cumplimiento**: políticas de borrado y *masking*.

---

## 6. CLI para operación reproducible

Ejemplo con **Typer**:

```python
# interfaces/cli.py
import typer
from evaluator.pipeline import run_evaluation
from evaluator.rubric import load_rubric
from evaluator.reporting.renderer import render_report

app = typer.Typer()

@app.command()
def evaluate(file: str, rubric_path: str = "configs/rubric.example.json", out_dir: str = "data/outputs"):
    rubric = load_rubric(rubric_path)
    result = run_evaluation(file, rubric)
    render_report(result, out_dir)

@app.command()
def batch(folder: str = "data/inputs", rubric_path: str = "configs/rubric.example.json"):
    # recorre PDFs y llama evaluate()
    ...

if __name__ == "__main__":
    app()
```

**Uso**:
- `python -m interfaces.cli evaluate data/inputs/sample/demo_tfm.pdf`
- `python -m interfaces.cli batch data/inputs/cohorte_2025/`

---

## 7. Servicio HTTP (opcional)

Con **FastAPI**:
- `POST /submit` → carga PDF (multipart), devuelve `job_id`.  
- `GET /status/{job_id}` → estado (pending/running/done/error).  
- `GET /report/{job_id}` → descarga informe PDF.  
- `POST /webhook` → notificación a LMS/terceros al finalizar.

Integra con el campus virtual o con un panel docente.

---

## 8. Orquestación (de lo simple a lo robusto)

**Nivel 1: Local reproducible**

- **Makefile** (fragmento):

```make
.PHONY: setup lint test run batch docker-build

setup:
\tuv sync  # o poetry install / pip-tools

lint:
\trufflehog filesystem --fail && ruff check .

test:
\tpytest -q

run:
\tpython -m interfaces.cli evaluate data/inputs/sample/demo_tfm.pdf

batch:
\tpython -m interfaces.cli batch data/inputs/cohorte_2025/

docker-build:
\tdocker build -f docker/Dockerfile -t tfm-eval:latest .
```

- `docker-compose.yml` (si usas colas Redis + worker):

```yaml
services:
  api:
    build: ../
    command: uvicorn interfaces.api:app --host 0.0.0.0 --port 8000
    env_file: ../.env
    volumes:
      - ../data:/app/data
    ports: ["8000:8000"]
  redis:
    image: redis:7
  worker:
    build: ../
    command: celery -A interfaces.workers worker -l info
    env_file: ../.env
    depends_on: [redis]
    volumes:
      - ../data:/app/data
```

**Nivel 2: CI/CD (GitHub Actions)**

- `ci.yml`: lint + tests + build de imagen en PR.  
- `release.yml`: en tag `v*`, *push* de imagen a GHCR y *attach* binarios (si empaquetas).  
- `scheduled-batch.yml`: *cron* para ejecutar lotes en runner self‑hosted o con artefactos de prueba.

CI mínimo:

```yaml
name: CI
on:
  pull_request:
  push:
    branches: [ main ]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -U pip && pip install -r requirements-dev.txt
      - run: ruff check .
      - run: pytest -q
```

**Nivel 3: Scheduler/Flow**

- Para campañas (convocatorias), **Prefect**: `Flow` con tareas `extract -> evaluate -> report -> publish`, agente en servidor docente, *retries*, *caching* y *observability*.

---

## 9. Observabilidad, calidad y auditoría

- **Logging estructurado** (`structlog`) con `student_id`, `file_hash`, `criterion_id`.  
- **Trazabilidad**: guardar prompts, respuestas y hashes (con *redaction* de datos personales).  
- **Testing**:  
  - **Unit**: `test_scoring.py` con rúbricas mínimas.  
  - **Golden files**: PDFs sintéticos con resultados esperados (tolerancias).  
  - **Contract tests**: validación contra `rubric.schema.json`.  
- **Revisión humana asistida**: interfaz que muestre *evidence_ref* como enlaces a páginas o recortes.

---

## 10. Seguridad y cumplimiento (GDPR/LOPDGDD)

- **Minimización**: usar `student_id` en lugar de nombres cuando sea posible.  
- **Cifrado en reposo**: LUKS/dm-crypt o S3 con SSE‑KMS; cifrado simétrico en JSON de traza si incluyen datos personales.  
- **Retención**: política por convocatoria (p. ej., 12 meses) con script de borrado verificable (`make purge`).  
- **Registro de actividades**: documentar finalidad, base jurídica docente, proveedor LLM como *encargado del tratamiento*, SCCs si aplica.  
- **Calidad de datos**: procedimientos de rectificación ante errores denunciados por estudiantes.

---

## 11. Generación de informes (profesional y trazable)

- **Plantilla Jinja2** (`report.md.j2`) con: portada (identificador, fecha, rúbrica vX.Y), resumen de calificación, desglose por criterio con *evidence_ref*, recomendaciones y *appendix* metodológico (temperatura, modelo, versión del pipeline).  
- **Render**:  
  - **Pandoc** (Markdown → PDF) con estilo LaTeX institucional.  
  - **WeasyPrint** (HTML/CSS → PDF) si se prefieren estilos CSS.  
- **Exportación dual**: Markdown (para Obsidian/Zotero) y PDF (para expediente).

---

## 12. Plan de adopción en tres oleadas (usando el repo actual)

**Oleada A (arranque)**  
- Estructura mínima, `pyproject.toml`, `Makefile`, `docker/Dockerfile`.  
- Portar el script actual a `evaluator/` (sin cambiar lógica).  
- CLI `evaluate` y `batch`.  
- `configs/rubric.schema.json` + tu rúbrica como `rubric.example.json`.  
- Primer reporte Markdown (sin PDF) y guardado de JSON de traza.

**Oleada B (consolidación)**  
- FastAPI básica (`POST /submit`, `GET /report`).  
- Render PDF (Pandoc/WeasyPrint) con plantilla estable.  
- GitHub Actions (lint + tests).  
- Script `make batch` para cohortes.  
- README de uso docente.

**Oleada C (escala y robustez)**  
- Colas (Celery/Redis) para picos.  
- Prefect/Airflow para *scheduling* por convocatoria.  
- Observabilidad reforzada (Prometheus/Grafana).  
- Endurecimiento de seguridad (escáner de secretos, SAST, políticas de retención).

---

## 13. Ejemplo de Dockerfile

```dockerfile
# docker/Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    pandoc poppler-utils tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --upgrade pip && pip install -e .

COPY . /app
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python","-m","interfaces.cli"]
```

Ejecución de ejemplo en contenedor:  
`docker run -v $(pwd)/data:/app/data tfm-eval:latest evaluate data/inputs/sample/demo_tfm.pdf`

---

## 14. Buenas prácticas para evaluación académica asistida por LLM

- **Temperature baja** (0.0–0.2) y *system prompt* que obligue a **no inventar referencias** y **citar páginas/figuras**.  
- **Estrategia por bloques**: un prompt por criterio (metodología, revisión bibliográfica, resultados, discusión, APA 7…).  
- **Determinismo operacional**: fijar `seed` si el proveedor lo permite; en su defecto, reintentos con variación acotada.  
- **Controles anti‑alucinación**: rechazar evidencias sin localización precisa; re‑pregunta con recorte del PDF (*grounded prompting*).  
- **Human‑in‑the‑loop**: interfaz de revisión con hipervínculos a *evidence_ref*.  
- **Transparencia metodológica** en el informe (alcance y límites; responsabilidad última del tribunal).

---

## 15. Entregables previstos

1. **Repo inicializado** con la estructura propuesta y *boilerplate* funcional.  
2. **CLI operativo** (`evaluate`/`batch`) con reportes Markdown y JSON de traza.  
3. **Plantilla de informe** Jinja + conversión a PDF.  
4. **CI básico** (lint + tests).  
5. **Imagen Docker** para despliegue homogéneo.  
6. (Opcional) **FastAPI** + `docker-compose` con Redis/worker.

---

## 16. Próximos pasos

1. Confirmar el **repositorio** a emplear (ya movido).  
2. Ubicar en `configs/` la **rúbrica** actual y las **instrucciones Markdown** (versionadas).  
3. Incorporar 2–3 **TFM PDF** de ejemplo (anonimizados si procede).  
4. Ejecutar la **Oleada A** para disponer de CLI + reportes base reproducibles.  
5. Tras la revisión, avanzar a **Oleada B** (API + PDF formal + CI) y definir el *playbook* para convocatoria.

---

## Referencias seleccionadas

- **UNESCO (2021)**. *Recommendation on the Ethics of Artificial Intelligence*.  
- **Jisc (2023)**. *AI in assessment: ethics and academic integrity guidance*.  
- **European University Association – EUA (2024)**. *AI in Higher Education: Opportunities, Risks, and Governance*.  
- **Pydantic** (validación y settings). **Typer**, **FastAPI**, **Jinja2**, **Pandoc**, **WeasyPrint**, **Celery**, **Redis**, **Prefect**, **Airflow** (documentación oficial).  
- **JSON Schema** – Especificación Draft 2020‑12.  
- *Python Packaging* – PEP 517/518 (paquetización moderna).
