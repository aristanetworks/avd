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

from ansible_collections.arista.avd.plugins.action.cv_workflow import ActionModule, setup_module_logging

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
    log_message = deploy_logs[0]
    assert "real-secret-token" not in log_message
    assert "real-secret-password" not in log_message
    assert "real-secret-proxy" not in log_message
    assert "<removed>" in log_message


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


def test_load_structured_config_logs_info_when_no_structured_config_dir(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """An INFO log naming the host is emitted when structured_config_dir is None."""
    module = action_module(ActionModule)

    with caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME):
        module.load_structured_config("my-device", None, "yml")

    assert any("No structured config file for my-device" in msg for msg in caplog.messages)


def test_load_structured_config_logs_info_when_file_does_not_exist(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
    tmp_path: Path,
) -> None:
    """An INFO log naming the host is emitted when the structured config file is missing."""
    module = action_module(ActionModule)

    with caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME):
        module.load_structured_config("missing-device", str(tmp_path), "yml")

    assert any("No structured config file for missing-device" in msg for msg in caplog.messages)


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
# setup_module_logging() — logging tests
# ---------------------------------------------------------------------------


def test_setup_module_logging_routes_warning_logs_to_result() -> None:
    """WARNING-level logs emitted via the AVD logger are appended to result['warnings'] by the handler."""
    result: dict = {}
    root_logger = logging.getLogger()
    original_level = root_logger.level
    original_handlers = root_logger.handlers[:]
    avd_logger = logging.getLogger(AVD_LOGGER_NAME)

    with patch(f"{MODULE_PATH}.display") as mock_display:
        mock_display.verbosity = 0
        setup_module_logging(result)
        root_logger.setLevel(logging.WARNING)
        avd_logger.warning("something went wrong during deployment")

    try:
        assert "warnings" in result
        assert any("something went wrong during deployment" in w for w in result["warnings"])
    finally:
        root_logger.setLevel(original_level)
        root_logger.handlers = original_handlers


def test_setup_module_logging_adds_handler_to_root_logger() -> None:
    """A PythonToAnsibleHandler is added to the root logger by setup_module_logging."""
    root_logger = logging.getLogger()
    original_handlers = root_logger.handlers[:]

    with patch(f"{MODULE_PATH}.PythonToAnsibleHandler") as mock_handler_cls:
        mock_handler = MagicMock()
        mock_handler_cls.return_value = mock_handler
        setup_module_logging({})

    try:
        assert mock_handler in root_logger.handlers
    finally:
        root_logger.handlers = original_handlers


@pytest.mark.parametrize(
    ("verbosity", "expected_level"),
    [
        pytest.param(3, logging.DEBUG, id="verbosity_3_sets_debug"),
        pytest.param(4, logging.DEBUG, id="verbosity_4_sets_debug"),
        pytest.param(1, logging.INFO, id="verbosity_1_sets_info"),
        pytest.param(2, logging.INFO, id="verbosity_2_sets_info"),
    ],
)
def test_setup_module_logging_sets_level_based_on_verbosity(
    verbosity: int,
    expected_level: int,
) -> None:
    """Root logger level is DEBUG when verbosity>=3, INFO when verbosity>=1."""
    root_logger = logging.getLogger()
    original_level = root_logger.level
    original_handlers = root_logger.handlers[:]

    with (
        patch(f"{MODULE_PATH}.display") as mock_display,
        patch(f"{MODULE_PATH}.PythonToAnsibleHandler"),
    ):
        mock_display.verbosity = verbosity
        setup_module_logging({})

    try:
        assert root_logger.level == expected_level
    finally:
        root_logger.setLevel(original_level)
        root_logger.handlers = original_handlers
