# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# list_compress filter
#
from itertools import count, groupby

from ..errors import AristaAvdError


def list_compress(list_to_compress):
    if not isinstance(list_to_compress, list):
        raise AristaAvdError(f"value must be of type list, got {type(list_to_compress)}")
    G = (list(x) for y, x in groupby(sorted(list_to_compress), lambda x, c=count(): next(c) - x))
    return ",".join("-".join(map(str, (g[0], g[-1])[: len(g)])) for g in G)
