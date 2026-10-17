---
title: "Sesión 21 — Ejecución H21 contra baseline congelada"
language: es
version: "v1.0"
status: "experiment executed; H21 falsified; stopped at first material falsifier; no shared repair"
date: "2026-09-13"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005; sin promoción"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Sesión 21 — Ejecución de H21

## EXPERIMENT EXECUTION

**H21 → FALSIFIED para la baseline congelada y el ámbito del ensayo.** Composition B se resuelve correctamente con identidad propia, pero no recibe las proyecciones de huésped y supervisión en su snapshot inicial. El experimento se detuvo en ese punto, antes de ejecutar comandos de alistamiento, Evidence o reset.

Se ejecutó el protocolo de la [auditoría aprobada](session-21-composition-boundary-factory-reusability-audit.md), precisado por la instrucción del 13 de septiembre. Se preservan Sesión 20 cerrada y A como referencia aceptada. No se abre Sesión 22.

El [harness H21](../prototype/src/demo-factory/composition-boundary-h21.test.ts) usa los exports reales, `resolveDemo()` y los providers reales. No modifica estado privado, no sustituye métodos y no renderiza una UI alternativa. La [traza JSON](session-21-execution-trace.json) conserva las entradas, ambas composiciones resueltas, los dos snapshots y el punto exacto de STOP.

Ejecución principal registrada: `2026-09-13T10:02:58.363Z` (11:02:58, Europe/Lisbon). La comprobación general posterior reprodujo el mismo punto de parada en el harness, sin sobrescribir la traza principal ni continuar el recorrido B. No se abrió navegador para continuar después del primer falsador: el fallo ya se observa en el límite público `getSnapshot()`.

## BASELINE HASH / SHARED FILES FROZEN

Baseline capturada **antes de añadir B** en [session-21-frozen-baseline.json](session-21-frozen-baseline.json).

```text
SHA-256 de la baseline congelada:
b21a44cc80cfe3d64ce753a5120bd4229a53938cddc2068f1d608d83d0570eb1
```

Se calcula sobre la concatenación ordenada por ruta de `ruta + NUL + SHA256(bytes) + LF` de los ocho archivos compartidos y los archivos protegidos enumerados en el JSON. El SHA del bootstrap original se registra aparte porque su import/registro es una excepción permitida. Las huellas se verificaron durante el harness y después de los checks. Las 55 entradas congeladas permanecen iguales, incluidas cuatro entradas de metadatos `.DS_Store` sin significado arquitectónico; las ocho fuentes y los documentos protegidos no cambiaron.

| Archivo compartido, relativo a prototype/ | SHA-256 antes = después |
| --- | --- |
| src/demo/mock-adapter.ts | `2329da2c2bf75683fe7fc04910d3fed0097d2b23b4c168af7281240cbb4d5b3b` |
| src/demo-factory/contracts.ts | `7b3a158d673cb3c3fac62ba0eb3cf795b1cc8dc10c55a5be89ec59cf008e08e0` |
| src/demo-factory/vertical-evaluation.ts | `ba2423dcdd8eab8e059bd3f8081d5eec240b7801e6a42d9beac0c8a0dd05745a` |
| src/demo-factory/cross-subject-evidence-admissibility.ts | `6a099cd4feb94de442988a933636718bc0cfacba3f6170c809d00987fcffa53d` |
| src/demo-factory/evidence-sufficiency.ts | `f6ac55e83641f89c208c9fbcc56d68fc7f6495a27981532e2c97c7e54a9a6949` |
| src/app/App.tsx | `90e16092157fa23b29da837dd86cd1b9ab0a0cc84f815eb14576abbc84ebc828` |
| src/styles/global.css | `dec89cf4dfa15f8f591d93c40de927916528e8682900f648cd1bf673985eb3fa` |
| src/main.tsx | `cb88ce48d25e4dfe894e0483efbdd495b77e2460e802a66cdbb7e43934e5fd9f` |

`bootstrap.ts` conserva su lógica íntegra. Al retirar únicamente el import de `costaFixture` y la línea `[costaFixture.id]: costaFixture`, el texto coincide byte a byte con el anterior, cuyo SHA-256 es `b102301382a4864c7970f75ea3de2cc075f200cb58b83fc7c7b11dfd76b8c220`.

También se contrastaron los archivos de catálogos con copias previas: retirando los registros/imports/declaración B de `artifacts.ts` y `manifests.ts` se recupera exactamente el texto anterior; `fixtures.ts` conserva íntegramente su contenido previo y añade B al final. No se cambia la Experience ni las composiciones existentes. El repositorio ya tenía cambios sin commit; estas verificaciones comparan con el estado de trabajo inmediatamente anterior al experimento, no con HEAD.

## COMPOSITION B CREATED

B existe como instrumento experimental, no como demo comercial aceptada. Está registrada con el mecanismo existente; no se añade selector.

| Elemento | Valor de B |
| --- | --- |
| demoId / prospectId | `hospitality-family-adventure-costa` / `costa-fixture` |
| brand / brandRef | Costa Clara Resort / `brand:costa-clara@1` |
| fixtureRef | `fixture:family-adventure-costa@1` |
| scenarioRef / scenario.id | `scenario:family-adventure-costa@1` / `family-adventure-costa` |
| scriptRef / script.id | `script:family-adventure-costa@1` / `family-adventure-costa` |
| Experience | `experience:family-adventure@1`, idéntica a A |
| property / booking / stay | `costa-clara-resort` / `CC-205` / `stay-CC-205` |
| Cuenta y nombres situados | Inés en fixture; Mateo en contenido y labels de Script |
| Presentación de pistas | Mirador / patio |
| Sujetos y sesión | `subject-p1`, `subject-p2`, ambos individual; sesión P1 |
| Semilla de estado | P1 not-enlisted, P2 not-enabled |
| Payloads simulados | `evidence-costa-a-p1` y `evidence-costa-b-p2`, con contextos CC |

Los actionIds, checkpoints, guardas declaradas y semántica de comandos coinciden con A. El harness compara las acciones de Scenario y las firmas semánticas del Script, incluidos tipo de Evidence, sujetos, fiabilidad y fuente. K, requisitos de autoridad y evaluadores permanecen congelados. C conserva su papel de alternativa en el criterio; no se añade una acción UI C que A tampoco tenía.

Los payloads declarados en Script son estímulos preparados, no Evidence factual ya incorporada. No se precargan habilitación actual, admisibilidad, K ni claim. El nombre de Mateo se aporta mediante superficies de contenido ya existentes; no se extiende un contrato compartido para forzar su renderizado. Ningún nombre situado llegó a probarse dentro de las perspectivas ausentes.

Archivos añadidos: [costa-artifacts.ts](../prototype/src/demo-factory/costa-artifacts.ts), [logo local](../prototype/src/demo-factory/costa-clara-logo.svg), harness y documentos/traza/huellas. `costa-artifacts.ts` contiene únicamente objetos de marca, Scenario y Script; no contiene maquinaria de ejecución. Se añaden datos/registros B en [fixtures.ts](../prototype/src/demo-factory/fixtures.ts), [manifests.ts](../prototype/src/demo-factory/manifests.ts), [artifacts.ts](../prototype/src/demo-factory/artifacts.ts) y el registro de fixture en [bootstrap.ts](../prototype/src/demo-factory/bootstrap.ts).

## RESOLUTION RESULT A/B

| Comprobación incremental | Resultado observado |
| --- | --- |
| Composition A resolves | Sí. |
| Composition B resolves | Sí. |
| ResolvedDemoRuntime A != B | Objetos distintos. |
| brand/context/fixture refs A != B | Distintos; contextos B corresponden a Costa Clara/CC-205. |
| Experience A == Experience B | Misma referencia resuelta y mismo experienceRef. |
| Provider A != Provider B | Instancias distintas. |
| Misma implementación | Ambos providers tienen el mismo prototipo. |
| getSnapshot A/B retorna | Ambos retornan, sin excepción. |
| Datos iniciales del fixture | A muestra Lucía; B muestra Inés y contenido Costa Clara. |
| Disponibilidad inicial | Ambos exponen `ready` y `enlist-p1`. |
| Perspectivas iniciales | A tiene ambas; B no tiene ninguna. STOP. |

`resolveDemo()` construye el provider dentro de la propia resolución. Por ello la instanciación no es una operación externa adicional: después de verificar los objetos resueltos se invoca su `getSnapshot()`.

La resolución y el branding correctos son fronteras observadas que funcionaron; **no son un PARTIAL PASS de H21**, que exige el pipeline completo.

## LAST SUCCESSFUL BOUNDARY

```text
Manifest/artefactos A y B
→ resolver existente
→ dos ResolvedDemoRuntime
→ dos instancias de la misma implementación de provider
→ retorno de snapshots genéricos iniciales con fixture propio y acción enlist-p1
```

## FIRST FAILING BOUNDARY

```text
scenario.id = family-adventure-costa
→ projectSnapshot()
→ guestPerspective ausente
→ supervisionPerspective ausente
```

| Campo requerido | Registro |
| --- | --- |
| input/action | `resolveDemo("hospitality-family-adventure-costa").provider.getSnapshot()` |
| expected behavior | Snapshot de Aventura con ambas perspectivas, P1 no alistado, P2 no habilitado, ninguna Evidence y ningún claim producido. |
| observed behavior | Snapshot genérico correcto de Inés, checkpoint ready y enlist-p1; no existen los campos guestPerspective/supervisionPerspective. |
| file / responsibility that would require modification | `prototype/src/demo/mock-adapter.ts:81`, selección de las proyecciones en projectSnapshot. |
| why modification would be necessary | El gate solo acepta el id de A. Los datos permitidos de B no pueden hacer que su identidad distinta cumpla esa igualdad. |
| audit finding | L2, confirmado en selección de proyecciones. |

Código congelado relevante:

```ts
if (scenario?.id === "family-adventure") {
  snapshot.guestPerspective = projectGuestPerspective(evaluation, scenario.subjects, subjectStates);
  snapshot.supervisionPerspective = projectSupervisionPerspective(
    evaluation, scenario.subjects, subjectStates, scenario.operationalSessionSubjectRef,
  );
}
```

No se afirma que la llamada lance error ni que `executeAction()` no pudiera ejecutar un comando si se invocara directamente. El fallo material es la ausencia de las perspectivas requeridas ya en el estado inicial. Continuar por otra superficie o ejecutar comandos a pesar de ese fallo eludiría el STOP establecido.

## OBSERVED EXECUTION TRACE

Extracto fiel de la [traza completa](session-21-execution-trace.json):

```text
resolveDemo(A) → returned
resolveDemo(B) → returned
A.experience === B.experience → true
A.provider !== B.provider → true
Object.getPrototypeOf(A.provider) === Object.getPrototypeOf(B.provider) → true
A.getSnapshot() → member Lucía; ready / enlist-p1; guest + supervision present
B.getSnapshot() → member Inés; ready / enlist-p1; guest + supervision absent
FIRST MATERIAL FALSIFIER → L2 / initial projections
executeAction calls in H21 → 0
reset calls in H21 → 0
STOP
```

Los constructores inicializan una evaluación vacía como sentinel. No se alcanzó la evaluación de Evidence de B ni la invocación de admisibilidad/suficiencia con hechos B. No se renderizaron pantallas B para buscar otros fallos después del STOP.

## A/B ISOLATION RESULT

**NOT REACHED** para controles de acciones, Evidence y resets. Solo se observó que los providers y objetos de runtime son distintos. Eso no demuestra aislamiento de evolución, ausencia de contaminación de hechos ni independencia de reset. Los tests de regresión existentes ejecutan otros recorridos en instancias propias; no cuentan como continuación del ensayo H21 ni como controles A/B de Costa Clara.

## CONTEXT INTEGRITY RESULT

Contextos **declarados y resueltos** A/B distintos, comprobados en el harness. Contexto factual/evaluado de B: **NOT REACHED**. La ausencia de sus read models no se interpreta como admisibilidad negativa ni como evidencia de que el contexto evaluado esté bien o mal.

## CONTENT LEAKAGE RESULT

Datos genéricos iniciales de B correspondientes a su fixture, observables en la traza: Inés, Costa Clara, CC-205, mirador y patio. Contenido de perspectivas/pantallas compartidas: **NOT REACHED**. No se declara ausencia global de contaminación de contenido, ni se confirma L3/L4/L5 observando únicamente el fixture inicial.

## AUDIT FINDINGS CONFIRMED BY EXECUTION

**L2 → EXECUTION-CONFIRMED**, específicamente la selección de proyecciones por `scenario.id` en `projectSnapshot()`.

El experimento aporta un caso material, con instancias reales y B correctamente registrada, de identidad situada usada como condición para entregar las perspectivas de la Experience compartida.

## AUDIT FINDINGS STILL INSPECTION-ONLY

| Hallazgo | Estado después del ensayo |
| --- | --- |
| L1: contexto fijo en integración de evaluación | SOURCE-INSPECTION FINDING; NOT EXECUTION-CONFIRMED BY H21. |
| L3: narrativa/identidad en guest projection | SOURCE-INSPECTION FINDING; NOT EXECUTION-CONFIRMED BY H21. |
| L4: literales situados en App | SOURCE-INSPECTION FINDING; NOT EXECUTION-CONFIRMED BY H21. |
| L5: narrativa en Runtime Activity | SOURCE-INSPECTION FINDING; NOT EXECUTION-CONFIRMED BY H21. |
| Segundo gate de L2, `executeAction()` selección de evaluación | Sigue respaldado por fuente; esa rama no fue ejecutada con B. |

No se reutilizó el scenario.id de A, no se alteraron gates y no se reparó L2 para alcanzar las siguientes fugas.

## FALSIFICATION ANALYSIS

La diferencia legítimamente situada es `scenario.id = family-adventure-costa`, conservando la misma Experience y los mismos comandos/checkpoints. B supera resolución y producción del snapshot genérico, pero el pipeline no entrega sus read models de aventura. Para cumplir la hipótesis sería necesario modificar una responsabilidad compartida congelada o falsear la identidad situada de B. Ninguna alternativa está permitida en esta baseline.

El fallo pertenece al objeto experimental, no a un problema de red, permisos o entorno. Por eso el veredicto no es INCONCLUSIVE. Tampoco basta el éxito de compilación o la coincidencia de provider para SUPPORTED WITH QUALIFICATION.

## H21 VERDICT

```text
H21 → FALSIFIED
FIRST MATERIAL FALSIFIER → L2: initial guest/supervision projection selection depends on Scenario A identity
LAST SUCCESSFUL FACTORY BOUNDARY → resolution + distinct provider instances + generic initial snapshots
```

La refutación es local al pipeline congelado y al ámbito A/B definido. No implica que la reutilización sea imposible ni que una futura reparación vaya a ser suficiente.

## Verificación técnica y reproducción

Desde `products/convercus-app/prototype/`:

```bash
H21_RECORD_PATH=../docs/session-21-execution-trace.json npm test -- src/demo-factory/composition-boundary-h21.test.ts
npm run check
```

El primer comando vuelve a generar la traza y su timestamp; conservar la evidencia existente antes de usarlo si se necesita trazabilidad de distintas ejecuciones. Sin `H21_RECORD_PATH`, el test reproduce y comprueba el STOP sin escribir la traza.

| Verificación del 13 de septiembre | Resultado |
| --- | --- |
| Harness focalizado | 1/1 PASS: registra falsación y se detiene. |
| Typecheck final | PASS. |
| Lint | PASS. |
| Suite completa | 83/83 PASS, 15 archivos. |
| Build TypeScript + Vite/PWA | PASS. |
| Archivos compartidos/protegidos congelados | Sin cambios. |
| Bootstrap fuera del import/registro B | Sin cambios. |
| Artefactos previos de A y otras demos | Preservados. |

El primer typecheck del harness necesitó una referencia a los tipos Node ya instalados para sus imports de filesystem/hash. Se añadió únicamente al nuevo archivo experimental; no se modificaron tsconfig, dependencias ni componentes compartidos. El ensayo ya había producido la observación L2 y ninguna corrección del harness cambió su punto de STOP.

Que el harness pase significa que la observación de falsación es reproducible. No es un test que declare funcional a B. Sus guardas de hashes pertenecen a esta baseline experimental; no promueven esas implementaciones a invariantes permanentes del producto.

## ARCHITECTURAL CONSEQUENCE

Se registra la responsabilidad observada: el adaptador común condiciona las perspectivas de una Experience a la identidad concreta de un Scenario. La distinción:

```text
Scenario identity != execution behavior selection
```

queda como **candidata a revisión**, sin seleccionar un mecanismo de resolución ni consolidarla como nueva arquitectura. No se crea un registro de comportamientos/capacidades ni un motor de Experience/perspectivas.

```text
Architecture v0.5 → ACTIVE / unchanged pending review
ADR-001–005 → ACCEPTED / unchanged
TES → unchanged
Product Semantic Contract → unchanged
PSC-P01 → unchanged
PSC-P02 → NOT CREATED
Group → NOT INTRODUCED
new ADR → NOT CREATED
```

## WHAT H21 DOES NOT PROVE

No prueba ejecución completa de B, validación de su semántica en interacción, aislamiento de acciones/resets A/B, integridad de su evaluación, ausencia de fugas de contenido ni funcionamiento de sus pantallas. No prueba que eliminar el gate baste para completar H21. Tampoco justifica una abstracción general, multi-tenant, motor de reglas, nuevo contrato semántico o promoción de formas experimentales.

## REMAINING PRESSURES

Quedan abiertas la relación entre identidad situada y selección de comportamiento, el binding del contexto factual a evaluación, la procedencia del contenido de proyección/pantalla/Activity y el aislamiento completo de instancias. L1/L3/L4/L5 conservan su estatus de inspección. Una reparación produciría otra baseline y requeriría otro ensayo; aquí no se elige ni se implementa.

```text
STOP → PRESERVED AT FIRST MATERIAL FALSIFIER
SHARED REPAIR → NOT PERFORMED
NEXT FRONTIER → NOT SELECTED
SESSION 22 / H22 → NOT OPENED / NOT SELECTED
```
