# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# /// script
# dependencies = [
#   "pyavd[ansible] @ file:///${PROJECT_ROOT}/python-avd",
#   "gitpython>=3.1.57",
#   "coverage[toml]==7.15.2",
#   "coverage_plugins @ file:///${PROJECT_ROOT}/development/coverage_plugins"
# ]
# requires-python = ">=3.11"
# # [tool.uv]
# # reinstall-package = ["pyavd"]
# ///
# pylint: disable=too-many-lines

from __future__ import annotations

import argparse
import dataclasses
import importlib
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
import tomllib
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
from pyavd._schema.store import init_store as pyavd_init_store
from pyavd._utils import default, strip_empties_from_dict, template
from pyavd._utils.avd_templar import AVDTemplar
from pyavd.api.pool_manager import PoolManager
from pyavd.api.schemas import AVDDesign
from pyavd.j2filters import add_md_toc

if typing.TYPE_CHECKING:
    from collections.abc import Generator
    from typing import TypeVar

    from ansible.inventory.host import Host
    from typing_extensions import Self

    class DataclassInstance(typing.Protocol):
        __dataclass_fields__: typing.ClassVar[dict[str, typing.Any]]

    DataclassT = TypeVar("DataclassT", bound=DataclassInstance)

ANSIBLE_ABOVE_2_19 = ansible_version.startswith(("2.2", "2.19"))
DEFAULT_FABRIC = "__UNSET_FABRIC_NAME__"
CUSTOM_TEMPLATES_CFG_TEMPLATE = str(
    pathlib.Path(__file__).parents[1].joinpath("ansible_collections/arista/avd/roles/eos_cli_config_gen/templates/eos/custom-templates.j2").resolve()
)
CUSTOM_TEMPLATES_DOC_TEMPLATE = str(
    pathlib.Path(__file__).parents[1].joinpath("ansible_collections/arista/avd/roles/eos_cli_config_gen/templates/documentation/custom-templates.j2").resolve()
)


class PathNotDirError(ValueError):
    field: str

    def __init__(self, field: str, *args: typing.Any) -> None:
        self.field = field
        super().__init__(field, *args)

    def __str__(self) -> str:
        return f"The {self.field} path is invalid. The path must point to a directory."


@dataclasses.dataclass
class DocumentationConfigOverrides:
    device_docs: bool | None = None
    device_docs_toc: bool | None = None
    fabric_doc: bool | None = None
    include_connected_endpoints: bool | None = None
    p2p_links_csv: bool | None = None
    toc: bool | None = None
    topology_csv: bool | None = None


@dataclasses.dataclass(frozen=True)
class DocumentationConfig:
    device_docs: bool
    device_docs_toc: bool
    fabric_doc: bool
    include_connected_endpoints: bool
    p2p_links_csv: bool
    toc: bool
    topology_csv: bool

    @classmethod
    def from_parent(
        cls,
        parent: Self,
        overrides: DocumentationConfigOverrides,
    ) -> Self:
        return cls(
            device_docs=default(overrides.device_docs, parent.device_docs),
            device_docs_toc=default(overrides.device_docs_toc, parent.device_docs_toc),
            fabric_doc=default(overrides.fabric_doc, parent.fabric_doc),
            include_connected_endpoints=default(overrides.include_connected_endpoints, parent.include_connected_endpoints),
            p2p_links_csv=default(overrides.p2p_links_csv, parent.p2p_links_csv),
            toc=default(overrides.toc, parent.toc),
            topology_csv=default(overrides.topology_csv, parent.topology_csv),
        )


@dataclasses.dataclass(frozen=True)
class ProjectDocumentationConfig(DocumentationConfig):
    """Project documentation config implementing defaults for DocumentationConfig."""

    device_docs: bool = True
    device_docs_toc: bool = True
    fabric_doc: bool = True
    include_connected_endpoints: bool = False
    topology_csv: bool = False
    p2p_links_csv: bool = False
    toc: bool = True


@dataclasses.dataclass
class FabricConfigOverrides:
    """Optional config overrides."""

    avd_design: bool | None = None
    clean: bool | None = None
    device_configs: bool | None = None
    digital_twin: bool | None = None
    docs_dir: str | None = None
    documentation: DocumentationConfigOverrides = dataclasses.field(default_factory=DocumentationConfigOverrides)
    dump_tracebacks: bool | None = None
    error_dir: str | None = None
    extra_vars: dict[str, typing.Any] | None = None
    output_dir: str | None = None
    structured_config_suffix: typing.Literal["yml", "yaml", "json"] | None = None


@dataclasses.dataclass(frozen=True)
class ProjectConfig:
    """Project config implementing defaults for Config."""

    project_dir: pathlib.Path
    avd_design: bool = True
    clean: bool = True
    custom_templates: bool = False
    custom_path: str | None = None
    device_configs: bool = True
    digital_twin: bool = False
    docs_dir: str = "documentation"
    documentation: DocumentationConfig = dataclasses.field(default_factory=ProjectDocumentationConfig)
    dump_tracebacks: bool = False
    error_dir: str = "errors"
    extra_vars: dict[str, typing.Any] | None = None
    inventory_file: str = "inventory.yml"
    output_dir: str = "intended"
    structured_config_suffix: typing.Literal["yml", "yaml", "json"] = "yml"

    @cached_property
    def full_project_dir(self) -> pathlib.Path:
        return self.project_dir.resolve()


@dataclasses.dataclass(frozen=True)
class ScenarioConfig:
    scenario_name: str
    project: ProjectConfig
    custom_path: str | None
    custom_templates: bool
    extra_vars: dict[str, typing.Any] | None
    inventory_file: str

    # Base config which may override the settings project level.
    avd_design: bool
    clean: bool
    device_configs: bool
    digital_twin: bool
    docs_dir: str
    documentation: DocumentationConfig
    dump_tracebacks: bool
    error_dir: str
    output_dir: str
    structured_config_suffix: typing.Literal["yml", "yaml", "json"]

    @classmethod
    def from_project(
        cls,
        scenario_name: str,
        project: ProjectConfig,
        overrides: ScenarioConfigOverrides,
    ) -> Self:
        return cls(
            scenario_name=scenario_name,
            project=project,
            custom_templates=default(overrides.custom_templates, project.custom_templates),
            custom_path=default(overrides.custom_path, project.custom_path),
            extra_vars=default(overrides.extra_vars, project.extra_vars),
            inventory_file=default(overrides.inventory_file, project.inventory_file),
            avd_design=default(overrides.avd_design, project.avd_design),
            clean=default(overrides.clean, project.clean),
            device_configs=default(overrides.device_configs, project.device_configs),
            digital_twin=default(overrides.digital_twin, project.digital_twin),
            docs_dir=default(overrides.docs_dir, project.docs_dir),
            documentation=DocumentationConfig.from_parent(project.documentation, overrides.documentation),
            dump_tracebacks=default(overrides.dump_tracebacks, project.dump_tracebacks),
            error_dir=default(overrides.error_dir, project.error_dir),
            output_dir=default(overrides.output_dir, project.output_dir),
            structured_config_suffix=default(overrides.structured_config_suffix, project.structured_config_suffix),
        )

    @property
    def full_project_dir(self) -> pathlib.Path:
        return self.project.full_project_dir

    @cached_property
    def full_inventory_file(self) -> pathlib.Path:
        return self.full_project_dir.joinpath(self.inventory_file).resolve()

    @cached_property
    def configs_dir(self) -> pathlib.Path:
        return self.full_output_dir.joinpath("configs").resolve()

    @cached_property
    def structured_configs_dir(self) -> pathlib.Path:
        return self.full_output_dir.joinpath("structured_configs").resolve()

    @cached_property
    def full_output_dir(self) -> pathlib.Path:
        return self.full_project_dir.joinpath(self.output_dir).resolve()

    @cached_property
    def full_docs_dir(self) -> pathlib.Path:
        return self.full_project_dir.joinpath(self.docs_dir).resolve()

    @cached_property
    def full_error_dir(self) -> pathlib.Path:
        return self.full_project_dir.joinpath(self.error_dir).resolve()

    @cached_property
    def full_custom_path(self) -> pathlib.Path | None:
        if self.custom_path is None:
            return None
        return self.full_project_dir.joinpath(self.custom_path).resolve()

    def get_cleanup_dirs(self) -> set[pathlib.Path]:
        """Return set of directories to clean up."""
        return {self.configs_dir, self.structured_configs_dir, self.full_docs_dir, self.full_error_dir}


@dataclasses.dataclass
class ScenarioConfigOverrides(FabricConfigOverrides):
    custom_templates: bool | None = None
    inventory_file: str | None = None
    custom_path: str | None = None
    extra_vars: dict[str, typing.Any] | None = None


@dataclasses.dataclass(frozen=True)
class FabricConfig:
    fabric_name: str
    scenario: ScenarioConfig

    # Base config which may override the settings project level,
    # except clean which is local for the fabric level.
    avd_design: bool
    device_configs: bool
    digital_twin: bool
    docs_dir: str
    documentation: DocumentationConfig
    dump_tracebacks: bool
    error_dir: str
    output_dir: str
    structured_config_suffix: typing.Literal["yml", "yaml", "json"]

    clean: bool = False

    @classmethod
    def from_scenario(
        cls,
        fabric_name: str,
        scenario: ScenarioConfig,
        overrides: FabricConfigOverrides,
    ) -> Self:
        return cls(
            fabric_name=fabric_name,
            scenario=scenario,
            clean=overrides.clean if overrides.clean is not None else False,
            avd_design=default(overrides.avd_design, scenario.avd_design),
            device_configs=default(overrides.device_configs, scenario.device_configs),
            digital_twin=default(overrides.digital_twin, scenario.digital_twin),
            docs_dir=default(overrides.docs_dir, scenario.docs_dir),
            documentation=DocumentationConfig.from_parent(scenario.documentation, overrides.documentation),
            dump_tracebacks=default(overrides.dump_tracebacks, scenario.dump_tracebacks),
            error_dir=default(overrides.error_dir, scenario.error_dir),
            output_dir=default(overrides.output_dir, scenario.output_dir),
            structured_config_suffix=default(overrides.structured_config_suffix, scenario.structured_config_suffix),
        )

    @property
    def project(self) -> ProjectConfig:
        return self.scenario.project

    @property
    def full_project_dir(self) -> pathlib.Path:
        return self.project.full_project_dir

    @property
    def custom_templates(self) -> bool:
        return self.scenario.custom_templates

    @cached_property
    def configs_dir(self) -> pathlib.Path:
        return self.full_output_dir.joinpath("configs").resolve()

    @cached_property
    def structured_configs_dir(self) -> pathlib.Path:
        return self.full_output_dir.joinpath("structured_configs").resolve()

    @cached_property
    def full_output_dir(self) -> pathlib.Path:
        return self.full_project_dir.joinpath(self.output_dir).resolve()

    @cached_property
    def full_docs_dir(self) -> pathlib.Path:
        return self.full_project_dir.joinpath(self.docs_dir).resolve()

    @cached_property
    def full_error_dir(self) -> pathlib.Path:
        return self.full_project_dir.joinpath(self.error_dir).resolve()

    def get_cleanup_dirs(self) -> set[pathlib.Path]:
        """Return set of directories to clean up."""
        return {self.configs_dir, self.structured_configs_dir, self.full_docs_dir, self.full_error_dir}


@dataclasses.dataclass(frozen=True)
class Project:
    config: ProjectConfig
    scenarios: list[Scenario]


@dataclasses.dataclass(frozen=True)
class Scenario:
    config: ScenarioConfig
    fabric_overrides: dict[str, FabricConfigOverrides]


class AnsibleInventory:  # pylint: disable=too-few-public-methods
    """Ansible Inventory wrapper."""

    def __init__(
        self,
        inventory_path: pathlib.Path,
        data_loader: DataLoader | None = None,
        vault_ids: list | None = None,
        extra_vars: dict[str, typing.Any] | None = None,
    ) -> None:
        """Initialize Ansible Inventory Manager."""
        self.inventory_path = inventory_path
        self.data_loader = data_loader if data_loader is not None else DataLoader()
        if vault_ids:
            CLI.setup_vault_secrets(self.data_loader, vault_ids=vault_ids)

        self.inventory_manager = InventoryManager(loader=self.data_loader, sources=[self.inventory_path.as_posix()], parse=True)
        self.variable_manager = VariableManager(loader=self.data_loader, inventory=self.inventory_manager)
        if extra_vars:
            self.variable_manager._extra_vars = extra_vars
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
    scenario: ScenarioConfig
    executor: Executor
    """ProcessPoolExecutor for CPU-intensive device builds."""
    inventory: AnsibleInventory
    validation_max_workers: int | None
    """Max workers for ThreadPoolExecutor used in validation."""

    _org_sys_path: list[str] | None = None

    def __init__(
        self,
        scenario: ScenarioConfig,
        max_workers: int | None = None,
        validation_max_workers: int | None = None,
    ) -> None:
        self.scenario = scenario

        # The build server has active threads, so avoid forking directly from it.
        self.executor = ProcessPoolExecutor(
            max_workers=max_workers,
            mp_context=get_context("forkserver"),
            initializer=initialize_worker,
            initargs=(scenario,),
        )
        try:
            self.validation_max_workers = validation_max_workers

            if scenario.custom_templates:
                # Initialize the Ansible plugin loader in the main process.
                # This must happen before gloading the inventory.
                _ensure_ansible_plugins_initialized()

            self.inventory = AnsibleInventory(scenario.full_inventory_file, extra_vars=scenario.extra_vars)

            # Initialize the schema store in main process
            _ensure_pyavd_store_initialized()

            self.add_custom_python_path()

        except Exception:
            self.close()
            raise

    def close(self) -> None:
        """Explicitly cleanup resources."""
        shutdown_process_pool_now(executor=self.executor)
        self.restore_python_path()

    def add_custom_python_path(self) -> None:
        if (full_custom_path := self.scenario.full_custom_path) is None:
            return

        custom_path_str = str(full_custom_path)
        if custom_path_str in sys.path:
            return

        self._org_sys_path = sys.path.copy()
        sys.path.insert(0, custom_path_str)

        importlib.invalidate_caches()

    def restore_python_path(self) -> None:
        if self._org_sys_path is None or (full_custom_path := self.scenario.full_custom_path) is None:
            return

        sys.path[:] = self._org_sys_path

        # Unload modules loaded from the custom path
        modules_to_unload = []
        for name, mod in list(sys.modules.items()):
            if mod is None:
                continue

            # Check file location
            file_attr = getattr(mod, "__file__", None)
            if file_attr:
                try:
                    if pathlib.Path(file_attr).resolve().is_relative_to(full_custom_path):
                        modules_to_unload.append(name)
                        continue
                except (ValueError, RuntimeError):
                    pass

            # Check package location
            for p in getattr(mod, "__path__", []):
                try:
                    if pathlib.Path(p).resolve().is_relative_to(full_custom_path):
                        modules_to_unload.append(name)
                        break
                except (ValueError, RuntimeError):
                    pass

        # Evict from import cache
        for name in modules_to_unload:
            del sys.modules[name]


class AvdV6Build:
    context: AvdBuildContext
    """Shared context between different fabric builds for the same inventory."""

    config: FabricConfig
    """Config for one Fabric build."""

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
        config: FabricConfig,
        context: AvdBuildContext,
        devices: list[str],
    ) -> None:
        """
        Initialize an AVD v6 build.

        Args:
            config: Build configuration for this fabric.
            context: Context object holding reusable objects like configuration and executor.
            devices: List of devices to include in this build.
        """
        self.config = config
        self.context = context
        self.devices = devices
        self._validated_inputs_json = {}  # Store validated JSON strings in main process
        self._validated_inputs_dict = {}  # Store validated inputs as dicts in main process
        self._avd_facts_shm_info = None
        self._loaded_avd_designs = {}

        self._finalizer = None

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
                validate_inputs_for_one_device, self.devices, (self.inventory.get_vars(device) for device in self.devices), repeat(self.config)
            )
            for result in results:
                if result.pyavd_utils_validated_data_result.validated_data is not None:
                    # Validation succeeded - store JSON in main process dict
                    self._validated_inputs_json[result.device_id] = result.pyavd_utils_validated_data_result.validated_data
                    self._validated_inputs_dict[result.device_id] = json.loads(result.pyavd_utils_validated_data_result.validated_data)
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
        if self.config.avd_design and self._avd_facts_shm_info is None:
            dump_error("avd_facts shared memory not initialized. Did you run common_build_stage()?", self.config, "internal_device")
            yield False
            return

        validated_devices = list(self._validated_inputs_dict.keys())
        yield from self.context.executor.map(
            build_validate_and_render_for_one_device,
            validated_devices,
            [self._loaded_avd_designs[d] for d in validated_devices] if self.config.avd_design else repeat(None),
            [self._validated_inputs_dict[d] for d in validated_devices],
            repeat(self._avd_facts_shm_info),
            repeat(self.config),
            chunksize=self._chunk_size(),
        )

        if self.config.avd_design:
            # Clear loaded AVDDesign objects and dicts - no longer needed
            self._loaded_avd_designs.clear()
            self._validated_inputs_dict.clear()

    def common_build_stage(self) -> bool:
        """
        Run PyAVD to get AVD facts for all devices.

        Load validated inputs from main process dict (created during validation)
        """
        for device_name, validated_inputs_dict in self._validated_inputs_dict.items():
            # Parse JSON and create AVDDesign object
            self._loaded_avd_designs[device_name] = AVDDesign._from_dict(validated_inputs_dict)

        # Clear validated JSON strings - no longer needed
        self._validated_inputs_json.clear()

        pool_manager = PoolManager(self.config.full_output_dir)
        # Get avd_facts from PyAVD
        try:
            avd_facts = get_facts(
                self._loaded_avd_designs,
                all_hostvars=self._validated_inputs_dict,
                pool_manager=pool_manager,
                templar=get_avd_templar(self.config),
                digital_twin=self.config.digital_twin,
            )
        except Exception as e:
            dump_exception(e, self.config, "avd_facts")
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
                dump_error("Shared Memory could not be created.", self.config, "internal_common")
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
            dump_exception(e, self.config, "internal")
            return False
        else:
            return True

    def common_documentation_stage(self) -> bool:
        """
        Generate fabric documentation, digital twin etc.

        Run this after all device_build_stages have completed.

        Ignores missing structured configs.
        """
        # Ensure avd_facts shared memory was created in common_build_stage
        if self._avd_facts_shm_info is None:
            dump_error("avd_facts shared memory not initialized. Did you run common_build_stage()?", self.config, "internal_common_doc")
            return False

        # Ensure avd_facts shared memory was created in common_build_stage
        if self._avd_facts_shm_info is None:
            dump_error("avd_facts shared memory not initialized. Did you run common_build_stage()?", self.config, "internal_common_doc")
            return False

        # Load avd_facts from shared memory.
        avd_facts = _load_avd_facts_from_shm(self._avd_facts_shm_info.name, self._avd_facts_shm_info.size)
        structured_configs = self.read_structured_configs()

        fabric_name: str = self.config.fabric_name

        doc_config = self.config.documentation
        output = pyavd.get_fabric_documentation(
            avd_facts=avd_facts,
            structured_configs=structured_configs,
            fabric_name=fabric_name,
            fabric_documentation=doc_config.fabric_doc,
            include_connected_endpoints=doc_config.include_connected_endpoints,
            topology_csv=doc_config.topology_csv,
            p2p_links_csv=doc_config.p2p_links_csv,
            toc=doc_config.toc,
            digital_twin=self.config.digital_twin,
        )
        fabric_doc_dir = self.config.full_docs_dir.joinpath("fabric")
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
        structured_config_dir = self.config.structured_configs_dir
        structured_config_suffix = self.config.structured_config_suffix
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


def validate_inputs_for_one_device(device: str, device_avd_inputs: dict, config: FabricConfig) -> DevicePyAVDUtilsValidatedDataResult:
    """
    Run PyAVD to validate AVD inputs for one device.

    Expected to be called in a ThreadPoolExecutor in a process where init_store has been called.
    """
    try:
        data_as_json = json.dumps(device_avd_inputs, skipkeys=True, default=lambda _: "<not serializable>")
    except (TypeError, ValueError, RecursionError) as e:
        msg = f"Unable to serialize inputs: {e}"
        raise ValueError(msg) from e

    if config.avd_design:
        pyavd_utils_config = pyavd_utils.validation.Configuration(warn_eos_config_keys=True)
        pyavd_utils_validated_data_result = pyavd_utils.validation.get_validated_data(
            data_as_json=data_as_json, schema_name="avd_design", configuration=pyavd_utils_config
        )
    else:
        pyavd_utils_validated_data_result = pyavd_utils.validation.get_validated_data(data_as_json=data_as_json, schema_name="eos_config")

    # Emit deprecation warnings to files
    if deprecations := pyavd_utils_validated_data_result.validation_result.deprecations:
        dump_deprecations(deprecations, config, "input_validation", device)

    # Check validation status
    if pyavd_utils_validated_data_result.validated_data is None:
        dump_violations(pyavd_utils_validated_data_result.validation_result.violations, config, "input_validation", device)

    return DevicePyAVDUtilsValidatedDataResult(device, pyavd_utils_validated_data_result)


def build_validate_and_render_for_one_device(
    device: str,
    device_avd_validated_inputs: AVDDesign | None,
    device_avd_validated_inputs_dict: dict,
    avd_facts_metadata: SharedMemoryMetadata,
    config: FabricConfig,
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
        config: FabricConfig object with dirs and other build parameters
    """
    if config.avd_design:
        device_avd_validated_inputs = typing.cast("AVDDesign", device_avd_validated_inputs)

        # Load (and cache) avd_facts from shared memory in this worker.
        avd_facts = _load_avd_facts_from_shm(avd_facts_metadata.name, avd_facts_metadata.size)

        # Phase 1: Build structured config
        try:
            eos_config = get_structured_config(
                hostname=device,
                inputs=device_avd_validated_inputs,
                hostvars=device_avd_validated_inputs_dict,
                all_facts=avd_facts,
                templar=get_avd_templar(config),
                digital_twin=config.digital_twin,
            )._as_dict()
        except Exception as e:
            dump_exception(e, config, "structured_config", device)
            return False
        finally:
            # Free device_avd_validated_inputs - no longer needed after structured config is built
            del device_avd_validated_inputs

        # Phase 2: Serialize structured config
        # TODO: Honor the config.structured_config_suffix setting
        config.structured_configs_dir.mkdir(parents=True, exist_ok=True)
        with config.structured_configs_dir.joinpath(f"{device}.yml").open("w", encoding="utf-8") as stream:
            yaml.dump(eos_config, stream=stream, Dumper=AnsibleDumper, indent=2, sort_keys=False, width=130)

        # Phase 3: Validate structured config
        validated_data_result = validate_structured_config(eos_config)

        # Emit deprecation warnings to files
        if deprecations := validated_data_result.validation_result.deprecations:
            dump_deprecations(deprecations, config, "structured_config_validation", device)

        # Check validation status
        if validated_data_result.validated_data is None:
            dump_violations(validated_data_result.validation_result.violations, config, "structured_config_validation", device)

            # Validation failed - free eos_config before returning
            del eos_config
            return False

    else:
        # Pure eos_cli_config_gen run
        eos_config = device_avd_validated_inputs_dict

    # Phase 4: Render EOS CLI
    if config.device_configs:
        try:
            eos_cli = pyavd.get_device_config(eos_config)
        except Exception as e:
            dump_exception(e, config, "eos_cli", device)
            return False

        if config.custom_templates and eos_config.get("custom_templates"):
            templar = get_avd_templar(config)
            eos_cli += template(CUSTOM_TEMPLATES_CFG_TEMPLATE, device_avd_validated_inputs_dict, templar)

        config.configs_dir.mkdir(parents=True, exist_ok=True)
        config.configs_dir.joinpath(f"{device}.cfg").write_text(eos_cli)
        del eos_cli

    # Phase 5: Render device documentation
    if config.documentation.device_docs:
        try:
            device_doc = pyavd.get_device_doc(eos_config, add_md_toc=False)
        except Exception as e:
            dump_exception(e, config, "device_doc", device)
            return False

        if config.custom_templates and eos_config.get("custom_templates"):
            templar = get_avd_templar(config)
            device_doc += template(CUSTOM_TEMPLATES_DOC_TEMPLATE, device_avd_validated_inputs_dict, templar)

        if config.documentation.device_docs_toc:
            device_doc = add_md_toc(device_doc, skip_lines=3)

        config.full_docs_dir.joinpath("devices").mkdir(parents=True, exist_ok=True)
        config.full_docs_dir.joinpath("devices", f"{device}.md").write_text(device_doc)
        del device_doc

    return True


def initialize_worker(config: ScenarioConfig) -> None:
    """Initialize various objects once per worker."""
    # Ensure the PyAVD store is initialized once per worker process.
    _ensure_pyavd_store_initialized()

    if config.custom_templates:
        _ensure_ansible_plugins_initialized()


def get_avd_templar(config: FabricConfig) -> AVDTemplar | None:
    if not config.custom_templates:
        return None

    searchpath = [
        str(config.full_project_dir.joinpath("templates")),
        str(config.full_project_dir),
    ]
    dataloader = DataLoader()
    return AVDTemplar(
        templar=Templar(loader=dataloader),
        loader=dataloader,
        searchpath=searchpath,
        ansible_above_2_19=ANSIBLE_ABOVE_2_19,
    )


def dump_deprecations(deprecations: list[pyavd_utils.validation.Deprecation], config: FabricConfig, stage: str, device: str) -> None:
    error_dir = config.full_error_dir.joinpath(config.fabric_name)
    error_dir = error_dir.joinpath(device) if device else error_dir
    error_dir.mkdir(parents=True, exist_ok=True)
    err_lines = [f"[{deprecation.path}]: '{deprecation.message}'" for deprecation in deprecations]
    error_dir.joinpath(f"{stage}_deprecations.txt").write_text("\n".join(err_lines))


def dump_violations(violations: list[pyavd_utils.validation.Violation], config: FabricConfig, stage: str, device: str) -> None:
    error_dir = config.full_error_dir.joinpath(config.fabric_name)
    error_dir = error_dir.joinpath(device) if device else error_dir
    error_dir.mkdir(parents=True, exist_ok=True)
    err_lines = [f"[{violation.path}]: '{violation.message}'" for violation in violations]
    error_dir.joinpath(f"{stage}_violations.txt").write_text("\n".join(err_lines))


def dump_error(error: str, config: FabricConfig, stage: str, device: str | None = None) -> None:
    error_dir = config.full_error_dir.joinpath(config.fabric_name)
    error_dir = error_dir.joinpath(device) if device else error_dir
    error_dir.mkdir(parents=True, exist_ok=True)
    error_dir.joinpath(f"{stage}_error.txt").write_text(error)


def dump_exception(exc: Exception, config: FabricConfig, stage: str, device: str | None = None) -> None:
    error_dir = config.full_error_dir.joinpath(config.fabric_name)
    error_dir = error_dir.joinpath(device) if device else error_dir
    error_dir.mkdir(parents=True, exist_ok=True)
    err_lines = traceback.format_exception(exc) if config.dump_tracebacks else traceback.format_exception_only(exc)
    error_dir.joinpath(f"{stage}_error.txt").write_text("\n".join(err_lines))


@lru_cache(maxsize=1)
def _ensure_pyavd_store_initialized() -> None:
    """Initialize the PyAVD store once per process."""
    pyavd_init_store()


@lru_cache(maxsize=1)
def _ensure_ansible_plugins_initialized() -> None:
    """Initialize the Ansible plugins once per process."""
    init_plugin_loader()


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


def load_config_from_dict(dataclass_type: type[DataclassT], documentation_type: type[DataclassInstance], data: dict[str, typing.Any]) -> DataclassT:
    fields = dataclasses.fields(dataclass_type)
    config_keys = {field.name for field in fields}
    raw_config = {key: value for key, value in data.items() if key in config_keys}
    if raw_documentation := raw_config.get("documentation"):
        if not isinstance(raw_documentation, dict):
            msg = "Invalid config. 'documentation' must be a dict."
            raise TypeError(msg)
        doc_fields = dataclasses.fields(documentation_type)
        doc_config_keys = {field.name for field in doc_fields}
        raw_doc_config = {key: value for key, value in raw_documentation.items() if key in doc_config_keys}
        raw_config["documentation"] = documentation_type(**raw_doc_config)
    return dataclass_type(**raw_config)


def load_config(project_dir: pathlib.Path) -> Project:
    with project_dir.joinpath("e2e-test.toml").open("rb") as stream:
        raw_config = tomllib.load(stream)

    project_config = load_config_from_dict(ProjectConfig, ProjectDocumentationConfig, dict(raw_config, project_dir=project_dir))
    scenarios: list[Scenario] = []
    if "scenarios" not in raw_config:
        scenarios.append(Scenario(ScenarioConfig.from_project("default", project_config, ScenarioConfigOverrides()), fabric_overrides={}))
    elif not isinstance((raw_scenarios := raw_config["scenarios"]), dict):
        msg = "Invalid config. 'scenarios'' must be a dict."
        raise TypeError(msg)
    else:
        for scenario_name, raw_scenario in raw_scenarios.items():
            if not isinstance(raw_scenario, dict):
                msg = f"Invalid config for scenario '{scenario_name}'. Each entry in 'scenarios' must be a dict."
                raise TypeError(msg)
            scenario_overrides = load_config_from_dict(ScenarioConfigOverrides, DocumentationConfigOverrides, raw_scenario)
            fabric_overrides = {}
            if "fabrics" not in raw_scenario:
                pass
            elif not isinstance((raw_fabrics := raw_scenario["fabrics"]), dict):
                msg = f"Invalid config for scenario '{scenario_name}'. 'fabrics' must be a list."
                raise TypeError(msg)
            else:
                for fabric_name, raw_fabric in raw_fabrics.items():
                    if not isinstance(raw_fabric, dict):
                        msg = f"Invalid config for fabric '{fabric_name}' under scenario '{scenario_name}'. Each entry in 'fabrics' must be a dict."
                        raise TypeError(msg)
                    one_fabric_overrides = load_config_from_dict(FabricConfigOverrides, DocumentationConfigOverrides, raw_fabric)
                    fabric_overrides[fabric_name] = one_fabric_overrides
            scenarios.append(Scenario(config=ScenarioConfig.from_project(scenario_name, project_config, scenario_overrides), fabric_overrides=fabric_overrides))
    return Project(config=project_config, scenarios=scenarios)


def clean_dirs(configuration: ScenarioConfig | FabricConfig) -> None:
    """Delete directories recursively."""
    for directory in configuration.get_cleanup_dirs():
        if directory.exists():
            shutil.rmtree(directory)


def build(scenario: Scenario) -> None:
    """
    Build AVD for the given inventory path.

    Outputs are written to the output_dir relative to the inventory path.
    Captures errors for each stage and writes error files in the output path under the error path.
    """
    if scenario.config.clean:
        clean_dirs(scenario.config)

    build_context = AvdBuildContext(scenario.config)
    try:
        fabric_devices = group_devices_per_fabric(build_context)
        for fabric_name, devices in fabric_devices.items():
            print("Building fabric", fabric_name)
            fabric_overrides = scenario.fabric_overrides.get(fabric_name, FabricConfigOverrides())
            fabric_config = FabricConfig.from_scenario(fabric_name, scenario.config, fabric_overrides)

            if fabric_config.clean:
                clean_dirs(fabric_config)

            build = AvdV6Build(fabric_config, build_context, devices)
            try:
                validation_result = list(build.validation_stage())
                if not any(validation_result):
                    # All devices failed validation so skip the rest
                    continue

                if fabric_config.avd_design and not build.common_build_stage():
                    continue

                list(build.device_build_stage())

                if fabric_config.avd_design:
                    build.common_documentation_stage()
            finally:
                build.close()
    finally:
        build_context.close()


def get_git_repo(path: pathlib.Path) -> git.Repo:
    """
    Returns the auto-detectsed Git repository root starting from the given path.

    Raises if no repo was found.
    """
    # search_parent_directories=True walks up from subdir_path until it finds .git
    return git.Repo(path, search_parent_directories=True)


@dataclasses.dataclass
class Args:
    project_dirs: list[pathlib.Path]


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "projects",
        type=pathlib.Path,
        nargs="+",
        help="One or more paths to git projects containing e2e-test.toml files. Also accepts paths directly to 'e2e-test.toml' files.",
    )
    args = parser.parse_args()

    project_dirs: list[pathlib.Path] = []
    for arg_project in args.projects:
        project: pathlib.Path = arg_project.resolve()
        if not project.exists():
            msg = f"The given project path '{project}' does not exist."
            raise FileNotFoundError(msg)
        if project.is_dir():
            project_dir = project
            if not project_dir.joinpath("e2e-test.toml").exists():
                msg = f"The given project directory '{project}' does not contain a 'e2e-test.toml' file."
                raise FileNotFoundError(msg)
        elif project.is_file():
            if not project.parts[-1].endswith("e2e-test.toml"):
                msg = f"The given project file '{project}' must be named e2e-test.toml."
                raise ValueError(msg)
            project_dir = project.parent
        else:
            msg = f"Project '{project}' must be a path to a directory or an 'e2e-test.toml' file."
            raise ValueError(msg)

        repo = get_git_repo(project_dir)
        if not repo:
            msg = f"The project path '{project_dir}' must be inside a git repo."
            raise ValueError(msg)

        project_dirs.append(project_dir)

    return Args(project_dirs=project_dirs)


def main() -> int:
    args = parse_args()
    for project_dir in args.project_dirs:
        project = load_config(project_dir)

        print("#" * 20, "Project", project.config.project_dir, "#" * 20)

        org_cwd = pathlib.Path.cwd()

        # Change to project dir to ensure things like PoolManager can resolve relative paths while running the scenarios.
        os.chdir(project.config.full_project_dir)

        for scenario in project.scenarios:
            print("Running scenario", scenario.config.scenario_name)
            build(scenario)

        os.chdir(org_cwd)

    return 0


if __name__ == "__main__":
    sys.exit(main())
