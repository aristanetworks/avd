# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.password_utils.password_utils import cbc_check_password, cbc_decrypt, cbc_encrypt

# password used is "arista"
VALID_PASSWORD_KEY_PAIRS = [("42.42.42.42", b"3QGcqpU2YTwKh2jVQ4Vj/A=="), ("AVD-TEST", b"bM7t58t04qSqLHAfZR/Szg==")]
INVALID_PASSWORD_KEY_PAIRS = [("10.42.42.43", b"3QGcqpU2YTwKh2jVQ4Vj/A=="), ("AVD-TEST-DUMMY", b"bM7t58t04qSqLHAfZR/Szg==")]


@pytest.mark.parametrize("key, expected", VALID_PASSWORD_KEY_PAIRS)
def test_cbc_encrypt(key, expected):
    """
    Valid cases for both neighbor IP and peer group name
    """
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_encrypt(augmented_key, b"arista") == expected


@pytest.mark.parametrize("key, password", VALID_PASSWORD_KEY_PAIRS)
def test_cbc_decrypt(key, password):
    """
    Valid cases for both neighbor IP and peer group name
    """
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_decrypt(augmented_key, password) == b"arista"


@pytest.mark.parametrize(
    "key, password, expected_raise",
    [
        pytest.param("TOTO", b"3QGcqpU2YTwKh2jVQ4Vj/A==", ValueError, id="ValueError"),
    ],
)
def test_cbc_decrypt_failure(key, password, expected_raise):
    """
    Valid cases for both neighbor IP and peer group name
    """
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    with pytest.raises(expected_raise):
        cbc_decrypt(augmented_key, password)


@pytest.mark.parametrize("key, password", VALID_PASSWORD_KEY_PAIRS)
def test_cbc_check_password_success(key, password):
    """
    Valid cases for both neighbor IP and peer group name
    """
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_check_password(augmented_key, password) is True


@pytest.mark.parametrize("key, password", INVALID_PASSWORD_KEY_PAIRS)
def test_cbc_check_password_invalid_values(key, password):
    """
    Invalid cases for both neighbor IP and peer group name
    """
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_check_password(augmented_key, password) is False
