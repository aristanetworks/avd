# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from os.path import join as path_join


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
        newsearchpath.append(path_join(p, "templates"))
        newsearchpath.append(p)
    return newsearchpath
