# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError


def get_all(data, path: str, required: bool = False, org_path=None):
    """
    Get all values from data matching a data path.

    Path supports dot-notation like "foo.bar" to do deeper lookups. Lists will be unpacked recursively.
    Returns an empty list if the path is not found and required is False.

    Parameters
    ----------
    data : any
        Data to walk through
    path : str
        Data Path - supporting dot-notation for nested dictionaries/lists
    required : bool
        Fail if the path is not found
    org_path : str
        Internal variable used for raising exception with the full path even when called recursively

    Returns
    -------
    list [ any ]
        List of values matching data path or empty list if no matches are found.

    Raises
    ------
    AristaAvdMissingVariableError
        If the path is not found and required == True
    """

    if org_path is None:
        org_path = path

    path_elements = str(path).split(".")
    if isinstance(data, list):
        output = []
        for data_item in data:
            output.extend(get_all(data_item, path, required=required, org_path=org_path))

        return output

    elif isinstance(data, dict):
        value = data.get(path_elements[0])

        if value is None:
            if required:
                raise AristaAvdMissingVariableError(org_path)

            return []

        if len(path_elements) > 1:
            return get_all(value, ".".join(path_elements[1:]), required=required, org_path=org_path)

        else:
            return [value]

    return []
