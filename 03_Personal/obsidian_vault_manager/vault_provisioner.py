#!/usr/bin/env python3
"""Read-only provisioning plan generator for Obsidian Bridge."""
import argparse
import json
import os
import sys
from pathlib import Path

import vault_manager


PLAN_SCHEMA_VERSION = "0.1"
PLUGIN_ID = "obsidian-local-rest-api"
PLUGIN_DIR = Path(".obsidian") / "plugins" / PLUGIN_ID
REQUIRED_PLUGIN_FILES = ("manifest.json", "main.js")


def _read_json_metadata(path):
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def _inspect_plugin(vault_path):
    plugin_path = vault_path / PLUGIN_DIR
    manifest_path = plugin_path / "manifest.json"
    required = [plugin_path / name for name in REQUIRED_PLUGIN_FILES]
    present = [path for path in required if path.is_file()]
    result = {
        "plugin_installation_status": "ABSENT",
        "plugin_version": None,
        "plugin_activation_status": "NOT_DECLARED",
        "plugin_files": [path.name for path in present],
        "plugin_metadata_status": "NOT_INSPECTED",
    }
    if present:
        result["plugin_installation_status"] = (
            "PRESENT" if len(present) == len(required) else "PARTIAL"
        )
    if manifest_path.is_file():
        try:
            manifest = _read_json_metadata(manifest_path)
        except (OSError, TypeError, ValueError):
            result["plugin_metadata_status"] = "INVALID"
        else:
            if manifest.get("id") != PLUGIN_ID or not isinstance(manifest.get("version"), str):
                result["plugin_metadata_status"] = "INVALID"
            else:
                result["plugin_metadata_status"] = "VALID"
                result["plugin_version"] = manifest["version"]

    enabled_path = vault_path / ".obsidian" / "community-plugins.json"
    if enabled_path.is_file():
        try:
            enabled = _read_json_metadata(enabled_path)
        except (OSError, TypeError, ValueError):
            result["plugin_activation_status"] = "UNKNOWN"
        else:
            if isinstance(enabled, list) and all(isinstance(item, str) for item in enabled):
                result["plugin_activation_status"] = (
                    "DECLARED_ENABLED" if PLUGIN_ID in enabled else "NOT_DECLARED"
                )
            else:
                result["plugin_activation_status"] = "UNKNOWN"
    return result


def _reason(result, code):
    result["reason_codes"].append(code)


def _build_vault_plan(data, row, root, catalog_errors):
    vault_id, relative_path, declared_port, displayed_scope = row
    result = {
        "vault_id": vault_id,
        "scope_type": "ORGANIZATIONAL" if displayed_scope == "ORGANIZATIONAL"
        else (
            "OPERATIONAL_NESTED"
            if displayed_scope == "NOT_OPERATIONAL_NESTED"
            else "OPERATIONAL"
        ),
        "relative_path": relative_path,
        "filesystem_status": "UNKNOWN",
        "plugin_installability": "UNKNOWN",
        "plugin_installation_status": "UNKNOWN",
        "plugin_version": None,
        "plugin_activation_status": "UNKNOWN",
        "provisioning_status": "BLOCKED",
        "connection_eligibility": "NOT_ELIGIBLE",
        "reason_codes": [],
        "planned_actions": [],
        "backup_required": False,
        "declared_port": declared_port,
        "port_status": "NOT_ASSIGNED" if declared_port is None else "DECLARED_UNVERIFIED",
        "candidate_ports": [],
    }

    if result["scope_type"] == "ORGANIZATIONAL":
        result["plugin_installability"] = "EXCLUDED"
        result["provisioning_status"] = "BLOCKED"
        result["connection_eligibility"] = "EXCLUDED_ORGANIZATIONAL"
        _reason(result, "ORGANIZATIONAL_SCOPE")
        return result

    if catalog_errors:
        result["filesystem_status"] = "INVALID_CATALOG"
        result["plugin_installability"] = "BLOCKED"
        _reason(result, "CATALOG_VALIDATION_FAILED")
        return result

    target = (root / relative_path).resolve(strict=False)
    if not root.is_dir():
        result["filesystem_status"] = "ROOT_UNAVAILABLE"
        result["plugin_installability"] = "BLOCKED"
        _reason(result, "ROOT_UNAVAILABLE")
        result["planned_actions"].append("INSPECT_ON_VAULT_HOST")
        return result
    if not target.is_dir():
        result["filesystem_status"] = "MISSING"
        result["plugin_installability"] = "BLOCKED"
        _reason(result, "VAULT_DIRECTORY_MISSING")
        result["planned_actions"].append("VERIFY_VAULT_PATH")
        return result

    result["filesystem_status"] = "AVAILABLE"
    result["plugin_installability"] = "PHYSICALLY_INSTALLABLE"
    if not (target / ".obsidian").is_dir():
        _reason(result, "OBSIDIAN_CONFIG_DIR_MISSING")
        result["planned_actions"].append("CREATE_PLUGIN_LAYOUT")

    result.update(_inspect_plugin(target))
    if result["plugin_metadata_status"] == "INVALID":
        result["provisioning_status"] = "CONFLICT"
        _reason(result, "PLUGIN_MANIFEST_INVALID")
        result["planned_actions"].append("REVIEW_PLUGIN_FILES")
    elif result["plugin_installation_status"] != "PRESENT":
        result["provisioning_status"] = "INSTALL_REQUIRED"
        result["backup_required"] = True
        _reason(result, "PLUGIN_ABSENT_OR_INCOMPLETE")
        result["planned_actions"].append("INSTALL_PLUGIN_FILES")
    elif result["plugin_activation_status"] == "UNKNOWN":
        result["provisioning_status"] = "CONFLICT"
        _reason(result, "PLUGIN_ACTIVATION_UNKNOWN")
        result["planned_actions"].append("REVIEW_ACTIVATION_METADATA")
    elif result["plugin_activation_status"] != "DECLARED_ENABLED":
        result["provisioning_status"] = "CONFIGURATION_REQUIRED"
        result["backup_required"] = True
        _reason(result, "PLUGIN_NOT_DECLARED_ENABLED")
        result["planned_actions"].append("ENABLE_PLUGIN")
    else:
        result["provisioning_status"] = "NOOP"
        _reason(result, "PLUGIN_PRESENT_AND_DECLARED")

    if result["scope_type"] == "OPERATIONAL_NESTED":
        result["connection_eligibility"] = "BLOCKED_NESTED_ISOLATION"
        _reason(result, "PARENT_CHILD_ISOLATION_PENDING")
    elif declared_port is None:
        result["connection_eligibility"] = "PENDING_PORT_ASSIGNMENT"
        _reason(result, "PORT_NOT_ASSIGNED")
    else:
        result["connection_eligibility"] = "PENDING_VM04"
        _reason(result, "SERVER_IDENTITY_NOT_VERIFIED")
    return result


def build_plan(data):
    rows, errors, warnings = vault_manager.report(data, inspect_fs=False)
    plan = {
        "plan_schema_version": PLAN_SCHEMA_VERSION,
        "generator": "Vault Provisioner v0.1",
        "mode": "plan",
        "catalog_status": "VALID" if not errors else "INVALID",
        "catalog_errors": errors,
        "catalog_warnings": warnings,
        "vaults": [],
        "network_checks_performed": False,
        "writes_performed": False,
        "secrets_read": False,
    }
    if not isinstance(data, dict) or not isinstance(data.get("root"), str):
        return plan
    root = Path(os.path.expanduser(data["root"])).resolve(strict=False)
    plan["vaults"] = [
        _build_vault_plan(data, row, root, errors)
        for row in rows
    ]
    return plan


def load_plan_catalog(path):
    return vault_manager.load_catalog(path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate read-only Obsidian provisioning plans"
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        default=Path(__file__).with_name("catalog.json"),
    )
    subparsers = parser.add_subparsers(dest="action", required=True)
    for action in ("inspect", "plan", "dry-run"):
        subparsers.add_parser(action)
    args = parser.parse_args()
    try:
        data = load_plan_catalog(args.catalog)
        plan = build_plan(data)
        plan["mode"] = args.action
        if args.action == "dry-run":
            plan["execution"] = "NO_ACTIONS_EXECUTED"
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 2 if plan["catalog_status"] == "INVALID" else 0
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
