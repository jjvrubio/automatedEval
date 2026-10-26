# Obsidian Bridge — Vault Manager v1.0.1

## Scope
Administers an existing `catalog.json` and checks duplicate identifiers, paths, ports, credential references, unsafe paths, nested-vault exclusions, and TCP availability on loopback. Uses Python standard library only.

**It does not implement R0–R4 authorization. It does not connect to MCP, access Keychain, edit iCloud vault files, or modify Codex configuration. A listening port is NOT proof of which vault owns the server.**

`documents-root` is an organizational inventory record only. It is never an
operational vault and cannot have a connection. Nested vault records retain
their independent identities, but are reported as `NOT_OPERATIONAL_NESTED`
when they are descendants of another operational vault. The `nested_vaults:
exclude` policy is therefore enforced as an operational exclusion, not as
removal of inventory records.

## Install on your Mac

1. Unzip the package to any location outside your iCloud Obsidian directory.
2. Copy your CURRENT `catalog.json` (the version you already edited to add METIS) into the same folder, replacing the example catalog if you use one.
3. In Terminal, `cd` to that folder.

## Commands

```bash
python3 vault_manager.py --catalog ./catalog.json list
python3 vault_manager.py --catalog ./catalog.json validate
python3 vault_manager.py --catalog ./catalog.json status
```

To add or update a connection in the catalog only:

```bash
python3 vault_manager.py --catalog ./catalog.json set-connection metis-vision --port 27125 --credential-ref obsidian-bridge-metis
```

Changes are atomic and preceded by a timestamped catalog backup. Existing catalog entries are preserved. Do not store actual tokens in the catalog.

Backups include microseconds and a collision check. Tests should always use a
temporary catalog copy; the production catalog is not modified by validation
or status checks.

## Limitations / next milestone

- Filesystem inventory is based on the local Mac; running `validate` elsewhere will warn that the root is unavailable.
- Catalog structure, policy values, connection fields, and reserved
  `documents-root` semantics are validated before filesystem inspection.
- Symlink components are denied, including intermediate components. Canonical
  paths that escape the configured root are rejected.
- `status` checks that a TCP service responds on a configured port, not that it belongs to the specified Obsidian vault or that the certificate is trusted. The next stage will verify server identity and authenticated read-only access.
- Deny all production write access until a policy-enforcing gateway blocks direct MCP writes and implements per-vault and per-document protections.
- Do not copy `.obsidian` into version control; this may include plugin secrets.

## Provisioning Plan Generator v0.1

`vault_provisioner.py` is a read-only planner. Its `inspect`, `plan`, and
`dry-run` commands inspect only the catalog, vault directories,
`manifest.json`, and `community-plugins.json`. It never reads plugin
`data.json`, Markdown documents, Keychain entries, or MCP endpoints.

```bash
python3 vault_provisioner.py --catalog ./catalog.json inspect
python3 vault_provisioner.py --catalog ./catalog.json plan
python3 vault_provisioner.py --catalog ./catalog.json dry-run
```

The output uses plan schema `0.1` and keeps these dimensions separate:

- `INVENTORIED` is represented by a catalog record.
- `PHYSICALLY_INSTALLABLE` describes a safe filesystem candidate.
- `PROVISIONED` describes plugin files and activation metadata only.
- `CONNECTION_ELIGIBLE` remains pending VM-04 or blocked for nested scopes.
- `DOCUMENT_ACCESS_AUTHORIZED` is never asserted by this tool.

`documents-root` is excluded from provisioning. Nested vaults remain in the
plan but their operational connection is blocked until parent-child isolation
is verified. Ports are reported as declared or unassigned; no TCP checks or
permanent assignments are performed.

## VP-04 / VP-05A.1: ejecución transaccional aislada

El ejecutor está en
[`vault_provisioner_executor.py`](./vault_provisioner_executor.py). Solo aplica
planes `0.1` preparados como planes ejecutables `0.2` a un `lab_root` absoluto
y explícito sobre fixtures temporales. Comprueba snapshots y hashes bajo lock,
usa escrituras descriptor-relative sin seguir symlinks, mantiene journal y
backup externos, y ofrece recuperación explícita con detección de conflictos.
No accede a Keychain, credenciales, `data.json`, Markdown, iCloud, servidores
MCP ni configuraciones reales.

La arquitectura, pruebas y límites están documentados en
[`VP-04_plan_executor.md`](./VP-04_plan_executor.md). La siguiente etapa
requiere autorización separada y un laboratorio nuevo, desechable y fuera de
iCloud; VP-05A.1 no aprovisiona las bóvedas reales ni asigna puertos
definitivos.

## VP-03: nested-vault isolation

The static analysis and disposable fixture laboratory are documented in
[`VP-03_nested_vault_isolation.md`](./VP-03_nested_vault_isolation.md). The
laboratory never opens Obsidian, starts REST/MCP servers, reads secrets, or
touches production vaults. Nested-vault connections remain blocked until the
approved dynamic protocol provides evidence; a catalog exclusion is not server
isolation.

## VP-03.1: topología tras reorganización física

La inspección read-only de las rutas trasladadas y la actualización propuesta,
todavía no aplicada, están documentadas en
[`VP-03.1_topology_reconciliation.md`](./VP-03.1_topology_reconciliation.md).
`Scaling Up` y `MIU - Certificado en Liderazgo` conservan sus identidades con
nuevas rutas independientes; `Martech/Cookieless` es una carpeta temática sin
`.obsidian` y no debe mantenerse como bóveda operativa.

## VP-03.2: corrección definitiva de topología

La verificación de que `MMAA MODAM` es la bóveda independiente y `Scaling Up`
una carpeta temática está documentada en
[`VP-03.2_topology_correction.md`](./VP-03.2_topology_correction.md). La
reconciliación propuesta añade `mmaa-modam`, retira `scaling-up` y
`cookieless`, y actualiza la ruta de `miu-liderazgo`; todavía no se ha aplicado
al catálogo.
