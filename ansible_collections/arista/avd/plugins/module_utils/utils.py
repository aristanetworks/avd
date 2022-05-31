from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class AristaAvdError(Exception):
    def __init__(self, message="An Error has occured in an arista.avd plugin"):
        self.message = message
        super().__init__(self.message)


class AristaAvdMissingVariableError(AristaAvdError):
    pass


def get(dictionary, key, default=None, required=False, org_key=None, separator="."):
    """
    Get a value from a dictionary or nested dictionaries.

    Key supports dot-notation like "foo.bar" to do deeper lookups.
    Returns the supplied default value or None if the key is not found and required is False.

    Parameters
    ----------
    dictionary : dict
        Dictionary to get key from
    key : str
        Dictionary Key - supporting dot-notation for nested dictionaries
    default : any
        Default value returned if the key is not found
    required : bool
        Fail if the key is not found
    org_key : str
        Internal variable used for raising exception with the full key name even when called recursively
    separator: str
        String to use as the separator parameter in the split function. Useful in cases when the key
        can contain variables with "." inside (e.g. hostnames)

    Returns
    -------
    any
        Value or default value

    Raises
    ------
    AristaAvdMissingVariableError
        If the key is not found and required == True
    """

    if org_key is None:
        org_key = key
    keys = str(key).split(separator)
    value = dictionary.get(keys[0])
    if value is None:
        if required is True:
            raise AristaAvdMissingVariableError(org_key)
        return default
    else:
        if len(keys) > 1:
            return get(value, separator.join(keys[1:]), default=default, required=required, org_key=org_key, separator=separator)
        else:
            return value


def default(*values):
    """
    Accepts any number of arguments. Return the first value which is not None

    Last resort is to return None.

    Parameters
    ----------
    *values : any
        One or more values to test

    Returns
    -------
    any
        First value which is not None
    """

    for value in values:
        if value is not None:
            return value
    return None


def unique(in_list):
    """
    Return list of unique items from the in_list

    Parameters
    ----------
    in_list : list

    Returns
    -------
    list
        Unique list items
    """

    list_set = set(in_list)
    return (list(list_set))


def template_var(template_file, template_vars, template_lookup_module):
    """
    Run Ansible Template Lookup Plugin

    The result is forced into a string and leading/trailing newlines and whitespaces are removed.

    Parameters
    ----------
    template_file : str
        Filename to pass to template_lookup_module
    template_vars : any
        Vars to pass to template_lookup_module
    template_lookup_module : func
        Instance of Ansible 'template' lookup module

    Returns
    -------
    str
        The rendered template
    """

    result = template_lookup_module.run([template_file], template_vars)[0]
    return str(result).strip()
