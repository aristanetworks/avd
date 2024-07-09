# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


def generate_lacp_id(esi_short: str) -> str:
    """
    Transforms short_esi `0303:0202:0101` to LACP ID format `0303.0202.0101`

    Args:
        esi_short (str): Short ESI value as per AVD definition in eos_designs
    Returns:
        str: LACP ID

    """
    return esi_short.replace(":", ".")
