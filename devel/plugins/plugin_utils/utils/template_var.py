from .template import template


def template_var(template_file, template_vars, templar):
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
    return str(template(template_file, template_vars, templar)).strip()
