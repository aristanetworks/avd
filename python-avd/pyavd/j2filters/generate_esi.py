# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
def generate_esi(esi_short, esi_prefix="0000:0000:"):
    return esi_prefix + esi_short
