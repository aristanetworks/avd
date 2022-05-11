#
# def arista.avd.combine
#
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from collections.abc import (MutableMapping, MutableSequence)


def merge_hash(x, y, recursive=True, list_merge='replace', primary_key='name'):
    """
    Return a new dictionary result of the merges of y into x
    """
    if list_merge != 'update_on_key':
        raise Exception(
            "merge_hash: 'list_merge' argument can only be equal to 'update_on_key'")

    # to speed things up: if x is empty or equal to y, return y
    # (this `if` can be removed without impact on the function
    #  except performance)
    if x == {} or x == y:
        return y.copy()

    # we don't want to modify y, so we create a copy of it
    y = y.copy()

    # Even though the merge is y into x, we use y as basis to get y_value for different value types.
    for key, x_value in x.items():
        # Add missing keys.
        if key not in y:
            y[key] = x_value
            continue

        y_value = y[key]

        # Skip key if x is equal to y
        if x_value == y_value:
            continue

        # Values are dictionaries
        if isinstance(x_value, MutableMapping) and isinstance(y_value, MutableMapping):
            if recursive:
                y[key] = merge_hash(x_value, y_value, recursive, list_merge, primary_key)
            continue

        # Values are lists
        if isinstance(x_value, MutableSequence) and isinstance(y_value, MutableSequence):
            # Update on primary key or fallback to append
            if list_merge == 'update_on_key':
                # To avoid reordering the original elements from x_value,
                # we have to update a copy of x_value as the basis for the result.
                x_value_copy = x_value.copy()

                for y_element in y_value:
                    found_y_in_x = False
                    for x_index, x_element in enumerate(x_value):
                        # Continue to the next y_element if x_element is equal to y_element
                        if x_element == y_element:
                            found_y_in_x = True
                            break
                        # Values are dictionaries
                        if isinstance(y_element, MutableMapping) and isinstance(x_element, MutableMapping):
                            if (
                                (primary_key in x_element and primary_key in y_element)
                                and (x_element[primary_key] == y_element[primary_key])
                            ):
                                if recursive:
                                    y_element = merge_hash(x_element, y_element, recursive,
                                                           list_merge, primary_key)
                                x_value_copy[x_index] = y_element
                                # Found and handled the maching key. Go to the next y_key
                                found_y_in_x = True
                                break

                    if not found_y_in_x:
                        x_value_copy.append(y_element)

                y[key] = x_value_copy

    return y


def combine(*terms, **kwargs):
    recursive = kwargs.pop('recursive', False)
    list_merge = kwargs.pop('list_merge', 'update_on_key')
    primary_key = kwargs.pop('primary_key', 'name')
    if kwargs:
        raise Exception("'recursive', 'list_merge' and 'primary_key' are the only valid keyword arguments")

    if not terms:
        return {}

    if len(terms) == 1:
        return terms[0]

    high_to_low_prio_dict_iterator = reversed(terms)
    result = next(high_to_low_prio_dict_iterator)
    for dictionary in high_to_low_prio_dict_iterator:
        result = merge_hash(dictionary, result, recursive, list_merge, primary_key)

    return result


class FilterModule(object):
    def filters(self):
        return {
            'combine': combine,
        }
