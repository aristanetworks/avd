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
from typing import TYPE_CHECKING, Any, Literal

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

    from pyavd._schema.store import init_store
    from pyavd._utils import get, strip_empties_from_dict

try:
    from pyavd_utils.validation import ValidationResult, get_validated_data

    from pyavd._schema.store import init_store
    from pyavd._utils import get, strip_empties_from_dict

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


@dataclass(frozen=True, slots=True)
class WorkerFailure:
    host: str
    error: str


@dataclass(frozen=True, slots=True)
class TemplateWorkerSuccess:
    host: str
    output_file: str


@dataclass(frozen=True, slots=True)
class ValidateWorkerSuccess:
    host: str
    validation_result: ValidationResult
    output_file: str | None
    """None if validation fails."""


TemplateWorkerResult = TemplateWorkerSuccess | WorkerFailure
"""Result from Phase 1 (templating, serializing, writing to file)."""
ValidateWorkerResult = ValidateWorkerSuccess | WorkerFailure
"""Result from Phase 2 (validating, writing to file)."""


PLUGIN_NAME = "arista.avd.validate_inputs"

# TODO: Create a single pyavd_utils logger.
TARGET_LOGGERS = ["ansible_collections.arista.avd", "validation", "pyvalidation"]

ARGUMENT_SPEC = {
    "batch_size": {"type": "int", "default": 10},
    "schema_name": {"type": "str", "default": "eos_designs", "choices": ["eos_designs", "eos_cli_config_gen"]},
    "template_inputs": {"type": "bool", "default": True},
    "input_dir": {"type": "str"},
    "input_suffix": {"type": "str", "default": "yml", "choices": ["yml", "yaml", "json"]},
    "fail_on_validation_errors": {"type": "bool", "default": True},
}

_HOSTVARS_MANAGER: ActionPluginVars | None = None


def set_worker_context(hostvars: ActionPluginVars) -> None:
    """
    Set the global worker context.

    Must be called by the parent process before forking.
    """
    global _HOSTVARS_MANAGER  # noqa: PLW0603
    _HOSTVARS_MANAGER = hostvars


def get_worker_hostvars() -> ActionPluginVars:
    """Retrieve hostvars in the worker process."""
    if _HOSTVARS_MANAGER is None:
        msg = "Worker context not initialized. 'set_worker_context' was not called before forking."
        raise RuntimeError(msg)
    return _HOSTVARS_MANAGER


class ActionModule(AvdActionPlugin):
    _logging_config = AvdLoggingConfig(target_loggers=TARGET_LOGGERS)

    def main(self, task_vars: dict[str, Any]) -> None:
        if not HAS_PYAVD:
            msg = f"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library. Got import error"
            raise ImportError(msg)

        # Get task arguments and validate them.
        _validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to JSON and back to remove any AnsibeUnsafe types.
        plugin_args = json_loads(json_dumps(validated_args))

        batch_size = get(plugin_args, "batch_size")
        schema_name = get(plugin_args, "schema_name")
        template_inputs = get(plugin_args, "template_inputs")
        input_dir = get(plugin_args, "input_dir")
        input_suffix = get(plugin_args, "input_suffix")
        fail_on_validation_errors = get(plugin_args, "fail_on_validation_errors")

        device_list = self._get_device_list(task_vars, schema_name)
        mp_workers, mt_workers = get_workers(len(device_list), task_vars.get("ansible_forks", 5))
        templated_path, validated_path = get_role_tmp_paths(schema_name)
        input_path = Path(input_dir) if input_dir else None

        set_worker_context(ActionPluginVars(self))

        self.logger.info(
            "Starting execution with %d multiprocessing workers and %d threads for %d hosts in batches of %d",
            mp_workers,
            mt_workers,
            len(device_list),
            batch_size,
        )

        # Track worker failures globally for the task.
        self.crashed_hosts = set()

        # Phase 1: Templating using multiprocessing.
        if template_inputs:
            hosts_to_validate = self._run_templating_phase(device_list, mp_workers, batch_size, input_path, input_suffix, templated_path)
        else:
            hosts_to_validate = device_list

        # Phase 2: Validation using multithreading.
        if hosts_to_validate:
            self._run_validation_phase(hosts_to_validate, mt_workers, templated_path, validated_path, schema_name, fail_on_validation_errors)

        if self.crashed_hosts:
            msg = f"Unexpected errors occurred while processing {len(self.crashed_hosts)} host(s): {', '.join(sorted(self.crashed_hosts))}. "
            raise RuntimeError(msg)

    def _get_device_list(self, task_vars: dict[str, Any], schema_name: Literal["eos_designs", "eos_cli_config_gen"]) -> list[str]:
        """Get the list of device to process."""
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        # For eos_cli_config_gen, the validation is per-device.
        # We only need to process the hosts currently targeted by the play.
        if schema_name == "eos_cli_config_gen":
            return ansible_play_hosts_all

        # For eos_designs, we require fabric-wide facts.
        # We need to process the entire fabric group, not just the play hosts.
        groups = task_vars.get("groups", {})
        fabric_name = self._templar.template(task_vars.get("fabric_name", ""))
        fabric_hosts = groups.get(fabric_name, [])

        # Check if fabric_name is set and that all play hosts are part Ansible group set in "fabric_name".
        if fabric_name is None or not set(ansible_play_hosts_all).issubset(fabric_hosts):
            msg = (
                "Invalid/missing 'fabric_name' variable. "
                "All hosts in the play must have the same 'fabric_name' value "
                "which must point to an Ansible Group containing the hosts."
                f"play_hosts: {ansible_play_hosts_all}"
            )
            raise ValueError(msg)

        return fabric_hosts

    def _run_templating_phase(self, hosts: list[str], workers: int, batch_size: int, input_dir: Path | None, input_suffix: str, output_dir: Path) -> list[str]:
        """
        Phase 1: Templating.

        Args:
            hosts: List of hosts to process.
            workers: The amount of multiprocessing workers to use.
            batch_size: The amount of hosts to template per child process.
            input_dir: Optional directory to load additional raw host variables to be templated.
            input_suffix: File suffix to use when loading host files from input_dir.
            output_dir: The directory path where templated JSON files will be written.

        Returns:
            List of hosts that were templated successfully.
        """
        start_time = perf_counter()
        successful_hosts = []

        # Partial to inject directories into the worker.
        worker_func = partial(_template_host_worker, input_dir=input_dir, input_suffix=input_suffix, output_dir=output_dir)
        ctx = get_context("fork")

        with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
            results = pool.map(worker_func, hosts, chunksize=batch_size)

            for result in results:
                if isinstance(result, WorkerFailure):
                    self.crashed_hosts.add(result.host)
                    self.logger.error("%s: %s", result.host, result.error)
                    continue

                self.logger.debug("Templated data for host %s saved to %s", result.host, result.output_file)
                successful_hosts.append(result.host)

        self.logger.info("Phase 1 (Templating) complete in %.2fs", perf_counter() - start_time)
        return successful_hosts

    def _run_validation_phase(
        self,
        hosts: list[str],
        workers: int,
        input_dir: Path,
        output_dir: Path,
        schema_name: Literal["eos_designs", "eos_cli_config_gen"],
        fail_on_validation_errors: bool,
    ) -> None:
        """
        Phase 2: Validation.

        Updates self.result directly with validation stats.

        Args:
            hosts: List of hosts to process.
            workers: The amount of multithreading workers to use.
            input_dir: The directory containing the templated JSON files (from Phase 1).
            output_dir: The directory where validated JSON files will be written.
            schema_name: Schema to use for validation.
            fail_on_validation_errors: Fail the task on schema validation errors.
        """
        start_time = perf_counter()

        data_validation_errors = 0

        init_store()

        # Partial to inject directories and schema name into the worker.
        worker_func = partial(_validate_host_worker, input_dir=input_dir, output_dir=output_dir, schema_name=schema_name)

        with ThreadPoolExecutor(max_workers=workers) as pool:
            results = pool.map(worker_func, hosts)

            for result in results:
                if isinstance(result, WorkerFailure):
                    self.crashed_hosts.add(result.host)
                    self.logger.error("%s: %s", result.host, result.error)
                    continue

                host_errors = parse_validation_result(validation_result=result.validation_result, hostname=result.host, ansible_display=display)

                if host_errors:
                    data_validation_errors += host_errors
                    if fail_on_validation_errors:
                        self.result["failed"] = True

                elif not result.output_file:
                    self.crashed_hosts.add(result.host)
                    self.logger.error("Host %s passed validation but no output file was generated.", result.host)

                else:
                    self.logger.debug("Validated data for host %s saved to %s", result.host, result.output_file)

        msg = build_result_message(data_validation_errors)
        if msg:
            self.result["msg"] = msg

        self.logger.info("Phase 2 (Validation) complete in %.2fs", perf_counter() - start_time)


def _template_host_worker(hostname: str, input_dir: Path | None, input_suffix: str, output_dir: Path) -> TemplateWorkerResult:
    """Phase 1 multiprocessing worker: Template, serialize, and dump a single host variables as JSON file to output_dir."""
    try:
        # Get the "Ansible Hostvars Manager"-like object which includes task, role, and play vars.
        hostvars_manager = get_worker_hostvars()

        overlay_data = {}
        if input_dir:
            input_file_path = input_dir / f"{hostname}.{input_suffix}"
            if input_file_path.exists():
                overlay_data = read_vars(input_file_path)

        # Take the HostVarsVars for this host. All variables will be templated on access and cached by Ansible's tooling.
        host_vars_wrapper = hostvars_manager.get_vars_with_overlay(hostname, overlay_data) if overlay_data else hostvars_manager[hostname]

        # The dict() here will force templating of all variables at once, potentially triggering issues for
        # missing variables in inline templates in Ansible 2.19.
        # TODO: Use a filtered_map to skip certain keys from being templated.
        host_templated_vars = dict(host_vars_wrapper)

        output_file_path = output_dir / f"{hostname}.json"
        with output_file_path.open(mode="w", encoding="utf-8") as f:
            json.dump(host_templated_vars, f, skipkeys=True, default=lambda _: "<not serializable>", indent=4)

        return TemplateWorkerSuccess(host=hostname, output_file=str(output_file_path))

    except Exception as e:
        return WorkerFailure(host=hostname, error=f"Unexpected error in templating worker process: {e}")


def _validate_host_worker(host: str, input_dir: Path, output_dir: Path, schema_name: Literal["eos_designs", "eos_cli_config_gen"]) -> ValidateWorkerResult:
    """Phase 2 multithreading worker: Read a single host JSON file from input_dir, validate in Rust, and write to output_dir."""
    try:
        input_file_path = input_dir / f"{host}.json"

        # If the input file is missing (unexpected), fail early.
        if not input_file_path.exists():
            return WorkerFailure(host=host, error=f"Missing templated data file: {input_file_path}")

        with input_file_path.open(mode="r", encoding="utf-8") as f:
            json_data = f.read()

        # Validation in Rust, releasing the GIL.
        validated_data_result = get_validated_data(data_as_json=json_data, schema_name=schema_name)
        validation_result, validated_data = validated_data_result.validation_result, validated_data_result.validated_data

        output_file = None
        if validated_data:
            output_file_path = output_dir / f"{host}.json"
            with output_file_path.open(mode="w", encoding="utf-8") as f:
                f.write(validated_data)
            output_file = str(output_file_path)

        return ValidateWorkerSuccess(host=host, validation_result=validation_result, output_file=output_file)

    except Exception as e:
        return WorkerFailure(host=host, error=f"Unexpected error in validation worker thread: {e}")


def read_vars(path: Path) -> dict[str, Any]:
    """TODO: Docstring."""
    with path.open(mode="r", encoding="utf-8") as f:
        if path.suffix in {".yml", ".yaml"}:
            return yaml.load(f, Loader=yaml.CSafeLoader)
        return json.load(f)
