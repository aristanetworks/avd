# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar


def template(template_file: str, template_vars: dict, templar: Templar | None) -> str:
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

    Returns:
    -------
    str
        The rendered template
    """
    if templar is None:
        msg = "Jinja Templating is not implemented in pyavd"
        raise NotImplementedError(msg)

    # We only get here when running from Ansible, so it is safe to import from ansible.
    from ansible.module_utils._text import to_text  # noqa: PLC0415
    from jinja2.loaders import FileSystemLoader  # noqa: PLC0415

    dataloader: DataLoader = templar._loader
    jinjaloader = templar.environment.loader
    searchpath = jinjaloader.searchpath if isinstance(jinjaloader, FileSystemLoader) else []
    template_file_path = dataloader.path_dwim_relative_stack(searchpath, "templates", template_file)
    j2template, dummy = dataloader._get_file_contents(template_file_path)
    j2template = to_text(j2template)

    with templar.set_temporary_context(available_variables=template_vars):
        # Since convert_data is False, we know the result is a string.
        return cast("str", templar.template(j2template, convert_data=False, escape_backslashes=False))
