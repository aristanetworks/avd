# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re
import sys
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from pyavd import get_avd_facts, get_device_structured_config, get_fabric_documentation, validate_inputs
from pyavd._eos_designs.structured_config.metadata.digital_twin import DigitalTwinMixin
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
        expected_error_message = re.sub(r" for host '[a-zA-Z0-9-_]+'.", "", host_inputs["expected_error_message"])
        validation_data_result = validate_inputs(host_inputs)
        if expected_error_message.endswith(" found during schema validation of input variables."):
            assert validation_data_result.validated_data is None
            assert len(validation_data_result.validation_result.violations) == int(expected_error_message.split(" ", maxsplit=1)[0])
        else:
            with pytest.raises(AristaAvdError, match=re.escape(expected_error_message)):
                _ = get_avd_facts(fabric_inputs, pool_manager=molecule_scenario.pool_manager)
    else:
        _is_digital_twin_host = molecule_host.hostvars.get("avd_digital_twin_mode", False)
        # Run get_avd_facts with no errors
        avd_facts = get_avd_facts(fabric_inputs, pool_manager=molecule_scenario.pool_manager, digital_twin=_is_digital_twin_host)
        # Run get_device_structured_config excepting an error to be raised.
        with pytest.raises(Exception, match=re.escape(host_inputs["expected_error_message"])):
            _ = get_device_structured_config(molecule_host.name, host_inputs, avd_facts, digital_twin=_is_digital_twin_host)


@pytest.mark.molecule_scenarios("digital_twin_containerlab_negative_tests")
def test_negative_containerlab_fabric_documentation(molecule_scenario: MoleculeScenario) -> None:
    """Test get_fabric_documentation errors for invalid Containerlab Digital Twin inputs."""
    tested_fabrics = set()

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        for molecule_host in molecule_scenario.hosts:
            fabric_name = molecule_host.hostvars["fabric_name"]
            if fabric_name in tested_fabrics:
                continue
            tested_fabrics.add(fabric_name)

            fabric_hosts = molecule_host.hostvars["groups"][fabric_name]
            fabric_inputs = {host.name: host for host in molecule_scenario.hosts if host.name in fabric_hosts}
            molecule_structured_configs = {host.name: deepcopy(host.structured_config) for host in fabric_inputs.values()}
            for structured_config in molecule_structured_configs.values():
                structured_config.setdefault("metadata", {}).setdefault("digital_twin", {})["environment"] = "containerlab"
            molecule_avd_facts = {host.name: molecule_scenario.avd_facts[host.name] for host in fabric_inputs.values()}

            with pytest.raises(AristaAvdError, match=re.escape(molecule_host.hostvars["expected_error_message"])) as exc_info:
                get_fabric_documentation(
                    avd_facts=molecule_avd_facts,
                    structured_configs=molecule_structured_configs,
                    fabric_name=fabric_name,
                    fabric_documentation=False,
                    topology_csv=False,
                    p2p_links_csv=False,
                    digital_twin=True,
                )

            for expected_mgmt_subnet in molecule_host.hostvars.get("expected_mgmt_subnets", []):
                assert expected_mgmt_subnet in str(exc_info.value)


def test_set_digital_twin_containerlab_and_unsupported_environment() -> None:
    """Test metadata Digital Twin match handling for cLab and unsupported environments."""
    digital_twin_metadata = MagicMock()
    structured_config = SimpleNamespace(metadata=SimpleNamespace(digital_twin=digital_twin_metadata))

    DigitalTwinMixin._set_digital_twin(
        SimpleNamespace(
            inputs=SimpleNamespace(digital_twin=SimpleNamespace(environment="containerlab")),
            structured_config=structured_config,
        )
    )

    digital_twin_metadata._update.assert_called_once_with(environment="containerlab")
    digital_twin_metadata.reset_mock()

    DigitalTwinMixin._set_digital_twin(
        SimpleNamespace(
            inputs=SimpleNamespace(digital_twin=SimpleNamespace(environment="unsupported")),
            structured_config=structured_config,
        )
    )

    digital_twin_metadata._update.assert_not_called()
