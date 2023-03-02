from __future__ import annotations

__metaclass__ = type

import importlib.metadata
import json
import os
import sys
from subprocess import PIPE, Popen

import yaml
from ansible.errors import AnsibleActionFail
from ansible.module_utils.compat.importlib import import_module
from ansible.plugins.action import ActionBase, display
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

HAS_PACKAGING = True
try:
    from packaging.requirements import InvalidRequirement, Requirement
    from packaging.specifiers import SpecifierSet
except ImportError:
    HAS_PACKAGING = False

# Python >= 3.8
MIN_PYTHON_SUPPORTED_VERSION = (3, 8)


def _validate_python_version(result: dict) -> bool:
    """
    TODO - avoid hardcoding the min supported version

    return False if the python version is not valid
    """
    result["python_version_info"] = {
        "major": sys.version_info.major,
        "minor": sys.version_info.minor,
        "micro": sys.version_info.micro,
        "releaselevel": sys.version_info.releaselevel,
        "serial": sys.version_info.serial,
    }
    result["python_path"] = sys.path

    if sys.version_info < MIN_PYTHON_SUPPORTED_VERSION:
        running_version = ".".join(str(v) for v in sys.version_info[:3])
        min_version = ".".join(str(v) for v in MIN_PYTHON_SUPPORTED_VERSION)
        display.error(f"Python Version running {running_version} - Minimum Version required is {min_version}", False)
        return False

    return True


def _validate_python_dependencies(dependencies: list[str], result: dict) -> bool:
    """
    Validate python lib versions

    return False if any python dependency is not valid
    """
    valid = True

    dependencies_dict = {
        "not_found": {},
        "valid": {},
        "mismatched": {},
        "parsing_failed": [],
    }

    # Remove the comments
    dependencies = [dep for dep in dependencies if dep[0] != "#"]
    for dep in dependencies:
        try:
            req = Requirement(dep)
        except InvalidRequirement as exc:
            raise AristaAvdError(f"Wrong format for dependency {dep}") from exc

        try:
            installed_version = importlib.metadata.version(req.name)
            display.vvvv(f"Found {req.name} {installed_version} installed!", "Verify Requirements")
        except importlib.metadata.PackageNotFoundError:
            dependencies_dict["not_found"][req.name] = {
                "installed": None,
                "desired": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            display.error(f"{req.name} required but not found - required version is {str(req.specifier)}", False)
            valid = False
            continue

        if req.specifier.contains(installed_version):
            dependencies_dict["valid"][req.name] = {
                "installed": installed_version,
                "desired": str(req.specifier) if len(req.specifier) > 0 else None,
            }
        else:
            display.error(f"{req.name} version running {installed_version} - required version is {str(req.specifier)}", False)
            dependencies_dict["mismatched"][req.name] = {
                "installed": installed_version,
                "desired": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            valid = False

    result["python_dependencies"] = dependencies_dict
    return valid


def _validate_ansible_version(collection_name: str, running_version: str, result: dict) -> bool:
    """
    Validate ansible version in use, running_version, based on the collection requirements

    Return False if Ansible version is not valid
    """
    collection_meta = _get_collection_metadata(collection_name)
    specifiers_set = SpecifierSet(collection_meta.get("requires_ansible", ""))
    result["ansible_version"] = running_version

    if len(specifiers_set) > 0:
        result["requires_ansible"] = str(specifiers_set)
    if not specifiers_set.contains(running_version):
        display.error(
            f"Ansible Version running {running_version} - Requirement is {str(specifiers_set)}",
            False,
        )
        return False

    return True


def _validate_ansible_collections(running_collection_name: str, result: dict) -> bool:
    """
    Verify the version of required ansible collections running based on the collection requirements

    Return True if all collection requirements are valid, False otherwise
    """
    valid = True

    collection = import_module(f"ansible_collections.{running_collection_name}")
    collection_path = os.path.dirname(collection.__file__)
    collections_file = os.path.join(collection_path, "collections.yml")
    with open(collections_file, "rb") as fd:
        metadata = yaml.safe_load(fd)
    if "collections" not in metadata:
        # no requirements
        return True

    dependencies_dict = {
        "not_found": {},
        "valid": {},
        "mismatched": {},
        "parsing_failed": [],
    }

    for collection_dict in metadata["collections"]:
        if "name" not in collection_dict:
            display.error("key `name` required but not found in collections requirement - please raise an issue on Github", False)
            continue

        collection_name = collection_dict["name"]
        # Check if there is a version requirement
        specifiers_set = SpecifierSet(collection_dict.get("version", ""))

        try:
            collection_path = _get_collection_path(collection_name)
        except ModuleNotFoundError:
            dependencies_dict["not_found"][collection_name] = {
                "installed": None,
                "desired": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
            if specifiers_set:
                display.error(f"{collection_name} required but not found - required version is {str(specifiers_set)}", False)
            else:
                display.error(f"{collection_name} required but not found", False)
            valid = False
            continue

        installed_version = _get_collection_version(collection_path)

        if specifiers_set.contains(installed_version):
            dependencies_dict["valid"][collection_name] = {
                "installed": installed_version,
                "desired": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
        else:
            display.error(f"{collection_name} version running {installed_version} - required version is {str(specifiers_set)}", False)
            dependencies_dict["mismatched"][collection_name] = {
                "installed": installed_version,
                "desired": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
            valid = False

    result["collection_dependencies"] = dependencies_dict
    return valid


def _get_collection_path(collection_name: str) -> str:
    """
    Retrieve the collection path based on the collection_name
    """
    collection = import_module(f"ansible_collections.{collection_name}")
    return os.path.dirname(collection.__file__)


def _get_collection_version(collection_path) -> str:
    """
    Returns the collection version based on the collection path
    """
    # Trying to find the version based on either galaxy.yml or MANIFEST.json
    try:
        galaxy_file = os.path.join(collection_path, "galaxy.yml")
        with open(galaxy_file, "rb") as fd:
            metadata = yaml.safe_load(fd)
    except FileNotFoundError:
        manifest_file = os.path.join(collection_path, "MANIFEST.json")
        with open(manifest_file, "rb") as fd:
            metadata = json.load(fd)["collection_info"]

    return metadata["version"]


def _get_running_collection_version(running_collection_name: str, result: dict) -> None:
    """
    Stores the version collection in result
    """
    collection_path = _get_collection_path(running_collection_name)
    version = _get_collection_version(collection_path)

    # Try to detect a git tag
    # Using subprocess for now
    with Popen(["git", "describe", "--tags"], stdout=PIPE, stderr=PIPE, cwd=collection_path) as process:
        output, err = process.communicate()
        if err:
            display.vvv("Not a git repository")
        else:
            display.vvv("This is a git repository, overwriting version with 'git describe --tags output'")
            version = output.decode("UTF-8").strip()

    result["collection"] = {
        "name": running_collection_name,
        "path": os.path.dirname(os.path.dirname(collection_path)),
        "version": version,
    }


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PACKAGING:
            raise AnsibleActionFail("packaging is required to run this plugin")

        if not (self._task.args and "dependencies" in self._task.args):
            raise AnsibleActionFail("The argument 'dependencies' must be set")

        py_dependencies = self._task.args.get("dependencies")
        avd_debug = self._task.args.get("avd_debug", False)
        # TODO - check the `-e` syntax
        if avd_debug in ["true", "True"]:
            avd_debug = True

        if not isinstance(py_dependencies, list):
            raise AnsibleActionFail("The argument 'dependencies' is not a list")

        running_ansible_version = task_vars["ansible_version"]["string"]
        running_collection_name = task_vars["ansible_collection_name"]

        result["failed"] = False
        result["ansible"] = {}
        result["python"] = {}

        _get_running_collection_version(running_collection_name, result["ansible"])
        display.display(f"AVD version {result['ansible']['collection']['version']}", color="blue")

        _validate_python_version(result["python"])
        _validate_python_dependencies(py_dependencies, result["python"])
        _validate_ansible_version(running_collection_name, running_ansible_version, result["ansible"])
        _validate_ansible_collections(running_collection_name, result["ansible"])

        if avd_debug is True:
            display.display(json.dumps(result, indent=4), color="blue")

        return result
