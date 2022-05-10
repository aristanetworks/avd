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

    for x_key, x_value in x.items():
        for y_key, y_value in y.items():
            if x_key == y_key:
                if isinstance(x_value, MutableMapping) and isinstance(y_value, MutableMapping):
                    if recursive:
                        y[y_key] = merge_hash(x_value, y_value, recursive, list_merge, primary_key)
                    continue
                if isinstance(x_value, MutableSequence) and isinstance(y_value, MutableSequence):
                    if list_merge == 'update_on_key':
                        for x_element in x_value:
                            flag = 0
                            for y_element in y_value:
                                if isinstance(y_element, dict) and isinstance(x_element, dict):
                                    if primary_key in x_element and primary_key in y_element:
                                        if x_element[primary_key] == y_element[primary_key]:
                                            flag = 1
                                            if recursive:
                                                x_element = merge_hash(x_element, y_element, recursive,
                                                                       list_merge, primary_key)

                                            for x_element_key, x_element_value in x_element.items():
                                                # if the key in x is not in y, add the key and value in y
                                                if x_element_key not in y_element:
                                                    y_element[x_element_key] = x_element_value
                                                continue

                            if flag == 0:
                                # if primary key does not match, append the x element to y
                                y[y_key].append(x_element)

        if x_key not in y.keys():
            # if the key in x is not in y, add the key and value in y
            y[x_key] = x_value

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
