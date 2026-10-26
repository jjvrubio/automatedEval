# VP-04 / VP-05A.1 — Ejecutor transaccional de aprovisionamiento

## Alcance implementado

[`vault_provisioner_executor.py`](./vault_provisioner_executor.py) aplica
planes de solo lectura `plan_schema_version: 0.1` después de prepararlos como
planes ejecutables `0.2`. El contrato ejecutable contiene la identidad
canónica, hashes del origen y un snapshot del estado esperado.

El ejecutor:

- exige un ámbito `OPERATIONAL` independiente y un `lab_root` absoluto;
- rechaza rutas ambiguas, escapes, symlinks, configuraciones inválidas y
  conflictos de identidad o versión;
- instala solamente `manifest.json` y `main.js` sintéticos del plugin 5.5.2;
- conserva plugins ajenos y entradas existentes de activación;
- verifica los hashes del origen y de los archivos instalados;
- rechaza planes obsoletos con `STALE_PLAN` antes de escribir;
- usa locks exclusivos compartidos por aplicación y recuperación;
- realiza rollback automático de cambios parciales;
- conserva un journal y respaldo independiente fuera de `lab_root`;
- no lee `data.json`, Markdown, Keychain ni credenciales, y no inicia MCP.

Las escrituras del laboratorio se realizan con descriptores de directorio,
`O_NOFOLLOW`, temporales únicos y reemplazos atómicos relativos al descriptor.
La protección no depende únicamente de `resolve()` o `is_symlink()`.

## Contratos de plan

El planador de [`vault_provisioner.py`](./vault_provisioner.py) conserva el
contrato `0.1` y continúa siendo de solo lectura. La función
`prepare_execution_plan()` añade `execution.schema_version: "0.2"` y captura:

- identidad de bóveda y ruta canónica;
- identidad y versión del plugin;
- hashes del origen;
- hashes, tamaños, permisos y existencia de `manifest.json`, `main.js` y
  `community-plugins.json`;
- estado de activación.

`apply_plan()` rechaza un plan sin esa preparación. Comprueba el snapshot bajo
el lock e informa `STALE_PLAN` si cambia cualquier precondición.

## Journal, respaldo y recuperación

Cada transacción crea fuera del laboratorio:

- un journal durable;
- un backup de los archivos existentes;
- hashes de cada backup;
- el estado esperado;
- las operaciones previstas y confirmadas;
- la última instantánea confirmada;
- el estado transaccional.

`recover_transaction()` solo restaura si el estado actual coincide exactamente
con la última instantánea confirmada y los backups conservan sus hashes. Si
detecta cambios devuelve `RECOVERY_CONFLICT` sin escribir. Los locks se
mantienen mediante `flock`; no se eliminan archivos de lock al finalizar para
evitar borrar el lock de otro proceso.

## Ejecución y pruebas

```bash
cd 03_Personal/obsidian_vault_manager
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_vault_provisioner.py test_vault_provisioner_executor.py
```

La suite actual pasa 37 tests. Los fixtures se crean en directorios
temporales; no leen ni escriben `catalog.json`, iCloud Drive,
`Obsidian-Bridge-Lab` ni configuraciones reales.

Las pruebas adversariales cubren:

- symlink inicial y sustitución de ruta durante la operación;
- lock con procesos independientes;
- aplicación y recuperación bajo el mismo lock;
- interrupción abrupta antes de completar la transacción;
- recuperación exitosa desde otro proceso;
- rechazo de recuperación tras cambios;
- plan obsoleto sin escrituras;
- reejecución idempotente;
- plugins ajenos;
- integridad de backups y journals;
- ausencia de escrituras fuera de la fixture.

## Interfaz de reversión

El rollback síncrono restaura los archivos que existían y elimina los creados.
La recuperación posterior requiere un recibo de transacción y una ruta
relativa coincidente. No existe restauración desde una ruta arbitraria.

## Límites residuales

- La protección descriptor-relative cubre las escrituras del ejecutor, no un
  proceso que modifique contenido mediante descriptores que ya posea.
- El journal y el backup dependen de que `backup_root` esté en un volumen local
  confiable y disponible.
- Una interrupción durante la creación del backup se rechaza si el backup no
  es íntegro; no se intenta restaurar desde un respaldo incompleto.
- No se prueba ni implementa todavía la activación funcional de Obsidian, REST,
  MCP, certificados, Keychain o puertos.

## Pendiente antes de una prueba autorizada

No se deben realizar instalaciones sobre
`/Users/juanjo/Obsidian-Bridge-Lab` ni sobre bóvedas reales. VP-05B requiere
un laboratorio nuevo, desechable y fuera de iCloud, Obsidian cerrado,
aprobación expresa y verificación independiente del backup.
