# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# arista.avd.hide_passwords filter
#
from ..errors import AristaAvdError


def hide_passwords(value: str, hide_passwords: bool = False) -> str:
    if not isinstance(hide_passwords, bool):
        raise AristaAvdError(f"{hide_passwords} in hide_passwords filter is not of type bool")
    return "<removed>" if hide_passwords else value
