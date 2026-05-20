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


@pytest.fixture
def action_module() -> Callable[..., ActionModule]:
    def _factory(task_args: dict | None = None) -> ActionModule:
        mock_task = MagicMock()
        mock_task.args = task_args if task_args is not None else {}
        mock_task.async_val = False
        mock_task.check_mode = False
        return ActionModule(
            task=mock_task,
            connection=MagicMock(),
            play_context=MagicMock(),
            loader=MagicMock(),
            templar=MagicMock(),
            shared_loader_obj=MagicMock(),
        )

    return _factory


@pytest.fixture
def reset_worker_context() -> Generator[None, None, None]:
    """Snapshot and restore the module-global ``_HOSTVARS_MANAGER``."""
    original = vi_module._HOSTVARS_MANAGER
    try:
        yield
    finally:
        vi_module._HOSTVARS_MANAGER = original


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
    module = action_module()
    plugin_args = MagicMock(
        tmp_dir="/tmp/x", read_from_input_dir=True, input_dir="/inputs", input_suffix="json", schema_name="avd_design", batch_size=10, device_list=None
    )

    vault_handler = MagicMock()
    vault_handler.has_vault_secrets = has_vault_secrets

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(module, "_get_plugin_args", return_value=plugin_args),
        patch.object(module, "_get_hosts_to_process", return_value=[]),
        patch.object(module, "_run_validation_phase"),
        patch(f"{MODULE_PATH}.get_workers", return_value=(1, 1)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/tmp/t"), Path("/tmp/v"))),
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
    module = action_module()
    plugin_args = MagicMock(
        tmp_dir="/tmp/x", read_from_input_dir=True, input_dir="/inputs", input_suffix="json", schema_name="avd_design", batch_size=7, device_list=None
    )

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(module, "_get_plugin_args", return_value=plugin_args),
        patch.object(module, "_get_hosts_to_process", return_value=["h1", "h2", "h3"]),
        patch.object(module, "_run_validation_phase"),
        patch(f"{MODULE_PATH}.get_workers", return_value=(4, 8)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/tmp/t"), Path("/tmp/v"))),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module.main(task_vars={"ansible_forks": 1, "ansible_play_hosts_all": []})

    assert "Starting execution with 4 multiprocessing workers and 8 threads for 3 hosts in batches of 7" in caplog.messages


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
    reset_worker_context: None,  # noqa: ARG001
    *,
    read_from_input_dir: bool,
    expected_message: str,
) -> None:
    """Verify the INFO log identifying where inputs are sourced from."""
    module = action_module()
    plugin_args = MagicMock(
        tmp_dir="/tmp/x",
        read_from_input_dir=read_from_input_dir,
        input_dir="/some/inputs",
        input_suffix="json",
        schema_name="avd_design",
        batch_size=10,
        device_list=None,
    )

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(module, "_get_plugin_args", return_value=plugin_args),
        patch.object(module, "_get_hosts_to_process", return_value=["h1"]),
        patch.object(module, "_run_templating_phase", return_value=["h1"]),
        patch.object(module, "_run_validation_phase"),
        patch(f"{MODULE_PATH}.get_workers", return_value=(1, 1)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/tmp/t"), Path("/tmp/v"))),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        patch(f"{MODULE_PATH}.ActionPluginVars"),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module.main(task_vars={"ansible_forks": 1, "ansible_play_hosts_all": []})

    assert expected_message in caplog.messages


def test_run_templating_phase_logs_start_and_completion_at_info(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Verify _run_templating_phase emits the 'Templating hostvars...' INFO log on start and a 'completed in ...s' INFO log on finish."""
    module = action_module()
    module.crashed_hosts = set()

    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([])

    with (
        patch(f"{MODULE_PATH}.ProcessPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.get_context"),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module._run_templating_phase(
            hostnames=[],
            workers=1,
            batch_size=1,
            output_path=Path("/tmp"),
            schema_name="avd_design",
            file_handler=MagicMock(),
        )

    info_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.INFO]
    assert "Templating hostvars..." in info_messages
    assert any(m.startswith("Templating of hostvars completed in ") and m.endswith("s") for m in info_messages)


def test_run_templating_phase_logs_worker_failure_at_error(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Worker failures during templating must log at ERROR with '<hostname>: <error>' format."""
    module = action_module()
    module.crashed_hosts = set()

    pool_results = [WorkerFailure(hostname="h-bad", error="boom"), MagicMock(hostname="h-good", output_file="/x/h-good.json")]
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter(pool_results)

    with (
        patch(f"{MODULE_PATH}.ProcessPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.get_context"),
        caplog.at_level(logging.DEBUG, logger=AVD_LOGGER_NAME),
    ):
        module._run_templating_phase(
            hostnames=["h-bad", "h-good"],
            workers=1,
            batch_size=1,
            output_path=Path("/tmp"),
            schema_name="avd_design",
            file_handler=MagicMock(),
        )

    assert "h-bad" in module.crashed_hosts
    error_records = [r for r in caplog.records if r.levelno == logging.ERROR]
    assert any("h-bad: boom" in r.getMessage() for r in error_records)


def test_run_templating_phase_logs_success_at_debug(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Successful templating must emit a DEBUG log with hostname and output file path."""
    module = action_module()
    module.crashed_hosts = set()

    success = MagicMock(spec_set=["hostname", "output_file"])
    success.hostname = "h1"
    success.output_file = "/tmp/h1.json"
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([success])

    with (
        patch(f"{MODULE_PATH}.ProcessPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.get_context"),
        caplog.at_level(logging.DEBUG, logger=AVD_LOGGER_NAME),
    ):
        module._run_templating_phase(
            hostnames=["h1"],
            workers=1,
            batch_size=1,
            output_path=Path("/tmp"),
            schema_name="avd_design",
            file_handler=MagicMock(),
        )

    debug_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.DEBUG]
    assert any("Templated data for host h1 saved to /tmp/h1.json" in m for m in debug_messages)


def _run_validation_phase_kwargs(file_handler: object | None = None) -> dict:
    """Return the default kwargs accepted by ActionModule._run_validation_phase."""
    return {
        "workers": 1,
        "input_path": Path("/in"),
        "input_suffix": "json",
        "output_path": Path("/out"),
        "schema_name": "avd_design",
        "fail_on_missing_input_files": True,
        "fail_on_validation_errors": False,
        "configuration": None,
        "file_handler": file_handler or MagicMock(),
    }


def test_run_validation_phase_logs_start_and_completion_at_info(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Verify _run_validation_phase emits 'Validating inputs...' on start and 'Validation of inputs completed in ...s' on finish."""
    module = action_module()
    module.crashed_hosts = set()

    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([])

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module._run_validation_phase(hostnames=[], **_run_validation_phase_kwargs())

    info_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.INFO]
    assert "Validating inputs..." in info_messages
    assert any(m.startswith("Validation of inputs completed in ") and m.endswith("s") for m in info_messages)


def test_run_validation_phase_logs_skipped_worker_at_info(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """A ValidateWorkerSkipped result must emit an INFO log 'Validation skipped for host <host>: <reason>'."""
    module = action_module()
    module.crashed_hosts = set()

    skipped = ValidateWorkerSkipped(hostname="h-skip", reason="No input file: /in/h-skip.json")
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([skipped])

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
        caplog.at_level(logging.INFO, logger=AVD_LOGGER_NAME),
    ):
        module._run_validation_phase(hostnames=["h-skip"], **_run_validation_phase_kwargs())

    info_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.INFO]
    assert "Validation skipped for host h-skip: No input file: /in/h-skip.json" in info_messages
    assert module.crashed_hosts == set()


def test_run_validation_phase_logs_worker_failure_at_error(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """A WorkerFailure result must emit an ERROR log '<host>: <error>' and add the host to crashed_hosts."""
    module = action_module()
    module.crashed_hosts = set()

    failure = WorkerFailure(hostname="h-bad", error="boom")
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([failure])

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
        caplog.at_level(logging.ERROR, logger=AVD_LOGGER_NAME),
    ):
        module._run_validation_phase(hostnames=["h-bad"], **_run_validation_phase_kwargs())

    error_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.ERROR]
    assert "h-bad: boom" in error_messages
    assert module.crashed_hosts == {"h-bad"}


def test_run_validation_phase_logs_missing_output_file_at_error(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """A ValidateWorkerSuccess with no output_file but no validation errors must log ERROR and crash the host."""
    module = action_module()
    module.crashed_hosts = set()

    success = ValidateWorkerSuccess(hostname="h-bug", validation_result=MagicMock(), output_file=None)
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([success])

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.parse_validation_result", return_value=0),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
        caplog.at_level(logging.ERROR, logger=AVD_LOGGER_NAME),
    ):
        module._run_validation_phase(hostnames=["h-bug"], **_run_validation_phase_kwargs())

    error_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.ERROR]
    assert "Host h-bug passed validation but no output file was generated." in error_messages
    assert module.crashed_hosts == {"h-bug"}


def test_run_validation_phase_logs_success_at_debug(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """A successful ValidateWorkerSuccess with an output_file must emit a DEBUG log."""
    module = action_module()
    module.crashed_hosts = set()

    success = ValidateWorkerSuccess(hostname="h1", validation_result=MagicMock(), output_file="/out/h1.json")
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([success])

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.parse_validation_result", return_value=0),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
        caplog.at_level(logging.DEBUG, logger=AVD_LOGGER_NAME),
    ):
        module._run_validation_phase(hostnames=["h1"], **_run_validation_phase_kwargs())

    debug_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.DEBUG]
    assert "Validated data for host h1 saved to /out/h1.json" in debug_messages
    assert module.crashed_hosts == set()


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


def test_get_worker_hostvars_raises_when_context_not_initialized(reset_worker_context: None) -> None:  # noqa: ARG001
    """get_worker_hostvars raises RuntimeError if set_worker_context was not called before forking."""
    vi_module._HOSTVARS_MANAGER = None
    with pytest.raises(RuntimeError, match=r"Worker context not initialized\. 'set_worker_context' was not called before forking\."):
        get_worker_hostvars()


def test_main_raises_import_error_when_pyavd_missing(action_module: Callable[..., ActionModule]) -> None:
    """When HAS_PYAVD is False, main raises ImportError naming the plugin."""
    module = action_module()
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        pytest.raises(ImportError, match=rf"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library\. Got import error\."),
    ):
        module.main(task_vars={})


def test_get_hosts_to_process_raises_for_invalid_fabric_name(action_module: Callable[..., ActionModule]) -> None:
    """_get_hosts_to_process raises ValueError when play hosts are not all in the fabric group."""
    module = action_module()
    module._templar = MagicMock()
    module._templar.template = lambda x: x

    expected = (
        r"Invalid/missing 'fabric_name' variable\. "
        r"All hosts in the play must have the same 'fabric_name' value "
        r"which must point to an Ansible Group containing the hosts\."
        r"play_hosts: \['host_outside_fabric'\]"
    )
    with pytest.raises(ValueError, match=expected):
        module._get_hosts_to_process(
            task_vars={
                "ansible_play_hosts_all": ["host_outside_fabric"],
                "groups": {"fabric_a": ["host_inside_fabric"]},
                "fabric_name": "fabric_a",
            },
            schema_name="avd_design",
            device_list=None,
        )


def test_main_raises_runtime_error_when_hosts_crashed(action_module: Callable[..., ActionModule]) -> None:
    """A non-empty crashed_hosts set at the end of main triggers a RuntimeError listing the hostnames."""
    module = action_module()
    plugin_args = MagicMock(
        tmp_dir="/tmp/x", read_from_input_dir=True, input_dir="/inputs", input_suffix="json", schema_name="avd_design", batch_size=10, device_list=None
    )

    def fake_validation(self_inner: ActionModule, **_kwargs: object) -> None:  # noqa: ARG001
        module.crashed_hosts.update({"h1", "h2"})

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch.object(module, "_get_plugin_args", return_value=plugin_args),
        patch.object(module, "_get_hosts_to_process", return_value=["h1", "h2"]),
        patch.object(module, "_run_validation_phase", side_effect=lambda **kwargs: fake_validation(module, **kwargs)),
        patch(f"{MODULE_PATH}.get_workers", return_value=(1, 1)),
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(Path("/tmp/t"), Path("/tmp/v"))),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        pytest.raises(RuntimeError, match=r"Unexpected errors occurred while processing 2 host\(s\): h1, h2\."),
    ):
        module.main(task_vars={"ansible_forks": 1, "ansible_play_hosts_all": []})


def test_template_host_worker_wraps_exceptions_as_worker_failure(reset_worker_context: None) -> None:  # noqa: ARG001
    """Any exception inside the templating worker is caught and returned as WorkerFailure."""
    with patch(f"{MODULE_PATH}.get_worker_hostvars", side_effect=RuntimeError("no context")):
        result = _template_host_worker("h1", output_path=Path("/x"), schema_name="avd_design", file_handler=MagicMock())

    assert isinstance(result, WorkerFailure)
    assert result.hostname == "h1"
    assert result.error == "Unexpected error in templating worker process: no context"


def test_validate_host_worker_returns_worker_failure_when_input_missing_and_fail_flag_true(tmp_path: Path) -> None:
    """fail_on_missing_input_files=True turns a missing input file into a WorkerFailure."""
    missing_file = tmp_path / "h1.json"  # exists() == False
    input_path = MagicMock()
    input_path.__truediv__.return_value = missing_file

    result = _validate_host_worker(
        hostname="h1",
        input_path=input_path,
        input_suffix="json",
        output_path=Path("/out"),
        schema_name="avd_design",
        configuration=None,
        file_handler=MagicMock(),
        fail_on_missing_input_files=True,
    )

    assert isinstance(result, WorkerFailure)
    assert result.hostname == "h1"
    assert result.error == f"Missing input data file: {missing_file}"


def test_validate_host_worker_returns_skipped_when_input_missing_and_fail_flag_false(tmp_path: Path) -> None:
    """fail_on_missing_input_files=False turns a missing input file into ValidateWorkerSkipped."""
    missing_file = tmp_path / "h1.json"  # exists() == False
    input_path = MagicMock()
    input_path.__truediv__.return_value = missing_file

    result = _validate_host_worker(
        hostname="h1",
        input_path=input_path,
        input_suffix="json",
        output_path=Path("/out"),
        schema_name="avd_design",
        configuration=None,
        file_handler=MagicMock(),
        fail_on_missing_input_files=False,
    )

    assert isinstance(result, ValidateWorkerSkipped)
    assert result.hostname == "h1"
    assert result.reason == f"No input file: {missing_file}"


def test_run_validation_phase_sets_failed_when_validation_errors_and_fail_flag_true(
    action_module: Callable[..., ActionModule],
) -> None:
    """If fail_on_validation_errors=True and a host has validation errors, self.result['failed'] is set to True."""
    module = action_module()
    module.crashed_hosts = set()

    success = ValidateWorkerSuccess(hostname="h1", validation_result=MagicMock(), output_file="/out/h1.json")
    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([success])

    kwargs = _run_validation_phase_kwargs()
    kwargs["fail_on_validation_errors"] = True

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.parse_validation_result", return_value=3),
        patch(f"{MODULE_PATH}.build_result_message", return_value=""),
    ):
        module._run_validation_phase(hostnames=["h1"], **kwargs)

    assert module.result.get("failed") is True
    assert module.crashed_hosts == set()


def test_run_validation_phase_sets_result_msg_when_build_result_message_returns_text(
    action_module: Callable[..., ActionModule],
) -> None:
    """A non-empty build_result_message return value populates self.result['msg']."""
    module = action_module()
    module.crashed_hosts = set()

    fake_pool_cm = MagicMock()
    fake_pool_cm.__enter__.return_value.map.return_value = iter([])

    with (
        patch(f"{MODULE_PATH}.ThreadPoolExecutor", return_value=fake_pool_cm),
        patch(f"{MODULE_PATH}.init_store"),
        patch(f"{MODULE_PATH}.build_result_message", return_value="3 data validation errors found"),
    ):
        module._run_validation_phase(hostnames=[], **_run_validation_phase_kwargs())

    assert module.result.get("msg") == "3 data validation errors found"


def test_validate_host_worker_wraps_exceptions_as_worker_failure(tmp_path: Path) -> None:
    """An exception raised inside the validation worker is wrapped as WorkerFailure with the thread prefix."""
    present_file = tmp_path / "h2.json"
    present_file.touch()  # exists() == True
    input_path = MagicMock()
    input_path.__truediv__.return_value = present_file

    file_handler = MagicMock()
    file_handler.read_file.side_effect = OSError("disk on fire")

    result = _validate_host_worker(
        hostname="h2",
        input_path=input_path,
        input_suffix="json",
        output_path=Path("/out"),
        schema_name="avd_design",
        configuration=None,
        file_handler=file_handler,
        fail_on_missing_input_files=True,
    )

    assert isinstance(result, WorkerFailure)
    assert result.hostname == "h2"
    assert result.error == "Unexpected error in validation worker thread: disk on fire"
