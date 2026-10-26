import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import vault_manager


BASE_CATALOG = {
    "schema_version": "1.0-draft",
    "status": "inventory_only_not_enforced",
    "root": "/unused",
    "default_policy": {
        "access": "R0",
        "writes_enabled": False,
        "symlinks": "deny",
        "nested_vaults": "exclude",
        "private_config": "deny",
    },
    "vaults": [
        {"id": "documents-root", "relative_path": ".", "access": "R1_candidate"},
        {"id": "parent", "relative_path": "parent", "access": "R1_candidate"},
        {"id": "child", "relative_path": "parent/child", "access": "R1_candidate"},
    ],
}


class VaultManagerTests(unittest.TestCase):
    def catalog(self):
        return json.loads(json.dumps(BASE_CATALOG))

    def test_existing_catalog_is_schema_compatible(self):
        data = self.catalog()
        rows, errors, warnings = vault_manager.report(data, inspect_fs=False)
        self.assertFalse(errors)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0][3], "ORGANIZATIONAL")
        self.assertEqual(rows[2][3], "NOT_OPERATIONAL_NESTED")
        self.assertFalse(warnings)

    def test_malformed_types_are_reported_without_traceback(self):
        data = self.catalog()
        data["default_policy"] = []
        rows, errors, warnings = vault_manager.report(data, inspect_fs=False)
        self.assertEqual(rows, [])
        self.assertTrue(any("default_policy must be an object" in error for error in errors))

    def test_duplicate_ids_and_ports_are_rejected(self):
        data = self.catalog()
        data["vaults"][1]["id"] = "child"
        data["vaults"][1]["connection"] = {
            "host": "127.0.0.1",
            "https_port": 27125,
            "credential_ref": "parent-ref",
        }
        data["vaults"][2]["connection"] = {
            "host": "127.0.0.1",
            "https_port": 27125,
            "credential_ref": "child-ref",
        }
        rows, errors, warnings = vault_manager.report(data, inspect_fs=False)
        self.assertTrue(any("duplicate id" in error for error in errors))
        self.assertTrue(any("port 27125" in error for error in errors))

    def test_intermediate_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            real = root / "real"
            real.mkdir()
            (real / "child").mkdir()
            link = root / "link"
            link.symlink_to(real, target_is_directory=True)
            data = self.catalog()
            data["root"] = str(root)
            data["vaults"] = [
                {"id": "documents-root", "relative_path": ".", "access": "R1_candidate"},
                {"id": "linked", "relative_path": "link/child", "access": "R1_candidate"},
            ]
            rows, errors, warnings = vault_manager.report(data)
            self.assertTrue(any("contains a symlink" in error for error in errors))

    def test_path_escape_is_rejected(self):
        data = self.catalog()
        data["vaults"] = [
            {"id": "documents-root", "relative_path": ".", "access": "R1_candidate"},
            {"id": "escape", "relative_path": "../outside", "access": "R1_candidate"},
        ]
        rows, errors, warnings = vault_manager.report(data, inspect_fs=False)
        self.assertTrue(any("unsafe relative_path" in error for error in errors))

    def test_document_fixture_is_not_modified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            vault = root / "vault"
            vault.mkdir()
            (vault / ".obsidian").mkdir()
            document = vault / "note.md"
            document.write_text("unchanged", encoding="utf-8")
            data = self.catalog()
            data["root"] = str(root)
            data["vaults"] = [
                {"id": "documents-root", "relative_path": ".", "access": "R1_candidate"},
                {"id": "vault", "relative_path": "vault", "access": "R1_candidate"},
            ]
            vault_manager.report(data)
            self.assertEqual(document.read_text(encoding="utf-8"), "unchanged")

    def test_backup_names_do_not_collide(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = Path(directory) / "catalog.json"
            catalog.write_text("{}", encoding="utf-8")
            with patch.object(vault_manager.datetime, "datetime") as clock:
                clock.now.return_value.strftime.return_value = "20261026-213801-123456"
                first = vault_manager.save_atomic(catalog, {"one": 1})
                catalog.write_text("{}", encoding="utf-8")
                second = vault_manager.save_atomic(catalog, {"two": 2})
            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())

    def test_diagnostics_do_not_use_keychain_or_mcp(self):
        data = self.catalog()
        with patch.object(vault_manager, "socket") as socket_module:
            rows, errors, warnings = vault_manager.report(data, inspect_fs=False)
        self.assertFalse(errors)
        socket_module.create_connection.assert_not_called()


if __name__ == "__main__":
    unittest.main()
