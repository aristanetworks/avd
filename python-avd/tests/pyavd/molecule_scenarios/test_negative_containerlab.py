# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re
import sys
from copy import deepcopy
from unittest.mock import patch

import pytest

from pyavd import get_fabric_documentation
from pyavd._errors import AristaAvdError
from tests.models import MoleculeScenario


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
