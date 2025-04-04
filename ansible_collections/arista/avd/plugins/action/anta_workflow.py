# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from asyncio import run
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from logging.handlers import QueueHandler, QueueListener
from multiprocessing import Queue, current_process, get_context
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler
from ansible_collections.arista.avd.plugins.plugin_utils.utils.anta_logging_filter import AntaLoggingFilter

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping

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
            "logs_dir": {"type": "str"},
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
STRUCTURED_CONFIGS: dict[str, dict[str, Any]] | None = None
MINIMAL_STRUCTURED_CONFIGS: dict[str, MinimalStructuredConfig] | None = None
PLUGIN_ARGS: dict[str, Any] | None = None
ANSIBLE_VARS: dict[str, dict[str, Any]] | None = None
USER_CATALOG: AntaCatalog | None = None


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
        queue = Queue()
        setup_module_logging(queue)
        listener = setup_queue_listener(result, queue)

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

        # Extract only the needed hostvars from each device
        ANSIBLE_VARS = extract_hostvars(device_list, task_vars["hostvars"])
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
                    LOGGER.warning("no tests found in the user-defined ANTA catalogs, exiting")
                    return result

            # Load the structured configs and build the minimal structured configs if needed
            if generate_avd_catalogs:
                STRUCTURED_CONFIGS = load_structured_configs(deployed_devices, structured_config_dir, get(PLUGIN_ARGS, "avd_catalogs.structured_config_suffix"))
                MINIMAL_STRUCTURED_CONFIGS = get_minimal_structured_configs(STRUCTURED_CONFIGS)

            with ProcessPoolExecutor(max_workers=max((ansible_forks - 1), 1), mp_context=get_context("fork")) as executor:
                batch_size = get(PLUGIN_ARGS, "runner.batch_size")
                batches = [deployed_devices[i : i + batch_size] for i in range(0, len(deployed_devices), batch_size)]
                batch_results = executor.map(run_anta, batches)

            # Build the ANTA reports
            build_reports(batch_results, get(PLUGIN_ARGS, "report"))

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
    joined_devices = ", ".join(devices)
    process_name = current_process().name

    # Setup process logging and get warning tracker
    has_warnings_ref, anta_log_filename = setup_process_logging()

    # Build the objects required to run ANTA
    result_manager, inventory, catalog = build_anta_runner_objects(devices)
    tags = set(get(PLUGIN_ARGS, "runner.tags", default=[])) or None

    # Run ANTA
    LOGGER.info("running ANTA in process %s for devices: %s", process_name, joined_devices)
    run(anta_runner(result_manager, inventory, catalog, tags=tags, dry_run=get(PLUGIN_ARGS, "runner.dry_run")))

    # Check if warnings/errors occurred in ANTA and notify via main logger
    # ANTA errors are typically handled properly within ANTA by marking impacted
    # tests as errors or failures, so we don't need to fail the task here
    if has_warnings_ref[0]:
        base_message = f"ANTA warnings/errors detected that could impact test results for devices {joined_devices}. "
        if anta_log_filename:
            base_message += f"See '{anta_log_filename}' for details."
            LOGGER.warning(base_message)
        else:
            base_message += "No log directory was provided to save ANTA logs."
            LOGGER.warning(base_message)

    LOGGER.info("ANTA process %s completed for devices: %s", process_name, joined_devices)
    return result_manager


def build_reports(batch_results: Iterator[ResultManager], report_settings: dict) -> None:
    """Build the ANTA reports from the batch results."""
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
    result_manager.sort(sort_by=["name", "categories", "test", "description", "result"])

    # TODO: Consider using multiprocessing to generate reports in parallel
    if csv_output_path:
        LOGGER.info("generating CSV report at %s", csv_output_path)
        path = Path(csv_output_path)
        report_csv = ReportCsv()
        report_csv.generate(result_manager, path)

    if md_output_path:
        LOGGER.info("generating Markdown report at %s", md_output_path)
        path = Path(md_output_path)
        md_report = MDReportGenerator()
        md_report.generate(result_manager, path)

    if json_output_path:
        LOGGER.info("generating JSON report at %s", json_output_path)
        path = Path(json_output_path)
        with path.open("w", encoding="UTF-8") as file:
            file.write(result_manager.json)


def extract_hostvars(device_list: list[str], hostvars: Mapping) -> dict:
    """Extract only the required hostvars for each device."""
    device_vars = {}

    for device in device_list:
        if device not in hostvars:
            msg = f"Device '{device}' not found in Ansible inventory"
            raise ValueError(msg)

        host_hostvars = hostvars[device]

        # Since we can run ANTA without any structured configs, i.e., only using user-defined catalogs,
        # we honor the `is_deployed` flag in the hostvars to skip devices that are not deployed.
        if get(host_hostvars, "is_deployed", default=True) is False:
            LOGGER.info("skipping %s - device marked as not deployed", device)
            continue

        # Adding the Ansible connection variables following the HTTPAPI connection plugin settings
        device_vars[device] = {key: get(host_hostvars, key) for key in ANSIBLE_CONNECTION_VARS}

        # Same as above, we also honor the `anta_tags` variable if provided in the hostvars
        device_vars[device]["anta_tags"] = get(host_hostvars, "anta_tags")

    return device_vars


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


def get_device_catalog_filters(device: str, avd_catalogs_filters: list[dict]) -> dict[str, list[str]]:
    """
    Get the test filters for a device from the provided AVD catalogs filters.

    More specific filters (appearing later in the list) override earlier ones.
    For example, if a device matches both a group filter and an individual filter,
    the individual filter's tests will completely replace the group's run_tests or
    skip_tests if they are specified.
    """
    final_filters = {"run_tests": [], "skip_tests": []}

    for filter_config in avd_catalogs_filters:
        if device in get(filter_config, "device_list", default=[]):
            run_tests = get(filter_config, "run_tests")
            skip_tests = get(filter_config, "skip_tests")

            # Override previous filters if new ones are specified
            if run_tests is not None:
                if final_filters["run_tests"] is not None:
                    LOGGER.debug("<%s> run_tests overridden from %s to %s", device, final_filters["run_tests"], run_tests)
                final_filters["run_tests"] = list(set(run_tests))

            if skip_tests is not None:
                if final_filters["skip_tests"] is not None:
                    LOGGER.debug("<%s> skip_tests overridden from %s to %s", device, final_filters["skip_tests"], skip_tests)
                final_filters["skip_tests"] = list(set(skip_tests))

    return final_filters


def build_anta_device(device: str) -> AsyncEOSDevice:
    """Build the ANTA device object for a device using the provided Ansible inventory variables."""
    # Required settings to create the AsyncEOSDevice object
    required_settings = ["host", "username", "password"]

    device_vars = ANSIBLE_VARS[device]

    # TODO: Confirm this is working with Ansible Vault
    device_settings = {
        "name": device,
        "host": get(device_vars, "ansible_host", default=get(device_vars, "inventory_hostname")),
        "username": get(device_vars, "ansible_user"),
        "password": default(
            get(device_vars, "ansible_password"),
            get(device_vars, "ansible_httpapi_pass"),
            get(device_vars, "ansible_httpapi_password"),
        ),
        "enable": get(device_vars, "ansible_become", default=False),
        "enable_password": get(device_vars, "ansible_become_password"),
        "port": get(
            device_vars,
            "ansible_httpapi_port",
            default=(80 if get(device_vars, "ansible_httpapi_use_ssl", default=True) is False else 443),
        ),
        "timeout": get(PLUGIN_ARGS, "runner.timeout"),
        "tags": set(get(device_vars, "anta_tags", default=[])),
    }

    # Make sure we found all required connection settings. Other settings have defaults in the ANTA device object
    if any(value is None for key, value in device_settings.items() if key in required_settings):
        msg = (
            f"Device '{device}' is missing required connection settings. "
            f"Please make sure all required connection variables are defined in the Ansible inventory, "
            f"following the Ansible HTTPAPI connection plugin settings: {ANSIBLE_HTTPAPI_CONNECTION_DOC}"
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
            LOGGER.warning("skipped catalog file %s - unsupported format", path_obj)
            continue

        LOGGER.info("loading catalog from %s", path_obj)
        catalog = AntaCatalog.parse(path_obj, file_format)
        catalogs.append(catalog)

    if not catalogs:
        LOGGER.info("no custom ANTA catalogs found in directory: %s", catalogs_dir)

    return AntaCatalog.merge_catalogs(catalogs)


def load_structured_configs(device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict:
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


def setup_queue_listener(result: dict, queue: Queue) -> QueueListener:
    """
    Setup and start the queue listener for centralized log handling.

    1. Creates a handler to convert Python logs to Ansible display format
    2. Starts a queue listener thread to process logs from all processes, including the main process

    The queue listener processes logs from the central queue configured in `setup_module_logging`
    and displays them in the Ansible console.
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)

    listener = QueueListener(queue, python_to_ansible_handler)
    listener.start()
    return listener


def setup_module_logging(queue: Queue) -> None:
    """
    Setup logging configuration for the module to handle logs across multiple processes.

    1. Clears existing handlers for the `pyavd` logger and enables propagation to use root queue handler
    2. Sets up a queue-based logging system where all logs are sent to a central queue
    3. Filters all logs from ANTA and its dependencies from the queue handler, ANTA logs are written to per-process files
    4. Sets appropriate log levels based on Ansible verbosity:
       - verbosity >= 3: DEBUG level
       - verbosity > 0: INFO level
       - verbosity = 0: WARNING level
    """
    # Clear handlers of `pyavd` logger and set it to propagate to use the root queue handler
    pyavd_logger = logging.getLogger("pyavd")
    pyavd_logger.handlers.clear()
    pyavd_logger.propagate = True

    # Setup the logging configuration for the root logger
    root_logger = logging.getLogger()

    # Create a handler to send logs to the queue and add it to the root logger
    # This handler only receives non-ANTA logs
    queue_handler = QueueHandler(queue)
    queue_handler.addFilter(AntaLoggingFilter(exclude=True))
    root_logger.addHandler(queue_handler)

    # Set the level based on Ansible verbosity
    verbosity = display.verbosity
    if verbosity >= 3:
        root_logger.setLevel(logging.DEBUG)
    elif verbosity > 0:
        root_logger.setLevel(logging.INFO)
    else:
        root_logger.setLevel(logging.WARNING)


def setup_process_logging() -> tuple[list[bool], str | None]:
    """
    Initialize logging for the child processes.

    The child processes inherit the logging configuration from the parent process,
    configured by `setup_module_logging`.

    In each child process:
    1. Non-ANTA logs go to the queue for display in the Ansible console
    2. All ANTA logs go to a dedicated log file (if `logs_dir` is provided to the plugin)
    3. Warnings logs and above from ANTA libraries update a warning tracker to signal the main process
    """
    root_logger = logging.getLogger()
    process_name = current_process().name

    # Create a boolean tracker wrapped in a list to make it mutable
    # because we need a mutable reference that can be updated by the filter
    has_warnings_ref = [False]
    anta_log_filename = None

    # Get log directory settings
    anta_logs_dir = get(PLUGIN_ARGS, "runner.logs_dir")

    # If a logs directory is provided, set up ANTA file handler
    if anta_logs_dir:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

        # Setup ANTA log file that captures all ANTA logs at the current log level
        anta_log_filename = f"{anta_logs_dir}/anta_{timestamp}_{process_name}.log"
        anta_handler = logging.FileHandler(anta_log_filename, delay=True)
        anta_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        anta_handler.setFormatter(anta_formatter)

        # Use AntaLoggingFilter to capture only ANTA library logs and update the warning tracker when warnings occur
        anta_handler.addFilter(AntaLoggingFilter(exclude=False, has_warnings_ref=has_warnings_ref))
        root_logger.addHandler(anta_handler)

    # Return the warning tracker and filename to be used later
    return has_warnings_ref, anta_log_filename
