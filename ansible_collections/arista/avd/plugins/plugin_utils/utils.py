from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

from ansible.module_utils._text import to_text


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
    return list(list_set)


def template_var(template_file, template_vars, templar, searchpath):
    """
    Wrap "template" for single values like IP addresses

    The result is forced into a string and leading/trailing newlines and whitespaces are removed.

    Parameters
    ----------
    template_file : str
        Path to Jinja2 template file
    template_vars : any
        Variables to use when rendering template
    templar : func
        Instance of Ansible Templar class
    searchpath : list of str
        List of Paths

    Returns
    -------
    str
        The rendered template
    """
    return str(template(template_file, template_vars, templar, searchpath)).strip()


def template(template_file, template_vars, templar, searchpath):
    """
    Run Ansible Templar with template file.

    This function does not support the following Ansible features:
    - No template_* vars (rarely used)
    - The template file path is not inserted into searchpath, so "include" must be absolute from searchpath.
    - No configurable convert_data (we set it to False)
    - Maybe something else we have not discovered yet...

    Parameters
    ----------
    template_file : str
        Path to Jinja2 template file
    template_vars : any
        Variables to use when rendering template
    templar : func
        Instance of Ansible Templar class
    searchpath : list of str
        List of Paths

    Returns
    -------
    str
        The rendered template
    """

    loader = templar._loader
    template_file_path = loader.path_dwim_relative_stack(searchpath, "templates", template_file)
    j2template, dummy = loader._get_file_contents(template_file_path)
    j2template = to_text(j2template)

    templar.available_variables = template_vars
    result = templar.template(j2template, convert_data=False, escape_backslashes=False)
    return result


def compile_searchpath(searchpath: list):
    """
    Create a new searchpath by inserting new items with <>/templates into the existing searchpath

    This is copying the behavior of the "ansible.builtin.template" lookup module, and is necessary
    to be able to load templates from all supported paths.

    Example
    -------
    compile_searchpath(["patha", "pathb", "pathc"]) ->
    ["patha", "patha/templates", "pathb", "pathb/templates", "pathc", "pathc/templates"]

    Parameters
    ----------
    searchpath : list of str
        List of Paths

    Returns
    -------
    list of str
        List of both original and extra paths with "/templates" added.
    """

    newsearchpath = []
    for p in searchpath:
        newsearchpath.append(os.path.join(p, "templates"))
        newsearchpath.append(p)
    return newsearchpath


def get_item(list_of_dicts: list, key, value, default=None, required=False, case_sensitive=False, var_name=None):
    """
    Get one dictionary from a list of dictionaries by matching the given key and value

    Returns the supplied default value or None if there is no match and "required" is False.

    Will return the first matching item if there are multiple matching items.

    Parameters
    ----------
    list_of_dicts : list(dict)
        List of Dictionaries to get list item from
    key : any
        Dictionary Key to match on
    value : any
        Value that must match
    default : any
        Default value returned if the key and value is not found
    required : bool
        Fail if there is no match
    case_sensitive : bool
        If the search value is a string, the comparison will ignore case by default
    var_name : str
        String used for raising exception with the full variable name

    Returns
    -------
    any
        Dict or default value

    Raises
    ------
    AristaAvdMissingVariableError
        If the key and value is not found and "required" == True
    """

    if var_name is None:
        var_name = key

    if (not isinstance(list_of_dicts, list)) or list_of_dicts == [] or value is None or key is None:
        if required is True:
            raise AristaAvdMissingVariableError(var_name)
        return default

    for list_item in list_of_dicts:
        if not isinstance(list_item, dict):
            # List item is not a dict as required. Skip this item
            continue
        if list_item.get(key) == value:
            # Match. Return this item
            return list_item

    # No Match
    if required is True:
        raise AristaAvdMissingVariableError(var_name)
    return default


def get_all(data, path: str, required: bool = False, org_path=None):
    """
    Get all values from data matching a data path.

    Path supports dot-notation like "foo.bar" to do deeper lookups. Lists will be unpacked recursively.
    Returns an empty list if the path is not found and required is False.

    Parameters
    ----------
    data : any
        Data to walk through
    path : str
        Data Path - supporting dot-notation for nested dictionaries/lists
    required : bool
        Fail if the path is not found
    org_path : str
        Internal variable used for raising exception with the full path even when called recursively

    Returns
    -------
    list [ any ]
        List of values matching data path or empty list if no matches are found.

    Raises
    ------
    AristaAvdMissingVariableError
        If the path is not found and required == True
    """

    if org_path is None:
        org_path = path

    path_elements = str(path).split(".")
    if isinstance(data, list):
        output = []
        for data_item in data:
            output.extend(get_all(data_item, path, required=required, org_path=org_path))

        return output

    elif isinstance(data, dict):
        value = data.get(path_elements[0])

        if value is None:
            if required:
                raise AristaAvdMissingVariableError(org_path)

            return []

        if len(path_elements) > 1:
            return get_all(value, ".".join(path_elements[1:]), required=required, org_path=org_path)

        else:
            return [value]

    return []
