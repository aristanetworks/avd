from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class AristaAvdError(Exception):
    def __init__(self, message="An Error has occured in an arista.avd plugin"):
        self.message = message
        super().__init__(self.message)


class AristaAvdMissingVariableError(AristaAvdError):
    pass


def get(dictionary, key, default=None, required=False, org_key=None):
    """
    Get vlans list based on network_services_keys and filters defined in fabric_topology data model

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
    keys = str(key).split('.')
    value = dictionary.get(keys[0])
    if value is None:
        if required is True:
            raise AristaAvdMissingVariableError(org_key)
        return default
    else:
        if len(keys) > 1:
            return get(value, '.'.join(keys[1:]), default=default, required=required, org_key=org_key)
        else:
            return value


def default(value, *default_values):
    """
    Return value or default_value if not None

    If Value is not None, the default values will be checked one by one.

    Parameters
    ----------
    value : any
        Primary value
    default_values : list of any
        Default values

    Returns
    -------
    any
        Value or default value
    """

    if value is not None:
        return value
    else:
        for default_value in default_values:
            if default_value is not None:
                return default_value

    return None


def unique(in_list):
    """
    Return list of unique items from the in_list

    If Value is not None, the default values will be checked one by one.

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
        Instance of Ansible 'template' lookup module used to render ip addresses with user-defined templates

    Returns
    -------
    str
        The rendered template
    """

    result = template_lookup_module.run([template_file], template_vars)[0]
    return str(result).strip()
