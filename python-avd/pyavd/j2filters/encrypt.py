# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pyavd._utils.password_utils import METHODS_DIR


def encrypt(value, passwd_type=None, key=None, **kwargs) -> str:
    """
    Umbrella function to execute the correct encrypt method based on the input type
    """
    if not passwd_type:
        raise TypeError("type keyword must be present to use this test")
    try:
        encrypt_method = METHODS_DIR[passwd_type][0]
    except KeyError as exc:
        raise KeyError(f"Type {passwd_type} is not supported for the encrypt filter") from exc
    return encrypt_method(str(value), key=key, **kwargs)
