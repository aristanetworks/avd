from pyavd import validate_inputs


def test_validate_inputs_with_valid_inputs(hostname: str, all_inputs: dict):
    """
    Test validate_inputs
    """
    inputs = all_inputs[hostname]
    validation_result = validate_inputs(inputs)
    assert hostname and validation_result.validation_errors == []
    assert hostname and validation_result.failed is False
