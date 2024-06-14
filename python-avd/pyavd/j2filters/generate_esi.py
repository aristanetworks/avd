# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
def generate_esi(short_esi: str, esi_prefix: str = "0000:0000:") -> str:
    """
    Transforms short_esi to EVPN ESI format.
    0303:0202:0101 (short_esi) -> 0000:0000:0303:0202:0101 (EVPN ESI).

    Args:
        esi_short: Short ESI value as per AVD definition in eos_designs
        esi_prefix: ESI prefix value, will be concatenated with the `short_esi`
    Returns:
        Concatenated string of `esi_prefix` and `short_esi` like `0000:0000:0303:0202:0101`

    """
    return esi_prefix + short_esi
