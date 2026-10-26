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
