# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.cv_workflow import ActionModule

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.cv_workflow"
LOG_HANDLERS_PATH = "ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_handlers"
LOG_CONFIG_PATH = "ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_config"
AVD_LOGGER_NAME = "ansible_collections.arista.avd"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_validated_args(**overrides: object) -> dict:
    """Build minimal validated args for deploy(), overridable per test."""
    defaults: dict = {
        "cv_servers": ["cv.example.com"],
        "cv_verify_certs": True,
        "configuration_dir": "/configs",
        "configlet_name_template": "AVD-${hostname}",
        "return_details": False,
    }
    defaults.update(overrides)
    return defaults


def _make_deploy_result_mock(**overrides: object) -> MagicMock:
    """Build a fake DeployToCvResult-like mock with all change-indicator attributes empty by default."""
    mock = MagicMock()
    mock.errors = []
    mock.warnings = []
    mock.failed = False
    mock.deployed_configs = []
    mock.deployed_static_config_containers = []
    mock.deployed_static_config_configlets = []
    mock.deployed_device_tags = []
    mock.deployed_interface_tags = []
    mock.deployed_cv_pathfinder_metadata = []
    mock.removed_configs = []
    mock.removed_static_config_containers = []
    mock.removed_static_config_configlets = []
    mock.removed_device_tags = []
    mock.removed_interface_tags = []
    for key, value in overrides.items():
        setattr(mock, key, value)
    return mock


# ---------------------------------------------------------------------------
# run() — error tests
# ---------------------------------------------------------------------------


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule]) -> None:
    """AnsibleActionFail is raised immediately when pyavd is not available."""
    module = action_module(ActionModule)
    module.ansible_name = "arista.avd.cv_workflow"
    shared_display = MagicMock(verbosity=0)

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{LOG_HANDLERS_PATH}.Display", return_value=shared_display),
        patch(f"{LOG_CONFIG_PATH}.Display", return_value=shared_display),
        pytest.raises(
            AnsibleActionFail,
            match=r"The 'arista.avd.cv_workflow' plugin requires the 'pyavd' Python library. Got import error",
        ),
    ):
        module.run(task_vars={})


def test_run_wraps_exceptions_as_action_fail(action_module: Callable[..., ActionModule]) -> None:
    """Any exception raised during deploy() is wrapped by run() as AnsibleActionFail with chaining."""
    module = action_module(ActionModule)
    module.ansible_name = "arista.avd.cv_workflow"
    original_error = RuntimeError("CloudVision connection failed")
    shared_display = MagicMock(verbosity=0)
    validated_args = _make_validated_args()

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.strip_empties_from_dict", new=lambda x: x, create=True),
        patch(f"{MODULE_PATH}.CloudVision", side_effect=original_error, create=True),
        patch(f"{LOG_HANDLERS_PATH}.Display", return_value=shared_display),
        patch(f"{LOG_CONFIG_PATH}.Display", return_value=shared_display),
        pytest.raises(
            AnsibleActionFail,
            match=r"Error during plugin 'arista.avd.cv_workflow' execution: CloudVision connection failed",
        ) as exc_info,
    ):
        module.run(task_vars={})

    assert exc_info.value.__cause__ is original_error


# ---------------------------------------------------------------------------
# deploy() — logging tests
# ---------------------------------------------------------------------------


def test_deploy_logs_info_with_redacted_secrets(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Secrets (cv_token, cv_password, proxy_password) are replaced with '<removed>' in the INFO log."""
    module = action_module(ActionModule)
    fake_credentials = ["real-secret-token", "real-secret-password", "real-secret-proxy"]
    validated_args = _make_validated_args(
        cv_token=fake_credentials[0],
        cv_password=fake_credentials[1],
        proxy_password=fake_credentials[2],
    )

    with (
        patch(f"{MODULE_PATH}.CloudVision", create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([], [], [], []), create=True),
        patch(f"{MODULE_PATH}.DeployToCvResult", return_value=_make_deploy_result_mock(), create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        asyncio.run(module.deploy(validated_args))

    deploy_logs = [msg for msg in caplog.messages if msg.startswith("deploy:")]
    assert deploy_logs, "Expected at least one INFO log starting with 'deploy:'"
    assert "<removed>" in deploy_logs[0]
    for secret in fake_credentials:
        assert secret not in deploy_logs[0]


# ---------------------------------------------------------------------------
# deploy() — error tests
# ---------------------------------------------------------------------------


def test_deploy_raises_when_read_from_validated_inputs_without_tmp_dir(
    action_module: Callable[..., ActionModule],
) -> None:
    """ValueError is raised when preview_features.read_from_validated_inputs=True but tmp_dir is absent."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(preview_features={"read_from_validated_inputs": True})

    with pytest.raises(
        ValueError,
        match=r"tmp_dir is required when preview_features.read_from_validated_inputs is true",
    ):
        asyncio.run(module.deploy(validated_args))


# ---------------------------------------------------------------------------
# deploy() — behaviour tests
# ---------------------------------------------------------------------------


def test_deploy_uses_tmp_dir_when_read_from_validated_inputs(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify get_tmp_paths is called with tmp_dir when read_from_validated_inputs=True."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(
        tmp_dir="/avd/tmp",
        preview_features={"read_from_validated_inputs": True},
    )

    with (
        patch(f"{MODULE_PATH}.CloudVision", create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), MagicMock())) as mock_get_tmp_paths,
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([], [], [], []), create=True),
        patch(f"{MODULE_PATH}.DeployToCvResult", return_value=_make_deploy_result_mock(), create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
    ):
        asyncio.run(module.deploy(validated_args))

    mock_get_tmp_paths.assert_called_once_with("/avd/tmp")


def test_deploy_includes_static_config_manifest_when_provided(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify static_config_manifest is built when provided in validated_args."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(static_config_manifest={"containers": []})

    with (
        patch(f"{MODULE_PATH}.CloudVision", create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([], [], [], []), create=True),
        patch(f"{MODULE_PATH}.AvdManifest") as mock_manifest,
        patch(f"{MODULE_PATH}.DeployToCvResult", return_value=_make_deploy_result_mock(), create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
    ):
        asyncio.run(module.deploy(validated_args))

    mock_manifest.from_dict.assert_called_once()


def test_deploy_includes_proxy_password_in_result_when_set(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify proxy_password is included in result when cloudvision.proxy_password is set."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(return_details=True)
    deploy_result = _make_deploy_result_mock()
    deploy_result.get_result.return_value = {}

    mock_cloudvision = MagicMock()
    mock_cloudvision.proxy_password = "secret-proxy-pass"  # noqa: S105

    with (
        patch(f"{MODULE_PATH}.CloudVision", return_value=mock_cloudvision, create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.get_result", return_value={}, create=True),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([], [], [], []), create=True),
        patch(f"{MODULE_PATH}.DeployToCvResult", return_value=deploy_result, create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
    ):
        asyncio.run(module.deploy(validated_args))

    assert "cloudvision" in module.result
    assert module.result["cloudvision"].get("proxy_password") == "<removed>"


def test_deploy_updates_result_with_full_details_when_return_details_true(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify cloudvision and configs keys are added to result when return_details=True."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(return_details=True)
    deploy_result = _make_deploy_result_mock()
    deploy_result.get_result.return_value = {}

    with (
        patch(f"{MODULE_PATH}.CloudVision", create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.get_result", return_value={}, create=True),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([], [], [], []), create=True),
        patch(f"{MODULE_PATH}.DeployToCvResult", return_value=deploy_result, create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
    ):
        asyncio.run(module.deploy(validated_args))

    assert "cloudvision" in module.result
    assert "configs" in module.result


def test_deploy_calls_deploy_to_cv_when_work_to_do(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify deploy_to_cv is awaited when extract_from_device_deployments returns at least one EOS config."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args()

    with (
        patch(f"{MODULE_PATH}.CloudVision", create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([MagicMock()], [], [], []), create=True),
        patch(f"{MODULE_PATH}.deploy_to_cv", new_callable=AsyncMock, return_value=_make_deploy_result_mock(), create=True) as mock_deploy,
        patch(f"{MODULE_PATH}.CVChangeControl", create=True),
        patch(f"{MODULE_PATH}.AvdChangeControl", create=True),
        patch(f"{MODULE_PATH}.CVTimeOuts", create=True),
        patch(f"{MODULE_PATH}.CVWorkspace", create=True),
        patch(f"{MODULE_PATH}.AvdWorkspace", create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
    ):
        asyncio.run(module.deploy(validated_args))

    mock_deploy.assert_awaited_once()
    assert module.result.get("failed") is False


def test_deploy_skips_deploy_to_cv_when_no_work_to_do(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify deploy_to_cv is not awaited when there are no configs, tags, or manifest to deploy."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args()

    with (
        patch(f"{MODULE_PATH}.CloudVision", create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([], [], [], []), create=True),
        patch(f"{MODULE_PATH}.deploy_to_cv", new_callable=AsyncMock, return_value=_make_deploy_result_mock(), create=True) as mock_deploy,
        patch(f"{MODULE_PATH}.DeployToCvResult", return_value=_make_deploy_result_mock(), create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
    ):
        asyncio.run(module.deploy(validated_args))

    mock_deploy.assert_not_awaited()
    assert module.result.get("notes") == ["No configurations, tags, or static config manifest found to deploy."]


def test_deploy_preserves_logged_warnings_in_result(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify logged warnings are captured and added to the deployment result warnings, independently of save_logs."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args()
    logged_warnings_list = ["Warning 1: Device offline", "Warning 2: Config mismatch"]

    with (
        patch(f"{MODULE_PATH}.CloudVision", create=True),
        patch(f"{MODULE_PATH}.CVDeployFuture", create=True),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", create=True),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", create=True),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([MagicMock()], [], [], []), create=True),
        patch(f"{MODULE_PATH}.deploy_to_cv", new_callable=AsyncMock, return_value=_make_deploy_result_mock(), create=True),
        patch(f"{MODULE_PATH}.CVChangeControl", create=True),
        patch(f"{MODULE_PATH}.AvdChangeControl", create=True),
        patch(f"{MODULE_PATH}.CVTimeOuts", create=True),
        patch(f"{MODULE_PATH}.CVWorkspace", create=True),
        patch(f"{MODULE_PATH}.AvdWorkspace", create=True),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]),
    ):
        # Set up logged warnings in the result
        module.result["logs"] = {"warnings": logged_warnings_list}
        asyncio.run(module.deploy(validated_args))

    # Verify logged warnings are preserved in the result
    assert "warnings" in module.result
    assert all(w in module.result["warnings"] for w in logged_warnings_list)


# ---------------------------------------------------------------------------
# Helper methods — testing coverage
# ---------------------------------------------------------------------------


def test_prepare_logged_args_masks_only_present_keys(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify _prepare_logged_args only masks keys that are present in the input."""
    module = action_module(ActionModule)
    # Only provide cv_token, not cv_password or proxy_password
    validated_args = {"cv_token": "secret-token", "cv_servers": ["cv.example.com"]}

    result = module._prepare_logged_args(validated_args)

    assert result["cv_token"] == "<removed>"  # noqa: S105
    assert result["cv_servers"] == ["cv.example.com"]
    assert "cv_password" not in result or result.get("cv_password") is None


def test_prepare_workspace_args_converts_build_warnings(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify _prepare_workspace_args converts build_warnings to AvdWorkspaceBuildWarningsConfig."""
    module = action_module(ActionModule)
    validated_args = {"workspace": {"build_warnings": {"errors": ["error1"]}}}

    with patch(f"{MODULE_PATH}.AvdWorkspaceBuildWarningsConfig") as mock_config:
        mock_config.from_dict.return_value = MagicMock()
        result = module._prepare_workspace_args(validated_args)

    mock_config.from_dict.assert_called_once_with({"errors": ["error1"]})
    assert "build_warnings" in result


# ---------------------------------------------------------------------------
# load_structured_config() — logging tests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("hostname", "use_none_dir"),
    [
        pytest.param("my-device", True, id="no_structured_config_dir"),
        pytest.param("missing-device", False, id="file_does_not_exist"),
    ],
)
def test_load_structured_config_logs_info_when_file_unavailable(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
    tmp_path: Path,
    hostname: str,
    use_none_dir: bool,
) -> None:
    """An INFO log naming the host is emitted when structured_config_dir is None or the file is missing."""
    module = action_module(ActionModule)
    structured_config_dir = None if use_none_dir else str(tmp_path)

    with caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME):
        module.load_structured_config(hostname, structured_config_dir, "yml")

    assert f"load_structured_config: No structured config file for {hostname}" in caplog.messages


# ---------------------------------------------------------------------------
# load_structured_config() — file-reading tests
# ---------------------------------------------------------------------------


def test_load_structured_config_reads_yaml_file(
    action_module: Callable[..., ActionModule],
    tmp_path: Path,
) -> None:
    """Verify a YAML structured config file is parsed and the metadata section is returned as a dict."""
    module = action_module(ActionModule)
    hostname = "spine1"
    yaml_content = "hostname: spine1\nmetadata:\n  serial_number: ABC123\nother_key: value\n"
    (tmp_path / f"{hostname}.yml").write_text(yaml_content, encoding="UTF-8")

    result = module.load_structured_config(hostname, str(tmp_path), "yml")

    assert result == {"metadata": {"serial_number": "ABC123"}}


def test_load_structured_config_reads_json_file(
    action_module: Callable[..., ActionModule],
    tmp_path: Path,
) -> None:
    """Verify a JSON structured config file is loaded via AVDFileHandler and returned as a dict."""
    module = action_module(ActionModule)
    hostname = "spine1"
    expected = {"hostname": "spine1", "serial_number": "XYZ789"}
    (tmp_path / f"{hostname}.json").write_text("{}", encoding="UTF-8")

    with (
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler") as mock_handler_cls,
    ):
        mock_handler_cls.return_value.load_json.return_value = expected
        result = module.load_structured_config(hostname, str(tmp_path), "json")

    mock_handler_cls.return_value.load_json.assert_called_once()
    assert result == expected


# ---------------------------------------------------------------------------
# build_device_deployment() — logging tests
# ---------------------------------------------------------------------------


def test_build_device_deployment_logs_info_for_each_device(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """An INFO log naming the device hostname is emitted at the start of build_device_deployment."""
    module = action_module(ActionModule)

    with (
        patch(f"{MODULE_PATH}.CVDeviceDeployment", create=True),
        patch(f"{MODULE_PATH}.CVDevice", create=True),
        patch(f"{MODULE_PATH}.AvdDevice", create=True),
        patch(f"{MODULE_PATH}.CVEosConfig", create=True),
        patch.object(module, "load_structured_config", return_value={}),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        asyncio.run(module.build_device_deployment("spine1", "/structured", "yml", "/configs", "AVD-${hostname}"))

    assert any("build_device_deployment: spine1" in msg for msg in caplog.messages)


# ---------------------------------------------------------------------------
# build_device_deployment() — behaviour tests
# ---------------------------------------------------------------------------


def test_build_device_deployment_returns_none_when_not_deployed(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify build_device_deployment returns None immediately when is_deployed=False in structured config."""
    module = action_module(ActionModule)

    with patch.object(module, "load_structured_config", return_value={"is_deployed": False}):
        result = asyncio.run(module.build_device_deployment("leaf1", "/structured", "yml", "/configs", "AVD-${hostname}"))

    assert result is None


def test_build_device_deployment_skips_eos_config_when_using_manifest(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify CVEosConfig is not created and eos_config=None when cv_use_static_config_manifest=True."""
    module = action_module(ActionModule)

    with (
        patch(f"{MODULE_PATH}.CVDeviceDeployment", create=True) as mock_deployment_cls,
        patch(f"{MODULE_PATH}.CVDevice", create=True),
        patch(f"{MODULE_PATH}.AvdDevice", create=True),
        patch(f"{MODULE_PATH}.CVEosConfig", create=True) as mock_eos_config_cls,
        patch.object(module, "load_structured_config", return_value={"cv_use_static_config_manifest": True}),
    ):
        asyncio.run(module.build_device_deployment("spine1", "/structured", "yml", "/configs", "AVD-${hostname}"))

    mock_eos_config_cls.assert_not_called()
    assert mock_deployment_cls.call_args.kwargs["eos_config"] is None
    assert mock_deployment_cls.call_args.kwargs["use_static_config_manifest"] is True


def test_build_device_deployment_creates_pathfinder_metadata_object(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify CVPathfinderMetadata is instantiated when cv_pathfinder_metadata is present in structured config."""
    module = action_module(ActionModule)

    with (
        patch(f"{MODULE_PATH}.CVDeviceDeployment", create=True),
        patch(f"{MODULE_PATH}.CVDevice", create=True),
        patch(f"{MODULE_PATH}.AvdDevice", create=True),
        patch(f"{MODULE_PATH}.CVEosConfig", create=True),
        patch(f"{MODULE_PATH}.CVPathfinderMetadata", create=True) as mock_pathfinder_cls,
        patch.object(module, "load_structured_config", return_value={"cv_pathfinder_metadata": {"wan_router": True}}),
    ):
        asyncio.run(module.build_device_deployment("spine1", "/structured", "yml", "/configs", "AVD-${hostname}"))

    mock_pathfinder_cls.assert_called_once()


# ---------------------------------------------------------------------------
# build_device_deployments() — behaviour tests
# ---------------------------------------------------------------------------


def test_build_device_deployments_filters_none_results(
    action_module: Callable[..., ActionModule],
) -> None:
    """Verify build_device_deployments runs one coroutine per host and drops None (not-deployed) entries."""
    module = action_module(ActionModule)
    mock_deployment = MagicMock()

    async def fake_build(hostname: str, *_args: object, **_kwargs: object) -> MagicMock | None:
        return mock_deployment if hostname == "deployed-device" else None

    with patch.object(module, "build_device_deployment", side_effect=fake_build):
        result = asyncio.run(
            module.build_device_deployments(
                device_list=["deployed-device", "not-deployed-device"],
                structured_config_dir=None,
                structured_config_suffix="yml",
                configuration_dir="/configs",
                configlet_name_template="AVD-${hostname}",
            )
        )

    assert result == [mock_deployment]
