# Arquitectura agéntica de `osint_ccus`

## 1. Estado y propósito del documento

**Revisión:** 2026-07-29
**Estado:** arquitectura vigente para Etapas 1 y 2; diseño objetivo para la
etapa posterior de cualificación MEDDPICC.

Este documento describe:

1. el comportamiento implementado de elegibilidad y potencialidad;
2. las puertas de control entre etapas;
3. la separación entre entregables y estado técnico;
4. el punto futuro en el que MEDDPICC pasa de opcional a obligatorio;
5. las diferencias conocidas entre la arquitectura objetivo y la
   implementación actual.

La interfaz operativa actual es CLI. No se requiere GUI para las Etapas 1 y 2.

## 2. Objetivo

`osint_ccus` procesa un CSV de compañías y responde secuencialmente:

1. **Elegibilidad:** ¿la empresa tiene escala suficiente?
2. **Potencialidad:** ¿existen señales públicas que justifiquen priorizarla?
3. **Cualificación futura:** ¿debe promoverse a trabajo comercial activo y
   construir o mantener un MEDDPICC?

El sistema separa investigación, evidencia y decisión. Los agentes estructuran
hallazgos; las puertas cuantitativas se resuelven mediante reglas
deterministas.

## 3. Contrato de entrada

Columnas mínimas:

| Columna | Uso |
|---|---|
| `Company Name` | Nombre comercial inicial |
| `# Employees` | Referencia que debe validarse |
| `Website` | Semilla principal de identidad e investigación |
| `Company Linkedin Url` | Semilla secundaria de identidad y plantilla |
| `Number of Retail Locations` | Referencia que debe completarse o validarse |

Se acepta `company Name` como alias de `Company Name`. Las columnas adicionales
se preservan.

La identidad de procesamiento combina fila, dominio, LinkedIn y compañía; no
depende únicamente del nombre.

### 3.1 CSV original

El procesamiento ordinario conserva el CSV de entrada y genera exportaciones
técnicas enriquecidas. Una escritura sobre el CSV original debe ser una acción
explícita, precedida por copia de seguridad y limitada a los campos acordados.
La actualización automática y transaccional del CSV original sigue siendo una
mejora pendiente.

## 4. Propiedad y estructura de carpetas

El usuario administra la carpeta que contiene el CSV y las carpetas comerciales
de las empresas, incluidas sus fuentes. La elegibilidad no determina si una
carpeta comercial existe.

Los entregables se sitúan junto al CSV:

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

Reglas:

- Etapa 1 publica su Markdown sin depender de Etapa 2.
- Etapa 2 publica su Markdown solo si sus tres investigaciones han terminado.
- Un informe incompleto no se presenta como informe final.
- Los JSON temáticos permiten revisar qué produjo cada investigador.
- MEDDPICC no es una dependencia de Etapas 1 o 2.

La implementación puede crear una subcarpeta de fase ausente para poder
escribir el entregable. Como evolución, el CLI deberá validar la correspondencia
entre `Company Name` y las carpetas comerciales preexistentes y advertir ante
ambigüedades, en lugar de inferir silenciosamente una carpeta.

## 5. Estado técnico

SQLite, auditorías, manifiestos y CSV de trabajo se guardan fuera de las
carpetas comerciales:

```text
$OSINT_DIR/.runtime/runs/<fecha-hora>_<csv>/
├── stage1_state.sqlite3
├── stage1_enriched.csv
├── stage1_pass_1a.csv
├── stage1_eligible.csv
├── stage1_audit.jsonl
├── stage1_summary.md
├── stage2_state.sqlite3
├── stage2_audit.jsonl
├── stage2_summary.md
└── *_manifest.json
```

`RUN_DIR` es estado reanudable, no una ubicación documental. Etapa 2 recibe el
mismo `RUN_DIR` para recuperar las decisiones de Etapa 1.

## 6. Flujo y puertas de control

```text
CSV_INGESTED
      |
      v
IDENTITY_AND_SCALE_RESEARCH
      |
      v
GATE_1A: empleados >100 AND puntos >10
      | PASS                       | FAIL / REVIEW
      v                            +--> STOP_STAGE_1A
REVENUE_RESEARCH
      |
      v
GATE_1B: facturación >15M EUR
      | ELIGIBLE                   | INELIGIBLE / REVIEW
      v                            +--> STOP_BEFORE_STAGE_2
SECTOR_CLASSIFICATION
      | ALLOWED                    | EXCLUDED / REVIEW
      v                            +--> STOP_STAGE_2
STAGE_2_SPECIALISTS
      |
      v
POTENTIALITY_REPORT_COMPLETE
      |
      v
PROMOTION_GATE_M  (futura)
      | PROMOTE                    | HOLD / MONITOR
      v                            +--> no MEDDPICC obligatorio
MEDDPICC_REQUIRED
      |
      v
QUALIFICATION_ACTIVE
```

Una fila en revisión nunca avanza automáticamente.

## 7. Etapa 1: elegibilidad

### 7.1 Puerta 1A: escala operativa

La compañía debe cumplir simultáneamente:

- más de 100 empleados;
- más de 10 puntos de venta o servicio.

Los límites son estrictos: 100 y 10 no cumplen.

Pueden contar:

- tiendas propias;
- franquicias;
- corners y shop-in-shop identificables;
- centros u oficinas que prestan servicio;
- puntos de terceros identificados y activos;
- un ecommerce oficial como un único canal.

No se cuentan automáticamente países, clientes B2B, distribuidores sin puntos
identificables, empleados ni presencias no verificadas en marketplaces.

### 7.2 Contradicciones materiales

Una diferencia numérica no es por sí sola un conflicto de puerta.

El resultado estructurado conserva `threshold_consensus`:

- `all_above`: todas las fuentes creíbles superan el umbral;
- `all_at_or_below`: todas quedan en el umbral o por debajo;
- `crosses`: existen cifras creíbles a ambos lados;
- `unknown`: no puede determinarse.

Si las cifras difieren pero todas superan el umbral, la decisión es
`VERIFIED_PASS`; la discrepancia se mantiene como trazabilidad. Solo un
conflicto material para la puerta produce `CONFLICTING`.

### 7.3 Puerta 1B: escala económica

Solo se investiga facturación para compañías que pasan 1A.

La compañía debe acreditar más de 15 millones de euros anuales. Se registran:

- importe y moneda;
- ejercicio;
- métrica —revenue, turnover, sales—;
- perímetro —marca, sociedad o grupo—;
- conversión a euros, cuando proceda.

### 7.4 Decisiones

Por criterio:

- `VERIFIED_PASS`
- `VERIFIED_FAIL`
- `UNKNOWN`
- `CONFLICTING`

Por etapa:

- `PASS_1A`
- `FAIL_1A`
- `ELIGIBLE`
- `INELIGIBLE`
- `REVIEW_REQUIRED`

La política determinista es:

```text
PASS_1A =
    employees == VERIFIED_PASS
    AND locations == VERIFIED_PASS

ELIGIBLE =
    PASS_1A
    AND revenue == VERIFIED_PASS
```

## 8. Etapa 2: potencialidad

Etapa 2 no necesita MEDDPICC. Solo recibe compañías con decisión
`ELIGIBLE`.

### 8.1 Puerta sectorial

Antes de ejecutar los tres especialistas, el investigador tecnológico clasifica
el sector.

Excluidos:

- banca;
- seguros;
- cuerpos o empresas de seguridad;
- administraciones públicas.

Excepción explícita:

- operadores de autobús, metro y transporte urbano, incluso con propiedad
  pública.

Un sector `excluded` o `review` detiene la investigación automática.

### 8.2 Investigadores especializados

#### Tecnología y experiencia de cliente — peso 40 %

Cobertura común:

- Martech, CRM, CDP e IA;
- fidelización y automatización;
- atención al cliente;
- datos, analítica y pagos.

Cobertura por vertical:

- **retail:** TPV/POS, ERP, OMS, WMS, PIM, inventario, promociones,
  ecommerce, devoluciones y omnicanalidad;
- **hoteles:** PMS, CRS/motor de reservas, channel manager, RMS, reputación,
  guest messaging, CRM/CDP y TPV de restauración;
- **restauración:** TPV/POS, reservas, KDS, delivery, inventario,
  fidelización y CRM/CDP;
- **transporte urbano:** ticketing/AFC, validadores, pagos, MaaS/app, CRM,
  información al viajero y atención.

#### Cambios corporativos y liderazgo — peso 25 %

Investiga cambios directivos, estructura, financiación, adquisiciones,
alianzas, resultados, reorganizaciones y señales de transformación.

#### Expansión y distribución — peso 35 %

Investiga aperturas, cierres, nuevos mercados, países, tiendas, franquicias,
corners, distribuidores, centros de servicio y cambios en la red.

### 8.3 Síntesis

Los tres resultados deben estar en estado `ok`. La síntesis:

- enlaza cada hallazgo con evidencia;
- conserva contradicciones y lagunas;
- identifica stakeholders públicos;
- prioriza señales;
- propone preguntas de discovery;
- no inventa ACV, ROI o payback.

La puntuación ponderada produce:

| Puntuación | Recomendación |
|---:|---|
| `>= 7.0` | `PRIORIDAD_ALTA` |
| `>= 4.5` y `< 7.0` | `PRIORIDAD_MEDIA` |
| `< 4.5` | `MONITORIZAR` |

La puntuación ordena candidatos; no sustituye la decisión comercial.

## 9. Puerta futura de MEDDPICC

### 9.1 Principio

MEDDPICC es opcional y no interviene en Etapas 1 y 2. Pasa a ser obligatorio
cuando una compañía se promueve desde candidato investigado a cualificación
comercial activa.

No debe arrancar únicamente porque la empresa sea `ELIGIBLE`: elegibilidad
demuestra escala, no prioridad ni oportunidad real.

### 9.2 `PROMOTION_GATE_M`

La puerta se evalúa después de completar el informe de Etapa 2.

Precondiciones:

1. Etapa 1 finaliza como `ELIGIBLE`;
2. el sector está permitido;
3. los tres especialistas de Etapa 2 están completos;
4. existe informe de potencialidad;
5. una decisión humana promueve la compañía a discovery o cualificación.

La recomendación de Etapa 2 orienta la revisión:

- `PRIORIDAD_ALTA`: proponer promoción;
- `PRIORIDAD_MEDIA`: exigir revisión humana;
- `MONITORIZAR`: no promover por defecto, aunque permite override humano.

La decisión humana es autoritativa. Una puntuación nunca crea por sí sola una
oportunidad comercial.

Estados objetivo:

```text
POTENTIALITY_COMPLETE
    -> AWAITING_PROMOTION
    -> MEDDPICC_REQUIRED
    -> MEDDPICC_IN_PROGRESS
    -> QUALIFICATION_ACTIVE
```

No se podrá declarar `QUALIFICATION_ACTIVE` sin un MEDDPICC canónico aportado.

### 9.3 Construcción y evolución

`osint_ccus` no genera un MEDDPICC alternativo. Su construcción se realizará
con el modelo canónico del usuario —actualmente, su Proyecto de ChatGPT— y se
aportará como Markdown.

El sistema deberá registrar:

- ruta de origen;
- SHA-256;
- versión y fecha declaradas;
- momento de incorporación;
- compañía y registro a los que pertenece.

Una nueva versión de MEDDPICC no obliga a repetir automáticamente la
investigación pública de Etapa 2. La evolución objetivo separará:

1. investigación pública ya completada;
2. contraste con MEDDPICC;
3. regeneración del informe de cualificación.

Solo se repetirá investigación web cuando haya caducado, cambie materialmente
la compañía o el usuario solicite una actualización.

La automatización de `PROMOTION_GATE_M` y la etapa de cualificación todavía no
está implementada.

## 10. Evidencia y seguridad

Cada cifra o hallazgo conserva:

- entidad y perímetro;
- valor o afirmación;
- tipo de valor;
- fecha;
- fuente, editor y URL;
- extracto;
- calidad y confianza;
- lagunas y contradicciones.

Prioridad general de fuentes:

1. informes, cuentas y web oficial;
2. registros y bases empresariales reconocidas;
3. casos de proveedores y LinkedIn corporativo;
4. medios sectoriales fiables;
5. directorios y otras fuentes secundarias.

LinkedIn es una señal, no una cifra contable. El sistema solo usa contenido
públicamente accesible y no elude autenticación, paywalls ni controles
antibot.

Las instrucciones encontradas en páginas web se tratan como datos no
confiables y nunca sustituyen las instrucciones del sistema.

## 11. Reanudación y errores

Cada tema guarda estado independiente:

- `pending`
- `running`
- `ok`
- `error`

Comportamiento:

- una ejecución repetida omite trabajos `ok`;
- `--retry-errors` repite solo los fallos;
- `--force` repite el alcance seleccionado;
- un timeout no destruye resultados ya completados;
- Etapa 2 no publica un informe nuevo hasta completar sus tres especialistas.

## 12. CLI vigente

### 12.1 Etapa 1 completa — 1A y 1B

```bash
python3 "$OSINT_DIR/stage1_cli.py" \
  --stage all \
  --input "$CSV" \
  --output-dir "$RUN_DIR" \
  --retry-errors
```

En `stage1_cli.py`, `--stage all` significa únicamente 1A + 1B.

### 12.2 Etapa 2

```bash
python3 "$OSINT_DIR/stage2_cli.py" \
  --input "$CSV" \
  --stage1-output-dir "$RUN_DIR" \
  --retry-errors
```

Etapa 2 filtra internamente las filas `ELIGIBLE`.

## 13. Componentes implementados

```text
osint_ccus/
├── stage1_cli.py
├── stage2_cli.py
├── stage1/
│   ├── csv_input.py
│   ├── research.py
│   ├── policy.py
│   ├── runner.py
│   ├── storage.py
│   ├── exporter.py
│   ├── deliverables.py
│   └── presentation.py
├── stage2/
│   ├── research.py
│   ├── runner.py
│   ├── storage.py
│   ├── report.py
│   └── deliverables.py
├── tests/
└── .runtime/
```

El prototipo anterior basado en Gemini y SerpAPI está aislado en
`archive/legacy-gemini-serpapi/` y no constituye parte del flujo vigente.

## 14. Pruebas de aceptación

- valida las cinco columnas mínimas;
- preserva columnas adicionales;
- 100 empleados falla y 101 pasa;
- 10 ubicaciones falla y 11 pasa;
- 15 millones de euros no cumple el umbral estricto;
- cuenta un ecommerce oficial como un canal;
- no mezcla sociedad, marca y grupo sin declarar el perímetro;
- una discrepancia no material no bloquea la puerta;
- una contradicción que cruza el umbral exige revisión;
- una compañía que falla 1A no consume investigación de facturación;
- una compañía no elegible no entra en Etapa 2;
- un sector excluido se detiene tras la clasificación;
- un timeout permite reanudar solo el investigador fallido;
- Etapa 1 publica su Markdown junto al CSV;
- Etapa 2 publica informe y JSON temáticos junto al CSV;
- los entregables no dependen de MEDDPICC;
- la auditoría y el estado técnico permanecen en `RUN_DIR`.

## 15. Evolución pendiente

Prioridad arquitectónica:

1. orquestador único para Etapas 1 y 2 que gestione `RUN_DIR`;
2. resolución controlada de carpetas comerciales preexistentes;
3. escritura explícita y segura de campos acordados en el CSV original;
4. `PROMOTION_GATE_M` y estados de cualificación;
5. incorporación versionada del MEDDPICC canónico;
6. política de caducidad y actualización selectiva de OSINT;
7. pruebas de aceptación para el paso a `QUALIFICATION_ACTIVE`.
