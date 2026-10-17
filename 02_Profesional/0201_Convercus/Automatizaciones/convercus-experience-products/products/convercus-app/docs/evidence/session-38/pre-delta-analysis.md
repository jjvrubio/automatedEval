# S38 — análisis y decisión anterior al delta

Esta decisión se registra después de reproducir los tres fallos y antes de modificar los harnesses del proyecto. El candidato se validará primero en una copia temporal del proyecto. No se han cambiado fuentes de producto, expectativas ni rutas históricas.

## Causa e intención histórica

| Sesión | Inventario recibido | Fallo y finalidad | Hipótesis / variable / veredicto conservado |
| --- | --- | --- | --- |
| H21 | 55 entradas = 8 shared + 47 protected; 51 materiales + 4 metadatos | Línea 69: SHA(read(frozenPath)) == hash, dentro de la preservación previa a resolveDemo; congela fuentes y documentos al añadir B | Reutilización de composición con maquinaria congelada; B distinto; FALSIFIED en las perspectivas iniciales B; cero acciones/reset |
| H22 | 78 entradas; 74 materiales + 4 metadatos; 2 excepciones ya declaradas | Línea 59: SHA(read(ruta histórica)) == hash; protege todo salvo dos cambios autorizados, verificados aparte | Dos selectores Scenario.id→experienceRef; SUPPORTED WITH QUALIFICATION; persiste contexto Aurora en B |
| H23 | 99 entradas; 94 materiales + 5 metadatos; 5 excepciones ya declaradas | Línea 44: mismo hash de cada entrada no exceptuada; diferencias de adapter/evaluation comprobadas aparte | Binding situado Scenario.contexts, sin reescribir Evidence; SUPPORTED WITH QUALIFICATION |

Las tres cadenas pasan primero por las rutas particulares de su sesión y luego historical-read S34→S36→node:fs. Ningún mapa contiene 00-governance/.DS_Store: cae en la lectura del working tree. ENOENT sucede antes del hash/assertion, no es una determinación semántica. La reproducción conserva stack y comando en failure-reproduction.log.

## Materialidad investigada

Una fuente es material cuando su contenido/identidad participa en lógica de producto/harness, declaraciones de composición/contrato, entradas/resultados/expectativas/trazas o preservación intencional de fuentes/documentos del experimento. Su hash se mantiene. No se reduce el conjunto porque un fichero no sea importado por JavaScript: documentos de autoridad y trazas anteriores también estaban protegidos intencionalmente.

El informe original H21, sección BASELINE HASH / SHARED FILES FROZEN, ya identifica sus cuatro .DS_Store como «sin significado arquitectónico». Los hashes de esas cuatro entradas se repiten en H22 y H23. H23 añade una quinta en prototype/src. La búsqueda en fuentes productivas no encuentra lector, generador, import ni interpretación de .DS_Store; las referencias encontradas son inventarios y controles de preservación. Traces H21–H23 no contienen datos obtenidos de sus bytes. Su alteración habría detenido un chequeo ambiental, sin cambiar el pipeline, sus facts ni el STOP semántico documentado.

No se preservaron los bytes de los cinco archivos históricos como evidencia: sólo sus hashes de inventario. El proceso concreto que creó esos archivos ausentes no puede reconstruirse. El archivo .DS_Store actualmente presente en la raíz del proyecto tiene cabecera 0000000142756431 (Bud1); su tipo y la clasificación documental corresponden a metadata Finder. No hay evidencia de que fuese una declaración experimental creada por producto/tests. Se clasifica cada una de las cinco rutas como INCIDENTAL ENVIRONMENT METADATA por estos usos y por el resultado documentado, no sólo por su extensión.

Los bytes de una muestra ambiental ya presente en este Mac se podrán usar exclusivamente dentro del fixture temporal B como perturbación. No se recupera/fabrica metadata de la baseline ni se instala .DS_Store en el working tree para obtener PASS.

## Familias inspeccionadas

| Familia | Observación / regla |
| --- | --- |
| .DS_Store | Cinco rutas concretas en H21–H23; exclusión individual auditada. Otros nombres iguales no se excluyen automáticamente del manifest |
| Thumbs.db / desktop.ini / AppleDouble ._* | No aparecen en inventarios/fuentes inspeccionados. Sin nueva blacklist. Archivos nuevos fuera del material declarado no afectan a replay; inclusión futura exige clasificación |
| Temporales editor / swap | Ninguno en inventario recibido. Podrían contener una fuente útil: no se decide por sufijo ni se borran |
| tsbuildinfo | Caché regenerable de tsc; no está en las baselines H21–H23 ni es input factual. Ya excluida en capturas recientes; no regla nueva sobre todas las extensiones |
| dist / build | Bundle/PWA generado por build; sin entradas H21–H23. No sustituye fuentes congeladas ni aceptación visual; logs de build históricos declarados sí se conservan |
| node_modules | Dependencias necesarias para ejecutar, reconstruibles desde package/lock; no byte-inventariadas por estas baselines. Versiones/toolchain son condición del entorno, no outcome semántico |

## Estrategias comparadas antes del delta

| Estrategia | Fidelidad / ocultación | Portabilidad | Coste / complejidad / reversibilidad | Compatibilidad |
| --- | --- | --- | --- | --- |
| A. Allowlist material explícita | Alta si particiona íntegramente baseline y conserva hashes; entrada nueva/no clasificada debe fallar | Independiente de archivos ambientales | Duplica inventario; acotable a tres baselines; fácil revertir | Conserva JSON y assertions originales |
| B. Exclusión incidental explícita | Adecuada sólo para rutas justificadas; glob por nombre puede ocultar evidencia futura | Resuelve el caso observado | Cambio pequeño; riesgo de crecimiento de blacklist | Compatible, pero frontera positiva más débil sola |
| C. Manifest por raíces/tipos del experimento | Positiva, pero puede omitir docs/formatos de las baselines heredadas | Buena para nuevas capturas delimitadas | Requiere definir ownership general; mayor cambio | No necesario para restaurar estos tres replays |
| D. Paquete hermético archivado | Puede fortalecer selección ejecutable, pero necesita closure de imports y runtime | Mejor aislamiento, no elimina toolchain | Reestructura todos los replays; alto coste | Excesivo para S38; no adoptado |
| E. Captura íntegra del filesystem | Iguala bytes sin separar materialidad | Acopla a Finder/equipo | Mantiene coste creciente; ausencia exige metadata imposible/no autorizada | Conserva mecanismo actual pero no soluciona dependencia |

Decisión candidata: A acotada a H21–H23, con partición auditada de las cinco rutas incidentales (evidencia B) y fail-closed para inventario/hash no coincidente. Todos los demás paths/hashes heredados se incluyen positivamente. No se edita ningún JSON histórico ni la lista original allowedChangedFiles. Se sustituirá sólo la enumeración de cada loop de preservación; el cuerpo del loop y el resto del harness deben quedar byte-idénticos.

## Gate antes de aplicar

El manifest candidato y el selector se instalan primero en fixtures temporales, junto con la sustitución exacta de import+enumeración de los tres harnesses. Se exige H21–H23 PASS con metadata ausente/presente y mismo resultado material; mutación y retirada de un archivo material deben fallar. La prueba actual H37 debe seguir usando fuentes actuales. Si falla un falsador material, STOP: no se propaga el candidato al proyecto.

Las rutas existentes y sus precedencias quedan congeladas. La normalización NFC del nuevo inventario sólo identifica rutas lógicas, rechaza colisiones y no modifica contenido; no se añade case-folding. La cadena antigua se ensaya tal como existe, sin sustituirla por un buscador de archivos.
