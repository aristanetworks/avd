from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.filter.bgp_encrypt import FilterModule, _parse_input, bgp_encrypt, bgp_decrypt
from ansible_collections.arista.avd.plugins.plugin_utils.utils import AristaAvdError, AristaAvdMissingVariableError

# NOTE: for now not testing anything with use_base64 False as this should not bew widely used

INCOMPLETE_DICT = [{"key": "only-key"}, {"password": "only-password"}, {"dummy": "only-other"}]
INPUT_DICT_ENCRYPT_EXPECTED = [
    ({"key": "42.42.42.42", "password": "arista"}, "3QGcqpU2YTwKh2jVQ4Vj/A=="),
    ({"key": "AVD-TEST", "password": "arista"}, "bM7t58t04qSqLHAfZR/Szg=="),
]
# password used is "arista"
VALID_INPUT_DICT_DECRYPT_EXPECTED = [
    ({"key": "42.42.42.42", "password": "3QGcqpU2YTwKh2jVQ4Vj/A=="}, "arista"),
    ({"key": "AVD-TEST", "password": "bM7t58t04qSqLHAfZR/Szg=="}, "arista"),
]
INVALID_INPUT_DICT_DECRYPT = [
    {"key": "10.42.42.43", "password": "3QGcqpU2YTwKh2jVQ4Vj/A=="},
    {"key": "AVD-TEST-DUMMY", "passwowrd": "bM7t58t04qSqLHAfZR/Szg=="},
]


f = FilterModule()


@pytest.mark.parametrize("input_dict", INCOMPLETE_DICT)
def test__parse_input_missing_arg(input_dict):
    """
    Missing values - expect AristaAvdMissingVariableError
    """
    with pytest.raises(AristaAvdMissingVariableError):
        _parse_input(input_dict)


@pytest.mark.parametrize("input_dict, expected", INPUT_DICT_ENCRYPT_EXPECTED)
def test__parse_input_correct_args(input_dict, expected):
    """
    Test that _parse_input returns the expected values
    """
    expected_key = bytes(f"{input_dict['key']}_passwd", encoding="utf-8")
    expected_password = bytes(input_dict["password"], encoding="utf-8")
    assert _parse_input(input_dict) == (expected_key, expected_password, True)
    input_dict["use_base64"] = False
    assert _parse_input(input_dict) == (expected_key, expected_password, False)


@pytest.mark.parametrize("input_dict, expected", INPUT_DICT_ENCRYPT_EXPECTED)
def test_bgp_encrypt(input_dict, expected):
    """
    Test bgp_encrypt
    """
    print(bgp_encrypt(input_dict))
    print(expected)
    assert bgp_encrypt(input_dict) == expected


@pytest.mark.parametrize("input_dict, expected", VALID_INPUT_DICT_DECRYPT_EXPECTED)
def test_bgp_decrypt_success(input_dict, expected):
    """
    Test bgp_decrypt successful cases
    """
    assert bgp_decrypt(input_dict) == expected


@pytest.mark.parametrize("input_dict", INVALID_INPUT_DICT_DECRYPT)
def test_bgp_decrypt_failure(input_dict):
    """
    Test bgp_decrypt failure cases
    """
    with pytest.raises(AristaAvdError):
        bgp_decrypt(input_dict)


def test_bgp_encrypt_module():
    """
    Assert:
      * bgp_encrypt
      * bgp_decrypt
    filters are part of the module
    """
    resp = f.filters()
    assert isinstance(resp, dict)
    assert "bgp_encrypt" in resp.keys()
    assert "bgp_decrypt" in resp.keys()
