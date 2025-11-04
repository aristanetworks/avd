# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Sequence


def as_path_list_match_from_bgp_asns(bgp_asns: Sequence[str]) -> str:
    """
    Create a match string for an EOS as-path access-list entry.

    For now this only escapes dots in case of dotted BGP ASN and joins them on underscore.
    """
    joined_bgp_asns = "_".join(bgp_asn.replace(".", "\\.") for bgp_asn in bgp_asns)
    # Enclosing `_`s are required for correct AS PATH matching when as-path ACL uses string regex mode
    return f"_{joined_bgp_asns}_"
