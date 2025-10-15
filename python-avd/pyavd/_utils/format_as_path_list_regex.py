# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
def format_as_path_list_regex(regex: str) -> str:
    """
    Format the given regex for an as-path access-list to conform to the regex rules.

    For now this only escapes dots in case of dotted BGP ASN.
    """
    return regex.replace(".", "\\.")
