#
# def arista.avd.convert_dicts
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined


def convert_dicts(dictionary, primary_key="name"):
    """
    convert_dicts will convert dictionary to list.

    The `arista.avd.convert_dicts` filter will convert nested dictionaries to lists of dictionaries
    and insert the outer dictionary keys into each list item using the primary_key `name`.

    This filter is intended for:

    - Seemless data model migration from dictionaries to lists.
    - Improve Ansible's processing performance when dealing with large dictionaries by converting them to lists of dictionaries.

    Note: If the variable is already a list, it will pass through untouched

    To use this filter:

    ```jinja
    {# convert list of dictionnary with default `name:` as the primary key #}
    {% for example_list in example_lists | arista.avd.convert_dicts %}
    {{ example_list }}
    {% endfor %}
    {# convert list of dictionnary with `id:` set as the primary key #}
    {% for example_list in example_lists | arista.avd.convert_dicts('id') %}
    {{ example_list }}
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
    if not isinstance(dictionary, dict):
        # Not a dictionary, return the original
        return dictionary
    else:
        output = []
        for key in dictionary.keys():
            if not isinstance(dictionary[key], dict):
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
