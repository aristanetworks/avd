# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# arista.avd.is_in_filter filter
#
def is_in_filter(self, hostname, hostname_filter):
    if hostname_filter is None:
        hostname_filter = ["all"]
    if "all" in hostname_filter:
        return True
    elif any(element in hostname for element in hostname_filter):
        return True
    return False
