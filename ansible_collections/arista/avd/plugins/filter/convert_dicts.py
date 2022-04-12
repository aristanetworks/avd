#
# def arista.avd.convert_dicts
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import os


def convert_dicts(dictionary, primary_key="name", secondary_key="items"):
    """
    The `arista.avd.convert_dicts` filter will convert a dictionary containing nested dictionaries to a list of
    dictionaries It inserts the outer dictionary keys into each list item using the primary_key `name` (key name is
    configurable) and if there is a list of dictionary in the dictionary value,it inserts this value list to
    secondary key "items" (key name is configurable).

    This filter is intended for:

    - Seemless data model migration from dictionaries to lists.
    - Improve Ansible's processing performance when dealing with large dictionaries by converting them to lists of dictionaries.

    Note: If the variable is a list of string/integer, it will pass through untouched

    To use this filter:

    ```jinja
    {# convert list of dictionary with default `name:` as the primary key and `items:` as secondary key #}
    {% set example_list = example_dictionary | arista.avd.convert_dicts %}
    {% for example_item in example_list %}
    item primary key is {{ example_item.name }}
    item secondary key is {{ example_item.items }}
    {% endfor %}

    {# convert list of dictionary with `id:` set as the primary key and `types:` set as the secondary key #}
    {% set example_list = example_dictionary | arista.avd.convert_dicts('id') %}
    {% for example_item in example_list %}
    item primary key is {{ example_item.id }}
    item secondary key is {{ example_item.types }}
    {% endfor %}
    ```

    Parameters
    ----------
    dictionary : any
        Nested Dictionary to convert - returned untouched if not a nested dictionary
    primary_key : str, optional
        Name of primary key used when inserting outer dictionary keys into items.
    secondary_key : str, optional
        Name of secondary key used when inserting dictionary values which are list of dictionaries into items.

    Returns
    -------
    any
        Returns list of dictionaries or input variable untouched if not a nested dictionary/list of dictionaries
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
                if isinstance(dictionary[key], list):
                    # Not a nested dictionary but a list of dictionaries, add secondary key for the list
                    item = {}
                    secondary_element = []
                    item.update({primary_key: key})
                    for element in dictionary[key]:
                        secondary_element.append(element)
                    item.update({secondary_key: secondary_element})
                    output.append(item)
                else:
                    # Not a nested dictionary but a string, return the original
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
