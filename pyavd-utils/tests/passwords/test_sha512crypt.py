# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise

import pytest

from pyavd_utils.passwords import sha512_crypt

SHA512_CRYPT_TEST_DATA = [
    pytest.param(
        "arista",
        "1234567890ABCDEF",
        "$6$1234567890ABCDEF$5h/.K2RuwSPqXTncNaqmw./4HduYZNE4RHDfivjrQ8nrYX3AcB8gKSsKFC1VSVOl3E46/QFZ85uHZWhxQGTeS0",
        does_not_raise(),
        id="Valid hash with salt",
    ),
    pytest.param(
        "arista",
        "",
        "",
        pytest.raises(ValueError, match=r"Invalid Salt: Salt cannot be empty."),
        id="Empty salt",
    ),
    pytest.param(
        "arista",
        "🐍",
        "",
        pytest.raises(ValueError, match="Invalid Salt: Salt contains an invalid character"),
        id="Invalid character in salt",
    ),
]


@pytest.mark.parametrize(("password", "salt", "expected_hash", "expected_raise"), SHA512_CRYPT_TEST_DATA)
def test_sha512_crypt(password: str, salt: str, expected_hash: str, expected_raise: AbstractContextManager[None]) -> None:
    """Test sha512_crypt function."""
    with expected_raise:
        assert sha512_crypt(password, salt) == expected_hash
