# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# /// script
# dependencies = [
#   "pyavd[ansible] @ file:///${PROJECT_ROOT}/python-avd",
#   "gitpython>=3.1.57",
# ]
# # [tool.uv]
# # reinstall-package = ["pyavd"]
# ///

from __future__ import annotations

import argparse
import dataclasses
import json
import os
import pathlib
import pickle
import shutil
import sys
import time
import traceback
import typing
import weakref
from concurrent.futures import Executor, ProcessPoolExecutor, ThreadPoolExecutor
from contextlib import suppress
from functools import cached_property, lru_cache
from itertools import repeat
from multiprocessing import get_context, shared_memory

import git
import pyavd_utils
import yaml
from ansible.cli import CLI
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.loader import init_plugin_loader
from ansible.release import __version__ as ansible_version
from ansible.template import Templar
from ansible.vars.hostvars import HostVars
from ansible.vars.manager import VariableManager
from yaml import CLoader as YamlLoader

import pyavd
from pyavd import validate_structured_config
from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
from pyavd._eos_designs.structured_config import get_structured_config
from pyavd._schema.avdschema import AvdSchema
from pyavd._schema.store import init_store as pyavd_init_store
from pyavd._utils import strip_empties_from_dict
from pyavd._utils.avd_templar import AVDTemplar
from pyavd.api.pool_manager import PoolManager
from pyavd.api.schemas import AVDDesign

if typing.TYPE_CHECKING:
    from collections.abc import Generator

    from ansible.inventory.host import Host

ANSIBLE_ABOVE_2_19 = ansible_version.startswith(("2.2", "2.19"))
DEFAULT_FABRIC = "__UNSET_FABRIC_NAME__"


class PathNotDirError(ValueError):
    field: str

    def __init__(self, field: str, *args: typing.Any) -> None:
        self.field = field
        super().__init__(field, *args)

    def __str__(self) -> str:
        return f"The {self.field} path is invalid. The path must point to a directory."


@dataclasses.dataclass(frozen=True)
class Documentation:
    device_docs: bool = True
    fabric_documentation: bool = True
    include_connected_endpoints: bool = False
    topology_csv: bool = False
    p2p_links_csv: bool = False
    toc: bool = True


@dataclasses.dataclass
class Configuration:
    inventory_dir: pathlib.Path
    output_dir: pathlib.Path
    docs_dir: pathlib.Path
    inventory_file: str
    no_clean: bool
    error_dir: pathlib.Path
    fabric_name: str
    """Fabric name. Will be overwritten for each fabric."""
    structured_config_suffix: typing.Literal["yml", "yaml", "json"] = "yml"
    digital_twin: bool = False
    documentation: Documentation = dataclasses.field(default_factory=Documentation)
    custom_templates: bool = False
    device_configs: bool = True
    dump_tracebacks: bool = False

    def __postinit__(self) -> None:
        if not self.inventory_dir.is_dir():
            msg = "inventory_dir"
            raise PathNotDirError(msg)
        if not self.output_dir.is_dir():
            msg_0 = "--output-dir"
            raise PathNotDirError(msg_0)
        if not self.docs_dir.is_dir():
            msg_1 = "--docs-dir"
            raise PathNotDirError(msg_1)

    def get_cleanup_dirs(self) -> set[pathlib.Path]:
        """Return set of directories to clean up."""
        return {self.output_dir.joinpath("configs"), self.output_dir.joinpath("structured_configs"), self.docs_dir, self.error_dir}


### Ansible wrappers


class AnsibleInventory:  # pylint: disable=too-few-public-methods
    """Ansible Inventory wrapper."""

    def __init__(self, inventory_path: pathlib.Path, data_loader: DataLoader | None = None, vault_ids: list | None = None) -> None:
        """Initialize Ansible Inventory Manager."""
        self.inventory_path = inventory_path
        self.data_loader = data_loader if data_loader is not None else DataLoader()
        if vault_ids:
            CLI.setup_vault_secrets(self.data_loader, vault_ids=vault_ids)

        self.inventory_manager = InventoryManager(loader=self.data_loader, sources=[self.inventory_path.as_posix()], parse=True)
        self.variable_manager = VariableManager(loader=self.data_loader, inventory=self.inventory_manager)
        self.hostvars = HostVars(
            inventory=self.inventory_manager,
            variable_manager=self.variable_manager,
            loader=self.data_loader,
        )

    def get_hosts(self, pattern: str, order: str = "sorted") -> list[Host]:
        """Takes a pattern or list of patterns and returns a list of matching inventory host."""
        return self.inventory_manager.get_hosts(pattern=pattern, order=order)

    def get_vars(self, host_name: str) -> dict:
        """Get host vars."""
        return dict(self.hostvars[host_name])


class AvdBuildContext:
    configuration: Configuration
    executor: Executor
    """
    ProcessPoolExecutor for CPU-intensive device builds.
    """
    inventory: AnsibleInventory
    validation_max_workers: int | None
    """Max workers for ThreadPoolExecutor used in validation."""

    def __init__(
        self,
        configuration: Configuration,
        max_workers: int | None = None,
        validation_max_workers: int | None = None,
    ) -> None:
        self.configuration = configuration

        # The build server has active threads, so avoid forking directly from it.
        self.executor = ProcessPoolExecutor(
            max_workers=max_workers,
            mp_context=get_context("forkserver"),
            initializer=initialize_worker,
            initargs=(configuration,),
        )
        self.validation_max_workers = validation_max_workers

        if configuration.custom_templates:
            # Initialize the Ansible plugin loader in the main process.
            # This must happen before loading the inventory.
            init_plugin_loader()

        self.inventory = AnsibleInventory(configuration.inventory_dir.joinpath(configuration.inventory_file))

        # Initialize the schema store in main process
        pyavd_init_store()

    def close(self) -> None:
        """Explicitly cleanup resources."""
        shutdown_process_pool_now(executor=self.executor)


class AvdV6Build:
    context: AvdBuildContext
    """Shared context between different fabric builds for the same inventory."""

    _avd_facts_shm_info: SharedMemoryMetadata | None
    """Shared memory metadata for avd_facts (created in common_build_stage, used by workers)."""
    _finalizer: weakref.finalize | None
    _loaded_avd_designs: dict[str, AVDDesign]
    """Map of device -> AVDDesign object. Created in common_build_stage, passed to workers."""
    _validated_inputs_dict: dict[str, dict]
    """Map of device -> validated inputs as dict. Created in common_build_stage, passed to workers."""
    _validated_inputs_json: dict[str, str]
    """Map of device -> validated JSON string. Created during validation."""

    def __init__(
        self,
        context: AvdBuildContext,
        devices: list[str],
    ) -> None:
        """
        Initialize an AVD v6 build.

        Args:
            context: Context object holding reusable objects like configuration and executor.
            devices: List of devices to include in this build.
        """
        self.context = context
        self.devices = devices
        self._validated_inputs_json = {}  # Store validated JSON strings in main process
        self._validated_inputs_dict = {}  # Store validated inputs as dicts in main process
        self._avd_facts_shm_info = None
        self._loaded_avd_designs = {}

        self._finalizer = None

    @property
    def configuration(self) -> Configuration:
        return self.context.configuration

    @property
    def inventory(self) -> AnsibleInventory:
        return self.context.inventory

    @staticmethod
    def _cleanup_resources(
        facts_shm_info: SharedMemoryMetadata | None = None,
    ) -> None:
        """
        Clean up shared memory resources.

        Args:
            facts_shm_info: SharedMemoryMetadata for avd_facts (or None)
        """
        # Cleanup avd_facts shared memory
        if facts_shm_info is not None:
            try:
                shm = shared_memory.SharedMemory(name=facts_shm_info.name)
                shm.close()
                shm.unlink()
            except (FileNotFoundError, AttributeError):
                # Expected: shared memory already cleaned up
                pass
            except OSError as e:
                print("Failed to cleanup avd_facts shared memory: %s", e)

    def close(self) -> None:
        """Explicitly cleanup resources."""
        # Unlink shared memory
        if hasattr(self, "_finalizer") and self._finalizer is not None:
            self._finalizer()

    def _device_count(self) -> int:
        """
        Return the number of devices to process.

        During validation, uses _devices_avd_inputs.
        During device build, uses _loaded_avd_designs.
        """
        if self._loaded_avd_designs:
            return len(self._loaded_avd_designs)
        return len(self.devices)

    def _chunk_size(self) -> int:
        """
        Return the number of tasks that should be sent to each worker.

        Only used for ProcessPoolExecutor (device_build_stage).
        Ignored by ThreadPoolExecutor (validation_stage doesn't use this).

        Returns a value between 1 and 20 based on the number of devices divided by CPU count.
        """
        cpu_count = os.cpu_count() or 8
        return min(max(self._device_count() // cpu_count, 1), 20)

    def validation_stage(self) -> Generator[bool, None, None]:
        """
        Use multithreading to validate inputs for all devices.

        Yielding device_build_result for each.
        """
        with ThreadPoolExecutor(max_workers=self.context.validation_max_workers) as executor:
            results = executor.map(
                validate_inputs_for_one_device, self.devices, (self.inventory.get_vars(device) for device in self.devices), repeat(self.configuration)
            )
            for result in results:
                if result.pyavd_utils_validated_data_result.validated_data is not None:
                    # Validation succeeded - store JSON in main process dict
                    self._validated_inputs_json[result.device_id] = result.pyavd_utils_validated_data_result.validated_data
                    yield True
                    continue

                yield False

    def device_build_stage(
        self,
    ) -> Generator[bool, None, None]:
        """
        Use multiprocessing to build EOS CLI for all devices.

        All phases (build, validate, render) run in the same worker process
        to avoid serialization overhead.

        Yielding device_build_result for each.
        """
        # Ensure avd_facts shared memory was created in common_build_stage
        if self._avd_facts_shm_info is None:
            self.configuration.error_dir.mkdir(parents=True, exist_ok=True)
            self.configuration.error_dir.joinpath("internal_error.txt").write_text("avd_facts shared memory not initialized. Did you run common_build_stage()?")
            yield False
            return

        # Pass cached AVDDesign objects directly to workers
        validated_devices = list(self._loaded_avd_designs.keys())
        yield from self.context.executor.map(
            build_validate_and_render_for_one_device,
            validated_devices,
            [self._loaded_avd_designs[d] for d in validated_devices],
            [self._validated_inputs_dict[d] for d in validated_devices],
            repeat(self._avd_facts_shm_info),
            repeat(self.configuration),
            chunksize=self._chunk_size(),
        )

        # Clear loaded AVDDesign objects - no longer needed
        self._loaded_avd_designs.clear()

    def common_build_stage(self) -> bool:
        """
        Run PyAVD to get AVD facts for all devices.

        Load validated inputs from main process dict (created during validation)
        """
        for device_name, validation_json in self._validated_inputs_json.items():
            # Parse JSON and create AVDDesign object
            self._validated_inputs_dict[device_name] = json.loads(validation_json)
            self._loaded_avd_designs[device_name] = AVDDesign._from_dict(self._validated_inputs_dict[device_name])

        # Clear validated JSON strings - no longer needed
        self._validated_inputs_json.clear()

        pool_manager = PoolManager(self.configuration.output_dir)
        # Get avd_facts from PyAVD
        try:
            avd_facts = get_facts(
                self._loaded_avd_designs,
                all_hostvars=self._validated_inputs_dict,
                pool_manager=pool_manager,
                templar=get_avd_templar(self.configuration),
                digital_twin=self.configuration.digital_twin,
            )
        except Exception as e:
            dump_error(e, self.configuration, "avd_facts")
            return False

        # Save poolmanager data
        pool_manager.save_updated_pools(dumper_cls=AnsibleDumper)  # pyright: ignore[reportArgumentType]

        try:
            # Store avd_facts in shared memory for workers to access.
            avd_facts_bytes = pickle.dumps(avd_facts, protocol=pickle.HIGHEST_PROTOCOL)
            avd_facts_size = len(avd_facts_bytes)
            shm = shared_memory.SharedMemory(create=True, size=avd_facts_size)

            if shm.buf is None:
                shm.close()
                self.configuration.error_dir.mkdir(parents=True, exist_ok=True)
                self.configuration.error_dir.joinpath("internal_error.txt").write_text("Shared Memory could not be created.")
                return False

            shm.buf[:avd_facts_size] = avd_facts_bytes

            # Store metadata and close shm immediately
            shm_name = shm.name
            shm.close()

            self._avd_facts_shm_info = SharedMemoryMetadata(
                name=shm_name,
                size=avd_facts_size,
            )

            # Register finalizer for avd_facts shared memory cleanup
            self._finalizer = weakref.finalize(
                self,
                self._cleanup_resources,
                self._avd_facts_shm_info,
            )
        except Exception as e:
            dump_error(e, self.configuration, "internal")
            return False
        else:
            return True

    # TODO: change name for eos_designs to avd_design in AvdSchema
    @cached_property
    def eos_designs_schema(self) -> AvdSchema:
        """Lazily initialize and cache the EOS designs schema."""
        return AvdSchema(schema_id="eos_designs")

    def common_documentation_stage(self) -> bool:
        """
        Generate fabric documentation, digital twin etc.

        Run this after all device_build_stages have completed.

        Ignores missing structured configs.
        """
        # Ensure avd_facts shared memory was created in common_build_stage
        if self._avd_facts_shm_info is None:
            self.configuration.error_dir.mkdir(parents=True, exist_ok=True)
            self.configuration.error_dir.joinpath("internal_error.txt").write_text("avd_facts shared memory not initialized. Did you run common_build_stage()?")
            return False

        # Ensure avd_facts shared memory was created in common_build_stage
        if self._avd_facts_shm_info is None:
            self.configuration.error_dir.mkdir(parents=True, exist_ok=True)
            self.configuration.error_dir.joinpath("internal_error.txt").write_text("avd_facts shared memory not initialized. Did you run common_build_stage()?")
            return False

        # Load avd_facts from shared memory.
        avd_facts = _load_avd_facts_from_shm(self._avd_facts_shm_info.name, self._avd_facts_shm_info.size)
        structured_configs = self.read_structured_configs()

        fabric_name: str = self.context.configuration.fabric_name

        doc_config = self.configuration.documentation
        output = pyavd.get_fabric_documentation(
            avd_facts=avd_facts,
            structured_configs=structured_configs,
            fabric_name=fabric_name,
            fabric_documentation=doc_config.fabric_documentation,
            include_connected_endpoints=doc_config.include_connected_endpoints,
            topology_csv=doc_config.topology_csv,
            p2p_links_csv=doc_config.p2p_links_csv,
            toc=doc_config.toc,
            digital_twin=self.configuration.digital_twin,
        )
        fabric_doc_dir = self.configuration.docs_dir.joinpath("fabric")
        if output.fabric_documentation:
            fabric_doc_dir.mkdir(parents=True, exist_ok=True)
            fabric_doc_dir.joinpath(f"{fabric_name}-documentation.md").write_text(output.fabric_documentation)

        if output.topology_csv:
            fabric_doc_dir.mkdir(parents=True, exist_ok=True)
            fabric_doc_dir.joinpath(f"{fabric_name}-topology.csv").write_text(output.topology_csv)

        if output.p2p_links_csv:
            fabric_doc_dir.mkdir(parents=True, exist_ok=True)
            fabric_doc_dir.joinpath(f"{fabric_name}-p2p-links.csv").write_text(output.p2p_links_csv)

        if output.digital_twin:
            content = strip_empties_from_dict(
                {
                    str(key).replace("_", "-"): list(value) if isinstance(value, tuple) else value
                    for key, value in dataclasses.asdict(output.digital_twin).items()
                }
            )
            fabric_doc_dir.mkdir(parents=True, exist_ok=True)
            with fabric_doc_dir.joinpath(f"{fabric_name}-topology.yml").open("w", encoding="utf-8") as stream:
                yaml.dump(content, stream=stream, Dumper=AnsibleDumper, sort_keys=False, indent=2, width=130)

        return True

    def read_structured_configs(self) -> dict[str, dict]:
        structured_configs = {}
        for device in self.devices:
            if structured_config := self.read_one_structured_config(device):
                structured_configs[device] = structured_config

        return structured_configs

    def read_one_structured_config(self, device: str) -> dict:
        structured_config_dir = self.configuration.output_dir.joinpath("structured_configs")
        structured_config_suffix = self.configuration.structured_config_suffix
        path = pathlib.Path(structured_config_dir, f"{device}.{structured_config_suffix}")
        if not path.exists():
            return {}

        with path.open(encoding="UTF-8") as stream:
            if structured_config_suffix in ["yml", "yaml"]:
                return yaml.load(stream, Loader=YamlLoader)  # noqa: S506

            # JSON
            return json.load(stream)


### Functions used in multiprocessing.
### Moved out of the class to avoid the whole class being pickled.


def validate_inputs_for_one_device(device: str, device_avd_inputs: dict, configuration: Configuration) -> DevicePyAVDUtilsValidatedDataResult:
    """
    Run PyAVD to validate AVD inputs for one device.

    Expected to be called in a ThreadPoolExecutor in a process where init_store has been called.
    """
    try:
        data_as_json = json.dumps(device_avd_inputs, skipkeys=True, default=lambda _: "<not serializable>")
    except (TypeError, ValueError, RecursionError) as e:
        msg = f"Unable to serialize inputs: {e}"
        raise ValueError(msg) from e

    pyavd_utils_config = pyavd_utils.validation.Configuration(warn_eos_config_keys=True)
    pyavd_utils_validated_data_result = pyavd_utils.validation.get_validated_data(
        data_as_json=data_as_json, schema_name="avd_design", configuration=pyavd_utils_config
    )

    # Emit deprecation warnings to files
    if deprecations := pyavd_utils_validated_data_result.validation_result.deprecations:
        dump_deprecations(deprecations, configuration, "input_validation", device)

    # Check validation status
    if pyavd_utils_validated_data_result.validated_data is None:
        dump_violations(pyavd_utils_validated_data_result.validation_result.violations, configuration, "input_validation", device)

    return DevicePyAVDUtilsValidatedDataResult(device, pyavd_utils_validated_data_result)


def build_validate_and_render_for_one_device(
    device: str,
    device_avd_validated_inputs: AVDDesign,
    device_avd_validated_inputs_dict: dict,
    avd_facts_metadata: SharedMemoryMetadata,
    configuration: Configuration,
) -> bool:
    """
    Build, validate, and render config for one device.

    All steps run in the same worker process to avoid serialization overhead:
    1. Load `avd_facts` from shared memory (once per worker, cached).
    2. Build structured config using the passed AVDDesign object.
    3. Validate structured config.
    4. Render EOS CLI and documentation as required.

    Caching strategy:
    - Each worker process has its own copy of the module.
    - We use `functools.lru_cache` with `maxsize=1` in helper
      functions to cache ``avd_facts`` and the PyAVD store initialization.
    - `maxsize=1` guarantees that a worker will never hold more than one
      `avd_facts` instance in memory, even if the process pool is reused
      across builds with different shared-memory blocks (which it should not be).

    Args:
        device: Device name.
        device_avd_validated_inputs: AVDDesign object.
        device_avd_validated_inputs_dict: Dict with validated inputs (hostvars)
        avd_facts_metadata: Metadata to access `avd_facts` shared memory.
        configuration: Configuration object with dirs
    """
    # Load (and cache) avd_facts from shared memory in this worker.
    avd_facts = _load_avd_facts_from_shm(avd_facts_metadata.name, avd_facts_metadata.size)

    # Phase 1: Build structured config
    try:
        eos_config = get_structured_config(
            hostname=device,
            inputs=device_avd_validated_inputs,
            hostvars=device_avd_validated_inputs_dict,
            all_facts=avd_facts,
            templar=get_avd_templar(configuration),
            digital_twin=configuration.digital_twin,
        )._as_dict()
    except Exception as e:
        dump_error(e, configuration, "structured_config", device)
        return False
    finally:
        # Free device_avd_validated_inputs - no longer needed after structured config is built
        del device_avd_validated_inputs

    # Phase 2: Serialize structured config
    configuration.output_dir.joinpath("structured_configs").mkdir(parents=True, exist_ok=True)
    with configuration.output_dir.joinpath("structured_configs", f"{device}.yml").open("w", encoding="utf-8") as stream:
        yaml.dump(eos_config, stream=stream, Dumper=AnsibleDumper, indent=2, sort_keys=False, width=130)

    # Phase 3: Validate structured config
    validated_data_result = validate_structured_config(eos_config)

    # Emit deprecation warnings to files
    if deprecations := validated_data_result.validation_result.deprecations:
        dump_deprecations(deprecations, configuration, "structured_config_validation", device)

    # Check validation status
    if validated_data_result.validated_data is None:
        dump_violations(validated_data_result.validation_result.violations, configuration, "structured_config_validation", device)

        # Validation failed - free eos_config before returning
        del eos_config
        return False

    # Phase 4: Render EOS CLI
    if configuration.device_configs:
        try:
            eos_cli = pyavd.get_device_config(eos_config)
        except Exception as e:
            dump_error(e, configuration, "eos_cli", device)
            return False

        configuration.output_dir.joinpath("configs").mkdir(parents=True, exist_ok=True)
        configuration.output_dir.joinpath("configs", f"{device}.cfg").write_text(eos_cli)
        del eos_cli

    # Phase 5: Render device documentation
    if configuration.documentation.device_docs:
        try:
            device_doc = pyavd.get_device_doc(eos_config, add_md_toc=True)
        except Exception as e:
            dump_error(e, configuration, "device_doc", device)
            return False

        configuration.docs_dir.joinpath("devices").mkdir(parents=True, exist_ok=True)
        configuration.docs_dir.joinpath("devices", f"{device}.md").write_text(device_doc)
        del device_doc

    return True


def initialize_worker(configuration: Configuration) -> None:
    """Initialize various objects once per worker."""
    # Ensure the PyAVD store is initialized once per worker process.
    _ensure_pyavd_store_initialized()

    if configuration.custom_templates:
        init_plugin_loader()


def get_avd_templar(configuration: Configuration) -> AVDTemplar | None:
    if not configuration.custom_templates:
        return None

    searchpath = [
        str(configuration.inventory_dir.joinpath("templates")),
        str(configuration.inventory_dir),
    ]
    dataloader = DataLoader()
    return AVDTemplar(
        templar=Templar(loader=dataloader),
        loader=dataloader,
        searchpath=searchpath,
        ansible_above_2_19=ANSIBLE_ABOVE_2_19,
    )


def dump_deprecations(deprecations: list[pyavd_utils.validation.Deprecation], configuration: Configuration, stage: str, device: str) -> None:
    error_dir = configuration.error_dir.joinpath(configuration.fabric_name)
    error_dir = error_dir.joinpath(device) if device else error_dir
    error_dir.mkdir(parents=True, exist_ok=True)
    err_lines = [f"[{deprecation.path}]: '{deprecation.message}'" for deprecation in deprecations]
    error_dir.joinpath(f"{stage}_deprecations.txt").write_text("\n".join(err_lines))


def dump_violations(violations: list[pyavd_utils.validation.Violation], configuration: Configuration, stage: str, device: str) -> None:
    error_dir = configuration.error_dir.joinpath(configuration.fabric_name)
    error_dir = error_dir.joinpath(device) if device else error_dir
    error_dir.mkdir(parents=True, exist_ok=True)
    err_lines = [f"[{violation.path}]: '{violation.message}'" for violation in violations]
    error_dir.joinpath(f"{stage}_violations.txt").write_text("\n".join(err_lines))


def dump_error(exc: Exception, configuration: Configuration, stage: str, device: str | None = None) -> None:
    error_dir = configuration.error_dir.joinpath(configuration.fabric_name)
    error_dir = error_dir.joinpath(device) if device else error_dir
    error_dir.mkdir(parents=True, exist_ok=True)
    err_lines = traceback.format_exception(exc) if configuration.dump_tracebacks else traceback.format_exception_only(exc)
    error_dir.joinpath(f"{stage}_error.txt").write_text("\n".join(err_lines))


@lru_cache(maxsize=1)
def _ensure_pyavd_store_initialized() -> None:
    """Initialize the PyAVD store once per worker process."""
    pyavd_init_store()


@lru_cache(maxsize=1)
def _load_avd_facts_from_shm(shm_name: str, shm_size: int) -> dict[str, typing.Any]:
    """
    Load `avd_facts` from shared memory and cache it per worker.

    Because each worker runs in its own process, this cache is implicitly
    per-worker. Using `maxsize=1` guarantees that a worker will never
    retain more than a single `avd_facts` instance, even if the same
    worker process is reused across multiple builds with different
    shared-memory blocks.
    """
    shm = shared_memory.SharedMemory(name=shm_name)
    if shm.buf is None:
        msg = f"Shared memory buffer is None for name {shm_name}"
        raise RuntimeError(msg)
    data_bytes = bytes(shm.buf[:shm_size])
    shm.close()
    return pickle.loads(data_bytes)  # noqa: S301


@dataclasses.dataclass(frozen=True, slots=True)
class DevicePyAVDUtilsValidatedDataResult:
    device_id: str
    pyavd_utils_validated_data_result: pyavd_utils.validation.ValidatedDataResult


### Shared memory objects and helpers


@dataclasses.dataclass(frozen=True, slots=True)
class SharedMemoryMetadata:
    """Metadata for accessing a shared memory block."""

    name: str
    """Name of the shared memory block (used by workers to attach)."""
    size: int
    """Size of data in the shared memory block."""


def shutdown_process_pool_now(executor: Executor, *, deadline_s: float = 1.5) -> None:
    """
    Shuts down the passed executor in such a way that golang won't need to issue a sigkill.

    The golang process managing the AVD python build processes issues a SIGKILL on the
    python process if it does not acknowledge the shutdown RPC within 2s.
    Drops queued futures and returns immediately; do not wait for  in-flight workers
    (would commonly block past the 2s window).
    Best-effort: terminate worker processes so they don't outlive as orphans of the
    forkserver (which would leak RSS until the pod restarts).
    """
    processes = getattr(executor, "_processes", None) or {}
    workers = list(processes.values())

    with suppress(Exception):
        executor.shutdown(wait=False, cancel_futures=True)

    for proc in workers:
        with suppress(Exception):
            proc.terminate()

    deadline = time.monotonic() + deadline_s
    for proc in workers:
        remaining = max(0.0, deadline - time.monotonic())
        with suppress(Exception):
            proc.join(timeout=remaining)

    for proc in workers:
        with suppress(Exception):
            if proc.is_alive():
                proc.kill()

    for proc in workers:
        remaining = max(0.0, deadline - time.monotonic())
        with suppress(Exception):
            proc.join(timeout=remaining)


def group_devices_per_fabric(context: AvdBuildContext) -> dict[str, list[str]]:
    inventory = context.inventory
    devices = inventory.get_hosts("all")
    fabric_devices: dict[str, list[str]] = {}
    for device in devices:
        fabric = inventory.get_vars(device.name).get("fabric_name")
        if fabric is None:
            fabric = DEFAULT_FABRIC

        fabric_devices.setdefault(fabric, []).append(device.name)

    return fabric_devices


def build(configuration: Configuration) -> None:
    """
    Build AVD for the given inventory path.

    Outputs are written to the output_dir relative to the inventory path.
    Captures errors for each stage and writes error files in the output path under the error path.
    """
    effective_output_dir = configuration.inventory_dir.joinpath(configuration.output_dir)
    print("Building inventory", configuration.inventory_dir)
    print("Outputs to", effective_output_dir)

    inventory_context = AvdBuildContext(configuration)
    fabric_devices = group_devices_per_fabric(inventory_context)
    for fabric, devices in fabric_devices.items():
        print("Building fabric", fabric)
        configuration.fabric_name = fabric
        build = AvdV6Build(inventory_context, devices)

        validation_result = list(build.validation_stage())
        if not any(validation_result):
            # All devices failed validation so skip the rest
            continue

        if not build.common_build_stage():
            continue

        _ = all(build.device_build_stage())

        build.common_documentation_stage()

        build.close()

    inventory_context.close()


def clean_dirs(configuration: Configuration) -> None:
    """Delete directories recursively."""
    for directory in configuration.get_cleanup_dirs():
        if directory.exists():
            shutil.rmtree(directory)


def get_git_repo(path: pathlib.Path) -> git.Repo:
    """
    Returns the auto-detectsed Git repository root starting from the given path.

    Raises if no repo was found.
    """
    # search_parent_directories=True walks up from subdir_path until it finds .git
    return git.Repo(path, search_parent_directories=True)


def get_subdir_diff(repo: git.Repo, path: pathlib.Path) -> str:
    """Returns combined staged + unstaged diffs for the given path."""
    # "HEAD" captures both staged and unstaged changes against the last commit
    return repo.git.diff("HEAD", "--", path)


def parse_args() -> Configuration:
    parser = argparse.ArgumentParser()
    parser.add_argument("inventory_dir", type=pathlib.Path)
    parser.add_argument("-o", "--output-dir", type=pathlib.Path, help="Output path relative to the inventory path.", default="intended/")
    parser.add_argument("-d", "--docs-dir", type=pathlib.Path, help="Documentation path relative to the inventory path.", default="documentation/")
    parser.add_argument("-i", "--inventory-file", help="Inventory file name.", default="inventory.yml")
    parser.add_argument("--no-clean", action="store_true", help="Don't clean output and documentation paths before running.", default=False)
    parser.add_argument("--no-device-configs", action="store_true", help="Don't generate device configs.", default=False)
    parser.add_argument("--no-device-docs", action="store_true", help="Don't generate device docs.", default=False)
    parser.add_argument("--no-fabric-doc", action="store_true", help="Don't generate fabric doc.", default=False)
    parser.add_argument("--no-toc", action="store_true", help="Don't generate TOC as part of the fabric documentation.", default=False)
    parser.add_argument("--include-connected-endpoints", action="store_true", help="Include connected endpoints in the fabric documentation.", default=False)
    parser.add_argument("--topology-csv", action="store_true", help="Generate topology CSV.", default=False)
    parser.add_argument("--p2p-links-csv", action="store_true", help="Generate p2p links CSV.", default=False)
    parser.add_argument("--digital-twin", action="store_true", help="Run in digital-twin mode.", default=False)
    parser.add_argument("--custom-templates", action="store_true", help="Support jinja templates for ip addressing and descriptions.", default=False)
    parser.add_argument("--tracebacks", action="store_true", help="Include tracebacks in dumped errors.", default=False)

    args = parser.parse_args()
    inventory_dir: pathlib.Path = args.inventory_dir.resolve()
    return Configuration(
        fabric_name=DEFAULT_FABRIC,
        inventory_dir=inventory_dir,
        output_dir=inventory_dir.joinpath(args.output_dir),
        docs_dir=inventory_dir.joinpath(args.docs_dir),
        inventory_file=args.inventory_file,
        no_clean=args.no_clean,
        digital_twin=args.digital_twin,
        device_configs=not args.no_device_configs,
        documentation=Documentation(
            device_docs=not args.no_device_docs,
            fabric_documentation=not args.no_fabric_doc,
            toc=not args.no_toc,
            include_connected_endpoints=args.include_connected_endpoints,
            topology_csv=args.topology_csv,
            p2p_links_csv=args.p2p_links_csv,
        ),
        error_dir=inventory_dir.joinpath("errors/"),
        custom_templates=args.custom_templates,
        dump_tracebacks=args.tracebacks,
    )


def main() -> int:
    configuration = parse_args()

    repo = get_git_repo(configuration.inventory_dir)
    if not repo:
        msg = "The inventory_dir must be inside a git repo."
        raise ValueError(msg)
    if not configuration.no_clean:
        clean_dirs(configuration)

    # Changing to inventory dir to ensure relative paths in things like pool manager files resolve correctly.
    os.chdir(configuration.inventory_dir)
    build(configuration)
    return 0


if __name__ == "__main__":
    sys.exit(main())
