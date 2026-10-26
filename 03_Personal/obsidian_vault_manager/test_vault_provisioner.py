import json
import tempfile
import unittest
from pathlib import Path

import vault_provisioner


def catalog_for(root, vaults):
    return {
        "schema_version": "1.0-draft",
        "status": "inventory_only_not_enforced",
        "root": str(root),
        "default_policy": {
            "access": "R0",
            "writes_enabled": False,
            "symlinks": "deny",
            "nested_vaults": "exclude",
            "private_config": "deny",
        },
        "vaults": vaults,
    }


class ProvisioningPlanTests(unittest.TestCase):
    def test_current_catalog_contains_fourteen_operational_and_one_organizational_record(self):
        source = Path(__file__).with_name("catalog.json")
        data = json.loads(source.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            data["root"] = directory
            for vault in data["vaults"]:
                (Path(directory) / vault["relative_path"]).mkdir(parents=True, exist_ok=True)
            plan = vault_provisioner.build_plan(data)
        self.assertEqual(len(plan["vaults"]), 15)
        self.assertEqual(
            sum(vault["scope_type"] == "OPERATIONAL" for vault in plan["vaults"]),
            14,
        )
        self.assertEqual(
            sum(vault["scope_type"] == "ORGANIZATIONAL" for vault in plan["vaults"]),
            1,
        )
        self.assertFalse(any(
            vault["scope_type"] == "OPERATIONAL_NESTED"
            for vault in plan["vaults"]
        ))

    def test_inventory_supports_valid_catalogs_of_other_sizes(self):
        with tempfile.TemporaryDirectory() as directory:
            data = catalog_for(directory, [
                {"id": "documents-root", "relative_path": ".", "access": "R1_candidate"},
                {"id": "one", "relative_path": "one", "access": "R1_candidate"},
            ])
            (Path(directory) / "one").mkdir()
            plan = vault_provisioner.build_plan(data)
        self.assertEqual(len(plan["vaults"]), 2)
        self.assertFalse(plan["catalog_errors"])

    def test_documents_root_is_excluded(self):
        with tempfile.TemporaryDirectory() as directory:
            data = catalog_for(directory, [
                {"id": "documents-root", "relative_path": ".", "access": "R1_candidate"},
            ])
            vault = vault_provisioner.build_plan(data)["vaults"][0]
        self.assertEqual(vault["scope_type"], "ORGANIZATIONAL")
        self.assertEqual(vault["plugin_installability"], "EXCLUDED")
        self.assertEqual(vault["connection_eligibility"], "EXCLUDED_ORGANIZATIONAL")

    def test_nested_vaults_remain_in_plan_but_connection_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "parent" / "child" / ".obsidian").mkdir(parents=True)
            data = catalog_for(root, [
                {"id": "parent", "relative_path": "parent", "access": "R1_candidate"},
                {"id": "child", "relative_path": "parent/child", "access": "R1_candidate"},
            ])
            vaults = vault_provisioner.build_plan(data)["vaults"]
        self.assertEqual(len(vaults), 2)
        self.assertEqual(vaults[1]["scope_type"], "OPERATIONAL_NESTED")
        self.assertEqual(vaults[1]["connection_eligibility"], "BLOCKED_NESTED_ISOLATION")

    def test_absent_plugin_requires_installation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "vault" / ".obsidian").mkdir(parents=True)
            data = catalog_for(root, [
                {"id": "vault", "relative_path": "vault", "access": "R1_candidate"},
            ])
            vault = vault_provisioner.build_plan(data)["vaults"][0]
        self.assertEqual(vault["plugin_installation_status"], "ABSENT")
        self.assertEqual(vault["provisioning_status"], "INSTALL_REQUIRED")

    def test_installed_plugin_version_and_activation_are_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plugin = root / "vault" / ".obsidian" / "plugins" / vault_provisioner.PLUGIN_ID
            plugin.mkdir(parents=True)
            (plugin / "manifest.json").write_text(
                json.dumps({"id": vault_provisioner.PLUGIN_ID, "version": "5.5.2"}),
                encoding="utf-8",
            )
            (plugin / "main.js").write_text("fixture", encoding="utf-8")
            (root / "vault" / ".obsidian" / "community-plugins.json").write_text(
                json.dumps([vault_provisioner.PLUGIN_ID]), encoding="utf-8"
            )
            data = catalog_for(root, [
                {"id": "vault", "relative_path": "vault", "access": "R1_candidate"},
            ])
            vault = vault_provisioner.build_plan(data)["vaults"][0]
        self.assertEqual(vault["plugin_version"], "5.5.2")
        self.assertEqual(vault["plugin_activation_status"], "DECLARED_ENABLED")
        self.assertEqual(vault["provisioning_status"], "NOOP")

    def test_activation_missing_requires_configuration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plugin = root / "vault" / ".obsidian" / "plugins" / vault_provisioner.PLUGIN_ID
            plugin.mkdir(parents=True)
            (plugin / "manifest.json").write_text(
                json.dumps({"id": vault_provisioner.PLUGIN_ID, "version": "5.5.2"}),
                encoding="utf-8",
            )
            (plugin / "main.js").write_text("fixture", encoding="utf-8")
            data = catalog_for(root, [
                {"id": "vault", "relative_path": "vault", "access": "R1_candidate"},
            ])
            vault = vault_provisioner.build_plan(data)["vaults"][0]
        self.assertEqual(vault["provisioning_status"], "CONFIGURATION_REQUIRED")

    def test_port_conflicts_are_reported_without_network_access(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = catalog_for(root, [
                {
                    "id": "one",
                    "relative_path": "one",
                    "access": "R1_candidate",
                    "connection": {
                        "host": "127.0.0.1",
                        "https_port": 27125,
                        "credential_ref": "one-ref",
                    },
                },
                {
                    "id": "two",
                    "relative_path": "two",
                    "access": "R1_candidate",
                    "connection": {
                        "host": "127.0.0.1",
                        "https_port": 27125,
                        "credential_ref": "two-ref",
                    },
                },
            ])
            plan = vault_provisioner.build_plan(data)
        self.assertEqual(plan["catalog_status"], "INVALID")
        self.assertTrue(any("port 27125" in error for error in plan["catalog_errors"]))
        self.assertFalse(plan["network_checks_performed"])

    def test_data_json_is_not_read_or_serialized(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            vault = root / "vault"
            vault.mkdir()
            (vault / "data.json").write_text("SECRET-FIXTURE", encoding="utf-8")
            data = catalog_for(root, [
                {"id": "vault", "relative_path": "vault", "access": "R1_candidate"},
            ])
            plan = vault_provisioner.build_plan(data)
        serialized = json.dumps(plan)
        self.assertNotIn("SECRET-FIXTURE", serialized)
        self.assertFalse(plan["secrets_read"])

    def test_plan_does_not_write_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "vault" / ".obsidian").mkdir(parents=True)
            data = catalog_for(root, [
                {"id": "vault", "relative_path": "vault", "access": "R1_candidate"},
            ])
            before = sorted(path.relative_to(root).as_posix() for path in root.rglob("*"))
            first = vault_provisioner.build_plan(data)
            second = vault_provisioner.build_plan(data)
            after = sorted(path.relative_to(root).as_posix() for path in root.rglob("*"))
        self.assertEqual(first, second)
        self.assertEqual(before, after)
        self.assertFalse(first["writes_performed"])

    def test_invalid_manifest_is_a_conflict(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plugin = root / "vault" / ".obsidian" / "plugins" / vault_provisioner.PLUGIN_ID
            plugin.mkdir(parents=True)
            (plugin / "manifest.json").write_text("{}", encoding="utf-8")
            (plugin / "main.js").write_text("fixture", encoding="utf-8")
            data = catalog_for(root, [
                {"id": "vault", "relative_path": "vault", "access": "R1_candidate"},
            ])
            vault = vault_provisioner.build_plan(data)["vaults"][0]
        self.assertEqual(vault["provisioning_status"], "CONFLICT")


if __name__ == "__main__":
    unittest.main()
