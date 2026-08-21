"""Deterministic Android build-plan compiler.

The compiler allocates authority; it does not emit trusted Kotlin, Rust, Gradle,
Android manifests or signing material. Frozen renderers and domain engines own
that later materialization step.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from typing import Any, Mapping


SAFE = re.compile(r"^[a-z][a-z0-9._-]{0,95}$")
FIELDS = {"application", "operations", "binding", "device_catalog", "target_profile"}
MODES = {"embedded_rust", "remote_axum", "device", "background"}


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _failure(code: str, message: str, **details: Any) -> dict[str, Any]:
    return {
        "schema_version": "polar.android-plan-receipt/v1",
        "status": "FAIL",
        "error": {"code": code, "message": message, **details},
        "evidence": [],
    }


def compile_android_plan(payload: Mapping[str, Any]) -> dict[str, Any]:
    unknown = sorted(set(payload) - FIELDS)
    missing = sorted(FIELDS - set(payload))
    if unknown or missing:
        return _failure("CLOSED_INPUT", "request fields do not match the frozen contract", unknown=unknown, missing=missing)
    application = payload["application"]
    binding = payload["binding"]
    operations = payload["operations"]
    catalog = payload["device_catalog"]
    profile = payload["target_profile"]
    if not all(isinstance(value, Mapping) for value in (application, binding, profile)):
        return _failure("TYPE", "application, binding and target_profile must be objects")
    if not isinstance(operations, list) or not isinstance(catalog, list):
        return _failure("TYPE", "operations and device_catalog must be arrays")
    application_id = application.get("application_id")
    if not isinstance(application_id, str) or SAFE.fullmatch(application_id) is None:
        return _failure("APPLICATION_ID", "application_id is outside the closed identifier alphabet")
    if binding.get("application_id") != application_id:
        return _failure("IDENTITY_CLOSURE", "binding application_id does not match")
    if binding.get("target") != "android.tauri-react-vite":
        return _failure("TARGET", "only android.tauri-react-vite is admitted in v1")
    if profile.get("rust_core") is not True or profile.get("tauri_mobile") is not True:
        return _failure("STACK", "Rust core and Tauri Mobile are mandatory")
    if profile.get("axum_policy") not in {"remote_only", "explicit_loopback_exception"}:
        return _failure("AXUM_POLICY", "Axum must remain a real network boundary")

    catalog_by_id: dict[str, Mapping[str, Any]] = {}
    for item in catalog:
        if not isinstance(item, Mapping) or not isinstance(item.get("capability_id"), str):
            return _failure("DEVICE_CATALOG", "device catalog entries require capability_id")
        capability_id = str(item["capability_id"])
        if SAFE.fullmatch(capability_id) is None or capability_id in catalog_by_id:
            return _failure("DEVICE_CATALOG", "device capability IDs must be safe and unique")
        if item.get("provider") not in {"tauri_official", "custom_kotlin"}:
            return _failure("DEVICE_PROVIDER", "device capability provider is not admitted")
        permissions = item.get("android_permissions", [])
        if not isinstance(permissions, list) or not all(isinstance(value, str) and value.startswith("android.permission.") for value in permissions):
            return _failure("ANDROID_PERMISSION", "permissions must be explicit Android permission symbols")
        catalog_by_id[capability_id] = item

    seen: set[str] = set()
    compiled: list[dict[str, Any]] = []
    permissions: set[str] = set()
    modules = {"frontend.react_vite", "shell.tauri_android", "core.rust"}
    obligations: list[dict[str, Any]] = []
    for operation in operations:
        if not isinstance(operation, Mapping):
            return _failure("OPERATION", "operation entries must be objects")
        operation_id = operation.get("operation_id")
        mode = operation.get("mode")
        if not isinstance(operation_id, str) or SAFE.fullmatch(operation_id) is None or operation_id in seen:
            return _failure("OPERATION_ID", "operation IDs must be safe and unique")
        seen.add(operation_id)
        if mode not in MODES:
            return _failure("OPERATION_MODE", f"unsupported operation mode for {operation_id}")
        row: dict[str, Any] = {
            "operation_id": operation_id,
            "mode": mode,
            "rust_command": f"app_{operation_id.replace('.', '_').replace('-', '_')}",
            "requires_fresh_user_gesture": bool(operation.get("requires_fresh_user_gesture", False)),
            "idempotency": operation.get("idempotency", "required"),
        }
        if mode == "device":
            capability_id = operation.get("device_capability_id")
            device = catalog_by_id.get(str(capability_id))
            if device is None:
                return _failure("DEVICE_CAPABILITY", f"operation {operation_id} references an unregistered device capability")
            row["device_capability_id"] = capability_id
            row["kotlin_adapter"] = device.get("kotlin_adapter")
            row["tauri_plugin"] = device.get("tauri_plugin")
            permissions.update(device.get("android_permissions", []))
            modules.add("platform.kotlin")
            obligations.append({
                "kind": "permission_lifecycle_fsm",
                "operation_id": operation_id,
                "states": ["unknown", "denied", "granted", "permanently_denied", "revoked"],
                "required_halting": ["denied", "granted", "permanently_denied"],
            })
        elif mode == "remote_axum":
            modules.add("service.axum_remote")
            row["endpoint_contract_id"] = operation.get("endpoint_contract_id")
            if not isinstance(row["endpoint_contract_id"], str) or SAFE.fullmatch(row["endpoint_contract_id"]) is None:
                return _failure("ENDPOINT_CONTRACT", f"operation {operation_id} needs a safe endpoint contract ID")
        elif mode == "background":
            modules.add("platform.workmanager")
            row["work_policy"] = operation.get("work_policy")
            if row["work_policy"] not in {"unique_keep", "unique_replace", "periodic"}:
                return _failure("WORK_POLICY", f"operation {operation_id} has no admitted WorkManager policy")
        compiled.append(row)
        obligations.append({"kind": "operation_refinement", "operation_id": operation_id, "mode": mode})

    if not compiled:
        return _failure("VACUOUS", "at least one operation is required")
    plan = {
        "schema_version": "polar.android-build-plan/v1",
        "application_id": application_id,
        "target": "android.tauri-react-vite",
        "web_ui_plan_sha256": binding.get("web_ui_plan_sha256"),
        "modules": sorted(modules),
        "operations": sorted(compiled, key=lambda item: item["operation_id"]),
        "android_permissions": sorted(permissions),
        "axum_policy": profile["axum_policy"],
        "euclid_obligations": obligations,
        "release_gates": [
            "schema", "rust", "kotlin", "tauri_capability", "gradle", "manifest",
            "instrumentation", "device", "accessibility", "lifecycle", "security", "mutation", "signing"
        ],
    }
    if not isinstance(plan["web_ui_plan_sha256"], str) or re.fullmatch(r"[a-f0-9]{64}", plan["web_ui_plan_sha256"]) is None:
        return _failure("WEB_PLAN", "binding must cite an exact Web Experience UI plan hash")
    return {
        "schema_version": "polar.android-plan-receipt/v1",
        "status": "PASS",
        "output": plan,
        "evidence": [
            {"class": "android.closed_build_plan", "sha256": _digest(plan)},
            {"class": "android.authority_partition", "sha256": _digest({"modules": plan["modules"], "operations": plan["operations"]})},
        ],
        "limits": [
            "PASS proves authority allocation and closed planning only.",
            "No Kotlin, Rust, Gradle, manifest, device behavior or release is certified by this receipt."
        ],
    }


def main() -> int:
    """Compile one JSON request from stdin and emit one canonical receipt."""
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        receipt = _failure("JSON", "stdin is not one valid JSON document", detail=str(exc))
    else:
        receipt = compile_android_plan(payload) if isinstance(payload, Mapping) else _failure(
            "TYPE", "request must be a JSON object"
        )
    sys.stdout.buffer.write(_canonical(receipt) + b"\n")
    return 0 if receipt["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
