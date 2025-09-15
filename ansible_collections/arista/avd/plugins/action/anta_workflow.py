# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
import os
import sys
from asyncio import run
from concurrent.futures import ProcessPoolExecutor
from logging.handlers import QueueHandler, QueueListener
from multiprocessing import Queue, get_context
from pathlib import Path
from typing import TYPE_CHECKING, Any
from uuid import uuid4

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import ActionPluginVars, AntaWorkflowFilter, AntaWorkflowHandler

if TYPE_CHECKING:
    from collections.abc import Iterator

    from pyavd.api._anta import MinimalStructuredConfig

PLUGIN_NAME = "arista.avd.anta_workflow"

try:
    from pyavd._anta.lib import AntaCatalog, AntaInventory, AsyncEOSDevice, MDReportGenerator, ReportCsv, ResultManager, anta_runner
    from pyavd._utils import default, get, strip_empties_from_dict
    from pyavd.api._anta import AvdCatalogGenerationSettings, InputFactorySettings, get_minimal_structured_configs
    from pyavd.get_device_test_catalog import get_device_test_catalog

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ANSIBLE_HTTPAPI_CONNECTION_DOC = "https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/httpapi_connection.html"

ANSIBLE_CONNECTION_VARS = [
    "inventory_hostname",
    "ansible_host",
    "ansible_user",
    "ansible_password",
    "ansible_httpapi_pass",
    "ansible_httpapi_password",
    "ansible_become",
    "ansible_become_password",
    "ansible_httpapi_port",
    "ansible_httpapi_use_ssl",
]

ANTA_VARS = [
    "anta_user",
    "anta_password",
    "anta_enable",
    "anta_enable_password",
    "anta_port",
    "anta_use_ssl",
    "anta_tags",
]

ARGUMENT_SPEC = {
    "device_list": {"type": "list", "elements": "str", "required": True},
    "avd_catalogs": {
        "type": "dict",
        "options": {
            "enabled": {"type": "bool", "default": True},
            "output_dir": {"type": "str"},
            "structured_config_dir": {"type": "str"},
            "structured_config_suffix": {"type": "str", "choices": ["yml", "yaml", "json"], "default": "yml"},
            "allow_bgp_vrfs": {"type": "bool", "default": False},
            "filters": {
                "type": "list",
                "elements": "dict",
                "options": {
                    "device_list": {"type": "list", "elements": "str"},
                    "run_tests": {"type": "list", "elements": "str"},
                    "skip_tests": {"type": "list", "elements": "str"},
                },
            },
        },
    },
    "user_catalogs": {
        "type": "dict",
        "options": {
            "input_dir": {"type": "str"},
        },
    },
    "runner": {
        "type": "dict",
        "options": {
            "timeout": {"type": "float", "default": 30.0},
            "batch_size": {"type": "int", "default": 5},
            "tags": {"type": "list", "elements": "str"},
            "dry_run": {"type": "bool", "default": False},
        },
    },
    "report": {
        "type": "dict",
        "options": {
            "csv_output": {"type": "str"},
            "md_output": {"type": "str"},
            "json_output": {"type": "str"},
            "filters": {
                "type": "dict",
                "options": {
                    "hide_statuses": {
                        "type": "list",
                        "elements": "str",
                        "choices": ["success", "failure", "error", "skipped", "unset"],
                    },
                },
            },
        },
    },
}

# Global variables to share data between processes. Since the plugin is forked, these variables are inherited by child processes.
# TODO: Consider aggregating some of them into a SHARED_VARS dict or use multiprocessing.Manager()
STRUCTURED_CONFIGS: dict[str, dict[str, Any]] | None = None
MINIMAL_STRUCTURED_CONFIGS: dict[str, MinimalStructuredConfig] | None = None
PLUGIN_ARGS: dict[str, Any] | None = None
ANSIBLE_VARS: dict[str, dict[str, Any]] | None = None
USER_CATALOG: AntaCatalog | None = None
LOG_QUEUE: Queue = Queue()


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        global STRUCTURED_CONFIGS, MINIMAL_STRUCTURED_CONFIGS, PLUGIN_ARGS, ANSIBLE_VARS, USER_CATALOG  # noqa: PLW0603

        self._supports_check_mode = False

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PYAVD:
            msg = f"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        # Setup the module logging using a logging queue with a listener
        has_errors_ref = [False]
        listener = setup_queue_listener(LOG_QUEUE, has_errors_ref)
        setup_parent_process_logging(LOG_QUEUE, display.verbosity)

        ansible_forks = task_vars.get("ansible_forks", 5)

        # Get task arguments and validate them
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        PLUGIN_ARGS = json.loads(json.dumps(validated_args))

        device_list = get(PLUGIN_ARGS, "device_list")
        if not device_list:
            msg = "'device_list' cannot be empty"
            raise AnsibleActionFail(msg)

        # Get the required Ansible variables for each device
        action_plugin_vars = ActionPluginVars(self)
        ANSIBLE_VARS = get_ansible_vars(device_list, action_plugin_vars)
        deployed_devices = list(ANSIBLE_VARS.keys())

        generate_avd_catalogs = get(PLUGIN_ARGS, "avd_catalogs.enabled")
        structured_config_dir = get(PLUGIN_ARGS, "avd_catalogs.structured_config_dir")
        user_catalog_dir = get(PLUGIN_ARGS, "user_catalogs.input_dir")

        if generate_avd_catalogs is False and user_catalog_dir is None:
            msg = (
                "When 'avd_catalogs.enabled' is False, a directory with user-defined ANTA catalogs "
                "must be provided using the 'user_catalogs.input_dir' argument"
            )
            raise AnsibleActionFail(msg)
        if generate_avd_catalogs is True and structured_config_dir is None:
            msg = (
                "When 'avd_catalogs.enabled' is True, a directory with device structured configurations "
                "must be provided using the 'avd_catalogs.structured_config_dir' argument"
            )
            raise AnsibleActionFail(msg)

        try:
            # Load the user-defined ANTA catalogs if provided
            if user_catalog_dir is not None:
                USER_CATALOG = load_user_catalogs(user_catalog_dir)
                if not generate_avd_catalogs and not USER_CATALOG.tests:
                    LOGGER.warning("No tests found in the user-defined ANTA catalogs, exiting")
                    return result

            # Load the structured configs and build the minimal structured configs if needed
            if generate_avd_catalogs:
                STRUCTURED_CONFIGS = load_structured_configs(deployed_devices, structured_config_dir, get(PLUGIN_ARGS, "avd_catalogs.structured_config_suffix"))
                MINIMAL_STRUCTURED_CONFIGS = get_minimal_structured_configs(STRUCTURED_CONFIGS)

            with ProcessPoolExecutor(max_workers=max((ansible_forks - 1), 1), mp_context=get_context("fork")) as executor:
                batch_size = get(PLUGIN_ARGS, "runner.batch_size")
                batches = [deployed_devices[i : i + batch_size] for i in range(0, len(deployed_devices), batch_size)]
                batch_results = executor.map(run_anta, batches)

            # Build the ANTA reports and summary
            anta_tests_summary = build_reports(batch_results, report_settings=get(PLUGIN_ARGS, "report"))

            result = update_ansible_result(result, anta_tests_summary, has_errors_ref)

        except Exception as error:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error
        finally:
            # Stop the logging queue listener
            listener.stop()

        return result


def run_anta(devices: list[str]) -> ResultManager:
    """Run ANTA."""
    # Generate a unique ID for this child process run
    unique_id = f"anta-run-{str(uuid4())[:8]}"

    # Setup child process logging
    setup_child_process_logging(LOG_QUEUE, display.verbosity, unique_id)

    # Build the objects required to run ANTA
    result_manager, inventory, catalog = build_anta_runner_objects(devices)
    tags = set(get(PLUGIN_ARGS, "runner.tags", default=[])) or None
    dry_run = get(PLUGIN_ARGS, "runner.dry_run")
    run_mode = "dry-run" if dry_run else "run"

    # Run ANTA
    joined_devices = ", ".join(devices)
    LOGGER.info("Starting ANTA %s for devices: %s", run_mode, joined_devices)
    run(anta_runner(result_manager, inventory, catalog, tags=tags, dry_run=dry_run))

    LOGGER.info("ANTA %s completed for devices: %s", run_mode, joined_devices)
    return result_manager


def build_reports(batch_results: Iterator[ResultManager], report_settings: dict[str, Any]) -> dict[str, Any]:
    """Build the ANTA reports from the batch results and return a summary dictionary containing ANTA test statistics."""
    hide_statuses = get(report_settings, "filters.hide_statuses")
    csv_output_path = get(report_settings, "csv_output")
    md_output_path = get(report_settings, "md_output")
    json_output_path = get(report_settings, "json_output")

    # Merge all results
    result_manager = ResultManager()
    for manager in batch_results:
        for result in manager.results:
            result_manager.add(result)

    # Filter the results based on the hide_statuses if provided
    if hide_statuses:
        result_manager = result_manager.filter(hide=set(hide_statuses))

    # Sort the result manager
    result_manager.sort(sort_by=["name", "categories", "test", "description", "result", "custom_field"])

    # TODO: Consider using multiprocessing to generate reports in parallel
    if csv_output_path:
        LOGGER.info("Generating CSV report at %s", csv_output_path)
        path = Path(csv_output_path)
        report_csv = ReportCsv()
        report_csv.generate(result_manager, path)

    if md_output_path:
        LOGGER.info("Generating Markdown report at %s", md_output_path)
        path = Path(md_output_path)
        md_report = MDReportGenerator()
        md_report.generate(result_manager, path)

    if json_output_path:
        LOGGER.info("Generating JSON report at %s", json_output_path)
        path = Path(json_output_path)
        with path.open("w", encoding="UTF-8") as file:
            file.write(result_manager.json)

    # Build a summary with ANTA test stats
    tests_summary = {
        "total_tests": result_manager.get_total_results(),
        "tests_passed": result_manager.get_total_results({"success"}),
        "tests_failed": result_manager.get_total_results({"failure"}),
        "tests_error": result_manager.get_total_results({"error"}),
        "tests_skipped": result_manager.get_total_results({"skipped"}),
        "tests_unset": result_manager.get_total_results({"unset"}),
        "devices_with_test_failures": [],
        "devices_with_test_errors": [],
    }
    for device, stat in result_manager.device_stats.items():
        if stat.tests_failure_count:
            tests_summary["devices_with_test_failures"].append(device)
        if stat.tests_error_count:
            tests_summary["devices_with_test_errors"].append(device)

    return tests_summary


def update_ansible_result(result: dict[str, Any], anta_tests_summary: dict[str, Any], has_errors_ref: list[bool]) -> dict[str, Any]:
    """
    Update the Ansible result dictionary from aggregated ANTA test results and workflow log errors.

    Ansible task is set to `failed` if any of the following occurs:
        - No tests ran (outside of a dry run)
        - Errors were logged by the plugin, PyAVD or ANTA
        - Any test failed or errored

    Args:
        result: The Ansible result dictionary to update.
        anta_tests_summary: The dictionary created from `build_reports` containing aggregated test statistics.
        has_errors_ref: The boolean list passed to the AntaWorkflowHandler to keep track of error logs.

    Returns:
        dict: The updated Ansible result dictionary.
    """
    workflow_log_msg = ""
    test_result_msg = ""

    # Process workflow errors first
    failed_by_logs = has_errors_ref[0]
    if failed_by_logs:
        workflow_log_msg = "Errors detected during ANTA workflow execution."
        result["failed"] = True

    # Intermediate flags for test outcomes
    has_test_issues = anta_tests_summary["tests_failed"] > 0 or anta_tests_summary["tests_error"] > 0
    no_tests_run = anta_tests_summary["total_tests"] == 0

    # Fail the task if no tests were run
    if no_tests_run:
        test_result_msg = "No ANTA tests were run."
        result["failed"] = True
    # Fail the task if tests have issues
    elif has_test_issues:
        test_result_msg = "Task failed due to ANTA test failures/errors." if not failed_by_logs else "ANTA tests reported failures/errors."
        result["failed"] = True

    # Tests ran, no issues found, and no log errors
    elif not failed_by_logs:
        test_result_msg = "ANTA tests completed without reported failures/errors."

    # Combine messages
    final_msg = " ".join(filter(None, [workflow_log_msg, test_result_msg]))
    if final_msg:
        result["msg"] = final_msg

    # Populate final result dictionary directly from summary
    result["anta_tests_summary"] = anta_tests_summary

    return result


def get_ansible_vars(device_list: list[str], action_plugin_vars: ActionPluginVars) -> dict[str, dict[str, Any]]:
    """Get the required Ansible variables from the Action plugin variables for each device."""
    ansible_vars = {}

    for device in device_list:
        device_vars = action_plugin_vars[device]

        # Since we can run ANTA without any structured configs, i.e., only using user-defined catalogs,
        # we honor the `is_deployed` flag in the hostvars to skip devices that are not deployed.
        if get(device_vars, "is_deployed", default=True) is False:
            LOGGER.info("<%s> Device marked as not deployed - Skipping all tests", device)
            continue

        ansible_vars[device] = {key: get(device_vars, key) for key in ANSIBLE_CONNECTION_VARS + ANTA_VARS}

    return ansible_vars


def build_anta_runner_objects(devices: list[str]) -> tuple[ResultManager, AntaInventory, AntaCatalog]:
    """Build the ANTA objects required to run an ANTA batch."""
    # Create the ANTA objects
    result_manager = ResultManager()
    inventory = AntaInventory()
    catalogs = []

    if USER_CATALOG is not None:
        catalogs.append(USER_CATALOG)

    input_factory_settings = InputFactorySettings(allow_bgp_vrfs=get(PLUGIN_ARGS, "avd_catalogs.allow_bgp_vrfs"))
    output_dir = get(PLUGIN_ARGS, "avd_catalogs.output_dir")
    avd_catalogs_filters = get(PLUGIN_ARGS, "avd_catalogs.filters", default=[])

    for device in devices:
        anta_device = build_anta_device(device)
        inventory.add_device(anta_device)
        # We generate the device's AVD catalog only if structured configs are loaded
        if STRUCTURED_CONFIGS is not None and MINIMAL_STRUCTURED_CONFIGS is not None:
            settings = AvdCatalogGenerationSettings(
                input_factory_settings=input_factory_settings,
                output_dir=output_dir,
                **get_device_catalog_filters(device, avd_catalogs_filters),
            )
            catalog = get_device_test_catalog(
                hostname=device,
                structured_config=STRUCTURED_CONFIGS[device],
                minimal_structured_configs=MINIMAL_STRUCTURED_CONFIGS,
                settings=settings,
            )
            catalogs.append(catalog)

    catalog = AntaCatalog.merge_catalogs(catalogs)

    return result_manager, inventory, catalog


def get_device_catalog_filters(device: str, avd_catalogs_filters: list[dict[str, list[str]]]) -> dict[str, list[str]]:
    """
    Get the test filters for a device from the provided AVD catalogs filters.

    A filter is applied to the device unless `device_list` is provided in the filter and the device is *not* part of it.

    Filters are not cumulative for the device. If the device matches multiple filters, the last filter (appearing later in the list) wins.

    Args:
        device: The device name to get the filters for.
        avd_catalogs_filters: The AVD catalogs filters from the plugin argument `avd_catalogs.filters`.

    Returns:
        dict: A dictionary with the list of tests to run and/or skip: `{"run_tests: [<test1>, ...], "skip_tests" [<test2>, ...]}`.
    """
    final_filters = {"run_tests": [], "skip_tests": []}

    for filter_config in avd_catalogs_filters:
        # Skip this filter for the device if it's not part of device_list if provided
        device_list = filter_config.get("device_list")
        if device_list is not None and device not in device_list:
            continue

        run_tests = filter_config.get("run_tests")
        skip_tests = filter_config.get("skip_tests")

        # Override previous filters if new ones are specified
        if run_tests is not None:
            if final_filters["run_tests"]:
                LOGGER.debug("<%s> run_tests overridden from %s to %s", device, final_filters["run_tests"], run_tests)
            final_filters["run_tests"] = list(set(run_tests))

        if skip_tests is not None:
            if final_filters["skip_tests"]:
                LOGGER.debug("<%s> skip_tests overridden from %s to %s", device, final_filters["skip_tests"], skip_tests)
            final_filters["skip_tests"] = list(set(skip_tests))

    return final_filters


def build_anta_device(device: str) -> AsyncEOSDevice:
    """Build the ANTA device object for a device using the provided Ansible inventory variables."""
    # Required settings to create the AsyncEOSDevice object
    required_settings = ["host", "username", "password"]

    device_vars = ANSIBLE_VARS[device]
    username = default(get(device_vars, "anta_user"), get(device_vars, "ansible_user"))
    password = default(
        get(device_vars, "anta_password"),
        get(device_vars, "ansible_password"),
        get(device_vars, "ansible_httpapi_pass"),
        get(device_vars, "ansible_httpapi_password"),
    )
    port = default(get(device_vars, "anta_port"), get(device_vars, "ansible_httpapi_port"))
    enable_mode = default(get(device_vars, "anta_enable"), get(device_vars, "ansible_become", default=False))
    enable_password = default(get(device_vars, "anta_enable_password"), get(device_vars, "ansible_become_password"))
    proto = "https" if default(get(device_vars, "anta_use_ssl"), get(device_vars, "ansible_httpapi_use_ssl", default=True)) else "http"

    device_settings = {
        "name": device,
        "host": get(device_vars, "ansible_host", default=get(device_vars, "inventory_hostname")),
        "username": username,
        "password": password,
        "enable": enable_mode,
        "enable_password": enable_password,
        "port": port,
        "proto": proto,
        "timeout": get(PLUGIN_ARGS, "runner.timeout"),
        "tags": set(get(device_vars, "anta_tags", default=[])),
    }

    # Make sure we found all required connection settings. Other settings have defaults in the ANTA device object
    if any(value is None for key, value in device_settings.items() if key in required_settings):
        msg = (
            f"Device '{device}' is missing required connection settings. "
            f"Please make sure all required connection variables are defined in the Ansible inventory, "
            "as specified in the role documentation."
        )
        raise ValueError(msg)

    return AsyncEOSDevice(**device_settings)


def load_user_catalogs(catalogs_dir: str) -> AntaCatalog:
    """Load user-defined ANTA catalogs from the provided directory. Supported file formats are YAML and JSON."""
    supported_formats = {".yml": "yaml", ".yaml": "yaml", ".json": "json"}
    catalogs = []

    for path_obj in Path(catalogs_dir).iterdir():
        # Skip directories and non-files
        if not path_obj.is_file():
            continue

        file_format = supported_formats.get(path_obj.suffix.lower())
        if not file_format:
            LOGGER.warning("Skipped user-defined ANTA catalog file %s - unsupported format", path_obj)
            continue

        LOGGER.info("Loading user-defined ANTA catalog from %s", path_obj)
        catalog = AntaCatalog.parse(path_obj, file_format)
        catalogs.append(catalog)

    if not catalogs:
        LOGGER.info("No user-defined ANTA catalogs found in directory: %s", catalogs_dir)

    return AntaCatalog.merge_catalogs(catalogs)


def load_structured_configs(device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict[str, Any]:
    """Load the structured configurations for the devices in the provided list from the given directory."""
    return {device: load_one_structured_config(device, structured_config_dir, structured_config_suffix) for device in device_list}


def load_one_structured_config(device: str, structured_config_dir: str, structured_config_suffix: str) -> dict[str, Any]:
    """Load the structured configuration for a device from the provided directory."""
    path = Path(structured_config_dir) / f"{device}.{structured_config_suffix}"
    if not path.exists():
        msg = f"Structured configuration file for device '{device}' not found: {path}"
        raise FileNotFoundError(msg)

    with path.open(encoding="UTF-8") as stream:
        if structured_config_suffix in {"yml", "yaml"}:
            return yaml.load(stream, Loader=yaml.CSafeLoader)
        return json.load(stream)


def setup_queue_listener(log_queue: Queue, has_errors_ref: list[bool]) -> QueueListener:
    """
    Set up and start the queue listener for centralized log handling.

    The listener handler formats logs with a unique ID for context, displays them in the
    Ansible console respecting verbosity, and track log errors via the has_errors_ref list.

    Args:
      log_queue: Shared queue used by the QueueListener to receive logs from everyone.
      has_errors_ref: Mutable boolean list to track error logs and above.

    Returns:
      QueueListener: The started QueueListener instance.
    """
    log_handler = AntaWorkflowHandler(has_errors_ref)

    listener = QueueListener(log_queue, log_handler)
    listener.start()
    return listener


def setup_parent_process_logging(log_queue: Queue, verbosity: int) -> None:
    """
    Initialize logging for the parent Ansible plugin process.

    Clear existing handlers from the `pyavd` logger configured by the `verify_requirements`
    plugin and enable propagation to use the shared `log_queue`.

    Args:
      log_queue: Shared queue for sending logs to the central listener thread.
      verbosity: Ansible verbosity level used to set the appropriate log level.
    """
    # Clear handlers of `pyavd` logger and set it to propagate to use the root queue handler
    pyavd_logger = logging.getLogger("pyavd")
    pyavd_logger.handlers.clear()
    pyavd_logger.propagate = True

    # Logs from the plugin itself will be prepended with 'anta-workflow'
    setup_root_logger(unique_id="anta-workflow", log_queue=log_queue, verbosity=verbosity)

    # Configure ANTA debug mode based on Ansible verbosity
    setup_anta_debug_mode(verbosity=verbosity)


def setup_child_process_logging(log_queue: Queue, verbosity: int, unique_id: str) -> None:
    """
    Initialize logging for child processes.

    Since the plugin is forked, root handlers inherited from the parent
    process must be cleared to avoid conflicts with Ansible handlers.

    Args:
      log_queue: Shared queue used to send logs from this child process to the listener thread.
      verbosity: Ansible verbosity level used to set the appropriate log level.
      unique_id: Identifier for the current run that will be prepended to all logs.
    """
    # Clear root handlers inherited from the parent process
    root_logger = logging.getLogger()
    root_logger.handlers.clear()

    setup_root_logger(unique_id=unique_id, log_queue=log_queue, verbosity=verbosity)


def setup_root_logger(unique_id: str, log_queue: Queue, verbosity: int) -> None:
    """
    Set up the root logger for parent (plugin) and child processes.

    Args:
      unique_id: Identifier for the current context that will be prepended to all logs.
      log_queue: Shared queue used to send logs from all processes to the listener thread.
      verbosity: Ansible verbosity level used to set the appropriate log level to different loggers.
    """
    root_logger = logging.getLogger()

    # ANTA low-level libraries are always at WARNING level except at full verbosity `-vvvvv`
    low_level_libraries = ("asyncio", "httpcore", "httpx")
    for logger_name in low_level_libraries:
        logging.getLogger(logger_name).setLevel(logging.WARNING)

    if verbosity >= 5:
        # All loggers (pyavd, anta, ansible_collections.arista.avd) including low-level libraries will be at DEBUG
        root_logger.setLevel(logging.DEBUG)
        for logger_name in low_level_libraries:
            logging.getLogger(logger_name).setLevel(logging.DEBUG)
    elif verbosity == 4:
        # All loggers except low-level libraries (WARNING) will be at DEBUG
        root_logger.setLevel(logging.DEBUG)
    elif verbosity == 3:
        # All loggers except anta (INFO) and low-level libraries (WARNING) will be at DEBUG
        root_logger.setLevel(logging.DEBUG)
        logging.getLogger("anta").setLevel(logging.INFO)
    elif verbosity in (1, 2):
        # All loggers except low-level libraries (WARNING) will be at INFO
        root_logger.setLevel(logging.INFO)
    else:
        # All loggers will be at WARNING
        root_logger.setLevel(logging.WARNING)

    # Create and configure the QueueHandler to send all logs to the listener thread
    queue_handler = QueueHandler(log_queue)
    queue_handler.set_name(f"QueueHandler_{unique_id}")

    # Create the filter that prepends the unique_id
    log_filter = AntaWorkflowFilter(unique_id=unique_id)
    queue_handler.addFilter(log_filter)

    # Add the configured QueueHandler to the root logger
    root_logger.addHandler(queue_handler)


def setup_anta_debug_mode(verbosity: int) -> None:
    """
    Aligns ANTA debug mode with Ansible verbosity level.

    Overrides `ANTA_DEBUG` to False if it's True and Ansible verbosity < 3 (-vvv).
    Also clears `PYTHONASYNCIODEBUG` if set by ANTA in this scenario.
    ANTA tracebacks require verbosity >= 3, following Ansible behavior.

    Args:
      verbosity: Ansible verbosity level.
    """
    anta_logger_module = sys.modules.get("anta.logger")

    # This should never happen because of the HAS_PYAVD check at the beginning of the plugin
    if anta_logger_module is None or not hasattr(anta_logger_module, "__DEBUG__"):
        msg = (
            "Cannot find the '__DEBUG__' attribute of the 'anta.logger' module, even though PyAVD dependencies were expected to be loaded. "
            "This indicates a severe issue with the Python environment or ANTA installation."
        )
        raise AnsibleActionFail(msg)

    current_anta_debug_flag = anta_logger_module.__DEBUG__
    LOGGER.debug("Initial ANTA_DEBUG value: %s", current_anta_debug_flag)

    if current_anta_debug_flag is True and verbosity < 3:
        LOGGER.debug("ANTA_DEBUG is True and Ansible verbosity (%d) < 3. Overriding ANTA_DEBUG to False for this plugin run", verbosity)
        anta_logger_module.__DEBUG__ = False

        if os.environ.get("PYTHONASYNCIODEBUG") == "1":
            LOGGER.debug(
                "ANTA_DEBUG was True (causing PYTHONASYNCIODEBUG=1). "
                "Since ANTA_DEBUG is now overridden to False by the plugin, deleting PYTHONASYNCIODEBUG environment variable"
            )
            del os.environ["PYTHONASYNCIODEBUG"]
    elif current_anta_debug_flag is True and verbosity >= 3:
        LOGGER.debug("ANTA_DEBUG is True and Ansible verbosity (%d) >= 3. ANTA debug mode will remain active as per the environment variable", verbosity)
    else:
        LOGGER.debug("ANTA_DEBUG is False. Plugin will not change ANTA debug settings")
