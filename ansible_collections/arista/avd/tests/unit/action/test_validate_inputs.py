# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest

from ansible_collections.arista.avd.plugins.action import validate_inputs as vi_module
from ansible_collections.arista.avd.plugins.action.validate_inputs import (
    PLUGIN_NAME,
    ActionModule,
    ValidateWorkerSkipped,
    ValidateWorkerSuccess,
    WorkerFailure,
    _template_host_worker,
    _validate_host_worker,
    get_worker_hostvars,
)

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.validate_inputs"
AVD_LOGGER_NAME = "ansible_collections.arista.avd"


# ---------------------------------------------------------------------------
# Fixtures and helpers
# ---------------------------------------------------------------------------


@pytest.fixture
def reset_worker_context() -> Generator[None, None, None]:
    """Snapshot and restore the module-global ``_HOSTVARS_MANAGER``."""
    original = vi_module._HOSTVARS_MANAGER
    try:
        yield
    finally:
        vi_module._HOSTVARS_MANAGER = original


def _make_pool_mock(results: list) -> MagicMock:
    """Return a fake pool context manager whose ``.map(...)`` yields the given results."""
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter(results)
    return fake_pool_cm


def _make_plugin_args(**overrides: object) -> MagicMock:
    """Build a MagicMock with the default plugin_args shape, overridable per test."""
    defaults: dict = {
        "tmp_dir": "/avd/tmp",
        "read_from_input_dir": True,
        "input_dir": "/inputs",
        "input_suffix": "json",
        "schema_name": "avd_design",
        "batch_size": 10,
        "device_list": None,
    }
    defaults.update(overrides)
    return MagicMock(**defaults)


def _run_validation_phase_kwargs(**overrides: object) -> dict:
    """Default kwargs accepted by ``ActionModule._run_validation_phase``, overridable per test."""
    kwargs: dict = {
        "workers": 1,
        "input_path": Path("/in"),
        "input_suffix": "json",
        "output_path": Path("/out"),
        "schema_name": "avd_design",
        "fail_on_missing_input_files": True,
        "fail_on_validation_errors": False,
        "configuration": None,
        "file_handler": MagicMock(),
    }
    kwargs.update(overrides)
    return kwargs


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("has_vault_secrets", "expected_message"),
    [
        pytest.param(True, "Ansible Vault secrets are configured - temporary files will be encrypted", id="vault_configured"),
        pytest.param(False, "Ansible Vault secrets are not configured - temporary files will not be encrypted", id="vault_not_configured"),
    ],
)
def test_main_logs_vault_status_at_info_level(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
    *,
    has_vault_secrets: bool,
    expected_message: str,
) -> None:
    """Verify main emits the Vault-status INFO log on the AVD logger."""
    module = action_module(ActionModule)
    vault_handler = MagicMock()
    vault_handler.has_vault_secrets = has_vault_secrets

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(module, "_get_plugin_args", return_value=_make_plugin_args()),
        patch.object(module, "_get_hosts_to_process", return_value=[]),
        patch.object(module, "_run_validation_phase"),
        patch(f"{MODULE_PATH}.get_workers", return_value=(1, 1)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/avd/templated"), Path("/avd/validated"))),
        patch(f"{MODULE_PATH}.AVDVaultHandler", return_value=vault_handler),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module.main(task_vars={"ansible_forks": 1, "ansible_play_hosts_all": []})

    assert expected_message in caplog.messages


def test_main_logs_starting_execution_summary(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Verify the 'Starting execution...' INFO log includes worker and batch counts."""
    module = action_module(ActionModule)

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(module, "_get_plugin_args", return_value=_make_plugin_args(batch_size=7)),
        patch.object(module, "_get_hosts_to_process", return_value=["host1", "host2", "host3"]),
        patch.object(module, "_run_validation_phase"),
        patch(f"{MODULE_PATH}.get_workers", return_value=(4, 8)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/avd/templated"), Path("/avd/validated"))),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module.main(task_vars={"ansible_forks": 1, "ansible_play_hosts_all": []})

    assert "Starting execution with 4 multiprocessing workers and 8 threads for 3 hosts in batches of 7" in caplog.messages


@pytest.mark.usefixtures("reset_worker_context")
@pytest.mark.parametrize(
    ("read_from_input_dir", "expected_message"),
    [
        pytest.param(False, "Reading inputs from hostvars", id="from_hostvars"),
        pytest.param(True, "Reading inputs from '/some/inputs'", id="from_input_dir"),
    ],
)
def test_main_logs_input_source(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
    *,
    read_from_input_dir: bool,
    expected_message: str,
) -> None:
    """Verify the INFO log identifying where inputs are sourced from."""
    module = action_module(ActionModule)

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(
            module,
            "_get_plugin_args",
            return_value=_make_plugin_args(read_from_input_dir=read_from_input_dir, input_dir="/some/inputs"),
        ),
        patch.object(module, "_get_hosts_to_process", return_value=["host1"]),
        patch.object(module, "_run_templating_phase", return_value=["host1"]),
        patch.object(module, "_run_validation_phase"),
        patch(f"{MODULE_PATH}.get_workers", return_value=(1, 1)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/avd/templated"), Path("/avd/validated"))),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        patch(f"{MODULE_PATH}.ActionPluginVars"),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module.main(task_vars={"ansible_forks": 1, "ansible_play_hosts_all": []})

    assert expected_message in caplog.messages


def test_run_templating_phase_logs_mixed_results(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Drive the templating loop with one failure and one success and assert every log line in one pass."""
    module = action_module(ActionModule)
    module.crashed_hosts = set()

    failure = WorkerFailure(hostname="host1", error="boom")
    success = MagicMock(spec_set=["hostname", "output_file"])
    success.hostname = "host2"
    success.output_file = "/output/host2.json"

    with (
        patch(f"{MODULE_PATH}.ProcessPoolExecutor", return_value=_make_pool_mock([failure, success])),
        patch(f"{MODULE_PATH}.get_context"),
        patch(f"{MODULE_PATH}.perf_counter", side_effect=[100.0, 101.23]),
        caplog.at_level(logging.DEBUG, logger=AVD_LOGGER_NAME),
    ):
        module._run_templating_phase(
            hostnames=["host1", "host2"],
            workers=1,
            batch_size=1,
            output_path=Path("/output"),
            schema_name="avd_design",
            file_handler=MagicMock(),
        )

    info_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.INFO]
    error_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.ERROR]
    debug_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.DEBUG]

    assert "Templating hostvars..." in info_messages
    assert "Templating of hostvars completed in 1.23s" in info_messages
    assert "host1: boom" in error_messages
    assert "Templated data for host host2 saved to /output/host2.json" in debug_messages
    assert module.crashed_hosts == {"host1"}


def test_run_validation_phase_logs_mixed_results(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Drive the validation loop with all four result types and assert every log line in one pass."""
    module = action_module(ActionModule)
    module.crashed_hosts = set()

    skipped = ValidateWorkerSkipped(hostname="host1", reason="No input file: /in/host1.json")
    failure = WorkerFailure(hostname="host2", error="boom")
    no_output = ValidateWorkerSuccess(hostname="host3", validation_result=MagicMock(), output_file=None)
    success = ValidateWorkerSuccess(hostname="host4", validation_result=MagicMock(), output_file="/out/host4.json")

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=_make_pool_mock([skipped, failure, no_output, success])),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.parse_validation_result", return_value=0),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
        patch(f"{MODULE_PATH}.perf_counter", side_effect=[200.0, 204.56]),
        caplog.at_level(logging.DEBUG, logger=AVD_LOGGER_NAME),
    ):
        module._run_validation_phase(hostnames=["host1", "host2", "host3", "host4"], **_run_validation_phase_kwargs())

    info_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.INFO]
    error_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.ERROR]
    debug_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.DEBUG]

    assert "Validating inputs..." in info_messages
    assert "Validation of inputs completed in 4.56s" in info_messages
    assert "Validation skipped for host host1: No input file: /in/host1.json" in info_messages
    assert "host2: boom" in error_messages
    assert "Host host3 passed validation but no output file was generated." in error_messages
    assert "Validated data for host host4 saved to /out/host4.json" in debug_messages
    assert module.crashed_hosts == {"host2", "host3"}


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("reset_worker_context")
def test_get_worker_hostvars_raises_when_context_not_initialized() -> None:
    """get_worker_hostvars raises RuntimeError if set_worker_context was not called before forking."""
    vi_module._HOSTVARS_MANAGER = None
    with pytest.raises(RuntimeError, match=r"Worker context not initialized\. 'set_worker_context' was not called before forking\."):
        get_worker_hostvars()


def test_main_raises_import_error_when_pyavd_missing(action_module: Callable[..., ActionModule]) -> None:
    """When HAS_PYAVD is False, main raises ImportError naming the plugin."""
    module = action_module(ActionModule)
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        pytest.raises(ImportError, match=rf"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library\. Got import error\."),
    ):
        module.main(task_vars={})


def test_get_hosts_to_process_raises_for_invalid_fabric_name(action_module: Callable[..., ActionModule]) -> None:
    """_get_hosts_to_process raises ValueError when play hosts are not all in the fabric group."""
    module = action_module(ActionModule)
    module._templar = MagicMock()
    module._templar.template = lambda x: x

    expected = (
        r"Invalid/missing 'fabric_name' variable\. "
        r"All hosts in the play must have the same 'fabric_name' value "
        r"which must point to an Ansible Group containing the hosts\."
        r"play_hosts: \['host1'\]"
    )
    with pytest.raises(ValueError, match=expected):
        module._get_hosts_to_process(
            task_vars={
                "ansible_play_hosts_all": ["host1"],
                "groups": {"fabric_a": ["host2"]},
                "fabric_name": "fabric_a",
            },
            schema_name="avd_design",
            device_list=None,
        )


def test_main_raises_runtime_error_when_hosts_crashed(action_module: Callable[..., ActionModule]) -> None:
    """A non-empty crashed_hosts set at the end of main triggers a RuntimeError listing the hostnames."""
    module = action_module(ActionModule)

    def fake_validation(**_kwargs: object) -> None:
        module.crashed_hosts.update({"host1", "host2"})

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(module, "_get_plugin_args", return_value=_make_plugin_args()),
        patch.object(module, "_get_hosts_to_process", return_value=["host1", "host2"]),
        patch.object(module, "_run_validation_phase", side_effect=fake_validation),
        patch(f"{MODULE_PATH}.get_workers", return_value=(1, 1)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/avd/templated"), Path("/avd/validated"))),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        pytest.raises(RuntimeError, match=r"Unexpected errors occurred while processing 2 host\(s\): host1, host2\."),
    ):
        module.main(task_vars={"ansible_forks": 1, "ansible_play_hosts_all": []})


def test_template_host_worker_wraps_exceptions_as_worker_failure() -> None:
    """Any exception inside the templating worker is caught and returned as WorkerFailure."""
    with patch(f"{MODULE_PATH}.get_worker_hostvars", side_effect=RuntimeError("no context")):
        result = _template_host_worker("host1", output_path=Path("/x"), schema_name="avd_design", file_handler=MagicMock())

    assert isinstance(result, WorkerFailure)
    assert result.hostname == "host1"
    assert result.error == "Unexpected error in templating worker process: no context"


def test_validate_host_worker_returns_worker_failure_when_input_missing_and_fail_flag_true(tmp_path: Path) -> None:
    """fail_on_missing_input_files=True turns a missing input file into a WorkerFailure."""
    missing_file = tmp_path / "host1.json"  # exists() == False
    input_path = MagicMock()
    input_path.__truediv__.return_value = missing_file

    result = _validate_host_worker(
        hostname="host1",
        input_path=input_path,
        input_suffix="json",
        output_path=Path("/out"),
        schema_name="avd_design",
        configuration=None,
        file_handler=MagicMock(),
        fail_on_missing_input_files=True,
    )

    assert isinstance(result, WorkerFailure)
    assert result.hostname == "host1"
    assert result.error == f"Missing input data file: {missing_file}"


def test_validate_host_worker_returns_skipped_when_input_missing_and_fail_flag_false(tmp_path: Path) -> None:
    """fail_on_missing_input_files=False turns a missing input file into ValidateWorkerSkipped."""
    missing_file = tmp_path / "host1.json"  # exists() == False
    input_path = MagicMock()
    input_path.__truediv__.return_value = missing_file

    result = _validate_host_worker(
        hostname="host1",
        input_path=input_path,
        input_suffix="json",
        output_path=Path("/out"),
        schema_name="avd_design",
        configuration=None,
        file_handler=MagicMock(),
        fail_on_missing_input_files=False,
    )

    assert isinstance(result, ValidateWorkerSkipped)
    assert result.hostname == "host1"
    assert result.reason == f"No input file: {missing_file}"


def test_run_validation_phase_sets_failed_when_validation_errors_and_fail_flag_true(
    action_module: Callable[..., ActionModule],
) -> None:
    """If fail_on_validation_errors=True and a host has validation errors, self.result['failed'] is set to True."""
    module = action_module(ActionModule)
    module.crashed_hosts = set()

    success = ValidateWorkerSuccess(hostname="host1", validation_result=MagicMock(), output_file="/out/host1.json")

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=_make_pool_mock([success])),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.parse_validation_result", return_value=3),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
    ):
        module._run_validation_phase(hostnames=["host1"], **_run_validation_phase_kwargs(fail_on_validation_errors=True))

    assert module.result.get("failed") is True
    assert module.crashed_hosts == set()


def test_run_validation_phase_sets_result_msg_when_build_result_message_returns_text(
    action_module: Callable[..., ActionModule],
) -> None:
    """A non-empty build_result_message return value populates self.result['msg']."""
    module = action_module(ActionModule)
    module.crashed_hosts = set()

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=_make_pool_mock([])),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.build_result_message", return_value="3 data validation errors found"),
    ):
        module._run_validation_phase(hostnames=[], **_run_validation_phase_kwargs())

    assert module.result.get("msg") == "3 data validation errors found"


def test_validate_host_worker_wraps_exceptions_as_worker_failure(tmp_path: Path) -> None:
    """An exception raised inside the validation worker is wrapped as WorkerFailure with the thread prefix."""
    present_file = tmp_path / "host1.json"
    present_file.touch()  # exists() == True
    input_path = MagicMock()
    input_path.__truediv__.return_value = present_file

    file_handler = MagicMock()
    file_handler.read_file.side_effect = OSError("disk on fire")

    result = _validate_host_worker(
        hostname="host1",
        input_path=input_path,
        input_suffix="json",
        output_path=Path("/out"),
        schema_name="avd_design",
        configuration=None,
        file_handler=file_handler,
        fail_on_missing_input_files=True,
    )

    assert isinstance(result, WorkerFailure)
    assert result.hostname == "host1"
    assert result.error == "Unexpected error in validation worker thread: disk on fire"
