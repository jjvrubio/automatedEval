import json
import multiprocessing
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import vault_provisioner
from vault_provisioner_executor import (
    ActiveLockError,
    ProvisioningError,
    RecoveryConflictError,
    StalePlanError,
    _lock_for,
    apply_plan,
    prepare_execution_plan,
    recover_transaction,
)


def _hold_lock(target, state_root, ready, release):
    lock_file, _ = _lock_for(target, state_root)
    ready.set()
    release.wait(5)
    lock_file.close()


def _crash_worker(plan, source, root):
    apply_plan(plan, source, root, crash_after=1)


def _crash_before_worker(plan, source, root):
    apply_plan(plan, source, root, crash_before=True)


class FixtureExecutorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "lab"
        self.root.mkdir()
        self.vault = self.root / "vault"
        (self.vault / ".obsidian").mkdir(parents=True)
        self.source = Path(self.temp.name) / "plugin"
        self.source.mkdir()
        (self.source / "manifest.json").write_text(
            json.dumps({"id": vault_provisioner.PLUGIN_ID, "version": "5.5.2"}),
            encoding="utf-8",
        )
        (self.source / "main.js").write_text("fixture-main", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def plan(self, **overrides):
        data = {
            "plan_schema_version": "0.1",
            "catalog_status": "VALID",
            "writes_performed": False,
            "vaults": [{
                "vault_id": "vault",
                "scope_type": "OPERATIONAL",
                "relative_path": "vault",
                "connection_eligibility": "PENDING_VM04",
                "provisioning_status": "INSTALL_REQUIRED",
            }],
        }
        data["vaults"][0].update(overrides)
        return data

    def execute(self, plan=None, **kwargs):
        prepared = prepare_execution_plan(plan or self.plan(), self.source, self.root)
        return apply_plan(prepared, self.source, self.root, **kwargs)

    def test_initial_installation(self):
        receipt = self.execute()
        plugin = self.vault / ".obsidian" / "plugins" / vault_provisioner.PLUGIN_ID
        self.assertEqual(receipt["status"], "APPLIED")
        self.assertTrue((plugin / "manifest.json").is_file())
        self.assertEqual(json.loads((self.vault / ".obsidian/community-plugins.json").read_text()), [vault_provisioner.PLUGIN_ID])

    def test_existing_installation_is_preserved(self):
        plugin = self.vault / ".obsidian/plugins" / vault_provisioner.PLUGIN_ID
        plugin.mkdir(parents=True)
        for name in ("manifest.json", "main.js"):
            (plugin / name).write_bytes((self.source / name).read_bytes())
        receipt = self.execute(self.plan(provisioning_status="NOOP"))
        self.assertEqual(receipt["status"], "APPLIED")

    def test_repetition_is_idempotent(self):
        self.execute()
        receipt = self.execute(self.plan(provisioning_status="NOOP"))
        self.assertEqual(receipt["status"], "NOOP")
        self.assertEqual(receipt["files_changed"], [])

    def test_version_conflict_is_rejected(self):
        plugin = self.vault / ".obsidian/plugins" / vault_provisioner.PLUGIN_ID
        plugin.mkdir(parents=True)
        (plugin / "manifest.json").write_text(json.dumps({"id": vault_provisioner.PLUGIN_ID, "version": "5.5.1"}))
        (plugin / "main.js").write_text("old")
        with self.assertRaises(ProvisioningError):
            self.execute(self.plan(provisioning_status="CONFLICT"))

    def test_ambiguous_path_is_rejected(self):
        with self.assertRaises(ProvisioningError):
            self.execute(self.plan(relative_path="../outside"))

    def test_symlink_is_rejected(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        shutil.rmtree(self.vault)
        self.vault.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ProvisioningError):
            self.execute()

    def test_symlink_lab_root_is_rejected(self):
        linked_root = Path(self.temp.name) / "linked-lab"
        linked_root.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ProvisioningError):
            apply_plan(
                prepare_execution_plan(self.plan(), self.source, linked_root),
                self.source,
                linked_root,
            )

    def test_backup_survives_success_for_recovery(self):
        activation = self.vault / ".obsidian/community-plugins.json"
        activation.write_text(json.dumps(["other-plugin"]) + "\n")
        result = self.execute()
        backup = Path(result["backup_path"])
        self.assertTrue(backup.is_dir())
        self.assertEqual(
            json.loads((backup / "activation").read_text()),
            ["other-plugin"],
        )

    def test_interruption_restores_partial_installation(self):
        with self.assertRaises(ProvisioningError):
            self.execute(fail_after=1)
        self.assertFalse((self.vault / ".obsidian/plugins").exists())
        self.assertFalse((self.vault / ".obsidian/community-plugins.json").exists())

    def test_existing_state_can_be_restored_by_failure_rollback(self):
        activation = self.vault / ".obsidian/community-plugins.json"
        activation.write_text(json.dumps(["other-plugin"]) + "\n")
        with self.assertRaises(ProvisioningError):
            self.execute(fail_after=1)
        self.assertEqual(json.loads(activation.read_text()), ["other-plugin"])

    def test_integrity_is_verified(self):
        receipt = self.execute()
        self.assertEqual(receipt["connections_started"], False)
        installed = self.vault / ".obsidian/plugins" / vault_provisioner.PLUGIN_ID / "main.js"
        self.assertEqual(installed.read_text(), "fixture-main")

    def test_unrelated_plugins_are_preserved(self):
        other = self.vault / ".obsidian/plugins/other-plugin"
        other.mkdir(parents=True)
        marker = other / "main.js"
        marker.write_text("untouched")
        self.execute()
        self.assertEqual(marker.read_text(), "untouched")

    def test_organizational_scope_is_rejected(self):
        with self.assertRaises(ProvisioningError):
            self.execute(self.plan(scope_type="ORGANIZATIONAL"))

    def test_root_relative_scope_is_rejected(self):
        with self.assertRaises(ProvisioningError):
            self.execute(self.plan(relative_path="."))

    def test_real_root_is_not_writable_without_explicit_lab_root(self):
        with self.assertRaises(ProvisioningError):
            apply_plan(
                prepare_execution_plan(self.plan(), self.source, Path(self.temp.name) / "missing"),
                self.source,
                Path(self.temp.name) / "missing",
            )

    def test_credentials_are_not_used(self):
        result = self.execute()
        self.assertFalse(result["secrets_read"])

    def test_no_mcp_connection_is_started(self):
        result = self.execute()
        self.assertFalse(result["connections_started"])

    def test_invalid_activation_is_not_overwritten(self):
        activation = self.vault / ".obsidian/community-plugins.json"
        activation.write_text('{"unknown": true}')
        with self.assertRaises(ProvisioningError):
            self.execute()
        self.assertEqual(activation.read_text(), '{"unknown": true}')

    def test_stale_plan_is_rejected_without_writes(self):
        prepared = prepare_execution_plan(self.plan(), self.source, self.root)
        activation = self.vault / ".obsidian/community-plugins.json"
        activation.write_text(json.dumps(["changed"]) + "\n")
        with self.assertRaises(StalePlanError) as context:
            apply_plan(prepared, self.source, self.root)
        self.assertIn("STALE_PLAN", str(context.exception))
        self.assertFalse((self.vault / ".obsidian/plugins").exists())

    def test_active_lock_rejects_application(self):
        prepared = prepare_execution_plan(self.plan(), self.source, self.root)
        state_root = self.root.parent / f".{self.root.name}-vp05-state"
        ready = multiprocessing.Event()
        release = multiprocessing.Event()
        process = multiprocessing.Process(
            target=_hold_lock,
            args=(self.vault, state_root, ready, release),
        )
        process.start()
        self.assertTrue(ready.wait(5))
        try:
            with self.assertRaises(ActiveLockError):
                apply_plan(prepared, self.source, self.root)
        finally:
            release.set()
            process.join(5)
            self.assertFalse(process.is_alive())

    def test_abrupt_interruption_is_recovered_from_journal(self):
        prepared = prepare_execution_plan(self.plan(), self.source, self.root)
        process = multiprocessing.Process(
            target=_crash_worker,
            args=(prepared, self.source, self.root),
        )
        process.start()
        process.join(5)
        self.assertFalse(process.is_alive())
        self.assertEqual(process.exitcode, 91)
        state_root = self.root.parent / f".{self.root.name}-vp05-state"
        journals = list((state_root / "transactions").glob("*/journal.json"))
        self.assertEqual(len(journals), 1)
        result = recover_transaction(journals[0], self.root)
        self.assertEqual(result["status"], "RECOVERED")
        self.assertFalse((self.vault / ".obsidian/plugins").exists())
        self.assertFalse((self.vault / ".obsidian/community-plugins.json").exists())

    def test_interruption_before_first_write_is_recovered(self):
        prepared = prepare_execution_plan(self.plan(), self.source, self.root)
        process = multiprocessing.Process(
            target=_crash_before_worker,
            args=(prepared, self.source, self.root),
        )
        process.start()
        process.join(5)
        self.assertEqual(process.exitcode, 91)
        journal = next((self.root.parent / f".{self.root.name}-vp05-state/transactions").glob("*/journal.json"))
        result = recover_transaction(journal, self.root)
        self.assertEqual(result["status"], "RECOVERED")
        self.assertFalse((self.vault / ".obsidian/plugins").exists())

    def test_recovery_respects_active_lock(self):
        prepared = prepare_execution_plan(self.plan(), self.source, self.root)
        process = multiprocessing.Process(
            target=_crash_worker,
            args=(prepared, self.source, self.root),
        )
        process.start()
        process.join(5)
        journal = next((self.root.parent / f".{self.root.name}-vp05-state/transactions").glob("*/journal.json"))
        state_root = self.root.parent / f".{self.root.name}-vp05-state"
        ready = multiprocessing.Event()
        release = multiprocessing.Event()
        holder = multiprocessing.Process(
            target=_hold_lock,
            args=(self.vault, state_root, ready, release),
        )
        holder.start()
        self.assertTrue(ready.wait(5))
        try:
            with self.assertRaises(ActiveLockError):
                recover_transaction(journal, self.root)
        finally:
            release.set()
            holder.join(5)
            self.assertFalse(holder.is_alive())

    def test_recovery_rejects_changed_state(self):
        prepared = prepare_execution_plan(self.plan(), self.source, self.root)
        process = multiprocessing.Process(
            target=_crash_worker,
            args=(prepared, self.source, self.root),
        )
        process.start()
        process.join(5)
        self.assertEqual(process.exitcode, 91)
        (self.vault / ".obsidian/plugins/obsidian-local-rest-api/main.js").write_text("changed")
        journal = next((self.root.parent / f".{self.root.name}-vp05-state/transactions").glob("*/journal.json"))
        with self.assertRaises(RecoveryConflictError):
            recover_transaction(journal, self.root)

    def test_backup_and_journal_are_integrity_checked(self):
        receipt = self.execute()
        journal = Path(receipt["transaction_path"])
        data = json.loads(journal.read_text())
        self.assertEqual(data["state"], "COMMITTED")
        self.assertEqual(data["schema_version"], "0.2")
        for backup in data["backups"].values():
            path = Path(backup["path"])
            self.assertEqual(_sha256(path), backup["sha256"])

    def test_route_replacement_is_rejected_without_external_write(self):
        prepared = prepare_execution_plan(self.plan(), self.source, self.root)
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        marker = outside / "marker"
        marker.write_text("untouched")
        import vault_provisioner_executor as executor

        original = executor._write_operation
        attacked = False

        def attack(target_fd, key, data):
            nonlocal attacked
            if not attacked:
                attacked = True
                plugin = self.vault / ".obsidian/plugins/obsidian-local-rest-api"
                plugin.parent.mkdir(parents=True, exist_ok=True)
                shutil.rmtree(plugin, ignore_errors=True)
                plugin.symlink_to(outside, target_is_directory=True)
            return original(target_fd, key, data)

        with mock.patch.object(executor, "_write_operation", side_effect=attack):
            with self.assertRaises(ProvisioningError):
                apply_plan(prepared, self.source, self.root)
        self.assertEqual(marker.read_text(), "untouched")


def _sha256(path):
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    unittest.main()
