# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re


def generate_route_target(esi_short: str | None) -> str | None:
    """
    generate_route_target transforms 3 octets ESI like 0303:0202:0101 to route-target

    Parameters
    ----------
    esi : str
        Short ESI value as per AVD definition in eos_designs

    Returns
    -------
    str:
        String based on route-target format like 03:03:02:02:01:01
    """
    if esi_short is None:
        return None
    delimiter = ":"
    esi = esi_short.replace(delimiter, "")
    esi_split = re.findall("..", esi)
    return delimiter.join(esi_split)
