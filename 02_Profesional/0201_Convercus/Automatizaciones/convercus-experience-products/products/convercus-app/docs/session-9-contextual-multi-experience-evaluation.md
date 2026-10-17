---
title: "Session 9 — Experimento de evaluación contextual multi-Experience"
aliases:
- "Contextual Multi-Experience Evaluation Experiment"
language: es
version: "v1.0"
status: "detenido por condición semántica"
date: "2026-09-04"
project: "Convercus App"
document_type: "informe de experimento"
scope: "evaluación de viabilidad semántica de H3 antes de implementación"
repository_role: "resultado de Session 9 y registro de stop condition"
semantic_authority: "análisis de producto y arquitectura subordinado; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 9 — Experimento de evaluación contextual multi-Experience

## Conclusión ejecutiva

**Implementación detenida por la stop condition 1: el repositorio no contiene dos Experience references semánticamente defendibles para el mismo input evidenciario.**

La llegada confirmada de Hospitality es un input apropiado para `experience:arrival-welcome@1`, la única Experience registrada en Demo Factory. No existe una segunda Experience Definition o reference con significado suficiente para evaluar esa misma evidencia sin inventar semántica. Los identificadores `experience-a` y `experience-b` de `routing.test.ts` son datos sintéticos sin definiciones; `canonicalDemoPackage.experiences` está vacío; `experience-simulation` es una capability propuesta, no una Experience.

Crear una segunda Experience solo para obtener dos resultados diferentes habría infringido las instrucciones y habría producido exactamente la falsa evidencia que el experimento debía evitar. Tampoco es válido reutilizar sin cambios `evaluateEventAcrossExperiences`: su entrada se denomina `SignificantEvent` y su salida admite `progression`, precisamente capas cuya implementación estaba excluida.

No se modificó código de aplicación, contratos, fixtures ni tests. La baseline permanece verde con **9 archivos de test y 31 tests**. H3 queda **INCONCLUSIVE**: la falta de material semántico impidió ejecutar la prueba, por lo que no se obtuvo evidencia a favor ni en contra de la proposición contextual.

## A. Base semántica

### TES fact

Según la interpretación semántica vigente y subordinada a TES:

- no todo hecho observable es automáticamente un Evento significativo;
- la significación debe comprenderse dentro de una Experience;
- Evidence/Trace y Evento TES no son equivalentes;
- Activity es una proyección de lectura y no autoridad factual o semántica;
- Pattern, Sequence, Progression, Result y Completion conservan responsabilidades distintas.

Session 9 no modifica ni amplía estas afirmaciones.

### Product Interpretation

`observed-occurrence-trace-event.md` preserva la posibilidad de considerar un input de forma independiente respecto de cero, una o varias Experiences. La cardinalidad es una interpretación de producto compatible con TES, no una regla TES ni una relación estática de pertenencia.

El input candidato, la confirmación de llegada de la reserva `AS-8842`, es defendible porque ya existe como `EvidenceInput`, conserva fuente y fiabilidad, y no necesita icono o tono para existir. Su relación con `experience:arrival-welcome@1` también es defendible: Scenario, Script e interpretación opcional existentes ya referencian esa Experience.

No existe una segunda relación defendible:

| Candidato inspeccionado | Evidencia del repositorio | Veredicto |
|---|---|---|
| `experience:arrival-welcome@1` | Experience registrada, Scenario Hospitality y evidencia de llegada relacionados explícitamente. | Válida como Experience A. |
| `experience-a` / `experience-b` | Solo IDs sintéticos dentro de `routing.test.ts`; no tienen definición, propósito, contexto ni referencia versionada. | No defendibles. |
| `experience-simulation` | Capability propuesta de `canonicalDemoPackage`; no es una Experience Definition. | No aplicable. |
| Experiences del paquete canónico | `canonicalDemoPackage.experiences` es `[]`. | Ninguna disponible. |
| Una Experience nueva de conveniencia | No existe fundamento previo que determine por qué la llegada sería relevante, irrelevante o produciría otro efecto. | Prohibida por stop condition 8. |

### Simplificación específica del experimento

La simplificación prevista habría sido un input in-memory evaluado de forma pura frente a dos referencias, con outcomes neutrales como `relevant` y `not_relevant`. No llegó a implementarse porque incluso una función mínima necesitaría dos contextos con una razón semántica previa. La simplicidad técnica no corrige la ausencia de fundamento.

## B. Inventario de cambios

### Archivo añadido

- `products/convercus-app/docs/session-9-contextual-multi-experience-evaluation.md`: este informe y registro de stop condition.

### Archivos modificados

- Ninguno.

### Áreas intencionadamente intactas

- `prototype/src/demo-factory/`: contratos, artifacts, bootstrap, fixtures, adapter y pruebas.
- `prototype/src/domain/`: `SignificantEvent`, reglas, efectos y routing previo.
- React, `/system`, Activity UI y presenter action de Session 7.
- Todos los ADR y documentos de autoridad TES.
- Persistencia, providers y composición de demos.

## C. Flujo de evaluación

### Flujo previsto, no implementado

```text
Evidence/Input X
      ↓
Contextual Evaluation
     / \
    /   \
Exp A   Exp B
 ↓       ↓
Outcome Outcome
   \     /
    Read Model
       ↓
    Activity/UI
```

### Punto exacto de detención

```text
arrival confirmation evidence
             │
             ├── experience:arrival-welcome@1  ✓ fundamento existente
             │
             └── segunda Experience             ✗ no existe fundamento
                                                        ↓
                                              STOP antes de codificar
```

No hubo flujo ejecutado ni Activity nueva. El presenter action de Session 7 conserva su proyección anterior.

## D. Evidencia de tests

### Baseline

Antes de cualquier implementación se ejecutó `npm run check` el 4 de septiembre de 2026:

- typecheck: correcto;
- lint: correcto;
- Vitest: **9 test files, 31 tests passed**;
- build Vite/PWA: correcto.

### Tests incrementales

**Ninguno.** Añadir tests con una Experience ficticia habría ocultado la stop condition bajo datos arbitrarios y no habría constituido evidencia válida de H3.

### Check final

La baseline completa ya constituye el check final, porque no se cambió código después de ejecutarla. Las regresiones de presenter action Hospitality y Retail incluidas en esos 31 tests permanecen verdes.

## E. Veredicto H3

**INCONCLUSIVE.**

El experimento no falsó la separación `input ≠ interpretation`, pero tampoco la demostró ejecutablemente en dos contextos reales. Solo se confirma documentalmente que:

- un input neutral es representable;
- una interpretación opcional puede almacenarse separada en el contrato actual;
- Activity ya se deriva de un source record;
- falta la segunda Experience necesaria para probar significación contextual.

H3 no está preparada para ADR. Clasificarla como supported confundiría viabilidad de tipos con evidencia contextual.

## F. Evaluación de `SignificantEvent`

El nombre `SignificantEvent` está situado demasiado pronto para ser la entrada neutral del experimento H3. El contrato incluye datos factuales razonables —identidad, tipo, tiempo, fuente, fiabilidad y propiedades—, pero el nombre presupone que la significación ya fue establecida antes de `evaluateEventAcrossExperiences`.

Además, el routing existente:

- recibe `SignificantEvent` en vez de evidencia u ocurrencia neutral;
- depende de `ExperienceParticipation` con `progression` y estados de participación;
- devuelve `ExperienceEffect`, que incluye `progression` y `state_change`;
- permite resultados distintos mediante rules sintéticas, pero no aporta fundamento semántico para esas diferencias.

Por tanto, `SignificantEvent` debe **retenerse con cualificación como contrato legacy/provisional en su capa actual**. Es apropiado únicamente si representa un Evento cuya significación ya fue reconocida por una frontera anterior; no es apropiado como input factual previo a reconocimiento. No se renombra ni reemplaza en Session 9. Una revisión futura deberá decidir su capa y migración con evidencia semántica real.

## G. Impacto sobre Architecture v0.4

**Architecture v0.4 sobrevive sin contradicción.**

La stop condition no afecta a la separación aceptada entre Experience Definition, Scenario, Demo Script, composición, runtime y read models. Refuerza una cualificación ya presente: una referencia técnica no basta para crear significado de Experience, y Activity no debe compensar esa carencia.

H3 permanece fuera de la arquitectura aceptada. No se añade un evaluation engine, ledger, store ni nueva flecha normativa al mapa.

## H. Deuda técnica y atajos experimentales observados

- Solo hay una Experience Definition registrada en Demo Factory.
- Esa definición es un header mínimo: `id`, `name` y `tesBaseline`.
- La interpretación opcional de la evidencia Hospitality ya incluye `experienceRef`, por lo que no prueba evaluación.
- `SignificantEvent` presupone significación en su nombre antes de routing contextual.
- `ExperienceParticipation` incorpora Progression y estados fuera del alcance H3.
- `ExperienceEffect` combina `progression`, `state_change`, `intervention` y `none`.
- El test de routing obtiene resultados distintos mediante reglas sintéticas sin Experience Definitions que justifiquen el contraste.
- Coexisten dos tipos distintos llamados `ExperienceDefinition`: el header de Demo Factory y el contrato de dominio más rico.
- `evaluateEventAcrossExperiences` no lo consume el runtime de Demo Factory.
- `EvidenceInput.interpretation` puede incentivar que la interpretación llegue resuelta en el propio input de acción.
- Activity source todavía contiene copy editorial aunque sus campos visuales se proyectan.

No se añadió nueva deuda para sortear estos límites.

## I. Reversibilidad

Session 9 no alteró comportamiento. Para retirar su único cambio basta eliminar este informe:

```text
products/convercus-app/docs/session-9-contextual-multi-experience-evaluation.md
```

No hay código, esquema, fixture, test, migración, dato persistido ni dependencia que revertir. Los artefactos anteriores permanecen exactamente en su baseline.

## J. Siguiente decisión

**Ninguna nueva decisión arquitectónica ha alcanzado madurez suficiente.**

En particular, no procede crear un ADR para H3, para una frontera de evaluación ni para sustituir `SignificantEvent`. Antes de reconsiderar H3 hace falta material semántico gobernado: una segunda Experience Definition/reference cuyo contexto permita justificar por qué el mismo input de llegada recibe un outcome distinto, o bien otro input existente que ya esté relacionado de forma defendible con dos Experiences.

Esto es un prerrequisito semántico, no una recomendación automática de implementación.

## Preguntas adversariales finales

1. **¿Se demostró significación contextual o se hard-codearon dos outputs?** No se demostró y no se hard-codeó. La implementación se detuvo precisamente para evitarlo.
2. **¿Podría existir el input independientemente de ambas Experiences?** La confirmación de llegada puede existir como evidencia de booking/stay sin icono, Activity ni interpretación TES. Esta independencia solo está respaldada conceptualmente y por la forma del contrato; no fue contrastada frente a dos Experiences.
3. **¿Alguna Experience necesitó mutar el input?** No hubo evaluación. La arquitectura prevista no lo habría permitido.
4. **¿Importó el orden de evaluación?** No se pudo probar.
5. **¿Se implementó accidentalmente parte de Progression?** No. El código existente de routing ya contiene Progression, pero Session 9 no lo reutilizó ni amplió.
6. **¿Está `SignificantEvent` nombrado en la capa correcta?** No como input previo a evaluación. Solo podría ser correcto después de reconocimiento contextual.
7. **¿Activity permaneció como proyección?** Sí; no fue modificada ni usada como input.
8. **¿Qué impide convertir H3 en ADR?** Falta una evaluación ejecutable y semánticamente fundada del mismo input frente a dos Experience contexts, incluida independencia, orden y zero-match.
9. **¿Qué comportamiento futuro de API podría invalidar el planteamiento?** Una API real que entregue únicamente eventos ya interpretados, que acople la interpretación a una participación concreta, que use reglas stateful/order-dependent o que no conserve una identidad evidenciaria común obligaría a cualificar la frontera de producto.
10. **¿Qué no debe generalizarse?** No debe inferirse que todo input sea neutral en cualquier sistema, que toda evidencia deba evaluarse contra N Experiences, que Activity resuma siempre varias relaciones, que `SignificantEvent` deba borrarse, ni que haga falta persistencia o un engine.

## Go / No-Go

**NO-GO para implementar el experimento H3 con el material actual.**

**GO para conservar Architecture v0.4 y la baseline ejecutable de Session 7.** La sesión se considera correctamente concluida como resultado de stop condition, no como fallo técnico ni como falsificación de H3.
