# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from natsort import os_sorted


def natural_sort(item_to_natural_sort):
    return os_sorted(item_to_natural_sort)
