# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from dataclasses import dataclass
from functools import partial
from multiprocessing import get_context
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING, Any, Literal, cast

import yaml
from ansible.plugins.action import display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    ActionPluginVars,
    AVDFileHandler,
    AVDVaultHandler,
    build_result_message,
    get_tmp_paths,
    get_workers,
    parse_validation_result,
)
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AvdActionPlugin, AvdLoggingConfig

if TYPE_CHECKING:
    from pyavd_utils.validation import Configuration, ValidationResult, get_validated_data

    from pyavd._schema.models.constants import CV_DEPLOY_INPUT_KEYS, EOS_CLI_CONFIG_GEN_INPUT_KEYS, EOS_CLI_CONFIG_GEN_ROLE_KEYS
    from pyavd._schema.store import init_store
    from pyavd._utils.filtered_map_view import FilteredMapView

try:
    from pyavd_utils.validation import Configuration, ValidationResult, get_validated_data

    from pyavd._schema.models.constants import CV_DEPLOY_INPUT_KEYS, EOS_CLI_CONFIG_GEN_INPUT_KEYS, EOS_CLI_CONFIG_GEN_ROLE_KEYS
    from pyavd._schema.store import init_store
    from pyavd._utils.filtered_map_view import FilteredMapView

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

    # Workaround to make ansible-test sanity happy.
    ValidationResult = object
    CV_DEPLOY_INPUT_KEYS = set()
    EOS_CLI_CONFIG_GEN_INPUT_KEYS = set()
    EOS_CLI_CONFIG_GEN_ROLE_KEYS = set()


@dataclass(frozen=True, slots=True)
class WorkerFailure:
    """Result returned when a worker encounters an error."""

    hostname: str
    """Hostname that failed processing."""
    error: str
    """Error message describing the failure."""


@dataclass(frozen=True, slots=True)
class TemplateWorkerSuccess:
    """Result returned when a worker successfully completes the templating phase for a host."""

    hostname: str
    """Hostname that was processed."""
    output_file: str
    """Path to the output JSON file containing templated data."""


@dataclass(frozen=True, slots=True)
class ValidateWorkerSuccess:
    """Result returned when a worker successfully completes the validation phase for a host."""

    hostname: str
    """Hostname that was processed."""
    validation_result: ValidationResult  # pyright: ignore[reportInvalidTypeForm]
    """Validation result from pyavd-utils."""
    output_file: str | None
    """Path to the output JSON file, or None if validation failed."""


@dataclass(frozen=True, slots=True)
class ValidateWorkerSkipped:
    """Result returned when a worker skips the validation phase for a host."""

    hostname: str
    """Hostname that was processed."""
    reason: str
    """Reason why the validation was skipped."""


TemplateWorkerResult = TemplateWorkerSuccess | WorkerFailure
"""Result type from Phase 1 (templating hostvars and writing to file)."""

ValidateWorkerResult = ValidateWorkerSuccess | ValidateWorkerSkipped | WorkerFailure
"""Result type from Phase 2 (validating data and writing to file)."""


PLUGIN_NAME = "arista.avd.validate_inputs"
SCHEMA_NAME = Literal["avd_design", "eos_config", "cv_deploy"]
SCHEMA_KEY_MAP = {
    "eos_config": {"inventory_hostname", *EOS_CLI_CONFIG_GEN_ROLE_KEYS, *EOS_CLI_CONFIG_GEN_INPUT_KEYS},
    "cv_deploy": {"inventory_hostname", *CV_DEPLOY_INPUT_KEYS},
}

# TODO: Create a single pyavd_utils logger.
TARGET_LOGGERS = ("ansible_collections.arista.avd", "validation", "pyvalidation")

ARGUMENT_SPEC = {
    "tmp_dir": {"type": "str", "required": True},
    "device_list": {"type": "list", "elements": "str", "required": True},
    "batch_size": {"type": "int", "default": 10},
    "schema_name": {"type": "str", "default": "avd_design", "choices": ["avd_design", "eos_config", "cv_deploy"]},
    "input_dir": {"type": "str"},
    "input_suffix": {"type": "str", "default": "yml", "choices": ["yml", "yaml", "json"]},
    "read_from_input_dir": {"type": "bool", "default": False},
    "fail_on_missing_input_files": {"type": "bool", "default": True},
    "fail_on_validation_errors": {"type": "bool", "default": False},
    "validation_configuration": {"type": "dict", "options": {"warn_eos_config_keys": {"type": "bool"}}},
    "vault_id": {"type": "str"},
}

REQUIRED_IF = [
    ("read_from_input_dir", True, ("input_dir",)),
]


@dataclass(frozen=True, slots=True)
class ResolvedPluginArgs:
    """Plugin arguments."""

    tmp_dir: str
    device_list: list[str]
    batch_size: int
    schema_name: SCHEMA_NAME
    input_dir: str | None
    input_suffix: Literal["yml", "yaml", "json"]
    read_from_input_dir: bool
    fail_on_missing_input_files: bool
    fail_on_validation_errors: bool
    validation_configuration: Configuration | None
    vault_id: str | None


_HOSTVARS_MANAGER: ActionPluginVars | None = None


def set_worker_context(hostvars: ActionPluginVars) -> None:
    """
    Set the global worker context.

    Must be called by the parent process before forking.

    Args:
        hostvars: ActionPluginVars instance for the current action plugin context.
    """
    global _HOSTVARS_MANAGER  # noqa: PLW0603
    _HOSTVARS_MANAGER = hostvars


def get_worker_hostvars() -> ActionPluginVars:
    """
    Retrieve the global worker context.

    Returns:
        ActionPluginVars instance for the current action plugin context.
    """
    if _HOSTVARS_MANAGER is None:
        msg = "Worker context not initialized. 'set_worker_context' was not called before forking."
        raise RuntimeError(msg)
    return _HOSTVARS_MANAGER


class ActionModule(AvdActionPlugin):
    """Ansible Action Plugin for validating inputs against AVD schemas."""

    _logging_config = AvdLoggingConfig(target_loggers=TARGET_LOGGERS)

    def main(self, task_vars: dict[str, Any]) -> None:
        """Execute the validate_inputs action plugin."""
        if not HAS_PYAVD:
            msg = f"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library. Got import error."
            raise ImportError(msg)

        plugin_args = self._get_plugin_args()
        hosts_to_process = self._get_hosts_to_process(task_vars, plugin_args.schema_name, plugin_args.device_list)
        mp_workers, mt_workers = get_workers(len(hosts_to_process), task_vars["ansible_forks"])
        templated_path, validated_path = get_tmp_paths(tmp_dir=plugin_args.tmp_dir, clean=True)

        # Create Vault and file handlers.
        vault_handler = AVDVaultHandler(self._loader, vault_id=plugin_args.vault_id)
        file_handler = AVDFileHandler(vault_handler)

        # Check if Vault secrets are configured for encrypting temporary files.
        if vault_handler.has_vault_secrets:
            self.logger.info("Ansible Vault secrets are configured - temporary files will be encrypted")
        else:
            self.logger.info("Ansible Vault secrets are not configured - temporary files will not be encrypted")

        # Track worker failures globally for the task.
        self.crashed_hosts = set()

        self.logger.info(
            "Starting execution with %d multiprocessing workers and %d threads for %d hosts in batches of %d",
            mp_workers,
            mt_workers,
            len(hosts_to_process),
            plugin_args.batch_size,
        )

        # Phase 1: If read_from_input_dir is False, run the templating phase on hostvars.
        if not plugin_args.read_from_input_dir:
            self.logger.info("Reading inputs from hostvars")
            set_worker_context(ActionPluginVars(self))
            hosts_to_validate = self._run_templating_phase(
                hostnames=hosts_to_process,
                workers=mp_workers,
                batch_size=plugin_args.batch_size,
                output_path=templated_path,
                schema_name=plugin_args.schema_name,
                file_handler=file_handler,
            )
            validation_input_path = templated_path
            validation_input_suffix = "json"
        else:
            # At this point, input_dir is guaranteed to be set by the Ansible argument spec validator (via required_if).
            input_dir = cast("str", plugin_args.input_dir)
            self.logger.info("Reading inputs from '%s'", input_dir)
            hosts_to_validate = hosts_to_process
            validation_input_path = Path(input_dir)
            validation_input_suffix = plugin_args.input_suffix

        # Phase 2: Run the validation phase on the input_dir files or the templated_path files.
        if hosts_to_validate:
            self._run_validation_phase(
                hostnames=hosts_to_validate,
                workers=mt_workers,
                input_path=validation_input_path,
                input_suffix=validation_input_suffix,
                output_path=validated_path,
                schema_name=plugin_args.schema_name,
                fail_on_missing_input_files=plugin_args.fail_on_missing_input_files,
                fail_on_validation_errors=plugin_args.fail_on_validation_errors,
                configuration=plugin_args.validation_configuration,
                file_handler=file_handler,
            )

        if self.crashed_hosts:
            msg = f"Unexpected errors occurred while processing {len(self.crashed_hosts)} host(s): {', '.join(sorted(self.crashed_hosts))}."
            raise RuntimeError(msg)

    def _get_plugin_args(self) -> ResolvedPluginArgs:
        """
        Get and validate plugin arguments.

        Returns:
            ResolvedPluginArgs instance with the validated arguments.
        """
        _validation_result, validated_args = self.validate_argument_spec(
            argument_spec=ARGUMENT_SPEC,
            required_if=REQUIRED_IF,
        )

        # Converting to JSON and back to remove any AnsibeUnsafe types.
        validated_args = json.loads(json.dumps(validated_args))
        configuration = self._get_validation_configuration(validated_args)
        validated_args.update({"validation_configuration": configuration})

        return ResolvedPluginArgs(**validated_args)

    def _get_validation_configuration(self, validated_args: dict[Any, Any]) -> Configuration | None:
        """
        Build the Configuration object for validation based on plugin arguments.

        Args:
            validated_args: Validated plugin arguments containing validation_configuration dict or None.

        Returns:
            Configuration object from the plugin arguments or None when validation_configuration is None.
        """
        if "validation_configuration" not in validated_args or (validation_configuration := validated_args["validation_configuration"]) is None:
            return None

        configuration = Configuration()
        if (warn_eos_config_keys := validation_configuration.get("warn_eos_config_keys")) is not None:
            configuration.warn_eos_config_keys = warn_eos_config_keys

        return configuration

    def _get_hosts_to_process(self, task_vars: dict[str, Any], schema_name: SCHEMA_NAME, device_list: list[str]) -> list[str]:
        """
        Get the list of hostnames to process based on the schema.

        For eos_config and cv_deploy, returns hosts from the provided device_list.
        For avd_design, returns all hosts in the fabric group (needed to generate facts).

        AVD roles using this plugin use `ansible_play_hosts_all` as the device_list,
        but the cv_deploy role can override this.

        Args:
            task_vars: Ansible task variables.
            schema_name: The schema being validated.
            device_list: List of hostnames to process.

        Returns:
            List of hostnames to process.

        Raises:
            ValueError: If fabric_name is invalid or missing for avd_design.
        """
        # For eos_config and cv_deploy, the validation is per-host.
        # We only need to process the hosts provided in the device_list.
        if schema_name in {"eos_config", "cv_deploy"}:
            return device_list

        # For avd_design, we require fabric-wide facts.
        # We need to process the entire fabric group, not just the play hosts.
        groups = task_vars.get("groups", {})
        fabric_name = self._templar.template(task_vars.get("fabric_name", ""))
        fabric_hosts = groups.get(fabric_name, [])

        # Check if fabric_name is set and that all play hosts are part of the Ansible group set in "fabric_name".
        if fabric_name is None or not set(device_list).issubset(fabric_hosts):
            msg = (
                "Invalid/missing 'fabric_name' variable. "
                "All hosts in the play must have the same 'fabric_name' value "
                "which must point to an Ansible Group containing the hosts."
                f"play_hosts: {device_list}"
            )
            raise ValueError(msg)

        return fabric_hosts

    def _run_templating_phase(
        self,
        hostnames: list[str],
        workers: int,
        batch_size: int,
        output_path: Path,
        schema_name: SCHEMA_NAME,
        file_handler: AVDFileHandler,
    ) -> list[str]:
        """
        Run Phase 1: Templating.

        Resolves Ansible hostvars for each host and writes them as JSON files.
        Uses multiprocessing for parallel execution across hosts.

        Args:
            hostnames: List of hostnames to process.
            workers: Number of multiprocessing workers to use.
            batch_size: Number of hosts to process per child process.
            output_path: Directory path where templated JSON files will be written.
            schema_name: Schema name used for filtering hostvars.
            file_handler: AVDFileHandler, used to read and write files, handling encryption if needed.

        Returns:
            List of hostnames that were templated successfully.
        """
        self.logger.info("Templating hostvars...")
        start_time = perf_counter()
        successful_hosts = []

        # Partial to inject arguments into the worker.
        worker_func = partial(_template_host_worker, output_path=output_path, schema_name=schema_name, file_handler=file_handler)
        ctx = get_context("fork")

        with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
            results = pool.map(worker_func, hostnames, chunksize=batch_size)

            for result in results:
                if isinstance(result, WorkerFailure):
                    self.crashed_hosts.add(result.hostname)
                    self.logger.error("%s: %s", result.hostname, result.error)
                    continue

                self.logger.debug("Templated data for host %s saved to %s", result.hostname, result.output_file)
                successful_hosts.append(result.hostname)

        self.logger.info("Templating of hostvars completed in %.2fs", perf_counter() - start_time)
        return successful_hosts

    def _run_validation_phase(
        self,
        hostnames: list[str],
        workers: int,
        input_path: Path,
        input_suffix: str,
        output_path: Path,
        schema_name: SCHEMA_NAME,
        fail_on_missing_input_files: bool,
        fail_on_validation_errors: bool,
        configuration: Configuration | None,
        file_handler: AVDFileHandler,
    ) -> None:
        """
        Run Phase 2: Validation.

        Reads input files (JSON or YAML), validates against the schema using pyavd-utils,
        and writes validated JSON files. Uses multithreading for parallel execution.

        Updates self.result directly with validation statistics.

        Args:
            hostnames: List of hostnames to process.
            workers: Number of multithreading workers to use.
            input_path: Directory containing input files (templated or user-provided).
            input_suffix: File suffix for input files (json, yml, yaml).
            output_path: Directory where validated JSON files will be written.
            schema_name: Schema to validate against.
            fail_on_missing_input_files: Whether to fail the task if the input file is missing.
            fail_on_validation_errors: Whether to fail the task on validation errors.
            configuration: Configuration for validation or None.
            file_handler: AVDFileHandler, used to read and write files, handling encryption if needed.
        """
        self.logger.info("Validating inputs...")
        start_time = perf_counter()

        data_validation_errors = 0

        init_store()

        # Partial to inject arguments into the worker.
        worker_func = partial(
            _validate_host_worker,
            input_path=input_path,
            input_suffix=input_suffix,
            output_path=output_path,
            schema_name=schema_name,
            configuration=configuration,
            file_handler=file_handler,
            fail_on_missing_input_files=fail_on_missing_input_files,
        )

        with ThreadPoolExecutor(max_workers=workers) as pool:
            results = pool.map(worker_func, hostnames)

            for result in results:
                if isinstance(result, ValidateWorkerSkipped):
                    self.logger.info("Validation skipped for host %s: %s", result.hostname, result.reason)
                    continue

                if isinstance(result, WorkerFailure):
                    self.crashed_hosts.add(result.hostname)
                    self.logger.error("%s: %s", result.hostname, result.error)
                    continue

                host_errors = parse_validation_result(validation_result=result.validation_result, hostname=result.hostname, ansible_display=display)

                if host_errors:
                    data_validation_errors += host_errors
                    if fail_on_validation_errors:
                        self.result["failed"] = True

                elif not result.output_file:
                    self.crashed_hosts.add(result.hostname)
                    self.logger.error("Host %s passed validation but no output file was generated.", result.hostname)

                else:
                    self.logger.debug("Validated data for host %s saved to %s", result.hostname, result.output_file)

        msg = build_result_message(data_validation_errors)
        if msg:
            self.result["msg"] = msg

        self.logger.info("Validation of inputs completed in %.2fs", perf_counter() - start_time)


def _template_host_worker(hostname: str, output_path: Path, schema_name: SCHEMA_NAME, file_handler: AVDFileHandler) -> TemplateWorkerResult:
    """
    Phase 1 multiprocessing worker: Template hostvars for a host.

    Retrieves Ansible hostvars for the host, templates them, and writes
    the result as a JSON file to the output directory.

    Args:
        hostname: Hostname to process.
        output_path: Directory path where the templated JSON file will be written.
        schema_name: Schema name used for filtering hostvars.
        file_handler: AVDFileHandler, used to read and write files, handling encryption if needed.

    Returns:
        TemplateWorkerSuccess on success, WorkerFailure on error.
    """
    try:
        # Get the "Ansible Hostvars Manager"-like object which includes task, role, and play vars.
        hostvars_manager = get_worker_hostvars()

        # Take the HostVarsVars for this host to be templated on access and cached by Ansible's tooling.
        hostvars_wrapper = hostvars_manager[hostname]

        # Wrap the hostvars in a filter to only template variables used by the schema.
        # We cannot filter for avd_design while we support dynamic keys.
        if allowed_keys := SCHEMA_KEY_MAP.get(schema_name):
            hostvars_wrapper = FilteredMapView(hostvars_wrapper, allowed_keys)

        # The dict() here will force templating of all variables at once, potentially triggering issues for
        # missing variables in inline templates in Ansible 2.19.
        templated_hostvars = dict(hostvars_wrapper)

        data = json.dumps(templated_hostvars, skipkeys=True, default=lambda _: "<not serializable>", indent=4).encode("utf-8")
        output_file_path = output_path / f"{hostname}.json"
        file_handler.write_file(output_file_path, data)

        return TemplateWorkerSuccess(hostname=hostname, output_file=str(output_file_path))

    except Exception as e:
        return WorkerFailure(hostname=hostname, error=f"Unexpected error in templating worker process: {e}")


def _validate_host_worker(
    hostname: str,
    input_path: Path,
    input_suffix: str,
    output_path: Path,
    schema_name: SCHEMA_NAME,
    configuration: Configuration | None,
    file_handler: AVDFileHandler,
    fail_on_missing_input_files: bool,
) -> ValidateWorkerResult:
    """
    Phase 2 multithreading worker: Validate input data for a host.

    Reads the input file (JSON or YAML), validates it against the schema using
    pyavd-utils, and writes the validated data as JSON to the output directory.

    Args:
        hostname: Hostname to process.
        input_path: Directory containing the input file.
        input_suffix: File suffix for the input file (json, yml, yaml).
        output_path: Directory path where the validated JSON file will be written.
        schema_name: Schema to validate against.
        configuration: Configuration for validation or None.
        file_handler: AVDFileHandler, used to read and write files, handling encryption if needed.
        fail_on_missing_input_files: Whether to return a ValidateWorkerSkipped or WorkerFailure if the input file is missing.

    Returns:
        ValidateWorkerSuccess on success (with validation result), ValidateWorkerSkipped on skipped, WorkerFailure on error.
    """
    try:
        input_file_path = input_path / f"{hostname}.{input_suffix}"

        # If the input file is missing, return a failure or skipped depending on fail_on_missing_input_files.
        if not input_file_path.exists():
            if fail_on_missing_input_files:
                return WorkerFailure(hostname=hostname, error=f"Missing input data file: {input_file_path}")
            return ValidateWorkerSkipped(hostname=hostname, reason=f"No input file: {input_file_path}")

        # Load file content (decrypted if Vault encrypted).
        file_content = file_handler.read_file(input_file_path)

        if input_suffix in {"yml", "yaml"}:
            # YAML input: parse and convert to JSON string for validation.
            data = yaml.load(file_content, Loader=yaml.CSafeLoader)
            json_data = json.dumps(data)
        else:
            # JSON input: decode bytes to string.
            json_data = file_content.decode("utf-8")

        # Validation in Rust, releasing the GIL.
        validated_data_result = get_validated_data(data_as_json=json_data, schema_name=schema_name, configuration=configuration)
        validation_result, validated_data = validated_data_result.validation_result, validated_data_result.validated_data

        output_file = None
        if validated_data:
            output_file_path = output_path / f"{hostname}.json"
            file_handler.write_file(output_file_path, validated_data.encode("utf-8"))
            output_file = str(output_file_path)

        return ValidateWorkerSuccess(hostname=hostname, validation_result=validation_result, output_file=output_file)

    except Exception as e:
        return WorkerFailure(hostname=hostname, error=f"Unexpected error in validation worker thread: {e}")
