#!/usr/bin/env python3
"""Transactional executor for disposable Vault Provisioner laboratories."""

import errno
import fcntl
import hashlib
import json
import os
import uuid
from pathlib import Path

import vault_provisioner


EXPECTED_PLUGIN_VERSION = "5.5.2"
PLUGIN_FILES = vault_provisioner.REQUIRED_PLUGIN_FILES
ACTIVATION_NAME = "community-plugins.json"
EXECUTION_SCHEMA_VERSION = "0.2"
TRANSACTION_DIR_NAME = "transactions"
LOCK_DIR_NAME = "locks"


class ProvisioningError(RuntimeError):
    """Raised when a laboratory operation is rejected or cannot be completed."""


class StalePlanError(ProvisioningError):
    """Raised when the filesystem no longer matches an executable plan."""


class RecoveryConflictError(ProvisioningError):
    """Raised when recovery would overwrite an unexpected filesystem state."""


class ActiveLockError(ProvisioningError):
    """Raised when another process owns the vault transaction lock."""


def _safe_relative_path(value):
    if not isinstance(value, str) or not value or value == "." or Path(value).is_absolute():
        raise ProvisioningError("Plan contains an ambiguous relative_path")
    path = Path(value)
    if any(part in ("", "..") for part in path.parts):
        raise ProvisioningError("Plan contains an unsafe relative_path")
    return path


def _reject_symlinks(path, stop):
    current = Path(path)
    stop = Path(stop)
    while True:
        if current.is_symlink():
            raise ProvisioningError(f"Symlink is not allowed: {current}")
        if current == stop:
            return
        if current.parent == current:
            raise ProvisioningError(f"Path escapes laboratory root: {path}")
        current = current.parent


def _ensure_under_lab_root(lab_root, relative_path):
    root = Path(lab_root).expanduser()
    if not root.is_absolute():
        raise ProvisioningError("lab_root must be an absolute path")
    _reject_symlinks(root, root.parent)
    root = root.resolve(strict=False)
    relative = _safe_relative_path(relative_path)
    target = root.joinpath(relative)
    if os.path.commonpath((str(root), str(target))) != str(root):
        raise ProvisioningError("Target escapes laboratory root")
    _reject_symlinks(target, root)
    return root, target


def _validate_source(plugin_source):
    source = Path(plugin_source)
    if not source.is_absolute() or not source.is_dir():
        raise ProvisioningError("Plugin source directory is unavailable")
    _reject_symlinks(source, source)
    for name in PLUGIN_FILES:
        source_file = source / name
        if not source_file.is_file() or source_file.is_symlink():
            raise ProvisioningError(f"Plugin source is missing safe file: {name}")
    try:
        manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, TypeError, ValueError) as exc:
        raise ProvisioningError("Plugin source manifest is invalid") from exc
    if manifest.get("id") != vault_provisioner.PLUGIN_ID or manifest.get("version") != EXPECTED_PLUGIN_VERSION:
        raise ProvisioningError("Plugin source manifest has an unsupported identity/version")
    return source


def _validate_plan(plan):
    if not isinstance(plan, dict) or plan.get("plan_schema_version") != vault_provisioner.PLAN_SCHEMA_VERSION:
        raise ProvisioningError("Only plan schema version 0.1 is supported")
    if plan.get("catalog_status") != "VALID" or plan.get("writes_performed"):
        raise ProvisioningError("Plan must be valid and read-only")
    vaults = plan.get("vaults")
    if not isinstance(vaults, list) or len(vaults) != 1:
        raise ProvisioningError("Exactly one vault must be selected for laboratory provisioning")
    vault = vaults[0]
    if not isinstance(vault, dict) or vault.get("scope_type") != "OPERATIONAL":
        raise ProvisioningError("Only an independent operational vault can be provisioned")
    if vault.get("connection_eligibility") in ("EXCLUDED_ORGANIZATIONAL", "BLOCKED_NESTED_ISOLATION"):
        raise ProvisioningError("Vault connection scope is not eligible")
    if vault.get("provisioning_status") == "CONFLICT":
        raise ProvisioningError("Plan reports an existing provisioning conflict")
    return vault


def _digest_bytes(value):
    return hashlib.sha256(value).hexdigest()


def _digest(path):
    with path.open("rb") as file:
        return _digest_bytes(file.read())


def _open_directory(path, *, dir_fd=None):
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        return os.open(path, flags, dir_fd=dir_fd)
    except OSError as exc:
        if exc.errno == errno.ELOOP:
            raise ProvisioningError(f"Symlink is not allowed: {path}") from exc
        raise


def _open_relative_directory(root_fd, relative):
    current_fd = os.dup(root_fd)
    try:
        for component in relative.parts:
            next_fd = _open_directory(component, dir_fd=current_fd)
            os.close(current_fd)
            current_fd = next_fd
        return current_fd
    except Exception:
        os.close(current_fd)
        raise


def _open_or_create_directory(parent_fd, name):
    try:
        return _open_directory(name, dir_fd=parent_fd)
    except FileNotFoundError:
        try:
            os.mkdir(name, mode=0o700, dir_fd=parent_fd)
        except FileExistsError:
            pass
        return _open_directory(name, dir_fd=parent_fd)


def _open_layout(target_fd, *, create=False):
    if create:
        obsidian_fd = _open_or_create_directory(target_fd, ".obsidian")
        try:
            plugins_fd = _open_or_create_directory(obsidian_fd, "plugins")
        except Exception:
            os.close(obsidian_fd)
            raise
    else:
        obsidian_fd = _open_directory(".obsidian", dir_fd=target_fd)
        try:
            plugins_fd = _open_directory("plugins", dir_fd=obsidian_fd)
        except FileNotFoundError:
            return obsidian_fd, None, None
        except Exception:
            os.close(obsidian_fd)
            raise
    try:
        plugin_fd = (
            _open_or_create_directory(plugins_fd, vault_provisioner.PLUGIN_ID)
            if create
            else _open_directory(vault_provisioner.PLUGIN_ID, dir_fd=plugins_fd)
        )
    except FileNotFoundError:
        plugin_fd = None
    return obsidian_fd, plugins_fd, plugin_fd


def _read_at(parent_fd, name):
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(name, flags, dir_fd=parent_fd)
    except FileNotFoundError:
        return None
    try:
        with os.fdopen(fd, "rb") as file:
            data = file.read()
        return data
    except OSError as exc:
        if exc.errno == errno.ELOOP:
            raise ProvisioningError(f"Symlink is not allowed: {name}") from exc
        raise


def _file_state(parent_fd, name):
    data = _read_at(parent_fd, name)
    if data is None:
        return {"exists": False, "sha256": None, "size": None, "mode": None}
    fd = os.open(name, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0), dir_fd=parent_fd)
    try:
        mode = os.fstat(fd).st_mode & 0o777
    finally:
        os.close(fd)
    return {
        "exists": True,
        "sha256": _digest_bytes(data),
        "size": len(data),
        "mode": mode,
    }


def _snapshot_from_fds(target_fd):
    try:
        obsidian_fd, plugins_fd, plugin_fd = _open_layout(target_fd)
    except FileNotFoundError:
        obsidian_fd = plugins_fd = plugin_fd = None
    try:
        files = {}
        for name in PLUGIN_FILES:
            files[f"plugin/{name}"] = (
                _file_state(plugin_fd, name) if plugin_fd is not None
                else {"exists": False, "sha256": None, "size": None, "mode": None}
            )
        files["activation"] = (
            _file_state(obsidian_fd, ACTIVATION_NAME) if obsidian_fd is not None
            else {"exists": False, "sha256": None, "size": None, "mode": None}
        )
        return {
            "files": files,
            "plugin_dir": plugin_fd is not None,
            "obsidian_dir": obsidian_fd is not None,
        }
    finally:
        for fd in (plugin_fd, plugins_fd, obsidian_fd):
            if fd is not None:
                os.close(fd)


def _source_bytes(source):
    source_fd = _open_directory(source)
    try:
        values = {}
        for name in PLUGIN_FILES:
            data = _read_at(source_fd, name)
            if data is None:
                raise ProvisioningError(f"Plugin source is missing safe file: {name}")
            values[name] = data
        return values
    finally:
        os.close(source_fd)


def prepare_execution_plan(plan, plugin_source, lab_root):
    """Attach a versioned, read-only filesystem snapshot to a 0.1 plan."""
    vault = _validate_plan(plan)
    source = _validate_source(plugin_source)
    root, target = _ensure_under_lab_root(lab_root, vault.get("relative_path"))
    if not target.is_dir():
        raise ProvisioningError("Laboratory vault directory is unavailable")
    root_fd = _open_directory(root)
    try:
        target_fd = _open_relative_directory(root_fd, _safe_relative_path(vault["relative_path"]))
        try:
            source_values = _source_bytes(source)
            enabled = _activation_value(target_fd)["enabled"]
            execution = {
                "schema_version": EXECUTION_SCHEMA_VERSION,
                "lab_root": str(root),
                "target_path": str(target),
                "vault_id": vault["vault_id"],
                "relative_path": vault["relative_path"],
                "plugin_id": vault_provisioner.PLUGIN_ID,
                "plugin_version": EXPECTED_PLUGIN_VERSION,
                "source_hashes": {name: _digest_bytes(value) for name, value in source_values.items()},
                "expected_state": _snapshot_from_fds(target_fd),
                "activation_enabled": enabled,
            }
        finally:
            os.close(target_fd)
    finally:
        os.close(root_fd)
    result = dict(plan)
    result["execution"] = execution
    return result


def _activation_value(target_fd):
    try:
        obsidian_fd, plugins_fd, plugin_fd = _open_layout(target_fd)
    except FileNotFoundError:
        return {"exists": False, "enabled": False, "sha256": None}
    try:
        data = _read_at(obsidian_fd, ACTIVATION_NAME)
        if data is None:
            return {"exists": False, "enabled": False, "sha256": None}
        try:
            values = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, TypeError, ValueError) as exc:
            raise ProvisioningError("Existing activation configuration is invalid") from exc
        if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
            raise ProvisioningError("Existing activation configuration is unknown")
        return {
            "exists": True,
            "enabled": vault_provisioner.PLUGIN_ID in values,
            "sha256": _digest_bytes(data),
        }
    finally:
        for fd in (plugin_fd, plugins_fd, obsidian_fd):
            if fd is not None:
                os.close(fd)


def _validate_execution(plan, root, target, vault, source_values):
    execution = plan.get("execution")
    if not isinstance(execution, dict) or execution.get("schema_version") != EXECUTION_SCHEMA_VERSION:
        raise ProvisioningError("Executable plan schema 0.2 is required; prepare the 0.1 plan first")
    if execution.get("lab_root") != str(root) or execution.get("target_path") != str(target):
        raise StalePlanError("STALE_PLAN: laboratory identity changed")
    if execution.get("vault_id") != vault.get("vault_id") or execution.get("relative_path") != vault.get("relative_path"):
        raise StalePlanError("STALE_PLAN: vault identity changed")
    expected_hashes = execution.get("source_hashes")
    actual_hashes = {name: _digest_bytes(value) for name, value in source_values.items()}
    if expected_hashes != actual_hashes:
        raise StalePlanError("STALE_PLAN: plugin source changed")
    return execution


def _external_root(root, backup_root):
    base = Path(backup_root).expanduser() if backup_root is not None else root.parent / f".{root.name}-vp05-state"
    if not base.is_absolute():
        raise ProvisioningError("backup_root must be an absolute path")
    _reject_symlinks(base, base.parent)
    base = base.resolve(strict=False)
    if os.path.commonpath((str(root), str(base))) == str(root):
        raise ProvisioningError("backup_root must be independent of lab_root")
    base.mkdir(parents=True, exist_ok=True)
    return base


def _lock_for(target, state_root):
    target = Path(target).expanduser().resolve(strict=False)
    lock_dir = state_root / LOCK_DIR_NAME
    lock_dir.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(str(target).encode("utf-8")).hexdigest()
    path = lock_dir / f"{key}.lock"
    file = path.open("a+")
    try:
        fcntl.flock(file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as exc:
        file.close()
        if exc.errno in (errno.EACCES, errno.EAGAIN):
            raise ActiveLockError("ACTIVE_LOCK: another transaction owns the vault") from exc
        raise
    return file, path


def _fsync_json(path, value):
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    with temporary.open("w", encoding="utf-8") as file:
        json.dump(value, file, ensure_ascii=False, indent=2)
        file.write("\n")
        file.flush()
        os.fsync(file.fileno())
    os.replace(temporary, path)
    directory_fd = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def _atomic_write(parent_fd, name, data, mode=0o600):
    temporary = f".vp05-{uuid.uuid4().hex}.tmp"
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(temporary, flags, mode, dir_fd=parent_fd)
    try:
        with os.fdopen(fd, "wb") as file:
            file.write(data)
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, name, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        os.fsync(parent_fd)
    except Exception:
        try:
            os.unlink(temporary, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        raise


def _backup_files(transaction_dir, target_fd):
    try:
        obsidian_fd, plugins_fd, plugin_fd = _open_layout(target_fd, create=False)
    except FileNotFoundError:
        obsidian_fd = plugins_fd = plugin_fd = None
    try:
        backup_dir = transaction_dir / "backup"
        backup_dir.mkdir()
        backups = {}
        for key, parent_fd, name in [
            *[(f"plugin/{item}", plugin_fd, item) for item in PLUGIN_FILES],
            ("activation", obsidian_fd, ACTIVATION_NAME),
        ]:
            data = _read_at(parent_fd, name) if parent_fd is not None else None
            if data is not None:
                backup_name = key.replace("/", "__")
                backup_path = backup_dir / backup_name
                backup_path.write_bytes(data)
                backups[key] = {"path": str(backup_path), "sha256": _digest_bytes(data)}
        return backups
    finally:
        for fd in (plugin_fd, plugins_fd, obsidian_fd):
            if fd is not None:
                os.close(fd)


def _state_equal(left, right):
    return left == right


def _read_enabled(target_fd):
    try:
        obsidian_fd, plugins_fd, plugin_fd = _open_layout(target_fd)
    except FileNotFoundError:
        return []
    try:
        data = _read_at(obsidian_fd, ACTIVATION_NAME)
        if data is None:
            return []
        try:
            values = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, TypeError, ValueError) as exc:
            raise ProvisioningError("Existing activation configuration is invalid") from exc
        if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
            raise ProvisioningError("Existing activation configuration is unknown")
        return values
    finally:
        for fd in (plugin_fd, plugins_fd, obsidian_fd):
            if fd is not None:
                os.close(fd)


def _write_operation(target_fd, key, data):
    obsidian_fd, plugins_fd, plugin_fd = _open_layout(target_fd, create=True)
    try:
        parent_fd, name = (plugin_fd, key.split("/", 1)[1]) if key.startswith("plugin/") else (obsidian_fd, ACTIVATION_NAME)
        _atomic_write(parent_fd, name, data)
    finally:
        for fd in (plugin_fd, plugins_fd, obsidian_fd):
            if fd is not None:
                os.close(fd)


def _remove_file(target_fd, key):
    try:
        obsidian_fd, plugins_fd, plugin_fd = _open_layout(target_fd)
    except FileNotFoundError:
        return
    try:
        parent_fd, name = (plugin_fd, key.split("/", 1)[1]) if key.startswith("plugin/") else (obsidian_fd, ACTIVATION_NAME)
        if parent_fd is not None:
            try:
                os.unlink(name, dir_fd=parent_fd)
                os.fsync(parent_fd)
            except FileNotFoundError:
                pass
    finally:
        for fd in (plugin_fd, plugins_fd, obsidian_fd):
            if fd is not None:
                os.close(fd)


def _cleanup_empty_layout(target_fd, expected_state):
    if expected_state.get("plugin_dir"):
        return
    try:
        obsidian_fd, plugins_fd, plugin_fd = _open_layout(target_fd)
    except FileNotFoundError:
        return
    try:
        if plugin_fd is not None:
            os.close(plugin_fd)
            plugin_fd = None
            try:
                os.rmdir(vault_provisioner.PLUGIN_ID, dir_fd=plugins_fd)
            except OSError:
                return
        try:
            os.rmdir("plugins", dir_fd=obsidian_fd)
        except OSError:
            return
        if not expected_state.get("obsidian_dir"):
            os.rmdir(".obsidian", dir_fd=target_fd)
    finally:
        for fd in (plugin_fd, plugins_fd, obsidian_fd):
            if fd is not None:
                os.close(fd)


def _restore_state(target_fd, expected_state, backups):
    for key, state in expected_state["files"].items():
        if state["exists"]:
            backup = backups.get(key)
            if backup is None:
                raise RecoveryConflictError(f"Missing backup for {key}")
            data = Path(backup["path"]).read_bytes()
            if _digest_bytes(data) != backup["sha256"] or backup["sha256"] != state["sha256"]:
                raise RecoveryConflictError(f"Backup integrity failure for {key}")
            _write_operation(target_fd, key, data)
        else:
            _remove_file(target_fd, key)
    _cleanup_empty_layout(target_fd, expected_state)


def _load_journal(path):
    try:
        with path.open(encoding="utf-8") as file:
            journal = json.load(file)
    except (OSError, TypeError, ValueError) as exc:
        raise ProvisioningError("Transaction journal is invalid") from exc
    if not isinstance(journal, dict) or journal.get("schema_version") != EXECUTION_SCHEMA_VERSION:
        raise ProvisioningError("Transaction journal schema is unsupported")
    return journal


def apply_plan(
    plan,
    plugin_source,
    lab_root,
    *,
    backup_root=None,
    fail_after=None,
    crash_after=None,
    crash_before=False,
):
    """Apply a prepared 0.2 plan using descriptor-relative writes."""
    vault = _validate_plan(plan)
    source = _validate_source(plugin_source)
    root, target = _ensure_under_lab_root(lab_root, vault.get("relative_path"))
    if not target.is_dir():
        raise ProvisioningError("Laboratory vault directory is unavailable")
    source_values = _source_bytes(source)
    state_root = _external_root(root, backup_root)
    lock_file, lock_path = _lock_for(target, state_root)
    try:
        root_fd = _open_directory(root)
        try:
            target_fd = _open_relative_directory(root_fd, _safe_relative_path(vault["relative_path"]))
            try:
                execution = _validate_execution(plan, root, target, vault, source_values)
                current = _snapshot_from_fds(target_fd)
                if not _state_equal(current, execution["expected_state"]):
                    raise StalePlanError("STALE_PLAN: laboratory state changed")
                if not target.is_dir():
                    raise StalePlanError("STALE_PLAN: target is no longer a directory")
                if vault.get("plugin_id") not in (None, vault_provisioner.PLUGIN_ID):
                    raise ProvisioningError("Plan plugin identity conflicts")
                enabled = _read_enabled(target_fd)
                if execution["activation_enabled"] != (vault_provisioner.PLUGIN_ID in enabled):
                    raise StalePlanError("STALE_PLAN: activation state changed")

                transaction_id = uuid.uuid4().hex
                transaction_dir = state_root / TRANSACTION_DIR_NAME / transaction_id
                transaction_dir.mkdir(parents=True)
                journal_path = transaction_dir / "journal.json"
                journal = {
                    "schema_version": EXECUTION_SCHEMA_VERSION,
                    "transaction_id": transaction_id,
                    "lab_root": str(root),
                    "target_path": str(target),
                    "vault_id": vault["vault_id"],
                    "relative_path": vault["relative_path"],
                    "expected_state": execution["expected_state"],
                    "last_state": current,
                    "operations": [f"plugin/{name}" for name in PLUGIN_FILES] + ["activation"],
                    "confirmed_operations": [],
                    "backups": {},
                    "state": "PREPARED",
                }
                _fsync_json(journal_path, journal)
                journal["backups"] = _backup_files(transaction_dir, target_fd)
                journal["state"] = "BACKED_UP"
                _fsync_json(journal_path, journal)
                if crash_before:
                    os._exit(91)

                changed = []
                for index, name in enumerate(PLUGIN_FILES, start=1):
                    key = f"plugin/{name}"
                    if current["files"][key]["sha256"] != _digest_bytes(source_values[name]):
                        _write_operation(target_fd, key, source_values[name])
                        changed.append(key)
                    journal["confirmed_operations"].append(key)
                    journal["last_state"] = _snapshot_from_fds(target_fd)
                    journal["state"] = "APPLYING"
                    _fsync_json(journal_path, journal)
                    if crash_after is not None and index >= crash_after:
                        os._exit(91)
                    if fail_after is not None and index >= fail_after:
                        raise ProvisioningError("Injected laboratory interruption")

                if vault_provisioner.PLUGIN_ID not in enabled:
                    enabled.append(vault_provisioner.PLUGIN_ID)
                    _write_operation(
                        target_fd,
                        "activation",
                        (json.dumps(enabled, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
                    )
                    changed.append("activation")
                journal["confirmed_operations"].append("activation")
                final_state = _snapshot_from_fds(target_fd)
                journal["last_state"] = final_state
                journal["state"] = "COMMITTED"
                _fsync_json(journal_path, journal)
                return {
                    "status": "NOOP" if not changed else "APPLIED",
                    "vault_id": vault["vault_id"],
                    "files_changed": changed,
                    "backup_path": str(transaction_dir / "backup"),
                    "transaction_path": str(journal_path),
                    "lock_path": str(lock_path),
                    "secrets_read": False,
                    "connections_started": False,
                }
            except Exception as exc:
                if "journal_path" in locals() and journal.get("state") not in ("COMMITTED", "ROLLED_BACK"):
                    try:
                        _restore_state(target_fd, journal["expected_state"], journal["backups"])
                        journal["last_state"] = _snapshot_from_fds(target_fd)
                        journal["state"] = "ROLLED_BACK"
                        _fsync_json(journal_path, journal)
                    except Exception as rollback_exc:
                        raise ProvisioningError(f"Provisioning rollback failed: {rollback_exc}") from exc
                if isinstance(exc, ProvisioningError):
                    raise
                raise ProvisioningError(str(exc)) from exc
            finally:
                os.close(target_fd)
        finally:
            os.close(root_fd)
    finally:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
        lock_file.close()


def recover_transaction(transaction_path, lab_root):
    """Recover an interrupted transaction only when its last state still matches."""
    journal_path = Path(transaction_path).expanduser()
    journal = _load_journal(journal_path)
    root, target = _ensure_under_lab_root(lab_root, journal["relative_path"])
    if str(root) != journal["lab_root"] or str(target) != journal["target_path"]:
        raise RecoveryConflictError("RECOVERY_CONFLICT: laboratory identity changed")
    state_root = journal_path.parent.parent.parent
    lock_file, lock_path = _lock_for(target, state_root)
    try:
        root_fd = _open_directory(root)
        try:
            target_fd = _open_relative_directory(root_fd, _safe_relative_path(journal["relative_path"]))
            try:
                current = _snapshot_from_fds(target_fd)
                if journal["state"] in ("COMMITTED", "ROLLED_BACK", "RECOVERED"):
                    return {"status": journal["state"], "transaction_path": str(journal_path)}
                if not _state_equal(current, journal["last_state"]):
                    raise RecoveryConflictError("RECOVERY_CONFLICT: filesystem changed after interruption")
                if journal["state"] == "PREPARED" and not journal["backups"]:
                    journal["state"] = "RECOVERED"
                    _fsync_json(journal_path, journal)
                    return {"status": "RECOVERED", "transaction_path": str(journal_path)}
                _restore_state(target_fd, journal["expected_state"], journal["backups"])
                restored = _snapshot_from_fds(target_fd)
                if not _state_equal(restored, journal["expected_state"]):
                    raise RecoveryConflictError("RECOVERY_CONFLICT: restored state failed verification")
                journal["last_state"] = restored
                journal["state"] = "RECOVERED"
                _fsync_json(journal_path, journal)
                return {
                    "status": "RECOVERED",
                    "transaction_path": str(journal_path),
                    "lock_path": str(lock_path),
                }
            finally:
                os.close(target_fd)
        finally:
            os.close(root_fd)
    finally:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
        lock_file.close()


def revert_receipt(receipt, lab_root, relative_path):
    """Recover a transaction receipt after explicit identity validation."""
    if not isinstance(receipt, dict) or not receipt.get("transaction_path"):
        raise ProvisioningError("A transaction receipt is required for recovery")
    journal = _load_journal(Path(receipt["transaction_path"]).expanduser())
    if journal.get("relative_path") != relative_path:
        raise RecoveryConflictError("RECOVERY_CONFLICT: receipt path does not match request")
    return recover_transaction(receipt["transaction_path"], lab_root)
