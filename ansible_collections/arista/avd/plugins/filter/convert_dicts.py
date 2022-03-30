#
# def arista.avd.convert_dicts
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import os


def convert_dicts(dictionary, primary_key="name"):
    """
    The `arista.avd.convert_dicts` filter will convert a dictionary containing nested dictionaries to a list of dictionaries
    and insert the outer dictionary keys into each list item using the primary_key `name` (key name is configurable).

    This filter is intended for:

    - Seemless data model migration from dictionaries to lists.
    - Improve Ansible's processing performance when dealing with large dictionaries by converting them to lists of dictionaries.

    Note: If the variable is already a list, it will pass through untouched

    To use this filter:

    ```jinja
    {# convert list of dictionary with default `name:` as the primary key #}
    {% set example_list = example_dictionary | arista.avd.convert_dicts %}
    {% for example_item in example_list %}
    item primary key is {{ example_item.name }}
    {% endfor %}

    {# convert list of dictionary with `id:` set as the primary key #}
    {% set example_list = example_dictionary | arista.avd.convert_dicts('id') %}
    {% for example_item in example_list %}
    item primary key is {{ example_item.id }}
    {% endfor %}
    ```

    Parameters
    ----------
    dictionary : any
        Nested Dictionary to convert - returned untouched if not a nested dictionary
    primary_key : str, optional
        Name of primary key used when inserting outer dictionary keys into items.

    Returns
    -------
    any
        Returns list of dictionaries or input variable untouched if not a nested dictionary
    """
    if not isinstance(dictionary, dict) or os.environ.get('AVD_DISABLE_CONVERT_DICTS'):
        # Not a dictionary, return the original
        return dictionary
    else:
        output = []
        for key in dictionary:
            if dictionary[key] is None:
                # Catch cornercase where dictionary has no value because of old data models
                output.append({primary_key: key})
            elif not isinstance(dictionary[key], dict):
                # Not a nested dictionary, return the original
                return dictionary
            else:
                item = dictionary[key]
                item.update({primary_key: key})
                output.append(item)
        return output


class FilterModule(object):
    def filters(self):
        return {
            'convert_dicts': convert_dicts,
        }
