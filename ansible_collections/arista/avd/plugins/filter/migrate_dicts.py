#
# def arista.avd.migrate_dicts
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined


def migrate_dicts(dictionary, primary_key="name"):
    """
    migrate_dicts will convert dictionary to list.

    Arista.avd.migrate_dicts will convert nested dictionaries to list of dictionaries
    and insert the outer dictionary keys into each list item using the primary_key name.

    This filter is intended for seemless data model migration.
    If variable is already converted to list, it will pass through untouched

    Example
    -------
    {# Migrate access_lists data model from dict to list #}
    {% set access_lists = access_lists | arista.avd.migrate_dicts %}
    {% for access_list in access_lists %}
    {#     Migrate access-lists.sequence_numbers data model from dict to list #}
    {%     do access_lists[loop.index0].update({'sequence_numbers': access_list.sequence_numbers | arista.avd.migrate_dicts('sequence')}) %}
    {% endfor %}
    access_lists: {{ access_lists }}

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
        output = list()
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
            'migrate_dicts': migrate_dicts,
        }
