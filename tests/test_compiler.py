from polar_pyro_android import compile_android_plan


def request() -> dict:
    return {
        "application": {"application_id": "field_ops"},
        "binding": {"application_id": "field_ops", "target": "android.tauri-react-vite", "web_ui_plan_sha256": "a" * 64},
        "operations": [
            {"operation_id": "jobs.list", "mode": "embedded_rust"},
            {"operation_id": "photo.capture", "mode": "device", "device_capability_id": "camera.capture", "requires_fresh_user_gesture": True},
            {"operation_id": "sync.push", "mode": "remote_axum", "endpoint_contract_id": "sync.v1"},
            {"operation_id": "sync.retry", "mode": "background", "work_policy": "unique_keep"},
        ],
        "device_catalog": [{
            "capability_id": "camera.capture", "provider": "custom_kotlin", "kotlin_adapter": "CameraAdapter",
            "tauri_plugin": "camera", "android_permissions": ["android.permission.CAMERA"]
        }],
        "target_profile": {"rust_core": True, "tauri_mobile": True, "axum_policy": "remote_only"},
    }


def test_compiler_allocates_authority_and_permissions() -> None:
    receipt = compile_android_plan(request())
    assert receipt["status"] == "PASS"
    plan = receipt["output"]
    assert plan["android_permissions"] == ["android.permission.CAMERA"]
    assert "platform.kotlin" in plan["modules"]
    assert "service.axum_remote" in plan["modules"]
    assert "platform.workmanager" in plan["modules"]
    assert receipt["evidence"]


def test_unregistered_device_capability_fails_closed() -> None:
    value = request()
    value["operations"][1]["device_capability_id"] = "camera.untrusted"
    assert compile_android_plan(value)["error"]["code"] == "DEVICE_CAPABILITY"


def test_unknown_fields_and_loopback_default_are_rejected() -> None:
    value = request()
    value["shell_command"] = "gradlew assembleRelease"
    assert compile_android_plan(value)["error"]["code"] == "CLOSED_INPUT"
    value = request()
    value["target_profile"]["axum_policy"] = "loopback_default"
    assert compile_android_plan(value)["error"]["code"] == "AXUM_POLICY"


def test_web_plan_hash_and_non_vacuous_operation_set_are_required() -> None:
    value = request()
    value["binding"]["web_ui_plan_sha256"] = "latest"
    assert compile_android_plan(value)["error"]["code"] == "WEB_PLAN"
    value = request()
    value["operations"] = []
    assert compile_android_plan(value)["error"]["code"] == "VACUOUS"
