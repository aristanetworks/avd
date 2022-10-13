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
# The following list uses all the molecule BGP passwords available
# and the expected encryption
# The password is always arista123
MOLECULE_PASSWORDS_TEST = [
    ({"key": "UNDERLAY-PEERS", "password": "arista123"}, "0nsCUm70mvSTxVO0ldytrg=="),
    ({"key": "UNDERLAY_PEERS", "password": "arista123"}, "af6F4WLl4wUrWRZcwbEwkQ=="),
    ({"key": "123.1.1.10", "password": "arista123"}, "oBztv71m2uhR7hh58/OCNA=="),
    ({"key": "123.1.1.11", "password": "arista123"}, "oBztv71m2uhR7hh58/OCNA=="),
    ({"key": "MPLS-IBGP-PEERS", "password": "arista123"}, "mWV4B6WpLCfOTyKATLWuBg=="),
    ({"key": "EVPN-OVERLAY-RS-PEERS", "password": "arista123"}, "dRx9sULvl+hzkCMYJLEQCw=="),
    ({"key": "EVPN-OVERLAY", "password": "arista123"}, "MY+KbyJy4kSu+X/blnVwsg=="),
    ({"key": "IPV4-UNDERLAY", "password": "arista123"}, "dt5J2fw8tymeDFPyoYLB3w=="),
    ({"key": "IPV6-UNDERLAY", "password": "arista123"}, "WkH9/oj4atEwv2MgOprY8A=="),
    ({"key": "IPV6-UNDERLAY-MLAG", "password": "arista123"}, "CXS0NveSYzQRmm6SRGp42w=="),
    ({"key": "IPV4-UNDERLAY-MLAG", "password": "arista123"}, "46jF9S9T7v5RRceVzhrlBg=="),
    ({"key": "MPLS-OVERLAY-PEERS", "password": "arista123"}, "SHsTgDgjVUU5a9blyxSt3Q=="),
    ({"key": "192.168.48.1", "password": "arista123"}, "toZKiUFLVUTU4hdS5V8F4Q=="),
    ({"key": "192.168.48.3", "password": "arista123"}, "OajzUG59/YF0NkgvOQyRnQ=="),
    ({"key": "MLAG-PEERS", "password": "arista123"}, "15AwQNBEJ1nyF/kBEtoAGw=="),
    ({"key": "OVERLAY-PEERS", "password": "arista123"}, "64fqSH5CFUNLRHErezMrRg=="),
    ({"key": "RR-OVERLAY-PEERS", "password": "arista123"}, "04FdfTXWrEfpDTUc3mlSjg=="),
    ({"key": "MLAG_PEER", "password": "arista123"}, "arwUnrq9ydqIhjfTwRhAlg=="),
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


@pytest.mark.parametrize("input_dict, expected", MOLECULE_PASSWORDS_TEST)
def test_molucule_bgp_encrypt(input_dict, expected):
    """
    Test bgp_encrypt
    """
    assert bgp_encrypt(input_dict) == expected
