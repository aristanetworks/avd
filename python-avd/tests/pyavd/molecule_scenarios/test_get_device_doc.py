# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd import get_device_doc, validate_structured_config
from pyavd._utils import get
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
def test_get_device_doc(molecule_host: MoleculeHost) -> None:
    """Test get_device_config."""
    # For eos_designs scenarios, only load structured config, so this will fail if any inputs are not covered by eos_designs schemas.
    structured_config = molecule_host.hostvars if molecule_host.scenario.name.startswith("eos_cli_config_gen") else molecule_host.structured_config

    if not get(structured_config, "eos_cli_config_gen_documentation.enable", default=True):
        return

    validated_data_result = validate_structured_config(structured_config)
    assert validated_data_result.validated_data is not None
    structured_config = validated_data_result.validated_data

    expected_doc = molecule_host.doc
    add_md_toc = get(structured_config, "eos_cli_config_gen_documentation.toc", default=True)
    device_doc = get_device_doc(structured_config, add_md_toc=add_md_toc)

    assert isinstance(device_doc, str)
    assert device_doc == expected_doc
