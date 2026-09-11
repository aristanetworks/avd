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
        asyncio.run(module.deploy(validated_args, {}))

    deploy_logs = [msg for msg in caplog.messages if msg.startswith("deploy:")]
    assert deploy_logs, "Expected at least one INFO log starting with 'deploy:'"
    assert "<removed>" in deploy_logs[0]


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


def test_build_decommission_device_deployment_preserves_tag_metadata(action_module: Callable[..., ActionModule]) -> None:
    """Tag objects are built for decommission devices but no EOS config object is built."""
    module = action_module(ActionModule)
    structured_config = {
        "metadata": {
            "is_deployed": False,
            "serial_number": "SN1",
            "cv_tags": {
                "device_tags": [{"name": "role", "value": "leaf"}],
                "interface_tags": [{"interface": "Ethernet1", "tags": [{"name": "link_type", "value": "underlay"}]}],
            },
        }
    }

    with patch.object(module, "load_structured_config", return_value=structured_config):
        deployment = asyncio.run(module.build_device_deployment("leaf1", "/structured", "yml", "/configs", "AVD-${hostname}", inventory_mode="controlled"))

    assert deployment is not None
    assert deployment.device.action == "decommission"
    assert deployment.eos_config is None
    assert [(tag.label, tag.value) for tag in deployment.device_tags] == [("role", "leaf")]
    assert [(tag.interface, tag.label, tag.value) for tag in deployment.interface_tags] == [("Ethernet1", "link_type", "underlay")]
