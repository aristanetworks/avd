# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from contextlib import nullcontext as does_not_raise

import pytest

from ansible_collections.arista.avd.plugins.filter.decrypt import decrypt
from ansible_collections.arista.avd.plugins.filter.encrypt import encrypt
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.password_utils.password import (
    bgp_decrypt,
    bgp_encrypt,
    ospf_message_digest_decrypt,
    ospf_message_digest_encrypt,
    ospf_simple_decrypt,
    ospf_simple_encrypt,
)

##########
# BGP
##########

BGP_INPUT_DICT_ENCRYPT_EXPECTED = [
    ("42.42.42.42", "arista", "3QGcqpU2YTwKh2jVQ4Vj/A=="),
    ("AVD-TEST", "arista", "bM7t58t04qSqLHAfZR/Szg=="),
]
# password used is "arista"
BGP_VALID_INPUT_DICT_DECRYPT_EXPECTED = [
    ("42.42.42.42", "3QGcqpU2YTwKh2jVQ4Vj/A==", "arista"),
    ("AVD-TEST", "bM7t58t04qSqLHAfZR/Szg==", "arista"),
]
BGP_INVALID_INPUT_DICT_DECRYPT = [
    ("10.42.42.43", "3QGcqpU2YTwKh2jVQ4Vj/A=="),
    ("AVD-TEST-DUMMY", "bM7t58t04qSqLHAfZR/Szg=="),
]
# The following list uses all the molecule BGP passwords available
# and the expected encryption
# The password is always arista123
BGP_MOLECULE_PASSWORDS_TEST = [
    ("UNDERLAY-PEERS", "arista123", "0nsCUm70mvSTxVO0ldytrg=="),
    ("UNDERLAY_PEERS", "arista123", "af6F4WLl4wUrWRZcwbEwkQ=="),
    ("123.1.1.10", "arista123", "oBztv71m2uhR7hh58/OCNA=="),
    ("123.1.1.11", "arista123", "oBztv71m2uhR7hh58/OCNA=="),
    ("MPLS-IBGP-PEERS", "arista123", "mWV4B6WpLCfOTyKATLWuBg=="),
    ("EVPN-OVERLAY-RS-PEERS", "arista123", "dRx9sULvl+hzkCMYJLEQCw=="),
    ("EVPN-OVERLAY", "arista123", "MY+KbyJy4kSu+X/blnVwsg=="),
    ("IPV4-UNDERLAY", "arista123", "dt5J2fw8tymeDFPyoYLB3w=="),
    ("IPV6-UNDERLAY", "arista123", "WkH9/oj4atEwv2MgOprY8A=="),
    ("IPV6-UNDERLAY-MLAG", "arista123", "CXS0NveSYzQRmm6SRGp42w=="),
    ("IPV4-UNDERLAY-MLAG", "arista123", "46jF9S9T7v5RRceVzhrlBg=="),
    ("MPLS-OVERLAY-PEERS", "arista123", "SHsTgDgjVUU5a9blyxSt3Q=="),
    ("192.168.48.1", "arista123", "toZKiUFLVUTU4hdS5V8F4Q=="),
    ("192.168.48.3", "arista123", "OajzUG59/YF0NkgvOQyRnQ=="),
    ("MLAG-PEERS", "arista123", "15AwQNBEJ1nyF/kBEtoAGw=="),
    ("OVERLAY-PEERS", "arista123", "64fqSH5CFUNLRHErezMrRg=="),
    ("RR-OVERLAY-PEERS", "arista123", "04FdfTXWrEfpDTUc3mlSjg=="),
    ("MLAG_PEER", "arista123", "arwUnrq9ydqIhjfTwRhAlg=="),
]


@pytest.mark.parametrize("key, password, expected", BGP_INPUT_DICT_ENCRYPT_EXPECTED)
def test_bgp_encrypt(key, password, expected):
    """
    Test bgp_encrypt
    """
    assert bgp_encrypt(password, key=key) == expected


@pytest.mark.parametrize("key, password,, expected", BGP_VALID_INPUT_DICT_DECRYPT_EXPECTED)
def test_bgp_decrypt_success(key, password, expected):
    """
    Test bgp_decrypt successful cases
    """
    assert bgp_decrypt(password, key=key) == expected


@pytest.mark.parametrize("key, password", BGP_INVALID_INPUT_DICT_DECRYPT)
def test_bgp_decrypt_failure(key, password):
    """
    Test bgp_decrypt failure cases
    """
    with pytest.raises(AristaAvdError):
        bgp_decrypt(password, key=key)


@pytest.mark.parametrize("key, password, expected", BGP_MOLECULE_PASSWORDS_TEST)
def test_molecule_bgp_encrypt(key, password, expected):
    """
    Test bgp_encrypt
    """
    assert bgp_encrypt(password, key=key) == expected


##########
# OSPF
##########
OSPF_INPUT_SIMPLE_DICT_ENCRYPT_EXPECTED = [
    ("Ethernet1", "arista", "qCTcuwOSntAmLZaW2QjKcA=="),
]
# password used is "arista"
OSPF_VALID_INPUT_SIMPLE_DICT_DECRYPT_EXPECTED = [
    ("Ethernet1", "qCTcuwOSntAmLZaW2QjKcA==", "arista"),
]
OSPF_INVALID_INPUT_SIMPLE_DICT_DECRYPT = [
    pytest.param("Ethernet1", "3QGcqpU2YTwKh2jVQ4Vj/A==", id="Wrong password simple auth"),
]
OSPF_INPUT_MD_DICT_ENCRYPT_EXPECTED = [
    ("Ethernet1", "arista", "md5", 42, "aPW9RqfXquTBASVDMYxSJw=="),
    ("Ethernet1", "arista", "sha512", 66, "tDvJjUyf8///ktvy/xpfeQ=="),
]
# password used is "arista"
OSPF_VALID_INPUT_MD_DICT_DECRYPT_EXPECTED = [
    ("Ethernet1", "aPW9RqfXquTBASVDMYxSJw==", "md5", 42, "arista"),
    ("Ethernet1", "tDvJjUyf8///ktvy/xpfeQ==", "sha512", 66, "arista"),
]
OSPF_INVALID_INPUT_MD_DICT_DECRYPT = [
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", "sha512", 42, id="Wrong password message digest key"),
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", "sha512", None, id="Missing key id"),
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", None, 42, id="Missing hash_algorithm"),
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", "sha666", 42, id="Wrong hash_algorithm"),
]
# The following list uses all the molecule OSPF passwords available
# and the expected encryption
# The password is always arista123
# TODO
# OSPF_MOLECULE_PASSWORDS_TEST = []


@pytest.mark.parametrize("key, password, expected", OSPF_INPUT_SIMPLE_DICT_ENCRYPT_EXPECTED)
def test_ospf_simple_encrypt(key, password, expected):
    """
    Test ospf_simple_encrypt
    """
    assert ospf_simple_encrypt(password, key=key) == expected


@pytest.mark.parametrize("key, password, expected", OSPF_VALID_INPUT_SIMPLE_DICT_DECRYPT_EXPECTED)
def test_ospf_simple_decrypt_success(key, password, expected):
    """
    Test ospf_simple_decrypt successful cases
    """
    assert ospf_simple_decrypt(password, key=key) == expected


@pytest.mark.parametrize("key, password", OSPF_INVALID_INPUT_SIMPLE_DICT_DECRYPT)
def test_ospf_simple_decrypt_failure(key, password):
    """
    Test ospf_simple_decrypt failure cases
    """
    with pytest.raises(AristaAvdError):
        ospf_simple_decrypt(password, key=key)


@pytest.mark.parametrize("key, password, hash_algorithm, key_id, expected", OSPF_INPUT_MD_DICT_ENCRYPT_EXPECTED)
def test_ospf_message_digest_encrypt(key, password, expected, hash_algorithm, key_id):
    """
    Test ospf_message_digest_encrypt
    """
    assert ospf_message_digest_encrypt(password, key=key, hash_algorithm=hash_algorithm, key_id=key_id) == expected


@pytest.mark.parametrize("key, password, hash_algorithm, key_id, expected", OSPF_VALID_INPUT_MD_DICT_DECRYPT_EXPECTED)
def test_ospf_message_digest_decrypt_success(key, password, hash_algorithm, key_id, expected):
    """
    Test ospf_message_digest_decrypt successful cases
    """
    assert ospf_message_digest_decrypt(password, key=key, hash_algorithm=hash_algorithm, key_id=key_id) == expected


@pytest.mark.parametrize("key, password, hash_algorithm, key_id", OSPF_INVALID_INPUT_MD_DICT_DECRYPT)
def test_ospf_message_digest_decrypt_failure(key, password, hash_algorithm, key_id):
    """
    Test ospf_message_digest_decrypt failure cases
    """
    with pytest.raises(AristaAvdError):
        ospf_message_digest_decrypt(password, key=key, hash_algorithm=hash_algorithm, key_id=key_id)


##########
# GENERIC
##########
@pytest.mark.parametrize(
    "password, passwd_type, key, kwargs, expected_raise",
    [
        pytest.param("dummy", None, "dummy", {}, pytest.raises(AristaAvdMissingVariableError), id="Missing Type"),
        pytest.param("dummy", "eigrp", "dummy", {}, pytest.raises(AristaAvdError), id="Wrong Type"),
        pytest.param(42, "bgp", "42.42.42.42", {}, does_not_raise(), id="Password is not a string"),
        pytest.param("arista", "bgp", "42.42.42.42", {}, does_not_raise(), id="Implemented Type BPG"),
        pytest.param("arista", "ospf_simple", "Ethernet1", {}, does_not_raise(), id="Implemented Type OSPF simple"),
        pytest.param("arista", "ospf_message_digest", "Ethernet1", {"hash_algorithm": "sha512", "key_id": 66}, does_not_raise(), id="Implemented Type OSPF MD"),
    ],
)
def test_encrypt(password, passwd_type, key, kwargs, expected_raise):
    """
    Test encrypt method for non existing and existing type
    """
    with expected_raise:
        encrypt(password, passwd_type=passwd_type, key=key, **kwargs)


@pytest.mark.parametrize(
    "password, passwd_type, key, kwargs, expected_raise",
    [
        pytest.param("dummy", None, "dummy", {}, pytest.raises(AristaAvdMissingVariableError), id="Missing Type"),
        pytest.param("dummy", "eigrp", "dummy", {}, pytest.raises(AristaAvdError), id="Wrong Type"),
        pytest.param("3QGcqpU2YTwKh2jVQ4Vj/A==", "bgp", "42.42.42.42", {}, does_not_raise(), id="Implemented Type BGP"),
        pytest.param("qCTcuwOSntAmLZaW2QjKcA==", "ospf_simple", "Ethernet1", {}, does_not_raise(), id="Implemented Type OSPF simple"),
        pytest.param(
            "tDvJjUyf8///ktvy/xpfeQ==",
            "ospf_message_digest",
            "Ethernet1",
            {"hash_algorithm": "sha512", "key_id": 66},
            does_not_raise(),
            id="Implemented Type OSPF MD",
        ),
    ],
)
def test_decrypt(password, passwd_type, key, kwargs, expected_raise):
    """
    Test decrypt method for non existing and existing type
    """
    with expected_raise:
        decrypt(password, passwd_type=passwd_type, key=key, **kwargs)
