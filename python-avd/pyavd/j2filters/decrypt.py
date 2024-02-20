# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ..errors import AristaAvdError, AristaAvdMissingVariableError
from ..utils.password import METHODS_DIR


def decrypt(value, passwd_type=None, key=None, **kwargs) -> str:
    """
    Umbrella function to execute the correct decrypt method based on the input type
    """
    if not passwd_type:
        raise AristaAvdMissingVariableError("type keyword must be present to use this test")
    try:
        decrypt_method = METHODS_DIR[passwd_type][1]
    except KeyError as exc:
        raise AristaAvdError(f"Type {passwd_type} is not supported for the decrypt filter") from exc
    return decrypt_method(str(value), key=key, **kwargs)
