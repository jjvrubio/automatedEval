# S33 — inspección anterior al delta

La baseline se capturó antes de modificar producto o harness. Esta decisión precede al cambio de App. No se reconstruyen H25–H32.

## Fuentes inspeccionadas

- `prototype/src/demo-factory/contracts.ts`: `SupervisionPerspectiveReadModel`, `SubjectReference`, `ScenarioDefinition`, `EvidenceInput`.
- `prototype/src/demo-factory/vertical-evaluation.ts`: `projectSupervisionPerspective()`.
- `prototype/src/demo-factory/artifacts.ts` y `costa-artifacts.ts`: Scenario A/B y declaraciones separadas H27.
- `prototype/src/demo/mock-adapter.ts`: construcción, `subjectStates`, `projectSnapshot`, aceptación de acciones, atribución y reset.
- `prototype/src/app/App.tsx`: rama `SystemPage` que consume `snapshot.supervisionPerspective`.

## Matriz por sujeto (misma estructura en A y B)

| Sujeto / campo fuente | Responsabilidad semántica | Representación previa | Información añadida | Autorización para ese añadido |
| --- | --- | --- | --- | --- |
| `subject-p1` / `Scenario.subjects[].id` → `SP.subjects[].id` | Referencia operacional literal | Encabezado `P1 · Lucía`; detalle `subject-p1` | Alias P1 y nombre Lucía | Ninguna en SP; branch local. H27 autoriza Lucía sólo para GP |
| `subject-p2` / misma ruta | Referencia operacional literal | Encabezado `P2 · Huésped 2`; detalle `subject-p2` | Alias P2 y presentación humana numerada | Ninguna en SP; rama else aplicable incluso a refs desconocidas |
| Ambos / presencia en `Scenario.subjects` → `exists: true` | Pertenencia a la colección operacional suministrada | `exists: true` | Ninguna dentro de esta semántica local | Proyector; no prueba identidad humana ni existencia universal |
| p1 / `subjectStates[id]` | Estado operacional, inicialmente `not-enlisted` | Estado literal | Ninguna | Estado mantenido por adapter; fallback existente `not-enabled` |
| p2 / `subjectStates[id]` | Estado operacional, inicialmente `not-enabled` | Estado literal | Ninguna | Misma autoridad; activar cambia estado, no identidad |
| Ambos / `evaluation.evidence[].subjects[].id` | Atribución por igualdad de id; recuento de elementos con al menos una coincidencia | `Evidence: n` y refs en lista de Evidence | Ninguna | Proyector; cuenta Evidence, no número de personas o identidades |
| p1 / `Scenario.operationalSessionSubjectRef` → `SP.sessionSubjectRef` | Referencia operacional de sesión | `Cuenta/sesión operativa: subject-p1` | Asociación verbal con cuenta, no establecida por ese campo | Presión separada; texto congelado |
| p2 / ausencia de selección como sesión | No es el ref de sesión declarado en A/B | Sin fila individual de sesión | No permite inferir propiedad, parentesco ni viewer | Ninguna de esas relaciones está declarada |

## Descomposición de copy

`P1` y `P2` no son valores declarados de SP ni alias explícitos de Scenario. El branch de App los añade. Extraerlos de la sintaxis de `subject-p1/p2` sería parsing no autorizado por H33.

`Lucía` coincide con fuentes de cuenta/GP en A pero SP no recibe esas relaciones. `Huésped 2` añade una presentación humana y numeración no declaradas por SP. En B el mismo branch conserva copy A, aunque GP use Inés/Mateo. No procede reemplazar nombres A por nombres B.

## Candidatos y decisión

`SubjectReference.type = individual` y `role = guest` existen en Scenario y Evidence. Son clasificación y rol; no son nombres, alias ni etiquetas humanas. El proyector no los transporta a SP. No se añade transporte: `SP.subjects[].id` ya basta para distinguir y correlacionar las tarjetas con estado, Evidence y sesión.

Selección: renderizar exactamente `subject.id` en el encabezado, sin parsing, índice, lookup, nombres humanos ni nueva relación. El detalle ya contiene ese mismo identificador; su repetición se conserva porque el detalle está fuera del delta autorizado.

SP conoce referencia, presencia declarada, estado, atribución/recuento, ref de sesión y resultados evaluados. No conoce nombre humano, propiedad de cuenta, viewer ni autoridad presentacional de GP. `same subjectRef != same presentation authority`.

## Controles previstos

App vigente A/B: recorrer acciones públicas y reset; navegar a Supervisión, Inicio y Activity en cada fase. Comparar contra App S32 archivada y traza S32: snapshots/evaluaciones completos idénticos; DOM idéntico salvo encabezados de sujetos en SP. Perturbar por separado H27, member.name, brand.name, intro H32, narrativa H30 y Activity H25. Estado/Evidence se ejercitan por acciones legítimas. Orden y ref desconocida se observan sólo en proyector/read model aislado, sin ampliar Scenario productivo ni ejecutar acciones con ese sujeto. Retail/Arrival deben seguir sin SP familiar. Validación DOM y visual se declararán por separado.

Condición de avance: fuente operacional existente suficiente para identificación diagnóstica neutral. Si la ejecución requiere relaciones adicionales, STOP. Esta selección no afirma suficiencia para UX humana, identidad real ni otros productos.
