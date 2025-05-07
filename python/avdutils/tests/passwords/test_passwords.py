# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from avdutils.passwords import sha512_crypt

SHA512_CRYPT_TEST_DATA = [
    pytest.param(
        "arista",
        "1234567890ABCDEF",
        "$6$1234567890ABCDEF$5h/.K2RuwSPqXTncNaqmw./4HduYZNE4RHDfivjrQ8nrYX3AcB8gKSsKFC1VSVOl3E46/QFZ85uHZWhxQGTeS0",
        id="Valid hash with Salt",
    )
]


@pytest.mark.parametrize(("password", "salt", "expected_hash"), SHA512_CRYPT_TEST_DATA)
def test_sha512_crypt(password: str, salt: str, expected_hash: str) -> None:
    """Test sha512_crypt function."""
    assert sha512_crypt(password, salt) == expected_hash
