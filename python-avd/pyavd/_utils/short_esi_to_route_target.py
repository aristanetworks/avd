# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re

MATCH_PATTERN = re.compile(r"(\n{2})(\n{2}):(\n{2})(\n{2}):(\n{2})(\n{2})")
REPLACE_PATTERN = re.compile(r"\1:\2:\3:\4:\5:\6")


def short_esi_to_route_target(short_esi: str) -> str:
    return re.sub(MATCH_PATTERN, REPLACE_PATTERN, short_esi)
