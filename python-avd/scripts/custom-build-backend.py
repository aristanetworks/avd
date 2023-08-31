# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from subprocess import Popen

from setuptools import build_meta as _orig
from setuptools.build_meta import *  # noqa: F401,F403 # pylint:disable=wildcard-import,unused-wildcard-import
from yaml import safe_load


def _translate_version(version: str, pyavd_prerelease: str) -> str:
    """
    Translate an Ansible collection version to Python package version
    """

    avd_base_version = version.split("-", maxsplit=1)[0]

    if pyavd_prerelease:
        return f"{avd_base_version}{pyavd_prerelease}"

    if "-dev" in version:
        avd_dev_version = version.split("-dev")[1]
        return f"{avd_base_version}.dev{avd_dev_version}"

    if "-rc" in version:
        avd_rc_version = version.split("-rc")[1]
        return f"{avd_base_version}rc{avd_rc_version}"

    return avd_base_version


def _insert_version() -> None:
    with open(Path(__file__).parents[2].joinpath("ansible_collections/arista/avd/galaxy.yml"), encoding="UTF-8") as galaxy_file:
        ansible_version = dict(safe_load(galaxy_file)).get("version")

    with open(Path(__file__).parents[1].joinpath("pyavd/__init__.py"), mode="r", encoding="UTF-8") as init_file:
        init_lines = init_file.readlines()

    pyavd_prerelease = ""
    for line in init_lines:
        if "PYAVD_PRERELEASE" in line:
            pyavd_prerelease = line.split("=", maxsplit=1)[1].split("#")[0].replace('"', "").strip()
            break

    version = _translate_version(ansible_version, pyavd_prerelease)

    for index, line in enumerate(init_lines):
        if "__version__" in line:
            init_lines[index] = f'__version__ = "{version}"\n'
            break

    with open(Path(__file__).parents[1].joinpath("pyavd/__init__.py"), mode="w", encoding="UTF-8") as init_file:
        init_file.writelines(init_lines)


def get_requires_for_build_wheel(config_settings=None):
    print("Fetch version from ansible.avd ansible collection and insert into __init__.py")
    _insert_version()

    print("Running 'make dep' to vendor various scripts and templates from arista.avd ansible collection")
    with Popen("make dep", shell=True) as make_process:
        if make_process.wait() != 0:
            raise RuntimeError("Something went wrong during 'make dep'")

    return _orig.get_requires_for_build_wheel(config_settings)
