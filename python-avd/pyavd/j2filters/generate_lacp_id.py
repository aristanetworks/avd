# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
def generate_lacp_id(esi_short):
    return esi_short.replace(":", ".")
