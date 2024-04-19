# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from asyncio import run
from typing import TYPE_CHECKING

from yaml import CSafeLoader, YAMLError, dump, load

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge_catalogs
from ansible_collections.arista.avd.plugins.plugin_utils.utils import NoAliasDumper, get_item
from ansible_collections.arista.avd.roles.eos_validate_state.python_modules.constants import AVD_TEST_CLASSES

if TYPE_CHECKING:
    from pathlib import Path

    from anta.catalog import RawCatalogInput
    from anta.device import AntaDevice
    from yaml import Dumper

    from .avdtestbase import AvdTestBase
    from .config_manager import ConfigManager

try:
    from anta.catalog import AntaCatalog
    from anta.inventory import AntaInventory
    from anta.logger import setup_logging
    from anta.result_manager import ResultManager
    from anta.result_manager.models import TestResult
    from anta.runner import main as anta_runner

    HAS_ANTA = True
except ImportError:
    HAS_ANTA = False

LOGGER = logging.getLogger(__name__)


def get_anta_results(
    anta_device: AntaDevice,
    config_manager: ConfigManager,
    logging_level: str,
    skipped_tests: list[dict],
    ansible_tags: dict | None = None,
    save_catalog_name: Path | None = None,
    custom_anta_catalogs: list[Path] | None = None,
    yaml_dumper: Dumper | None = NoAliasDumper,
    *,
    dry_run: bool = False,
) -> list[dict]:
    """Get the ANTA results for a given device.

    Args:
    ----
      anta_device (AntaDevice): An instantiated AntaDevice.
                                When running in Ansible, the action plugin will pass an AnsibleEOSDevice instance.
      config_manager (ConfigManager): The device ConfigManager object containing data to be used by the tests.
      logging_level (str): The level at which ANTA should be logging.
      skipped_tests (list[dict]): A list of dictionary containing the categories and/or tests to skip.
      ansible_tags (dict): An optional dictionary containing the tags to maintain legacy filtering behavior for
                           `eos_validate_state`. This is ignored if `skipped_tests` is set.
      save_catalog_name (str): When set, the generated catalog is saved to a file using this name.
      custom_anta_catalogs (list[Path]): An optional list of custom ANTA catalog files to merge with the generated catalog.
      yaml_dumper (Dumper): Dumper to use to dump the ANTA catalog. Default is NoAliasDumper to avoid anchors.
      dry_run (bool): If True, no test is actually run. Useful in conjunction with `save_catalog_name`.

    Returns:
    -------
      results (list[dict]): A list of dictionary containing the ANTA results for the device.

    TODO: When moving to pyavd: Make anta_device optional and use ANTA default AntaDevice class.
    """
    if not HAS_ANTA:
        raise AristaAvdError(message="AVD could not import the required 'anta' Python library")

    # Setup ANTA logging
    setup_logging(level=logging_level)

    if skipped_tests:
        LOGGER.warning("The variable 'skipped_tests' has been set. Ansible tags are ignored for filtering tests.")
    # Backward compatibility with legacy eos_validate_state Ansible tags
    elif ansible_tags:
        run_tags = ansible_tags.get("ansible_run_tags", ())
        skip_tags = ansible_tags.get("ansible_skip_tags", ())
        # Update the skipped_tests variable according to Ansible tags
        skipped_tests = get_skipped_tests_from_tags(run_tags, skip_tags)

    device_name = anta_device.name

    # Load and merge the custom catalogs for the device if any
    custom_catalog = load_custom_catalogs(custom_anta_catalogs) if custom_anta_catalogs else None

    # Create the ANTA Catalog object with the appropriate skipped tests if any
    tests = generate_tests(config_manager, skipped_tests, custom_catalog)
    anta_catalog = AntaCatalog.from_dict(data=tests) if tests else AntaCatalog()

    if save_catalog_name is not None:
        dump_to_file(tests, save_catalog_name, yaml_dumper)

    # Create the ANTA ResultManager object to store results
    manager = ResultManager()

    if dry_run:
        LOGGER.info("DRY RUN - Generating empty results")
        create_dry_run_report(device_name, anta_catalog, manager)
    else:
        # Create the ANTA Inventory object and add the single AntaDevice device to it
        inventory = AntaInventory()
        inventory.add_device(anta_device)

        # Run ANTA
        run(anta_runner(manager, inventory, anta_catalog)) if len(anta_catalog.tests) > 0 else LOGGER.warning("Test catalog is empty!")

    # Convert the ANTA TestResult models to dictionaries, excluding default values
    results = [result.model_dump(exclude_defaults=True) for result in manager.results]

    # Return sorted results
    return sorted(
        results,
        key=lambda result: (
            result.get("categories", [""])[0].lower(),
            result.get("test", "").lower(),
            result.get("custom_field", "").lower(),
        ),
    )


def load_custom_catalogs(catalog_files: list[Path]) -> dict:
    """Load the custom ANTA catalogs from the provided files and merge them together.

    Args:
    ----
      catalog_files (list[Path]): List of Path objects pointing to the custom ANTA catalog files.

    Returns:
    -------
      dict: The merged custom ANTA catalog.
    """
    catalog_list = []
    for file in catalog_files:
        try:
            with file.open("r", encoding="UTF-8") as fd:
                catalog = load(fd, Loader=CSafeLoader)
                catalog_list.append(catalog)
        except (OSError, YAMLError) as error:
            msg = f"Failed to load the custom ANTA catalog from {file}: {error!s}"
            raise AristaAvdError(msg) from error

    return merge_catalogs(*catalog_list) if catalog_list else {}


def dump_to_file(tests: dict, filename: Path, yaml_dumper: Dumper = NoAliasDumper) -> None:
    """Dump the generated tests to a YAML file.

    Args:
    ----
        tests (dict): The tests to dump.
        filename (Path): The file where the tests should be saved.
        yaml_dumper (Dumper): An optional custom YAML Dumper, default is NoAliasDumper.
    """
    with filename.open("w", encoding="UTF-8") as fd:
        dump(tests, fd, Dumper=yaml_dumper)


def get_skipped_tests_from_tags(run_tags: tuple, skip_tags: tuple) -> list[dict]:
    """Get the list of AVD test categories to skip from the Ansible tags.

    Args:
    ----
      run_tags (tuple): Tuple of run_tags used to run the playbook.
      skip_tags (tuple): Tuple of skip_tags used to run the playbook.

    Returns:
    -------
      result (list[dict]): List of dictionary containing the categories to skip.
    """
    result = []
    for cls, cls_info in AVD_TEST_CLASSES.items():
        class_legacy_tags = set(cls_info.get("legacy_ansible_tags", {}))

        if run_tags and "never" in class_legacy_tags:
            other_tags = class_legacy_tags - {"never"}
            if not other_tags.intersection(set(run_tags)):
                result.append({"category": cls.__name__})
                continue

        if class_legacy_tags.intersection(set(skip_tags)):
            result.append({"category": cls.__name__})
            continue

        if run_tags and run_tags != ("all",) and not class_legacy_tags.intersection(set(run_tags)):
            result.append({"category": cls.__name__})

    return result


def generate_tests(config_manager: ConfigManager, skipped_tests: list[dict], custom_catalog: dict | None = None) -> RawCatalogInput:
    """Create the test catalog in a dictionary format generated from the AVD test classes.

    Test definitions are generated from the AVD structured_config for each AVD test classes and are merged together
    with an optional custom_catalog to create the final catalog.

    Tests can be skipped from the catalog depending on `skipped_tests`.

    Args:
    ----
        config_manager (ConfigManager): The device ConfigManager object containing data to be used by the tests.
        skipped_tests (list[dict]): A list of dictionary containing the categories and/or tests to skip.
        custom_catalog (dict): An optional custom catalog to merge with the generated catalog.

    Returns:
    -------
        RawCatalogInput: The catalog containing all tests generated from AVD_TEST_CLASSES.
                          This output is used as an input to the AntaCatalog object creation.
    """
    catalog = {}

    for avd_test_class in AVD_TEST_CLASSES:
        # Check if the whole class is to be skipped
        class_skip_config = get_item(skipped_tests, "category", avd_test_class.__name__)
        if class_skip_config is not None and not class_skip_config.get("tests"):
            msg = f"Skipping all tests of {avd_test_class.__name__} per the `skipped_tests` input variable."
            LOGGER.info(msg)
            continue

        # Initialize the test class
        eos_validate_state_module: AvdTestBase = avd_test_class(config_manager)
        generated_tests = eos_validate_state_module.render()

        # Remove the individual tests that are to be skipped
        if class_skip_config is not None and (avd_test_class_skipped_tests := class_skip_config.get("tests")) is not None:
            msg = f"Skipping the following tests of {avd_test_class.__name__} per the `skipped_tests` input variable: "
            msg += ", ".join(avd_test_class_skipped_tests)
            LOGGER.info(msg)
            for anta_tests in generated_tests.values():
                anta_tests[:] = [test for test in anta_tests if next(iter(test.keys())) not in avd_test_class_skipped_tests]

        catalog = merge_catalogs(catalog, generated_tests)

    # Return the merged generated catalog with the custom catalog if any
    return merge_catalogs(catalog, custom_catalog) if custom_catalog else catalog


def create_dry_run_report(device_name: str, catalog: AntaCatalog, manager: ResultManager) -> None:
    """Create a dry run report.

    When dry_run is True in get_anta_results, this function is used to go through all the tests
    in the catalog and create a TestResult object to add to the ResultManager.

    Args:
    ----
        device_name (str): The device_name that should be associated with the TestResult object.
        catalog (AntaCatalog): The ANTA Catalog object containing all the tests.
        manager (ResultManager): The ANTA Result Manager object to store the TestResult objects.

    """
    for test_definition in catalog.tests:
        # Manually overwriting the default values of the TestResult object if needed
        res_ow = test_definition.inputs.result_overwrite
        categories = res_ow.categories if res_ow and res_ow.categories else test_definition.test.categories
        description = res_ow.description if res_ow and res_ow.description else test_definition.test.description
        custom_field = res_ow.custom_field if res_ow else None

        manager.add(
            TestResult(
                name=device_name,
                test=test_definition.test.name,
                categories=categories,
                description=description,
                custom_field=custom_field,
            )
        )
