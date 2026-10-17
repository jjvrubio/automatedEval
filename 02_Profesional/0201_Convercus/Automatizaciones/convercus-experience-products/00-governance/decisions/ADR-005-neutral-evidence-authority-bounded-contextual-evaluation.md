---
title: "ADR-005 — Evidencia neutral y evaluación contextual acotada por autoridad"
aliases:
- "Neutral Evidence and Authority-Bounded Contextual Evaluation"
language: es
version: "v1.0"
status: "aceptado"
date: "2026-09-04"
project: "Convercus Experience Products"
document_type: "registro de decisión de arquitectura"
scope: "separación entre evidencia factual y evaluación contextual, y límite de autoridad de los claims derivados"
repository_role: "decisión de arquitectura transversal"
semantic_authority: "principio de producto y arquitectura subordinado a ADR-001; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
decision_id: "ADR-005"
decision_status: "accepted"
---

# ADR-005 — Evidencia neutral y evaluación contextual acotada por autoridad

## Estado

**Aceptado.**

## Contexto

Una misma ocurrencia factual puede resultar relevante para una Experience y no estar determinada para otra. Guardar esa interpretación dentro de la evidencia convertiría un hecho reusable en una conclusión dependiente de contexto. En el extremo contrario, tratar toda ausencia de coincidencia como negativa confundiría conocimiento incompleto con exclusión demostrada.

Sessions 11–13 separaron evidencia, evaluación relativa a Experience y proyección de Activity. La evidencia ejecutable mostró además que, manteniendo constantes evidencia y contexto, una variación en la autoridad clasificatoria disponible puede cambiar legítimamente el tipo de conclusión: una afirmación positiva explícita permite una conclusión positiva; una exclusión suficientemente respaldada permite una negativa; y conocimiento incompleto, autoridad ausente, autoridad fuera de scope o conflicto sin precedencia exigen conservar la indeterminación.

La clasificación fue la dimensión manipulada por el experimento, pero no es la única premisa de una evaluación. También intervienen la autoridad factual del origen, la madurez de la interpretación de Experience, el contexto situado y la transformación evaluadora. En particular, las Product Experience Definitions empleadas son candidatas interpretadas contra TES, no definiciones validadas por TES. Una premisa fuerte no eleva silenciosamente la madurez de otra.

## Decisión

La evidencia factual y la evaluación relativa a una Experience son responsabilidades distintas. La evidencia debe poder conservar su identidad, procedencia y contenido factual sin incorporar como hecho universal la relevancia que adquiere dentro de una Experience concreta.

Todo claim contextual derivado queda limitado por la autoridad, el scope y la madurez de las premisas utilizadas para producirlo. La transformación evaluadora no puede conceder a su resultado una autoridad mayor que la que esas premisas permiten conjuntamente.

La falta de información, clasificación, contexto o autoridad suficiente no puede convertirse silenciosamente en una conclusión negativa. Una conclusión negativa requiere base suficiente para excluir la relación dentro del scope evaluado. Esta regla no prescribe cómo se representa o acredita dicha suficiencia.

La relevancia contextual no constituye por sí misma reconocimiento de un Evento TES. Cualquier frontera futura de reconocimiento permanece separada y sin decidir.

Activity y los demás read models permanecen downstream. Pueden presentar una evaluación preservando su procedencia y cualificaciones, pero no pueden originar ni fortalecer la autoridad del claim representado.

`Authority Frontier` es un concepto analítico de producto y arquitectura para razonar sobre qué puede afirmar un artefacto, con qué premisas y dentro de qué scope. No es un concepto TES ni una afirmación de que TES prescriba una evaluación técnica open-world.

## Alcance de autoridad

| Ámbito | Autoridad o función | Límite |
|---|---|---|
| Evidencia factual | Fuente competente para la ocurrencia declarada | No determina por sí sola relevancia para una Experience ni reconocimiento TES. |
| Interpretación de Experience | Artefacto semántico con su madurez y trazabilidad declaradas | Una definición candidata solo sostiene claims con esa misma cualificación; `tesBaseline` no equivale a validación. |
| Contexto situado | Fuente competente para el ámbito contextual declarado | No se convierte por conveniencia en autoridad taxonómica o factual universal. |
| Clasificación | Fuente competente dentro de su scope | El experimento prueba el límite de autoridad clasificatoria, no una taxonomía ni una topología final. Los mappings entre vocabularios permanecen unresolved y requerirían una Authority Frontier propia. |
| Transformación de evaluación | Deriva un claim desde premisas explícitas | No crea hechos, autoridad semántica, precedencia ni certeza ausentes en sus inputs. |
| Runtime | Ejecuta comportamiento permitido y conserva estado cuando aplica | No eleva la autoridad epistémica de una evaluación por ejecutarla. |
| Activity/read model | Proyecta para consumo o presentación | No es evidence ledger, evaluator ni fuente de autoridad del claim. |

Este reparto es una frontera de responsabilidades. No exige un servicio, aggregate, registry, store o artefacto independiente para cada fila.

## Consecuencias positivas

- Una misma evidencia puede evaluarse para varias Experiences sin duplicarse ni adquirir interpretaciones universales.
- Los consumers pueden distinguir una exclusión respaldada de una respuesta todavía no resoluble.
- La autoridad de cada premisa permanece visible y no se blanquea a través del evaluator, runtime o UI.
- Las Product Experience Definitions candidatas pueden participar en experimentos sin presentarse como validadas por TES.
- La arquitectura puede adaptarse a fuentes y taxonomías reales diferentes sin invalidar el invariante.
- Activity conserva su papel de proyección establecido por ADR-002.

## Costes y obligaciones

- Una evaluación debe conservar trazabilidad suficiente hacia las premisas y scopes relevantes para interpretar su claim.
- Los contratos de consumo deben evitar colapsar indeterminación y exclusión cuando esa distinción afecte al comportamiento.
- La madurez de una Product Experience Definition debe permanecer explícita en usos donde condicione la autoridad del resultado.
- Las integraciones futuras deberán resolver cómo acreditar competencia, scope, suficiencia y posibles conflictos sin asumir que los mecanismos experimentales son definitivos.
- Las proyecciones y la UI deberán preservar las cualificaciones epistémicas que sean relevantes; su representación concreta queda abierta.
- Los cambios de fuente, mapping, definición o transformación pueden exigir reevaluación en vez de reinterpretación silenciosa.

## Interpretaciones prohibidas

Esta decisión no implica ni fija:

- los literales, enums o códigos de motivo usados por el experimento;
- `ActivityClassificationAuthority`, `authorityRef`, `coverage` o su forma de `scope`;
- una taxonomía compartida, mappings, autoridad de mapping o equivalencia entre vocabularios;
- un provider, service, registry, aggregate, trust framework o modelo de acreditación;
- una política de precedencia o resolución de conflictos;
- un modelo definitivo de fiabilidad, confianza o exhaustividad;
- persistencia, audit log, event sourcing o composición runtime de autoridades;
- que Scenario sea autoridad taxonómica o factual por defecto;
- que una Product Experience Definition candidata esté validada por TES;
- que `ExperienceDefinition` más `tesBaseline` certifiquen validación semántica;
- que una evaluación positiva reconozca un Evento TES o deba migrar a `SignificantEvent`;
- que Activity participe en la evaluación o determine su resultado;
- una UI, copy, iconografía o visualización concreta para resultados no resueltos;
- que TES prescriba semántica técnica open-world.

## Evidencia de aceptación

- Session 11 demuestra que una evidencia factual neutral puede evaluarse contra dos contextos de Experience sin branches por identificador y sin convertir Activity en input.
- Session 12 identifica adversarialmente que ausencia de conocimiento y negación son claims distintos, y delimita `Authority Frontier` como herramienta analítica no-TES.
- Session 13 mantiene Evidence y ExperienceContext constantes y varía únicamente autoridad clasificatoria y su suficiencia dentro de scope.
- Sus tests verifican afirmación positiva explícita, exclusión explícita, ausencia con conocimiento insuficiente, ausencia con base suficiente para excluir, autoridad ausente o fuera de scope y conflicto sin precedencia.
- El evaluator no importa Activity, `ExperienceDefinition`, bootstrap ni reconocimiento de Event; tampoco contiene branches por las Experiences usadas como fixtures.
- La ejecución focalizada de Session 14 supera los 12 tests de `evidence-relevance.test.ts`.
- ADR-001 sustenta que una derivación no puede adquirir autoridad TES por conveniencia; ADR-002 mantiene Activity downstream; ADR-003 separa intención y resolución efectiva; ADR-004 separa definición, contexto, presentación y runtime.

La generalización desde autoridad clasificatoria hacia todas las premisas no se presenta como evidencia experimental simétrica. Se acepta como principio arquitectónico de no escalado porque se deriva de la evidencia acumulada y de las fronteras de autoridad ya aceptadas. La forma concreta de cada autoridad sigue provisional o no resuelta.

## Implicaciones de versionado

1. Versionar una evidencia no versiona automáticamente su evaluación contextual.
2. Una evaluación reproducible debe poder identificar las versiones o revisiones relevantes de sus premisas cuando estas puedan cambiar el claim.
3. Cambiar una Product Experience Definition, Scenario, fuente clasificatoria, mapping o transformación no reinterpreta silenciosamente evaluaciones históricas.
4. La baseline TES declarada y la madurez de validación de una Product Experience Definition son dimensiones distintas.
5. Los contratos concretos de versionado, almacenamiento y reevaluación se decidirán cuando existan consumers o APIs reales.

## Condiciones de reconsideración

La decisión debe revisarse si:

- una API real demuestra que no puede conservarse una frontera entre evidencia factual e interpretación contextual;
- el dominio aplicable declara de forma autoritativa un mundo cerrado que permita negativos sin la cualificación aquí exigida;
- nueva evidencia TES establece una relación normativa diferente entre evaluación contextual y reconocimiento de Event;
- las premisas necesarias no pueden identificarse ni acotarse con trazabilidad proporcionada;
- preservar indeterminación produce una contradicción operacional demostrable que no puede resolverse en el consumer;
- una integración real demuestra que Activity debe originar claims y no solo proyectarlos, en contradicción con ADR-002;
- la distinción entre madurez de definición y baseline TES deja de ser válida por una decisión expresa de gobernanza TES.

## Revisión de aceptación

La decisión promueve el invariante que sobrevivió a la falsificación, no su implementación actual. Sobrevive a reemplazar enums, reason codes, fixtures, taxonomías, shapes y providers porque solo exige separación de evidencia, límites de premisas y tratamiento explícito de la insuficiencia.

La evidencia directa es más fuerte para la frontera clasificatoria que para las demás premisas. Ese límite no bloquea la aceptación: ADR-001 ya prohíbe elevar derivaciones por encima de su fuente, las Product Experience Definitions declaran su madurez candidata y ADR-002–004 mantienen runtime y proyecciones fuera de la autoridad semántica. Permanecen abiertas la topología de autoridad, la alineación taxonómica, la acreditación, la precedencia, el reconocimiento de Event y la representación de resultados.
