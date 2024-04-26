# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Dummy. Not needed for pyavd, but is imported in __init__.py
"""


def template(*args) -> str:
    raise NotImplementedError("Jinja Templating is not implemented in pyavd")
