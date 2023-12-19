# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from asyncio import run
from json import loads
from typing import TYPE_CHECKING, Mapping

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import NoAliasDumper
from ansible_collections.arista.avd.roles.eos_validate_state.python_modules.constants import AVD_TEST_CLASSES

from .catalog import Catalog

if TYPE_CHECKING:
    from anta.device import AntaDevice
    from yaml import Dumper

try:
    from anta.inventory import AntaInventory
    from anta.loader import setup_logging
    from anta.result_manager import ResultManager
    from anta.result_manager.models import TestResult
    from anta.runner import main as anta_runner

    HAS_ANTA = True
except ImportError:
    HAS_ANTA = False


LOGGER = logging.getLogger(__name__)


def _get_skipped_tests_from_tags(run_tags: tuple, skip_tags: tuple) -> list[dict]:
    """
    Arguments:
      run_tags (tuple): Tuple of run_tags used to run the playbook.
      skip_tags (tuple): Tuple of skip_tags used to run the playbook.

    Returns:
      result (list[dict]): List of dictionary containing the categories to skip
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


def get_anta_results(
    anta_device: AntaDevice,
    hostvars: Mapping,
    logging_level: str,
    skipped_tests: list[dict],
    ansible_tags: dict | None = None,
    save_catalog_name: str | None = None,
    dry_run: bool = False,
    yaml_dumper: Dumper | None = NoAliasDumper,
) -> list[dict]:
    """
    Args:
      anta_device (AntaDevice): An instantiated AntaDevice
                                When running in ansible, the action plugin will pass an AnsibleEOSDevice
      hostvars (Mapping): A mapping that contains a key for each device with a value of the structured_config.
                                When using Ansible, this is the `task_vars['hostvars']` object.
      logging_level (str): The level at which ANTA should be logging
      skipped_tests (list[dict]): A list of dictionary
      ansible_tags (dict): An optional dictionary containing the tags to maintain legacy filtering behavior for
                           `eos_validate_state`. This is ignored is `skipped_tests` is set.
      save_catalog_name (str): When set, the generated catalog is saved to a file using this name.
      dry_run (boolean): if True, no test is actually run, useful in conjunction with save_catalog_name.
      yaml_dumper (Dumper): Dumper to use to dump Anta Catalog, default is NoAliasDumper to avoid anchors.


    TODO when moving to pyavd: Make the anta_device optional and use ANTA default AntaDevice class
    """
    if not HAS_ANTA:
        raise AristaAvdError("AVD could not import the required 'anta' Python library")

    # Setup ANTA logging
    setup_logging(level=logging_level)

    if skipped_tests:
        LOGGER.warning("The variable 'skipped_tests' has been set. Ansible tags are ignored for filtering tests.")
    # Backward compatibility with eos_validate_state Ansible tags
    elif ansible_tags:
        # Retrieve the run_tags
        run_tags = ansible_tags.get("ansible_run_tags", ())
        # Retrieve the skip_tags
        skip_tags = ansible_tags.get("ansible_skip_tags", ())
        # Update the skipped_ variable according to legacy tags
        skipped_tests = _get_skipped_tests_from_tags(run_tags, skip_tags)

    device_name = anta_device.name
    # Create the ANTA catalog object with the appropriate skipped tests if any
    catalog = Catalog(device_name, hostvars, skipped_tests=skipped_tests)

    if save_catalog_name is not None:
        catalog.dump_to_file(save_catalog_name, yaml_dumper)

    # Create the ANTA ResultManager object
    manager = ResultManager()

    if dry_run:
        LOGGER.info("DRY-RUN - generating empty results")
        _create_dry_run_report(device_name, catalog.tests, manager)
    else:
        # Create the ANTA Inventory object and add the single AntaDevice device to it
        inventory = AntaInventory()
        inventory.add_device(anta_device)

        # Run
        # Go around a bug in ANTA:
        if not len(catalog.tests):
            LOGGER.warning("Test catalog is empty!")
        else:
            run(anta_runner(manager, inventory, catalog.tests))

    # Save the results
    results: list[dict] = loads(manager.get_results(output_format="json"))

    # Return sorted results
    return sorted(
        results,
        key=lambda result: (
            result.get("categories", [""])[0].lower(),
            result.get("description", "").lower(),
            result.get("custom_field", "").lower(),
        ),
    )


def _create_dry_run_report(device_name: str, tests: list[tuple], manager: ResultManager) -> None:
    """
    When dry_run is True in get_anta_results. this function is used to go through all the tests
    in the catalog and create a TestResult object and append it to the ResultManager

    Args:
        device_name (str): The device_name that should be associated with the TestResult Object
        tests (list[tuple]): As returned by the parse_catalog function from Anta
        manager (ResultManager): The result manager object

    """
    for test_class, test_params in tests:
        # Ovewriting default if needed by looking in the params
        # This is done in ANTA when actually instantiating the AntaTest but needs
        # to be done manually here
        result_overwrite = test_params.get("result_overwrite", {})
        description = result_overwrite.get("description", test_class.description)
        categories = result_overwrite.get("categories", test_class.categories)
        custom_field = result_overwrite.get("custom_field", None)

        manager.add_test_result(TestResult(name=device_name, test=test_class.name, categories=categories, description=description, custom_field=custom_field))
