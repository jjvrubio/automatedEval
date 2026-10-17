# S38 — Evidence-integrity manifest

Estado: TEST INFRASTRUCTURE EVIDENCE RULE / LOCAL / EXPERIMENTAL / NOT PROMOTED. Aplicación limitada a las baselines H21–H23 y sus tres harnesses. No modifica TES, PSC ni arquitectura.

## Inclusión material

El manifest positivo [material-source-set.json](../../../prototype/src/demo-factory/test-fixtures/h38/material-source-set.json) mantiene todo path/hash original excepto las cinco rutas Finder auditadas individualmente. Incluye fuentes, harnesses, contratos, declaraciones, resultados y documentación cuya preservación pertenecía al experimento. Totales: 51, 74 y 94 entradas materiales; no son archivos únicos.

Antes de enumerar se verifica SHA-256 del JSON histórico completo y la partición exacta material+incidental. Membresía desconocida, hash distinto, omisión o clasificación conflictiva falla. Las excepciones allowedChangedFiles y sus comprobaciones siguen en cada harness sin cambios.

## Metadata incidental

Sólo 00-governance/.DS_Store, 01-semantic-contract/.DS_Store, 01-semantic-contract/source-excerpts/.DS_Store, 02-shared-contracts/.DS_Store y, para H23, products/convercus-app/prototype/src/.DS_Store. La justificación es uso/provenance experimental documentado, no extensión.

Sus hashes permanecen en los inventarios históricos como registro de captura; no se leen los archivos ambientales. Un .DS_Store declarado material sí debe verificarse. Nuevos archivos del filesystem fuera del conjunto no alteran replay; nuevas entradas en el inventario exigen clasificación explícita y de lo contrario fallan.

## Identidad y bytes

El selector identifica paths lógicos POSIX mediante NFC; rechaza colisiones, traversal, absolutos y backslash. No aplica case-folding ni normaliza contenido. Los hashes siguen midiendo bytes exactos.

Los lectores heredados conservan sus rutas léxicas y requieren cwd/rutas absolutas coherentes. No garantizan equivalencia /var↔/private/var. NFC/NFD observado en macOS no certifica otros filesystems.

## Precedencia y separación

Ruta específica de la sesión → mapas antiguos explícitos del harness → reader H34 → reader H36 → fs nativo. Una ruta archivada antigua ya elegida no se sustituye por una nueva; archivo requerido ausente produce fallo. No hay búsqueda por presencia ni recursión de mapas.

H37 y verificaciones actuales usan fuentes actuales y lector nativo; los mocks archivados permanecen locales a los harnesses históricos. Las copias nuevas h37 sólo prueban el delta de infraestructura. No se instala un interceptador global.

## Falsabilidad

Metadata ausente/presente: mismos resultados materiales. Mutación material: hash mismatch. Retirada material: error de import/lectura. Fuente actual mutada: falla H37, no los replays que usan su archive. Shadow control: antigua seleccionada aunque existan nueva y actual.

La igualdad de bytes no reemplaza el replay ejecutable; se requieren ambos. No hay fuente material del conjunto protegida únicamente por existencia. Las trazas comparadas conservan todo salvo el timestamp superior de observación entre ejecuciones; ningún timestamp factual se descarta.

## Límites y gobierno

La prueba se realizó con macOS arm64, Node oficial 24.14.0 y dependencias existentes. Las comparaciones temporales mantienen origen del logo constante y declaran acceso Vite al asset compartido. DOM con URL absoluta y alias de paths siguen como presiones abiertas. No hay portabilidad universal, instalación hermética ni regla general para sesiones futuras.

Preservar informes, inventarios, trazas y fallos originales. Nuevas clasificaciones requieren nueva evidencia; nunca regenerar hashes históricos desde el working tree para obtener PASS.
