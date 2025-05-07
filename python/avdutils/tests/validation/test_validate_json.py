# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
from pathlib import Path
from typing import cast

import pytest

from avdutils.validation import Issue, Violation, init_store_from_fragments, validate_json


@pytest.fixture
def init_store() -> None:
    org_path = sys.path
    # Insert /python-avd into the python path to be able to import constants from schema_tools.
    mocked_path = [str(Path(__file__).parents[4] / "python-avd"), *org_path]
    sys.path = mocked_path
    from schema_tools.constants import SCHEMAS

    init_store_from_fragments(
        eos_cli_config_gen=cast("Path", SCHEMAS["eos_cli_config_gen"].fragments_dir),
        eos_designs=cast("Path", SCHEMAS["eos_designs"].fragments_dir),
    )
    sys.path = org_path


@pytest.mark.usefixtures("init_store")
def test_validate_json() -> None:
    feedback_list = validate_json('{"ethernet_interfaces": [{"name": "Ethernet1"}, {"name": "Ethernet1"}, {}]}', "eos_cli_config_gen")
    feedback_iter = iter(feedback_list)
    feedback = next(feedback_iter)
    assert feedback.path == ["ethernet_interfaces", "2"]
    assert isinstance(feedback.issue, Issue.Validation)
    assert isinstance(feedback.issue._0, Violation.MissingRequiredKey)
    assert feedback.issue._0.key == "name"
    feedback = next(feedback_iter)
    assert feedback.path == ["ethernet_interfaces", "0", "name"]
    assert isinstance(feedback.issue, Issue.Validation)
    assert isinstance(feedback.issue._0, Violation.ValueNotUnique)
    assert feedback.issue._0.other_path == ["ethernet_interfaces", "1", "name"]
    feedback = next(feedback_iter)
    assert feedback.path == ["ethernet_interfaces", "1", "name"]
    assert isinstance(feedback.issue, Issue.Validation)
    assert isinstance(feedback.issue._0, Violation.ValueNotUnique)
    assert feedback.issue._0.other_path == ["ethernet_interfaces", "0", "name"]

    """
    Preparing for updated code where we emit default value inserted.
    # feedback = next(feedback_iter)
    # assert feedback.path == ["avd_data_validation_mode"]
    # assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    # feedback = next(feedback_iter)
    # assert feedback.path == ["config_end"]
    # assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    # feedback = next(feedback_iter)
    # assert feedback.path == ["generate_default_config"]
    # assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    # feedback = next(feedback_iter)
    # assert feedback.path == ["generate_device_documentation"]
    # assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    # feedback = next(feedback_iter)
    # assert feedback.path == ["is_deployed"]
    # assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    # feedback = next(feedback_iter)
    # assert feedback.path == ["transceiver_qsfp_default_mode_4x10"]
    # assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    """
