# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from asyncio import run
from json import loads
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import NoAliasDumper
from ansible_collections.arista.avd.roles.eos_validate_state.python_modules.constants import ACRONYM_CATEGORIES, AVD_TEST_CLASSES

from .ansible_eos_device import AnsibleEOSDevice
from .catalog import Catalog

if TYPE_CHECKING:
    from ansible.plugins.connection import ConnectionBase
    from yaml import Dumper

try:
    from anta.inventory import AntaInventory
    from anta.loader import setup_logging
    from anta.result_manager import ResultManager, TestResult
    from anta.runner import main as anta_runner

    HAS_ANTA = True
except ImportError:
    HAS_ANTA = False


LOGGER = logging.getLogger(__name__)


def _get_skipped_tests_from_tags(run_tags: list, skip_tags: tuple) -> list[dict]:
    """
    Arguments:
      run_tags (list): List of run_tags used to run the playbook.
      skip_tags (tuple): Tuple of skip_tags used to run the playbook.

    Returns:
      result (list[dict]): List of dictionary containing the categories to skip
    """
    result = []
    for cls, cls_info in AVD_TEST_CLASSES.items():
        class_legacy_tags = set(cls_info["legacy_ansible_tags"])

        if "never" in class_legacy_tags:
            other_tags = class_legacy_tags - {"never"}
            if not other_tags.intersection(set(run_tags)):
                result.append({"category": cls.__name__})
                continue

        if class_legacy_tags.intersection(set(skip_tags)):
            result.append({"category": cls.__name__})
            continue

        if run_tags and not class_legacy_tags.intersection(set(run_tags)):
            result.append({"category": cls.__name__})

    return result


def get_anta_results(
    device_name: str,
    hostvars: dict,
    connection: ConnectionBase,
    logging_level: str,
    skipped_tests: dict,
    ansible_tags: dict | None = None,
    save_catalog_name: str | None = None,
    dry_run: bool = False,
    yaml_dumper: Dumper | None = NoAliasDumper,
) -> dict:
    """
    Args:
      device_name (str): The current device name for which the plugin is being run
      hostvars (dict): A dictionnary that contains a key for each device with a value of the structured_config
                   when using Ansible, this is the equivalent of `task_vars['hostvars']`
      connection (Connection): The connection to the device
                               when using Ansible, this is the `self._connection` of the module
      logging_level (str): The level at which ANTA should be logging
      skipped_tests (list[dict]): A list of dictionary
      ansible_tags (dict): An optional dictionary containing the tags to maintain legacy filtering behavior for
                           `eos_validate_state`. This is ignored is `skipped_tests` is set.
      save_catalog_name (bool): When set, the generated catalog is saved to a file using this name.
      dry_run (boolean): if True, no test is actually run, useful in conjunction with save_catalog_name.
      yaml_dumper (Dumper): Dumper to use to dump Anta Catalog, default is NoAliasDumper to avoid anchors.
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
        run_tags = ansible_tags.get("ansible_run_tags", [])
        # Retrieve the skip_tags
        skip_tags = ansible_tags.get("ansible_skip_tags", [])
        # Update the skipped_ variable according to legacy tags
        skipped_tests = _get_skipped_tests_from_tags(run_tags, skip_tags)

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
        # Create the ANTA device object with the HttpApi connection session
        device = AnsibleEOSDevice(name=device_name, connection=connection)
        # Create the ANTA Inventory object and add the AnsibleEOSDevice device to it
        inventory = AntaInventory()
        inventory.add_device(device)

        # Run
        run(anta_runner(manager, inventory, catalog.tests))

    # Save the results
    results = loads(manager.get_results(output_format="json"))

    # Format the data properly for the eos_validate_state report
    for item in results:
        categories_list = []
        for category in item["categories"]:
            category_list = [word.upper() if word.lower() in ACRONYM_CATEGORIES else word.title() for word in category.split()]
            categories_list.append(" ".join(category_list))
        item["categories"] = ", ".join(categories_list)

        # Need to remove `,` for the CSV dump
        item["messages"] = "\n".join(item["messages"]).replace(",", "-")

    return results


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
