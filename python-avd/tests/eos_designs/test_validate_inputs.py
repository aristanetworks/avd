# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import validate_inputs


def test_validate_inputs_with_valid_inputs(hostname: str, all_inputs: dict):
    """
    Test validate_inputs
    """
    inputs = all_inputs[hostname]
    validation_result = validate_inputs(inputs)
    assert hostname and validation_result.validation_errors == []
    assert hostname and validation_result.failed is False
