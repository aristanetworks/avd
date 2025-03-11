# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re
from copy import deepcopy

import pytest

from pyavd import get_avd_facts, get_device_structured_config, validate_inputs
from pyavd._errors import AristaAvdError
from tests.models import MoleculeHost, MoleculeScenario


@pytest.mark.molecule_scenarios(
    "eos_designs_negative_unit_tests",
)
def test_negative_eos_designs(molecule_scenario: MoleculeScenario, molecule_host: MoleculeHost) -> None:
    """
    For each device run get_avd_facts for the subset of devices given by fabric_name and run get_device_structured_config for one device.

    If the device is part of the group EOS_DESIGNS_FACTS_FAILURES we will assert an error during get_avd_facts.
    Otherwise we will assert an error during get_device_structured_config.
    """
    fabric_name = molecule_host.hostvars["fabric_name"]
    fabric_hosts = molecule_host.hostvars["groups"][fabric_name]
    fabric_inputs = {host.name: deepcopy(host.hostvars) for host in molecule_scenario.hosts if host.name in fabric_hosts}
    host_inputs = fabric_inputs[molecule_host.name]

    if molecule_host.name in host_inputs["groups"].get("EOS_DESIGNS_FAILURES_EXCLUDED"):
        return

    if molecule_host.name in host_inputs["groups"].get("EOS_DESIGNS_FACTS_FAILURES"):
        # Run get_avd_facts and expecting an error to be raised.
        # Patching the expected error message since the suffix is added by the ansible action plugin which we are not using here...
        expected_error_message = re.sub(r" for host '[a-zA-Z1-9-_]+'.", "", host_inputs["expected_error_message"])
        validation_result = validate_inputs(host_inputs)
        if expected_error_message.endswith(" errors found during schema validation of input vars."):
            assert validation_result.failed
            assert len(validation_result.validation_errors) == int(expected_error_message.split(" ", maxsplit=1)[0])
        else:
            with pytest.raises(AristaAvdError, match=re.escape(expected_error_message)):
                _ = get_avd_facts(fabric_inputs, pool_manager=molecule_scenario.pool_manager)
    else:
        # Run get_avd_facts with no errors
        avd_facts = get_avd_facts(fabric_inputs, pool_manager=molecule_scenario.pool_manager)
        # Run get_device_structured_config excepting an error to be raised.
        with pytest.raises(Exception, match=re.escape(host_inputs["expected_error_message"])):
            _ = get_device_structured_config(molecule_host.name, host_inputs, avd_facts)
