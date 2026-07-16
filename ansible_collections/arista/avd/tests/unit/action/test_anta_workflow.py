# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
import sys
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, mock_open, patch

import pytest
from ansible.errors import AnsibleActionFail

import ansible_collections.arista.avd.plugins.action.anta_workflow as anta_module
from ansible_collections.arista.avd.plugins.action.anta_workflow import (
    PLUGIN_NAME,
    ActionModule,
    build_anta_device,
    build_anta_runner_objects,
    build_reports,
    get_ansible_vars,
    get_device_catalog_filters,
    load_one_structured_config,
    load_user_catalogs,
    run_anta,
    setup_anta_debug_mode,
)

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.anta_workflow"
AVD_LOGGER_NAME = "ansible_collections.arista.avd"


def test_get_ansible_vars_logs_info_when_device_not_deployed(caplog: pytest.LogCaptureFixture) -> None:
    """An INFO log is emitted for each device skipped because is_deployed=False."""
    apv = MagicMock()
    apv.__getitem__.side_effect = lambda device: {"leaf1": {"inventory_hostname": "leaf1", "is_deployed": False}}[device]
    with caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME):
        get_ansible_vars(["leaf1"], apv)
    assert "<leaf1> Device marked as not deployed - Skipping all tests" in caplog.messages


@pytest.mark.parametrize(
    ("filter_key", "expected_msg"),
    [
        pytest.param(
            "run_tests",
            "<leaf1> run_tests overridden from ['TestBGP'] to ['TestMTU']",
            id="run_tests_overridden",
        ),
        pytest.param(
            "skip_tests",
            "<leaf1> skip_tests overridden from ['TestBGP'] to ['TestMTU']",
            id="skip_tests_overridden",
        ),
    ],
)
def test_get_device_catalog_filters_logs_debug_when_filter_overridden(
    caplog: pytest.LogCaptureFixture,
    *,
    filter_key: str,
    expected_msg: str,
) -> None:
    """A DEBUG log is emitted when a later filter overrides an already-set run_tests or skip_tests."""
    filters = [{filter_key: ["TestBGP"]}, {filter_key: ["TestMTU"]}]
    with caplog.at_level(logging.DEBUG, logger=AVD_LOGGER_NAME):
        get_device_catalog_filters("leaf1", filters)
    assert expected_msg in caplog.messages


def test_build_anta_runner_objects_logs_warning_when_eapi_not_enabled(monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture) -> None:
    """A WARNING is emitted when a device's structured config has neither enable_https nor enable_http."""
    monkeypatch.setattr(anta_module, "STRUCTURED_CONFIGS", {"leaf1": {"management_api_http": {}}})
    monkeypatch.setattr(anta_module, "FABRIC_DATA", MagicMock())
    monkeypatch.setattr(anta_module, "PLUGIN_ARGS", {"avd_catalogs": {"filters": []}})
    monkeypatch.setattr(anta_module, "USER_CATALOG", None)
    with (
        patch(f"{MODULE_PATH}.ResultManager"),
        patch(f"{MODULE_PATH}.AntaInventory"),
        patch(f"{MODULE_PATH}.AntaCatalog"),
        caplog.at_level(logging.WARNING, logger=AVD_LOGGER_NAME),
    ):
        build_anta_runner_objects(["leaf1"])
    assert "<leaf1> Device eAPI is not enabled in the structured configuration - Skipping all tests" in caplog.messages


def test_load_user_catalogs_logs_warning_for_unsupported_file_format(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """A WARNING is emitted for each catalog file whose extension is not YAML or JSON."""
    catalog_file = tmp_path / "catalog.txt"
    catalog_file.touch()
    with (
        patch(f"{MODULE_PATH}.AntaCatalog") as mock_catalog,
        caplog.at_level(logging.WARNING, logger=AVD_LOGGER_NAME),
    ):
        mock_catalog.merge_catalogs.return_value = MagicMock()
        load_user_catalogs(str(tmp_path))
    assert f"Skipped user-defined ANTA catalog file {catalog_file} - unsupported format" in caplog.messages


def test_load_user_catalogs_logs_info_when_loading_catalog(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """An INFO log naming the catalog file is emitted when a supported catalog is loaded."""
    catalog_file = tmp_path / "catalog.yml"
    catalog_file.touch()
    with (
        patch(f"{MODULE_PATH}.AntaCatalog") as mock_catalog,
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        mock_catalog.parse.return_value = MagicMock()
        mock_catalog.merge_catalogs.return_value = MagicMock()
        load_user_catalogs(str(tmp_path))
    assert f"Loading user-defined ANTA catalog from {catalog_file}" in caplog.messages


def test_load_user_catalogs_logs_info_when_no_catalogs_found(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """An INFO log is emitted when the catalog directory contains no supported files."""
    with (
        patch(f"{MODULE_PATH}.AntaCatalog") as mock_catalog,
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        mock_catalog.merge_catalogs.return_value = MagicMock()
        load_user_catalogs(str(tmp_path))
    assert f"No user-defined ANTA catalogs found in directory: {tmp_path}" in caplog.messages


@pytest.mark.parametrize(
    ("debug_flag", "verbosity", "pythonasynciodebug", "expected_msg"),
    [
        pytest.param(
            True,
            2,
            False,
            "Initial ANTA_DEBUG value: True",
            id="initial_value_logged",
        ),
        pytest.param(
            True,
            2,
            False,
            "ANTA_DEBUG is True and Ansible verbosity (2) < 3. Overriding ANTA_DEBUG to False for this plugin run",
            id="overriding_flag",
        ),
        pytest.param(
            True,
            1,
            True,
            "ANTA_DEBUG was True (causing PYTHONASYNCIODEBUG=1). "
            "Since ANTA_DEBUG is now overridden to False by the plugin, deleting PYTHONASYNCIODEBUG environment variable",
            id="deleting_pythonasynciodebug",
        ),
        pytest.param(
            True,
            3,
            False,
            "ANTA_DEBUG is True and Ansible verbosity (3) >= 3. ANTA debug mode will remain active as per the environment variable",
            id="remaining_active_high_verbosity",
        ),
        pytest.param(
            False,
            0,
            False,
            "ANTA_DEBUG is False. Plugin will not change ANTA debug settings",
            id="flag_already_false",
        ),
    ],
)
def test_setup_anta_debug_mode_logs_debug_messages(
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
    *,
    debug_flag: bool,
    verbosity: int,
    pythonasynciodebug: bool,
    expected_msg: str,
) -> None:
    """Each setup_anta_debug_mode code path emits the expected DEBUG log message."""
    fake_mod = MagicMock()
    fake_mod.__DEBUG__ = debug_flag
    monkeypatch.setitem(sys.modules, "anta.logger", fake_mod)
    if pythonasynciodebug:
        monkeypatch.setenv("PYTHONASYNCIODEBUG", "1")
    with caplog.at_level(logging.DEBUG, logger=AVD_LOGGER_NAME):
        setup_anta_debug_mode(verbosity=verbosity)
    assert expected_msg in caplog.messages


def test_action_module_run_logs_warning_when_user_catalog_has_no_tests(action_module: Callable[..., ActionModule], caplog: pytest.LogCaptureFixture) -> None:
    """A WARNING is emitted and the task exits early when user catalogs are empty and AVD catalogs are disabled."""
    module = action_module(ActionModule)
    validated_args = {
        "device_list": ["leaf1"],
        "avd_catalogs": {"enabled": False},
        "user_catalogs": {"enabled": True, "input_dir": "/some/catalogs"},
    }
    empty_catalog = MagicMock()
    empty_catalog.tests = []
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch(f"{MODULE_PATH}.setup_queue_listener", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.setup_parent_process_logging"),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.strip_empties_from_dict", side_effect=lambda d: d),
        patch(f"{MODULE_PATH}.get_ansible_vars", return_value={"leaf1": {}}),
        patch(f"{MODULE_PATH}.ActionPluginVars"),
        patch(f"{MODULE_PATH}.load_user_catalogs", return_value=empty_catalog),
        caplog.at_level(logging.WARNING, logger=AVD_LOGGER_NAME),
    ):
        module.run(task_vars={})
    assert "No tests found in the user-defined ANTA catalogs, exiting" in caplog.messages


@pytest.mark.parametrize(
    ("dry_run", "expected_run_mode"),
    [
        pytest.param(False, "run", id="normal_run"),
        pytest.param(True, "dry-run", id="dry_run"),
    ],
)
def test_run_anta_logs_info_for_start_and_completion(
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
    *,
    dry_run: bool,
    expected_run_mode: str,
) -> None:
    """INFO logs are emitted when ANTA starts and completes for the given devices and run mode."""
    monkeypatch.setattr(anta_module, "PLUGIN_ARGS", {"runner": {"dry_run": dry_run, "tags": []}})
    with (
        patch(f"{MODULE_PATH}.setup_child_process_logging"),
        patch(f"{MODULE_PATH}.build_anta_runner_objects", return_value=(MagicMock(), MagicMock(), MagicMock())),
        patch(f"{MODULE_PATH}.anta_runner", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.run"),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        run_anta(["leaf1", "leaf2"])
    assert f"Starting ANTA {expected_run_mode} for devices: leaf1, leaf2" in caplog.messages
    assert f"ANTA {expected_run_mode} completed for devices: leaf1, leaf2" in caplog.messages


def test_build_reports_logs_warning_when_all_results_hidden_by_filters(caplog: pytest.LogCaptureFixture) -> None:
    """A WARNING is emitted when exclude_statuses hides every result leaving an empty report."""
    mock_result_manager = MagicMock()
    mock_result_manager.results = [MagicMock()]
    mock_result_manager.get_total_results.return_value = 0
    mock_result_manager.device_stats = {}

    mock_filtered_manager = MagicMock()
    mock_filtered_manager.results = []
    mock_result_manager.filter.return_value = mock_filtered_manager

    batch_manager = MagicMock()
    batch_manager.results = [MagicMock()]

    report_settings = {
        "filters": {"exclude_statuses": ["success"]},
        "sorting": {
            "sort_fields": ["device", "test"],
            "status_priority": ["error", "failure", "skipped", "success", "unset"],
        },
    }

    with (
        patch(f"{MODULE_PATH}.ResultManager", return_value=mock_result_manager),
        patch(f"{MODULE_PATH}.sort_result_manager"),
        caplog.at_level(logging.WARNING, logger=AVD_LOGGER_NAME),
    ):
        build_reports(iter([batch_manager]), report_settings)

    assert "The report is empty because all results were hidden by the provided status filters: success" in caplog.messages


@pytest.mark.parametrize(
    ("report_settings_extra", "expected_log"),
    [
        pytest.param({"csv_output": "/out/report.csv"}, "Generating CSV report at /out/report.csv", id="csv"),
        pytest.param({"md_output": "/out/report.md"}, "Generating Markdown report at /out/report.md", id="markdown"),
        pytest.param({"json_output": "/out/report.json"}, "Generating JSON report at /out/report.json", id="json"),
    ],
)
def test_build_reports_logs_info_for_each_report_type(
    caplog: pytest.LogCaptureFixture,
    *,
    report_settings_extra: dict,
    expected_log: str,
) -> None:
    """An INFO log naming the output path is emitted for each report format that is configured."""
    mock_result_manager = MagicMock()
    mock_result_manager.results = []
    mock_result_manager.get_total_results.return_value = 0
    mock_result_manager.device_stats = {}

    report_settings = {
        "sorting": {
            "sort_fields": ["device", "test"],
            "status_priority": ["error", "failure", "skipped", "success", "unset"],
        },
        **report_settings_extra,
    }

    with (
        patch(f"{MODULE_PATH}.ResultManager", return_value=mock_result_manager),
        patch(f"{MODULE_PATH}.sort_result_manager"),
        patch(f"{MODULE_PATH}.ReportCsv"),
        patch(f"{MODULE_PATH}.MDReportGenerator"),
        patch("pathlib.Path.open", mock_open()),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        build_reports(iter([]), report_settings)

    assert expected_log in caplog.messages


def test_action_module_run_raises_when_pyavd_missing(action_module: Callable[..., ActionModule]) -> None:
    """run() raises AnsibleActionFail with the full message when HAS_PYAVD is False."""
    module = action_module(ActionModule)
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        pytest.raises(
            AnsibleActionFail,
            match=rf"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library. Got import error",
        ),
    ):
        module.run(task_vars={})


@pytest.mark.parametrize(
    ("validated_args", "error_match"),
    [
        pytest.param(
            {"device_list": []},
            r"'device_list' cannot be empty",
            id="empty_device_list",
        ),
        pytest.param(
            {"device_list": ["leaf1"], "avd_catalogs": {"enabled": False}, "user_catalogs": {"enabled": False}},
            r"At least one of 'avd_catalogs.enabled' or 'user_catalogs.enabled' must be set to True",
            id="both_catalogs_disabled",
        ),
        pytest.param(
            {"device_list": ["leaf1"], "avd_catalogs": {"enabled": True}},
            (
                r"When 'avd_catalogs.enabled' is True, a directory with device structured configurations "
                r"must be provided using the 'avd_catalogs.structured_config_dir' argument"
            ),
            id="avd_catalogs_without_structured_config_dir",
        ),
        pytest.param(
            {"device_list": ["leaf1"], "avd_catalogs": {"enabled": False}, "user_catalogs": {"enabled": True}},
            (
                r"When 'user_catalogs.enabled' is True, a directory with user-defined ANTA catalogs "
                r"must be provided using the 'user_catalogs.input_dir' argument"
            ),
            id="user_catalogs_without_input_dir",
        ),
    ],
)
def test_action_module_run_raises_on_invalid_args(
    action_module: Callable[..., ActionModule],
    *,
    validated_args: dict,
    error_match: str,
) -> None:
    """run() raises AnsibleActionFail for invalid argument combinations (empty device list, disabled catalogs, missing dirs)."""
    module = action_module(ActionModule)
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch(f"{MODULE_PATH}.setup_queue_listener", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.setup_parent_process_logging"),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.strip_empties_from_dict", side_effect=lambda d: d),
        patch(f"{MODULE_PATH}.get_ansible_vars", return_value={"leaf1": {}}),
        patch(f"{MODULE_PATH}.ActionPluginVars"),
        pytest.raises(AnsibleActionFail, match=error_match),
    ):
        module.run(task_vars={})


def test_action_module_run_wraps_unexpected_exception_via_raise_action_fail(
    action_module: Callable[..., ActionModule],
) -> None:
    """Any exception inside the try block is passed to raise_action_fail as 'Error during plugin execution: <error>'."""
    module = action_module(ActionModule)
    validated_args = {
        "device_list": ["leaf1"],
        "avd_catalogs": {"enabled": False},
        "user_catalogs": {"enabled": True, "input_dir": "/some/catalogs"},
    }
    mock_raise_action_fail = MagicMock()
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch(f"{MODULE_PATH}.setup_queue_listener", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.setup_parent_process_logging"),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.strip_empties_from_dict", side_effect=lambda d: d),
        patch(f"{MODULE_PATH}.get_ansible_vars", return_value={"leaf1": {}}),
        patch(f"{MODULE_PATH}.ActionPluginVars"),
        patch(f"{MODULE_PATH}.load_user_catalogs", side_effect=RuntimeError("disk on fire")),
        patch(f"{MODULE_PATH}.raise_action_fail", mock_raise_action_fail),
    ):
        module.run(task_vars={})
    mock_raise_action_fail.assert_called_once()
    assert mock_raise_action_fail.call_args[0][0] == "Error during plugin execution: disk on fire"


def test_setup_anta_debug_mode_raises_when_anta_logger_absent() -> None:
    """AnsibleActionFail is raised when anta.logger is not present in sys.modules."""
    with (
        patch.dict(sys.modules, {"anta.logger": None}),
        pytest.raises(
            AnsibleActionFail,
            match=(
                r"Cannot find the '__DEBUG__' attribute of the 'anta.logger' module, "
                r"even though PyAVD dependencies were expected to be loaded. "
                r"This indicates a severe issue with the Python environment or ANTA installation."
            ),
        ),
    ):
        setup_anta_debug_mode(verbosity=0)


def test_build_anta_device_raises_when_required_settings_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """ValueError with the device name is raised when host, username, or password cannot be resolved."""
    monkeypatch.setattr(anta_module, "ANSIBLE_VARS", {"leaf1": {}})
    monkeypatch.setattr(anta_module, "PLUGIN_ARGS", {})
    with pytest.raises(
        ValueError,
        match=(
            r"Device 'leaf1' is missing required connection settings. "
            r"Please make sure all required connection variables are defined in the Ansible inventory, "
            r"as specified in the role documentation."
        ),
    ):
        build_anta_device("leaf1")


def test_validate_argument_spec_materializes_runner_defaults(action_module: Callable[..., ActionModule]) -> None:
    """`apply_defaults` materializes runner defaults even when the runner block is omitted."""
    module = action_module(ActionModule, task_args={"device_list": ["leaf1"]})

    _validation_result, validated_args = module.validate_argument_spec(anta_module.ARGUMENT_SPEC)
    validated_args = anta_module.strip_empties_from_dict(validated_args)

    assert validated_args["runner"]["timeout"] == 30.0
    assert validated_args["runner"]["batch_size"] == 5
    assert validated_args["runner"]["dry_run"] is False


def test_validate_argument_spec_materializes_report_sorting_defaults(action_module: Callable[..., ActionModule]) -> None:
    """`apply_defaults` materializes report.sorting defaults when report is provided without sorting."""
    module = action_module(
        ActionModule,
        task_args={
            "device_list": ["leaf1"],
        },
    )

    _validation_result, validated_args = module.validate_argument_spec(anta_module.ARGUMENT_SPEC)
    validated_args = anta_module.strip_empties_from_dict(validated_args)

    assert validated_args["report"]["sorting"]["status_priority"] == ["error", "failure", "skipped", "success", "unset"]
    assert validated_args["report"]["sorting"]["sort_fields"] == ["device", "categories", "test", "description", "custom_field"]


def test_load_one_structured_config_raises_for_missing_file(tmp_path: Path) -> None:
    """FileNotFoundError is raised when the structured config file does not exist."""
    with pytest.raises(FileNotFoundError, match=r"Structured configuration file for device 'leaf1' not found"):
        load_one_structured_config("leaf1", str(tmp_path), "yml")
