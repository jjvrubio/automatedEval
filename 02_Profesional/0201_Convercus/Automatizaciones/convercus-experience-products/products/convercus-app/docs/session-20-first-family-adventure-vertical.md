---
title: "Sesión 20 — Corrección de Aventura Familiar y navegación"
language: es
version: "v1.3"
status: "closed; exact 22-step acceptance passed; executable with presentation gaps"
date: "2026-09-08"
updated: "2026-09-12"
project: "Convercus App"
document_type: "informe de corrección experimental"
semantic_authority: "subordinado a TES y contratos vigentes; sin promoción"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Sesión 20 — Corrección de la primera vertical

Informe recuperado en la carpeta principal de sesiones el 12 de septiembre de 2026. Su ubicación anterior era `docs/experiments/`; el cambio de ubicación no modifica su carácter experimental ni el estado de aceptación.

Esta revisión supera el informe anterior y su declaración de aceptación. La observación posterior del usuario invalidó aquella aceptación: la navegación no era clara. El cierre de Sesión 20 precede a la auditoría de H21 solicitada el 12 de septiembre de 2026.

## Specification misunderstanding found

**ROOT CAUSE.** La anomalía combinaba presentación, contrato de acción, estado operativo y disponibilidad:

| Capa inspeccionada | Diagnóstico anterior | Corrección |
| --- | --- | --- |
| ScenarioDefinition | P1 y P2 ya existían, pero ambos usaban el mismo inicio genérico. | Estados iniciales explícitos; alistamiento de P1 y activación de P2 distintos; sesión operativa P1. |
| DemoScript | Las dos acciones de inicio se presentaban como comenzar una aventura para un huésped. | Cuatro acciones con etiquetas situadas y distintas. El Script no modifica estado. |
| Public Action | `interactionStart` no distinguía alistamiento de activación. | Operaciones locales `enlist` y `activate`, sin Evidence. |
| Runtime / MockDataAdapter | Validaba que el sujeto enviado estuviera activo, sin exigir la atribución prevista para la acción. | Guarda de sujeto, habilitación y tipo de Evidence; activación desde sesión P1. |
| GuestPerspectiveReadModel | `active` y un contador no explicaban quién estaba alistado, habilitado o había aportado pistas. | Estado por huésped, cuenta común y mensajes específicos para cada intervalo sin Evidence. |
| SupervisionPerspectiveReadModel | Mostraba interacción genérica, sin separar existencia, habilitación y cuenta. | Existencia, estado operativo, Evidence por sujeto, sesión y evaluación. |
| UI | Después de activar P2, el botón seguía diciendo «Comenzar aventura para Huésped 2» aunque ejecutaba B. La aventura quedaba debajo del saldo y entre navegación de cupones/perfil. | Pantalla dedicada, siguiente acción única y pestañas Mi aventura / Actividad / Supervisión. Supervisión observa; se actúa en Mi aventura. |
| Fixtures | No creaban P2 durante el recorrido. El fixture compartido conserva datos históricos de estancia. | Sin cambios al fixture; la existencia procede del Scenario, no del botón. |
| Action availability | Fallback al presenterAction aunque ninguna acción configurada estuviera disponible. | Sin fallback en escenarios con lista de acciones. |
| Acceso a la demo | El enlace cambiaba el query con React Router, pero el bootstrap solo leía la URL una vez. | Entrar desde otra demo recarga la composición. Navegar dentro de Aventura conserva el runtime y el query. |

**BEHAVIOR BEFORE:** inicio genérico → active → exploración poco situada; el mismo texto de inicio de P2 terminaba ejecutando Evidence B. La interfaz no permitía entender correctamente la operación.

**BEHAVIOR AFTER:** sujetos existentes → Alistarme → P1 habilitado / cero pistas → hallar pista del jardín → A@P1 → activar al huésped 2 existente → P2 habilitado / cero pistas propias → hallar pista de la fuente atribuida a P2 → B@P2 → evaluación → resultado compartido.

## Subject existence

P1 y P2 están en `ScenarioDefinition.subjects` desde el principio, ambos individuales. `initialSubjectStates` declara P1 `not-enlisted` y P2 `not-enabled`. Las operaciones no añaden sujetos. Supervisión muestra `exists: true` para ambos antes de actuar.

## Enlistment

`Alistarme → executeAction(enlist-p1) → Runtime`. Solo cambia el estado operativo de P1 a `enabled`. Evidence permanece vacía, suficiencia `not-attempted` y claim `not-produced`. React recibe un snapshot; no escribe el estado operativo. `DemoEnableAction` y `DemoSubjectState` son artefactos locales experimentales, no un contrato productivo de Enrollment.

## P2 activation

`Activar al huésped 2 desde mi cuenta → executeAction(activate-p2)`. La sesión declarada sigue siendo P1 y debe estar habilitada. P2 debe existir y encontrarse `not-enabled`. Después cambia a `enabled`, conservando exactamente la Evidence anterior.

El recorrido mínimo conserva la secuencia A antes de activar P2: permite observar P1 habilitado, P2 habilitado y Evidence `[A@P1]`. No ofrece una rama adicional de activación antes de A. Esto corresponde a la alternativa permitida por la instrucción.

## Evidence contribution

El botón del jardín produce A@P1; el botón de la fuente produce B@P2. Son acciones simuladas de Experience, separadas del alistamiento y la activación. El runtime rechaza acciones de sujetos no habilitados, atribuciones distintas a las configuradas y payloads que mezclan habilitación con Evidence. Los registros de actividad usan lenguaje de hallazgos.

K sigue siendo `A AND (B OR C)`. A+B establece la condición; B+C no la establece. Las funciones de Sesión 17 `evaluateJointAdmissibility()` y `evaluateCrossSubjectEvidenceSufficiency()`, y el módulo de suficiencia, no se modificaron; se verificó igualdad binaria con la copia previa a esta corrección.

## Attribution

`operationalSessionSubjectRef = subject-p1` permanece constante. A lleva `subject-p1`; B lleva `subject-p2`. Usar la cuenta de Lucía no sustituye la atribución factual de B. Es una sesión simulada declarada en el Scenario, no autenticación ni autorización productiva.

## Multiple perspectives

El adaptador conserva estado operativo, Evidence y resultado de evaluación. La evaluación se actualiza al recibir Evidence. Las dos proyecciones leen ese mismo resultado, sin recalcular K dentro de la UI ni al cambiar de pestaña.

Mi aventura prioriza el siguiente paso y el estado de cada huésped. Actividad muestra registros de hallazgos y el historial del fixture. Supervisión muestra existencia, habilitación, atribución, admisibilidad, K y claim. Las pestañas indican la vista activa. Reiniciar aventura queda en una zona separada y restaura el estado inicial; no es una acción de Experience.

## Semantic observations

Se preserva: activar P2 != crear P2; P1+P2 != Group; alistamiento != Evidence; activación != Evidence; cuenta != subjectRef; estado operativo != read model != estado de interfaz; perspectivas distintas != fuentes distintas.

No se introducen conceptos productivos nuevos, ontología de Group/Participant/Contributor/Membership, roles, TES Event/Progression/Result ni motores de perspectivas. La premisa autoritativa sigue siendo experimental y simulada. El claim no recibe dueño, beneficiario ni sujeto colectivo. H18 no se modifica ni se amplía a una nueva reutilización contextual.

**ARCHITECTURAL IMPACT:** corrección local de escenario, runtime y presentación. Architecture v0.5, TES, ADR existentes, Product Semantic Contract y PSC-P01 permanecen sin cambios en esta corrección. No se crea ADR ni PSC-P02 y no se promueven artefactos.

## Test results

Verificación final, 8 de septiembre de 2026, después del ajuste de navegación:

| Comprobación | Resultado |
| --- | --- |
| Tests focalizados `family-adventure-vertical.test.ts` | 10/10 PASS |
| Suite completa | 82/82 PASS; 14 archivos |
| Typecheck | PASS |
| Lint | PASS |
| Build TypeScript + Vite/PWA | PASS |
| `git diff --check` | PASS |
| Comparación de evaluadores de Sesión 17 | Sin cambios |

Los tests cubren existencia inicial, intervalos sin Evidence, guardas antes de habilitar, activación sin Evidence nueva, atribución A/P1 y B/P2, K positivo y B+C negativo, rechazo de payloads incompatibles, reset completo, aislamiento del snapshot y recorrido UI con navegación entre las tres vistas.

Recomprobación del 12 de septiembre de 2026: se ejecutaron de nuevo las 10 pruebas focalizadas, con resultado 10/10 PASS. Los resultados de suite completa, typecheck, lint, build y navegador de este informe corresponden a la validación del 8 de septiembre; no se presentan como nuevas ejecuciones del día 12.

## Manual browser acceptance

Se recorrió una pestaña real de Microsoft Edge mediante controles de la página y CDP, con inspección visual de capturas. Se usó un perfil temporal aislado, carga limpia y viewport móvil 393 × 852. No se alteró el estado interno con DevTools para avanzar. Es revisión por el agente en navegador; no representa aceptación humana del usuario ni prueba de Safari/iPhone real.

### Exact 22-step acceptance result — cierre del 12 de septiembre de 2026

La checklist original fue aportada por el usuario el 12 de septiembre. Se coteja a continuación en su orden y con su contenido exactos. Se reutiliza, con autorización explícita en esa instrucción, el recorrido de navegador del 8 de septiembre, su registro de observaciones ya documentado y las cinco capturas conservadas, inspeccionadas nuevamente durante el cierre. No se afirma una nueva ejecución del navegador el día 12 ni una aceptación humana del usuario.

Referencias de evidencia:

- **I:** [estado inicial](experiments/session-20-acceptance/initial.png).
- **E:** [P1 alistado, cero Evidence](experiments/session-20-acceptance/enlisted.png).
- **P:** [P2 habilitado, cero Evidence propia](experiments/session-20-acceptance/p2-enabled.png).
- **D:** [atribución A/P1 y B/P2; sesión y evaluación](experiments/session-20-acceptance/attribution.png).
- **Z:** [reset](experiments/session-20-acceptance/reset.png).
- **R:** recorrido de navegador registrado el 8 de septiembre; las 22 observaciones locales originales se conservan debajo. R acredita los clics y las vistas intermedias; las capturas son estados, no un vídeo de las transiciones.
- **C:** inspección de [MockDataAdapter](../prototype/src/demo/mock-adapter.ts), [integración vertical](../prototype/src/demo-factory/vertical-evaluation.ts) y [evaluación de Sesión 17](../prototype/src/demo-factory/cross-subject-evidence-admissibility.ts). Complementa la observación visual para el orden interno de evaluación; no sustituye al navegador.

| # | Checklist original exacta | Resultado y evidencia |
| --- | --- | --- |
| 1 | abrir la demo; | PASS — R2, I: Aventura Familiar disponible. |
| 2 | P1 existe como sujeto/huésped; | PASS — I: Tú / huésped 1; Z: `exists: true`. |
| 3 | P2 existe como segundo sujeto disponible en el contexto, aunque todavía no esté habilitado en la Experience; | PASS — I: huésped 2 ya existe en esta estancia, sin habilitar. |
| 4 | P1 todavía no está alistado; | PASS — I: sin alistar, cero pistas. |
| 5 | P1 pulsa “Alistarme”; | PASS — R7: clic ejecutado; transición I → E. |
| 6 | se observa un cambio perceptible; | PASS — E: mensaje de alistamiento, estado habilitado y nueva acción. |
| 7 | no existe todavía Evidence A; | PASS — E: cero pistas; R9 confirma Evidence 0 en supervisión. |
| 8 | aparece una acción comprensible de Experience para P1; | PASS — E: Encontrar la pista del jardín · yo. |
| 9 | P1 ejecuta esa acción; | PASS — R11–12: clic de hallazgo del jardín. |
| 10 | aparece Evidence A@P1; | PASS — R12 y R16: una Evidence A@P1 antes de B; P conserva una pista propia de P1. |
| 11 | desde la misma cuenta/sesión aparece la posibilidad de activar P2; | PASS — R13: Activar al huésped 2 desde mi cuenta; cuenta de Lucía sin cambio. |
| 12 | P1 activa P2; | PASS — R14: clic de activación desde la cuenta de P1. |
| 13 | P2 queda habilitado; | PASS — P: Habilitado por ti. |
| 14 | activar P2 no produce Evidence; | PASS — P y R16: total sigue en una, P2 tiene cero, solo A@P1 en supervisión. |
| 15 | aparece una acción atribuible a P2; | PASS — P: Encontrar la pista de la fuente · huésped 2. |
| 16 | se ejecuta esa acción; | PASS — R17–18: clic de hallazgo de la fuente. |
| 17 | aparece Evidence B@P2; | PASS — D: `evidence-b-p2 · subject-p2`, además de A@P1. |
| 18 | se evalúa la admisibilidad conjunta; | PASS — D: established; C confirma llamada a `evaluateJointAdmissibility()` antes de suficiencia. |
| 19 | se aplica K; | PASS — D: `A AND (B OR C)` y K established; C confirma evaluación con la Evidence admitida. |
| 20 | se produce la afirmación derivada; | PASS — D: afirmación derived established; C confirma que procede del evaluador. |
| 21 | perspectiva del huésped y perspectiva de supervisión se actualizan coherentemente; | PASS — R18–20: resultado de huésped, una pista por huésped, dos Evidence y K/claim established al cambiar de vista en el mismo runtime. |
| 22 | el reset devuelve la demo al estado inicial. | PASS — Z y R21–22: P1 not-enlisted, P2 not-enabled, Evidence 0, K not-attempted, claim not-produced; vuelve Alistarme. |

**Resultado exacto: 22/22 PASS.** La aceptación cubre esta vertical, esta secuencia local y los límites declarados. La aparición conjunta en pantalla de admisibilidad/K/claim no prueba por sí sola su orden causal; ese orden está corroborado por C. El control B+C sigue validado en tests, sin afirmar una acción C visible en navegador.

### Registro previo de comprobaciones locales (R)

Se conserva como evidencia histórica; su numeración no sustituye a la checklist exacta de arriba.

| # | Comprobación local en navegador | Resultado |
| --- | --- | --- |
| 1 | Entrar desde Retail por Búsqueda del tesoro carga realmente Aventura Familiar | PASS |
| 2 | Carga limpia muestra Aventura disponible y Alistarme | PASS |
| 3 | P1 existe sin alistar | PASS |
| 4 | P2 existe sin habilitar | PASS |
| 5 | Supervisión inicial: cero Evidence, K no intentado y claim no producido | PASS |
| 6 | Volver a Mi aventura conserva ese estado | PASS |
| 7 | Alistarme muestra P1 alistado y habilitado | PASS |
| 8 | P1 alistado conserva cero pistas | PASS |
| 9 | Supervisión confirma P1 enabled con Evidence 0 | PASS |
| 10 | P2 sigue not-enabled y sin Evidence | PASS |
| 11 | Volver a Mi aventura ofrece el hallazgo del jardín | PASS |
| 12 | Hallazgo del jardín aporta una pista de P1 | PASS |
| 13 | Aparece una acción distinta para activar al huésped existente | PASS |
| 14 | Activar P2 lo muestra habilitado por P1 | PASS |
| 15 | P2 habilitado sigue con cero pistas propias | PASS |
| 16 | Supervisión conserva únicamente A@P1; K sigue not-established | PASS |
| 17 | Volver ofrece la acción de la fuente atribuida al huésped 2 | PASS |
| 18 | Hallazgo de la fuente muestra resultado y una pista por huésped | PASS |
| 19 | Actividad muestra ambos hallazgos; volver conserva el resultado | PASS |
| 20 | Supervisión mantiene sesión P1, A@P1 y B@P2, admisibilidad/K/claim established | PASS |
| 21 | Reset restaura P1 not-enlisted, P2 not-enabled, Evidence vacía y claim not-produced | PASS |
| 22 | Volver a Mi aventura tras reset muestra Alistarme y cero pistas | PASS |

El control negativo B+C fue comprobado por tests; esta UI mínima no ofrece una acción C y no se afirma haberlo recorrido en navegador.

Capturas del recorrido final: [inicio](experiments/session-20-acceptance/initial.png), [P1 sin Evidence](experiments/session-20-acceptance/enlisted.png), [P2 sin Evidence propia](experiments/session-20-acceptance/p2-enabled.png), [atribución y evaluación](experiments/session-20-acceptance/attribution.png), [reset](experiments/session-20-acceptance/reset.png).

```text
LOCAL BROWSER WALKTHROUGH → PASS
MANUAL BROWSER ACCEPTANCE → PASS
EXACT ORIGINAL 22-STEP CHECKLIST → 22/22 PASS
Previous unqualified MANUAL BROWSER ACCEPTANCE PASS → SUPERSEDED
```

## Files changed

Rutas relativas a `products/convercus-app/`:

- `prototype/src/demo-factory/contracts.ts`: estado y operaciones locales, campos de las dos proyecciones.
- `prototype/src/demo-factory/artifacts.ts`: Scenario y Script corregidos.
- `prototype/src/demo-factory/vertical-evaluation.ts`: proyecciones comprensibles desde evaluación común.
- `prototype/src/demo/mock-adapter.ts`: guardas, evaluación en runtime, disponibilidad y reset.
- `prototype/src/demo-factory/family-adventure-vertical.test.ts`: diez pruebas focalizadas.
- `prototype/src/app/App.tsx`: navegación, pantalla de aventura, supervisión y reset.
- `prototype/src/styles/global.css`: estilos de la navegación y superficies de esta demo.
- `docs/session-20-first-family-adventure-vertical.md`: informe revisado; la ubicación anterior conserva un enlace a este documento.
- `docs/experiments/session-20-acceptance/`: cinco capturas de evidencia visual.

Los cambios previos del usuario en otros archivos no forman parte de esta corrección.

## Revised verdict

```text
SESSION 20 CORRECTION → IMPLEMENTED / TESTS PASS
LOCAL BROWSER WALKTHROUGH → PASS
SESSION 20 FINAL STATUS → CLOSED
EXACT 22-STEP ACCEPTANCE → 22/22 PASS
MANUAL BROWSER ACCEPTANCE → PASS
FIRST VERTICAL DEMO → EXECUTABLE WITH PRESENTATION GAPS
```

Los tres estados centrales exigidos son observables y la checklist original queda cotejada. Se cierra Sesión 20 con aceptación de este recorrido; este cierre no acredita reutilización de una segunda composición ni consolida H21. Persisten límites de presentación: escenario mock, secuencia local corta, historial compartido del fixture, supervisión técnica provisional y falta de validación en iPhone real. Ninguno se presenta como una capacidad productiva.
