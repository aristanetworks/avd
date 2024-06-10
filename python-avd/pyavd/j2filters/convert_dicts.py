# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import os


def convert_dicts(dictionary: dict | list, primary_key: str = "name", secondary_key: str | None = None) -> list:
    """
    The `arista.avd.convert_dicts` filter will convert a dictionary containing nested dictionaries to a list of
    dictionaries. It inserts the outer dictionary keys into each list item using the primary_key `name` (key name is
    configurable) and if there is a non-dictionary value,it inserts this value to
    secondary key (key name is configurable), if secondary key is provided.

    This filter is intended for:

    - Seamless data model migration from dictionaries to lists.
    - Improve processing performance when dealing with large dictionaries by converting them to lists of dictionaries.

    Note: If there is a non-dictionary value with no secondary key provided, it will pass through untouched

    To use this filter:

    ```jinja
    {# convert list of dictionary with default `name:` as the primary key and None secondary key #}
    {% set example_list = example_dictionary | arista.avd.convert_dicts %}
    {% for example_item in example_list %}
    item primary key is {{ example_item.name }}
    {% endfor %}

    {# convert list of dictionary with `id:` set as the primary key and `types:` set as the secondary key #}
    {% set example_list = example_dictionary | arista.avd.convert_dicts('id','types') %}
    {% for example_item in example_list %}
    item primary key is {{ example_item.id }}
    item secondary key is {{ example_item.types }}
    {% endfor %}
    ```

    Parameters
    ----------
    dictionary : any
        Nested Dictionary to convert - returned untouched if not a nested dictionary and list
    primary_key : str, optional
        Name of primary key used when inserting outer dictionary keys into items.
    secondary_key : str, optional
        Name of secondary key used when inserting dictionary values which are list into items.

    Returns
    -------
    any
        Returns list of dictionaries or input variable untouched if not a nested dictionary/list.
    """
    if not isinstance(dictionary, (dict, list)) or os.environ.get("AVD_DISABLE_CONVERT_DICTS"):
        # Not a dictionary/list, return the original
        return dictionary
    if isinstance(dictionary, list):
        output = []
        for element in dictionary:
            if not isinstance(element, dict):
                output.append({primary_key: element})
            elif primary_key not in element and secondary_key is not None:
                # if element of nested dictionary is a dictionary but primary key is missing, insert primary and secondary keys.
                for key in element:
                    output.append(
                        {
                            primary_key: key,
                            secondary_key: element[key],
                        }
                    )
            else:
                output.append(element)
        return output
    # This is now a dict
    output = []
    for key in dictionary:
        if secondary_key is not None:
            # Add secondary key for the values if secondary key is provided
            output.append(
                {
                    primary_key: key,
                    secondary_key: dictionary[key],
                }
            )
        else:
            if not isinstance(dictionary[key], dict):
                # Not a nested dictionary
                output.append({primary_key: key})
            else:
                # Nested dictionary
                output.append(
                    {
                        primary_key: key,
                        **dictionary[key],
                    }
                )
    return output
