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
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        pytest.raises(
            AnsibleActionFail,
            match=r"The 'arista.avd.cv_workflow' plugin requires the 'pyavd' Python library. Got import error",
        ),
    ):
        module.run(task_vars={})


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
        result = asyncio.run(module.deploy(validated_args, {}))

    deploy_logs = [msg for msg in caplog.messages if msg.startswith("deploy:")]
    assert deploy_logs, "Expected at least one INFO log starting with 'deploy:'"
    assert "<removed>" in deploy_logs[0]
    assert result["notes"] == ["No configurations, tags, or static config manifest found to deploy."]
    assert result["changed"] is False


def test_deploy_converts_successful_deployment_to_ansible_result(
    action_module: Callable[..., ActionModule],
) -> None:
    """A mocked PyAVD deployment is converted to the detailed Ansible result shape."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(
        return_details=True,
        static_config_manifest={"containers": [{"name": "container-1"}]},
        workspace={"build_warnings": {"enabled": True}},
        change_control={"name": "cc-1"},
    )
    device_deployment = MagicMock(name="device_deployment")
    config = MagicMock(name="config")
    device_tag = MagicMock(name="device_tag")
    interface_tag = MagicMock(name="interface_tag")
    pathfinder_metadata = MagicMock(name="pathfinder_metadata")
    static_manifest = MagicMock(name="static_manifest")
    cloudvision = MagicMock(proxy_password="proxy-secret")  # noqa: S106 - deliberate redaction test value
    result_object = _make_deploy_result_mock(
        errors=[ValueError("cv-error")],
        warnings=[RuntimeError("cv-warning")],
        deployed_configs=[config],
        failed=True,
    )
    result_object.get_result.return_value = {"workflow_result": "complete"}

    with (
        patch(f"{MODULE_PATH}.CloudVision", return_value=cloudvision),
        patch(f"{MODULE_PATH}.CVDeployFuture", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.AvdManifest.from_dict", return_value=static_manifest),
        patch(f"{MODULE_PATH}.AvdWorkspaceBuildWarningsConfig.from_dict", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVChangeControl", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.AvdChangeControl", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVTimeOuts", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVWorkspace", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.AvdWorkspace", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([config], [device_tag], [interface_tag], [pathfinder_metadata])),
        patch(f"{MODULE_PATH}.get_result", side_effect=lambda value: {"value": value}),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[device_deployment]),
        patch(f"{MODULE_PATH}.deploy_to_cv", new_callable=AsyncMock, return_value=result_object) as deploy_to_cv,
    ):
        result = asyncio.run(module.deploy(validated_args, {"warnings": ["logger-warning"]}))

    deploy_to_cv.assert_awaited_once()
    assert result["cloudvision"]["token"] == "<removed>"  # noqa: S105 - deliberate redaction test
    assert result["cloudvision"]["proxy_password"] == "<removed>"  # noqa: S105 - deliberate redaction test
    assert result["configs"] == [{"value": config}]
    assert result["device_tags"] == [{"value": device_tag}]
    assert result["interface_tags"] == [{"value": interface_tag}]
    assert result["cv_pathfinder_metadata"] == [{"value": pathfinder_metadata}]
    assert result["static_config_manifest"] == {"value": static_manifest}
    assert result["workflow_result"] == "complete"
    assert result["changed"] is True
    assert result_object.errors == ["cv-error"]
    assert result_object.warnings == ["cv-warning", "logger-warning"]


def test_deploy_reads_validated_inputs_from_tmp_dir(
    action_module: Callable[..., ActionModule],
    tmp_path: Path,
) -> None:
    """The preview input mode passes the validated JSON directory to deployment building."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(
        tmp_dir=str(tmp_path),
        preview_features={"read_from_validated_inputs": True},
    )
    empty_result = _make_deploy_result_mock()
    validated_path = tmp_path / "validated"

    with (
        patch(f"{MODULE_PATH}.CloudVision", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVDeployFuture", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVGRPCChannelConfiguration", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVGRPCKeepalives", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(tmp_path / "templated", validated_path)),
        patch(f"{MODULE_PATH}.extract_from_device_deployments", return_value=([], [], [], [])),
        patch(f"{MODULE_PATH}.DeployToCvResult", return_value=empty_result),
        patch.object(module, "build_device_deployments", new_callable=AsyncMock, return_value=[]) as build_deployments,
    ):
        asyncio.run(module.deploy(validated_args, {}))

    build_deployments.assert_awaited_once_with(
        device_list=[],
        structured_config_dir=str(validated_path),
        structured_config_suffix="json",
        configuration_dir="/configs",
        configlet_name_template="AVD-${hostname}",
    )


# ---------------------------------------------------------------------------
# deploy() — error tests
# ---------------------------------------------------------------------------


def test_deploy_raises_when_read_from_validated_inputs_without_tmp_dir(
    action_module: Callable[..., ActionModule],
) -> None:
    """AnsibleActionFail is raised when preview_features.read_from_validated_inputs=True but tmp_dir is absent."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args(preview_features={"read_from_validated_inputs": True})

    with pytest.raises(
        AnsibleActionFail,
        match=r"tmp_dir is required when preview_features.read_from_validated_inputs is true",
    ):
        asyncio.run(module.deploy(validated_args, {}))


def test_deploy_wraps_exceptions_as_action_fail(
    action_module: Callable[..., ActionModule],
) -> None:
    """Any exception raised inside deploy() is caught and re-raised as AnsibleActionFail with chaining."""
    module = action_module(ActionModule)
    validated_args = _make_validated_args()
    original_error = RuntimeError("CloudVision connection failed")

    with (
        patch(f"{MODULE_PATH}.CloudVision", side_effect=original_error, create=True),
        pytest.raises(
            AnsibleActionFail,
            match=r"Error during plugin execution: CloudVision connection failed",
        ) as exc_info,
    ):
        asyncio.run(module.deploy(validated_args, {}))

    assert exc_info.value.__cause__ is original_error


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


def test_build_device_deployment_builds_config_tags_and_pathfinder_metadata(
    action_module: Callable[..., ActionModule],
) -> None:
    """Structured-config metadata is mapped to the corresponding CV deployment objects."""
    module = action_module(ActionModule)
    structured_config = {
        "serial_number": "global-serial",
        "system_mac_address": "00:00:00:00:00:01",
        "cv_device_tags": [{"name": "ignored", "value": "global"}],
        "metadata": {
            "serial_number": "metadata-serial",
            "system_mac_address": "00:00:00:00:00:02",
            "cv_use_static_config_manifest": False,
            "cv_tags": {
                "device_tags": [
                    {"name": "topology_hint_datacenter", "value": "DC1"},
                    {"name": "missing-value"},
                ],
                "interface_tags": [
                    {
                        "interface": "Ethernet3",
                        "tags": [
                            {"name": "peer_device_interface", "value": "Ethernet3"},
                            {"name": "missing-value"},
                        ],
                    },
                    {"interface": "Ethernet4"},
                ],
            },
            "cv_pathfinder": {"role": "edge"},
        },
    }

    with (
        patch.object(module, "load_structured_config", return_value=structured_config),
        patch(f"{MODULE_PATH}.AvdDevice", return_value=MagicMock(name="avd_device")) as avd_device,
        patch(f"{MODULE_PATH}.CVDevice", return_value=MagicMock(name="device")) as cv_device,
        patch(f"{MODULE_PATH}.CVEosConfig", return_value=MagicMock(name="eos_config")) as eos_config,
        patch(f"{MODULE_PATH}.CVDeviceTag", return_value=MagicMock(name="device_tag")) as device_tag,
        patch(f"{MODULE_PATH}.CVInterfaceTag", return_value=MagicMock(name="interface_tag")) as interface_tag,
        patch(f"{MODULE_PATH}.CVPathfinderMetadata", return_value=MagicMock(name="pathfinder")) as pathfinder,
        patch(f"{MODULE_PATH}.CVDeviceDeployment", return_value=MagicMock(name="deployment")) as deployment,
    ):
        result = asyncio.run(module.build_device_deployment("leaf1", "/structured", "yml", "/configs", "cfg-${hostname}"))

    assert result is deployment.return_value
    avd_device.assert_called_once_with(hostname="leaf1", serial_number="metadata-serial", system_mac_address="00:00:00:00:00:02")
    cv_device.assert_called_once()
    eos_config.assert_called_once_with(
        file="/configs/leaf1.cfg",
        device=cv_device.return_value,
        configlet_name="cfg-leaf1",
    )
    device_tag.assert_called_once_with(label="topology_hint_datacenter", value="DC1", device=cv_device.return_value)
    interface_tag.assert_called_once_with(
        label="peer_device_interface",
        value="Ethernet3",
        device=cv_device.return_value,
        interface="Ethernet3",
    )
    pathfinder.assert_called_once_with(metadata={"role": "edge"}, device=cv_device.return_value)
    deployment.assert_called_once_with(
        device=cv_device.return_value,
        use_static_config_manifest=False,
        eos_config=eos_config.return_value,
        device_tags=[device_tag.return_value],
        interface_tags=[interface_tag.return_value],
        cv_pathfinder_metadata=pathfinder.return_value,
    )


@pytest.mark.parametrize(
    ("structured_config", "expected_result"),
    [
        pytest.param({"metadata": {"is_deployed": False}}, None, id="not-deployed"),
        pytest.param(
            {"metadata": {"serial_number": "serial", "cv_use_static_config_manifest": True}},
            "deployment",
            id="static-config-manifest",
        ),
    ],
)
def test_build_device_deployment_handles_not_deployed_and_static_manifest(
    action_module: Callable[..., ActionModule],
    *,
    structured_config: dict,
    expected_result: str | None,
) -> None:
    """Undeployed devices are omitted and manifest devices have no flat EOS config."""
    module = action_module(ActionModule)
    with (
        patch.object(module, "load_structured_config", return_value=structured_config),
        patch(f"{MODULE_PATH}.CVDevice", return_value=MagicMock()) as cv_device,
        patch(f"{MODULE_PATH}.AvdDevice", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.CVDeviceDeployment", return_value=expected_result) as deployment,
        patch(f"{MODULE_PATH}.CVEosConfig") as eos_config,
    ):
        result = asyncio.run(module.build_device_deployment("leaf1", "/structured", "yml", "/configs", "cfg-${hostname}"))

    assert result == expected_result
    if expected_result is None:
        cv_device.assert_not_called()
        deployment.assert_not_called()
        eos_config.assert_not_called()
    else:
        cv_device.assert_called_once()
        deployment.assert_called_once_with(
            device=cv_device.return_value,
            use_static_config_manifest=True,
            eos_config=None,
            device_tags=[],
            interface_tags=[],
            cv_pathfinder_metadata=None,
        )
        eos_config.assert_not_called()
