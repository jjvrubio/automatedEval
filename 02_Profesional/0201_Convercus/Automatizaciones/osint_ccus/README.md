# `osint_ccus`

Pipeline agéntico de investigación OSINT por lotes para validar compañías y
priorizar oportunidades comerciales.

El flujo activo utiliza la OpenAI Responses API con búsqueda web. No requiere
NotebookLM, Gemini ni SerpAPI.

## Flujo

```text
CSV
 |
 v
Etapa 1A: empleados >100 y puntos de venta/servicio >10
 |
 v
Etapa 1B: facturación >15M EUR
 |
 v
ELIGIBLE
 |
 v
Etapa 2: tecnología + corporativo + expansión
 |
 v
Informe de potencialidad
```

Etapa 2 solo procesa compañías cuya decisión final de Etapa 1 sea `ELIGIBLE`.
MEDDPICC no es necesario para ejecutar las Etapas 1 y 2.

La arquitectura completa y la futura puerta de cualificación MEDDPICC están en
[ARQUITECTURA_AGENTICA.md](ARQUITECTURA_AGENTICA.md).

## Entrada

El CSV debe contener:

| Columna | Descripción |
|---|---|
| `Company Name` | Nombre comercial |
| `# Employees` | Plantilla de referencia |
| `Website` | Sitio web oficial |
| `Company Linkedin Url` | LinkedIn corporativo |
| `Number of Retail Locations` | Puntos de venta o servicio |

Se acepta `company Name` como alias. Las columnas adicionales se conservan.

## Configuración

Copia el ejemplo de entorno y añade tu clave:

```bash
cd "$OSINT_DIR"
cp .env.example .env
```

Contenido:

```env
OPENAI_API_KEY=tu_clave_openai
```

El modelo predeterminado de los investigadores es `gpt-5.6-terra`.

## Rutas

### Documentos

Los documentos se guardan junto al CSV, agrupados por compañía:

```text
<carpeta-del-CSV>/
├── empresas.csv
└── <Nombre comercial>/
    ├── 01 - Elegibilidad/
    │   └── Resultado Etapa 1.md
    └── 02 - Potencialidad/
        ├── Informe de potencialidad.md
        ├── Investigación/
        │   ├── Tecnología.json
        │   ├── Corporativo.json
        │   └── Expansión.json
        └── Fuentes aportadas/
```

Etapa 1 genera su documento independientemente de Etapa 2. Etapa 2 solo
publica un informe cuando han terminado sus tres investigadores.

Puede forzarse otra raíz documental en ambos comandos mediante:

```text
--accounts-output-root "/otra/ruta"
```

### Estado técnico

El estado reanudable se guarda en:

```text
$OSINT_DIR/.runtime/runs/<ejecución>/
```

Incluye SQLite, manifiestos, auditorías y exportaciones CSV. `RUN_DIR` no es una
carpeta de documentos; permite que Etapa 2 recupere el trabajo de Etapa 1.

## Ejecución completa

Define el CSV y una carpeta de ejecución:

```bash
CSV="/ruta/al/archivo.csv"
RUN_DIR="$OSINT_DIR/.runtime/runs/$(date +%Y%m%d_%H%M%S)_lote"
```

### Etapa 1

Ejecuta 1A y 1B para todas las filas:

```bash
python3 "$OSINT_DIR/stage1_cli.py" \
  --stage all \
  --input "$CSV" \
  --output-dir "$RUN_DIR" \
  --retry-errors
```

En `stage1_cli.py`, `--stage all` significa solamente **Etapa 1A + Etapa 1B**.

### Etapa 2

```bash
python3 "$OSINT_DIR/stage2_cli.py" \
  --input "$CSV" \
  --stage1-output-dir "$RUN_DIR" \
  --retry-errors
```

No es necesario pasar MEDDPICC.

## Prueba limitada

Para investigar únicamente la primera fila:

```bash
python3 "$OSINT_DIR/stage1_cli.py" \
  --stage all \
  --input "$CSV" \
  --output-dir "$RUN_DIR" \
  --limit 1

python3 "$OSINT_DIR/stage2_cli.py" \
  --input "$CSV" \
  --stage1-output-dir "$RUN_DIR" \
  --limit 1
```

## Simulación sin llamadas API

```bash
python3 "$OSINT_DIR/stage1_cli.py" \
  --stage all \
  --input "$CSV" \
  --output-dir "$RUN_DIR" \
  --dry-run

python3 "$OSINT_DIR/stage2_cli.py" \
  --input "$CSV" \
  --stage1-output-dir "$RUN_DIR" \
  --dry-run
```

## Reanudación

Reutiliza el mismo `RUN_DIR`.

- Sin opciones adicionales, se omiten los trabajos ya terminados.
- `--retry-errors` repite solo los fallos.
- `--force` repite el alcance seleccionado.

Si un investigador de Etapa 2 falla, los otros resultados se conservan. El
informe se publica cuando tecnología, corporativo y expansión están en `ok`.

## Umbrales y decisiones

Los umbrales son estrictos:

- `100` empleados falla; `101` pasa.
- `10` puntos falla; `11` pasa.
- `15.000.000 EUR` falla; una cifra superior pasa.

Una discrepancia numérica no implica automáticamente `CONFLICTING`. Si todas
las fuentes creíbles quedan por encima del umbral, la decisión es
`VERIFIED_PASS` y la diferencia se conserva como trazabilidad.

## Cobertura de Etapa 2

Los tres investigadores cubren:

1. tecnología y experiencia de cliente;
2. cambios corporativos y liderazgo;
3. expansión y distribución.

El investigador tecnológico adapta su búsqueda al sector:

- retail: Martech, CRM/CDP, fidelización, IA, TPV/POS, ERP, OMS, WMS, PIM,
  inventario y omnicanalidad;
- hoteles: PMS, reservas/CRS, channel manager, RMS, reputación y TPV;
- restauración: TPV, reservas, KDS, delivery, inventario y fidelización;
- transporte urbano: ticketing, pagos, MaaS, CRM e información al viajero.

Se excluyen banca, seguros, seguridad y administraciones públicas. Los
operadores de transporte urbano constituyen una excepción permitida, incluso
con propiedad pública.

## Salidas técnicas de Etapa 1

```text
stage1_enriched.csv
stage1_pass_1a.csv
stage1_eligible.csv
stage1_audit.jsonl
stage1_summary.md
stage1_state.sqlite3
```

El CSV original no se sobrescribe automáticamente. La escritura sobre el
original debe ser explícita y contar con copia de seguridad.

## Pruebas

```bash
cd "$OSINT_DIR"
PYTHONPYCACHEPREFIX=/private/tmp/osint_ccus_pycache \
  python3 -m unittest discover -s tests -q
```

## Código activo

```text
osint_ccus/
├── stage1_cli.py
├── stage2_cli.py
├── stage1/
├── stage2/
├── tests/
├── ARQUITECTURA_AGENTICA.md
└── README.md
```

El prototipo anterior basado en Gemini y SerpAPI se conserva únicamente como
referencia histórica en:

```text
archive/legacy-gemini-serpapi/
```
