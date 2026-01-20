# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from dataclasses import dataclass
from functools import partial
from json import dumps as json_dumps
from json import loads as json_loads
from multiprocessing import get_context
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING, Any, Literal, NotRequired, TypedDict

import yaml
from ansible.plugins.action import display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    ActionPluginVars,
    build_result_message,
    get_role_tmp_paths,
    get_workers,
    parse_validation_result,
)
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AvdActionPlugin, AvdLoggingConfig

if TYPE_CHECKING:
    from pyavd_utils.validation import ValidationResult, get_validated_data

    from pyavd._schema.models.constants import EOS_CLI_CONFIG_GEN_INPUT_KEYS, EOS_CLI_CONFIG_GEN_ROLE_KEYS
    from pyavd._schema.store import init_store
    from pyavd._utils import strip_empties_from_dict
    from pyavd._utils.filtered_map_view import FilteredMapView

try:
    from pyavd_utils.validation import ValidationResult, get_validated_data

    from pyavd._schema.models.constants import EOS_CLI_CONFIG_GEN_INPUT_KEYS, EOS_CLI_CONFIG_GEN_ROLE_KEYS
    from pyavd._schema.store import init_store
    from pyavd._utils import strip_empties_from_dict
    from pyavd._utils.filtered_map_view import FilteredMapView

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

    # Workaround to make ansible-test sanity happy.
    ValidationResult = object


@dataclass(frozen=True, slots=True)
class WorkerFailure:
    """Result returned when a worker encounters an error."""

    device: str
    """Device name that failed processing."""
    error: str
    """Error message describing the failure."""


@dataclass(frozen=True, slots=True)
class TemplateWorkerSuccess:
    """Result returned when a worker successfully completes the templating phase for a device."""

    device: str
    """Device name that was processed."""
    output_file: str
    """Path to the output JSON file containing templated data."""


@dataclass(frozen=True, slots=True)
class ValidateWorkerSuccess:
    """Result returned when a worker successfully completes the validation phase for a device."""

    device: str
    """Device name that was processed."""
    validation_result: ValidationResult  # pyright: ignore[reportInvalidTypeForm]
    """Validation result from pyavd-utils."""
    output_file: str | None
    """Path to the output JSON file, or None if validation failed."""


TemplateWorkerResult = TemplateWorkerSuccess | WorkerFailure
"""Result type from Phase 1 (templating hostvars and writing to file)."""

ValidateWorkerResult = ValidateWorkerSuccess | WorkerFailure
"""Result type from Phase 2 (validating data and writing to file)."""


PLUGIN_NAME = "arista.avd.validate_inputs"
SCHEMA_NAME = Literal["eos_designs", "eos_cli_config_gen"]

# TODO: Create a single pyavd_utils logger.
TARGET_LOGGERS = ["ansible_collections.arista.avd", "validation", "pyvalidation"]

ARGUMENT_SPEC = {
    "batch_size": {"type": "int", "default": 10},
    "schema_name": {"type": "str", "default": "eos_designs", "choices": ["eos_designs", "eos_cli_config_gen"]},
    "input_dir": {"type": "str"},
    "input_suffix": {"type": "str", "default": "json", "choices": ["yml", "yaml", "json"]},
    "fail_on_validation_errors": {"type": "bool", "default": True},
}


class PluginArgs(TypedDict):
    """Plugin arguments."""

    batch_size: int
    schema_name: SCHEMA_NAME
    input_dir: NotRequired[str]
    input_suffix: Literal["yml", "yaml", "json"]
    fail_on_validation_errors: bool


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

        batch_size = plugin_args["batch_size"]
        schema_name = plugin_args["schema_name"]
        input_dir = plugin_args.get("input_dir")
        input_suffix = plugin_args["input_suffix"]
        fail_on_validation_errors = plugin_args["fail_on_validation_errors"]

        device_list = self._get_device_list(task_vars, schema_name)
        mp_workers, mt_workers = get_workers(len(device_list), task_vars.get("ansible_forks", 5))
        templated_path, validated_path = get_role_tmp_paths(schema_name)

        # Track worker failures globally for the task.
        self.crashed_devices = set()

        self.logger.info(
            "Starting execution with %d multiprocessing workers and %d threads for %d devices in batches of %d",
            mp_workers,
            mt_workers,
            len(device_list),
            batch_size,
        )

        # Phase 1: If no input_dir is provided, run the templating phase on hostvars.
        if input_dir is None:
            set_worker_context(ActionPluginVars(self))
            devices_to_validate = self._run_templating_phase(
                device_list=device_list,
                workers=mp_workers,
                batch_size=batch_size,
                output_path=templated_path,
                schema_name=schema_name,
            )
            devices_to_validate = device_list
        else:
            devices_to_validate = device_list

        # Phase 2: Run the validation phase on the input_dir or the templated files.
        if devices_to_validate:
            self._run_validation_phase(
                device_list=devices_to_validate,
                workers=mt_workers,
                input_path=Path(input_dir) if input_dir else templated_path,
                input_suffix=input_suffix if input_dir else "json",
                output_path=validated_path,
                schema_name=schema_name,
                fail_on_validation_errors=fail_on_validation_errors,
            )

        if self.crashed_devices:
            msg = f"Unexpected errors occurred while processing {len(self.crashed_devices)} device(s): {', '.join(sorted(self.crashed_devices))}. "
            raise RuntimeError(msg)

    def _get_plugin_args(self) -> PluginArgs:
        """
        Get and validate plugin arguments.

        Returns:
            Plugin arguments as a dictionary.
        """
        _validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to JSON and back to remove any AnsibeUnsafe types.
        return json_loads(json_dumps(validated_args))

    def _get_device_list(self, task_vars: dict[str, Any], schema_name: SCHEMA_NAME) -> list[str]:
        """
        Get the list of devices to process based on the schema.

        For eos_cli_config_gen, returns devices targeted by the current play.
        For eos_designs, returns all devices in the fabric group (fabric-wide processing).

        Args:
            task_vars: Ansible task variables.
            schema_name: The schema being validated.

        Returns:
            List of device names to process.

        Raises:
            ValueError: If fabric_name is invalid or missing for eos_designs.
        """
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        # For eos_cli_config_gen, the validation is per-device.
        # We only need to process the devices currently targeted by the play.
        if schema_name == "eos_cli_config_gen":
            return ansible_play_hosts_all

        # For eos_designs, we require fabric-wide facts.
        # We need to process the entire fabric group, not just the play devices.
        groups = task_vars.get("groups", {})
        fabric_name = self._templar.template(task_vars.get("fabric_name", ""))
        fabric_devices = groups.get(fabric_name, [])

        # Check if fabric_name is set and that all play devices are part of the Ansible group set in "fabric_name".
        if fabric_name is None or not set(ansible_play_hosts_all).issubset(fabric_devices):
            msg = (
                "Invalid/missing 'fabric_name' variable. "
                "All hosts in the play must have the same 'fabric_name' value "
                "which must point to an Ansible Group containing the hosts. "
                f"play_hosts: {ansible_play_hosts_all}"
            )
            raise ValueError(msg)

        return fabric_devices

    def _run_templating_phase(
        self,
        device_list: list[str],
        workers: int,
        batch_size: int,
        output_path: Path,
        schema_name: SCHEMA_NAME,
    ) -> list[str]:
        """
        Run Phase 1: Templating.

        Resolves Ansible hostvars for each device and writes them as JSON files.
        Uses multiprocessing for parallel execution across devices.

        Args:
            device_list: List of device names to process.
            workers: Number of multiprocessing workers to use.
            batch_size: Number of devices to process per child process.
            output_path: Directory path where templated JSON files will be written.
            schema_name: Schema name used for filtering hostvars.

        Returns:
            List of device names that were templated successfully.
        """
        start_time = perf_counter()
        successful_devices = []

        # Partial to inject directories into the worker.
        worker_func = partial(_template_device_worker, output_path=output_path, schema_name=schema_name)
        ctx = get_context("fork")

        with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
            results = pool.map(worker_func, device_list, chunksize=batch_size)

            for result in results:
                if isinstance(result, WorkerFailure):
                    self.crashed_devices.add(result.device)
                    self.logger.error("%s: %s", result.device, result.error)
                    continue

                self.logger.debug("Templated data for device %s saved to %s", result.device, result.output_file)
                successful_devices.append(result.device)

        self.logger.info("Phase 1 (Templating) complete in %.2fs", perf_counter() - start_time)
        return successful_devices

    def _run_validation_phase(
        self,
        device_list: list[str],
        workers: int,
        input_path: Path,
        input_suffix: str,
        output_path: Path,
        schema_name: Literal["eos_designs", "eos_cli_config_gen"],
        fail_on_validation_errors: bool,
    ) -> None:
        """
        Run Phase 2: Validation.

        Reads input files (JSON or YAML), validates against the schema using pyavd-utils,
        and writes validated JSON files. Uses multithreading for parallel execution.

        Updates self.result directly with validation statistics.

        Args:
            device_list: List of device names to process.
            workers: Number of multithreading workers to use.
            input_path: Directory containing input files (templated or user-provided).
            input_suffix: File suffix for input files (json, yml, yaml).
            output_path: Directory where validated JSON files will be written.
            schema_name: Schema to validate against.
            fail_on_validation_errors: Whether to fail the task on validation errors.
        """
        start_time = perf_counter()

        data_validation_errors = 0

        init_store()

        # Partial to inject directories and schema name into the worker.
        worker_func = partial(_validate_device_worker, input_path=input_path, input_suffix=input_suffix, output_path=output_path, schema_name=schema_name)

        with ThreadPoolExecutor(max_workers=workers) as pool:
            results = pool.map(worker_func, device_list)

            for result in results:
                if isinstance(result, WorkerFailure):
                    self.crashed_devices.add(result.device)
                    self.logger.error("%s: %s", result.device, result.error)
                    continue

                device_errors = parse_validation_result(validation_result=result.validation_result, hostname=result.device, ansible_display=display)

                if device_errors:
                    data_validation_errors += device_errors
                    if fail_on_validation_errors:
                        self.result["failed"] = True

                elif not result.output_file:
                    self.crashed_devices.add(result.device)
                    self.logger.error("Device %s passed validation but no output file was generated.", result.device)

                else:
                    self.logger.debug("Validated data for device %s saved to %s", result.device, result.output_file)

        msg = build_result_message(data_validation_errors)
        if msg:
            self.result["msg"] = msg

        self.logger.info("Phase 2 (Validation) complete in %.2fs", perf_counter() - start_time)


def _template_device_worker(device: str, output_path: Path, schema_name: SCHEMA_NAME) -> TemplateWorkerResult:
    """
    Phase 1 multiprocessing worker: Template hostvars for a device.

    Retrieves Ansible hostvars for the device, templates them, and writes
    the result as a JSON file to the output directory.

    Args:
        device: Device name (inventory hostname) to process.
        output_path: Directory path where the templated JSON file will be written.
        schema_name: Schema name used for filtering hostvars.

    Returns:
        TemplateWorkerSuccess on success, WorkerFailure on error.
    """
    try:
        # Get the "Ansible Hostvars Manager"-like object which includes task, role, and play vars.
        hostvars_manager = get_worker_hostvars()

        # Take the HostVarsVars for this device to be templated on access and cached by Ansible's tooling.
        hostvars_wrapper = hostvars_manager[device]

        # Wrap the hostvars in a filter to only template variables used by eos_cli_config_gen.
        # We cannot filter for eos_designs while we support dynamic keys.
        if schema_name == "eos_cli_config_gen":
            allowed_keys = {"inventory_hostname"}
            allowed_keys.update(EOS_CLI_CONFIG_GEN_ROLE_KEYS, EOS_CLI_CONFIG_GEN_INPUT_KEYS)
            hostvars_wrapper = FilteredMapView(hostvars_wrapper, allowed_keys)

        # The dict() here will force templating of all variables at once, potentially triggering issues for
        # missing variables in inline templates in Ansible 2.19.
        templated_hostvars = dict(hostvars_wrapper)

        output_file_path = output_path / f"{device}.json"
        with output_file_path.open(mode="w", encoding="utf-8") as f:
            json.dump(templated_hostvars, f, skipkeys=True, default=lambda _: "<not serializable>", indent=4)

        return TemplateWorkerSuccess(device=device, output_file=str(output_file_path))

    except Exception as e:
        return WorkerFailure(device=device, error=f"Unexpected error in templating worker process: {e}")


def _validate_device_worker(device: str, input_path: Path, input_suffix: str, output_path: Path, schema_name: SCHEMA_NAME) -> ValidateWorkerResult:
    """
    Phase 2 multithreading worker: Validate input data for a device.

    Reads the input file (JSON or YAML), validates it against the schema using
    pyavd-utils, and writes the validated data as JSON to the output directory.

    Args:
        device: Device name (inventory hostname) to process.
        input_path: Directory containing the input file.
        input_suffix: File suffix for the input file (json, yml, yaml).
        output_path: Directory path where the validated JSON file will be written.
        schema_name: Schema to validate against.

    Returns:
        ValidateWorkerSuccess on success (with validation result), WorkerFailure on error.
    """
    try:
        input_file_path = input_path / f"{device}.{input_suffix}"

        # If the input file is missing (unexpected), fail early.
        if not input_file_path.exists():
            return WorkerFailure(device=device, error=f"Missing input data file: {input_file_path}")

        # Load data based on file suffix.
        if input_suffix in {"yml", "yaml"}:
            # YAML input: load and convert to JSON for validation.
            with input_file_path.open(mode="r", encoding="utf-8") as f:
                data = yaml.load(f, Loader=yaml.CSafeLoader)
            json_data = json.dumps(data)
        else:
            # JSON input: read directly.
            with input_file_path.open(mode="r", encoding="utf-8") as f:
                json_data = f.read()

        # Validation in Rust, releasing the GIL.
        validated_data_result = get_validated_data(data_as_json=json_data, schema_name=schema_name)
        validation_result, validated_data = validated_data_result.validation_result, validated_data_result.validated_data

        output_file = None
        if validated_data:
            output_file_path = output_path / f"{device}.json"
            with output_file_path.open(mode="w", encoding="utf-8") as f:
                f.write(validated_data)
            output_file = str(output_file_path)

        return ValidateWorkerSuccess(device=device, validation_result=validation_result, output_file=output_file)

    except Exception as e:
        return WorkerFailure(device=device, error=f"Unexpected error in validation worker thread: {e}")
