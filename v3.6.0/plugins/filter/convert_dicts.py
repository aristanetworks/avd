#
# def arista.avd.convert_dicts
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import os


def convert_dicts(dictionary, primary_key="name", secondary_key=None):
    """
    The `arista.avd.convert_dicts` filter will convert a dictionary containing nested dictionaries to a list of
    dictionaries. It inserts the outer dictionary keys into each list item using the primary_key `name` (key name is
    configurable) and if there is a non-dictionary value,it inserts this value to
    secondary key (key name is configurable), if secondary key is provided.

    This filter is intended for:

    - Seemless data model migration from dictionaries to lists.
    - Improve Ansible's processing performance when dealing with large dictionaries by converting them to lists of dictionaries.

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
    if not isinstance(dictionary, (dict, list)) or os.environ.get('AVD_DISABLE_CONVERT_DICTS'):
        # Not a dictionary/list, return the original
        return dictionary
    elif isinstance(dictionary, list):
        output = []
        for element in dictionary:
            if not isinstance(element, dict):
                item = {}
                item.update({primary_key: element})
                output.append(item)
            else:
                output.append(element)
        return output
    else:
        output = []
        for key in dictionary:
            if not isinstance(dictionary[key], dict):
                # Not a nested dictionary, add secondary key for the values if secondary key is provided
                if secondary_key is not None:
                    item = {}
                    item.update({primary_key: key})
                    item.update({secondary_key: dictionary[key]})
                    output.append(item)
                else:
                    # Catch cornercase where dictionary value is not a dict because of old data models
                    # Ex <key>: "none" or <key>: null or <key>: "" will all be overwritten with {<primary_key>: <key>}
                    output.append({primary_key: key})
            else:
                item = dictionary[key].copy()
                item.update({primary_key: key})
                output.append(item)
        return output


class FilterModule(object):
    def filters(self):
        return {
            'convert_dicts': convert_dicts,
        }
