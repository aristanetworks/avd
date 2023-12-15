# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Mapping

from yaml import Dumper, dump, safe_load

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import NoAliasDumper, get_item
from ansible_collections.arista.avd.roles.eos_validate_state.python_modules.constants import AVD_TEST_CLASSES

try:
    from anta.loader import parse_catalog

    HAS_ANTA = True
except ImportError:
    HAS_ANTA = False

try:
    from deepmerge import always_merger

    HAS_DEEPMERGE = True
except ImportError:
    HAS_DEEPMERGE = False

if TYPE_CHECKING:
    from .avdtestbase import AvdTestBase


class Catalog:
    """
    Catalog class that handles management of ANTA catalogs from AVD.
    """

    def __init__(
        self, device_name: str, hostvars: Mapping, skipped_tests: list[dict], custom_catalog: dict | None = None, custom_catalog_path: str | None = None
    ):
        """
        Initialize the Catalog class.

        For now it generates a catalog specific to a given device

        Args:
            device_name (str): The device for which this catalog is built
            hostvars (Mapping): A mapping that contains a key for each device with a value of the structured_config.
                                      When using Ansible, this is the `task_vars['hostvars']` object.
            skipped_tests (list[dict]): Dictionary of AVD test classes to be skipped.
            custom_catalog (dict): An optional dictionary representing an ANTA Catalog
            custom_catalog_path (str): An optional string representing a path to an Anta Catalog
        """
        if not HAS_ANTA:
            raise AristaAvdError("AVD could not import the required 'anta' Python library")
        if not HAS_DEEPMERGE:
            raise AristaAvdError("AVD could not import the required 'deepmerge' Python library")

        self.device_name = device_name
        self.hostvars = hostvars
        self.skipped_tests = skipped_tests

        self.tests = parse_catalog(self._input_catalog(custom_catalog, custom_catalog_path) or self._default_catalog())

    def _input_catalog(self, custom_catalog, custom_catalog_path) -> dict:
        """
        NOTE: This feature is currently not availbale from the calling Ansible module eos_validate_state_runner
        NOTE: No validation for now
        NOTE: Does not handle skipped tests

        Get the input catalog from the input value.  The logic is as follow:

        * if custom_catalog is provided, it is used
        * elif custom_catalog_path is provided, it is opened and used

        Returns:
            dict: The input catalog based on input vars or an empty dict if none provided.

        Raises:
            AristaAvdError: Will raise an error if the input catalog cannot be loaded or is empty.

        """
        if custom_catalog is not None:
            if not isinstance(custom_catalog, dict):
                raise AristaAvdError("The provided custom_catalog is not a dictionary.")
            return custom_catalog

        elif custom_catalog_path is not None:
            try:
                with open(custom_catalog_path, "r", encoding="UTF-8") as file:
                    input_catalog = safe_load(file) or {}
            except Exception as error:
                raise AristaAvdError(f"Exception raised while processing file {custom_catalog_path}. Details: {str(error)}") from error

            return input_catalog

        return {}

    def _default_catalog(self) -> dict:
        """
        Create the default catalog based on the AVD test classes.

        Test definitions are generated from the AVD structured_config for each AVD test classes and are merged together to create the final default catalog.

        Tests can be skipped from the default catalog depending on the self.skipped_tests attribute.

        Returns:
            dict: The default catalog generated from AVD_TEST_CLASSES.
        """
        default_catalog = {}

        for avd_test_class in AVD_TEST_CLASSES:
            # Check if the whole class is to be skipped
            class_skip_config = get_item(self.skipped_tests, "category", avd_test_class.__name__)
            if class_skip_config is not None and not class_skip_config.get("tests"):
                continue

            # Initialize the test class
            eos_validate_state_module: AvdTestBase = avd_test_class(device_name=self.device_name, hostvars=self.hostvars)
            generated_tests = eos_validate_state_module.render()

            # Remove the individual tests that are to be skipped
            if class_skip_config is not None and (avd_test_class_skipped_tests := class_skip_config.get("tests")) is not None:
                for anta_tests in generated_tests.values():
                    anta_tests[:] = [test for test in anta_tests if list(test.keys())[0] not in avd_test_class_skipped_tests]

            default_catalog = self.merge_catalogs(default_catalog, generated_tests)

        return default_catalog

    @staticmethod
    def merge_catalogs(*args: dict) -> dict:
        """
        Utility function to merge catalogs according to the ANTA catalog structure.

        Args:
            *args (dict): Catalogs to merge.

        Returns:
            dict: The merged catalog.
        """
        merged_catalog = {}
        for catalog in args:
            always_merger.merge(merged_catalog, catalog)

        return merged_catalog

    def dump_to_file(self, filename: str, yaml_dumper: Dumper = NoAliasDumper) -> None:
        """
        Dump the catalog to a file, filename using the YAML dumper yaml_dumper.

        Args:
            filename (str): The file where the catalog should be saved
            yaml_dumper (Dumper): An optional custom YAML Dumper, default is NoAliasDumper
        """
        dumpable = {}
        for test_class, test_params in self.tests:
            dumpable.setdefault(test_class.__module__, []).append({test_class.name: test_params})
        with open(filename, "w", encoding="UTF-8") as fd:
            dump(dumpable, fd, Dumper=yaml_dumper)
