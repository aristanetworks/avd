# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import json
import sys
import warnings
from importlib import import_module
from importlib.metadata import Distribution, PackageNotFoundError, metadata, version
from logging import getLogger
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Any

import yaml
from ansible import constants as C  # noqa: N812
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata

from ansible_collections.arista.avd.plugins import PYTHON_AVD_PATH, RUNNING_FROM_SOURCE
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AvdActionPlugin, AvdLoggingConfig

try:
    # Relying on packaging installed by ansible
    from packaging.requirements import InvalidRequirement, Requirement
    from packaging.specifiers import SpecifierSet

    HAS_PACKAGING = True
except ImportError:
    HAS_PACKAGING = False
    # Making ansible-test sanity happy
    Requirement = object

LOGGER = getLogger("ansible_collections.arista.avd")

MIN_PYTHON_SUPPORTED_VERSION = (3, 10)
DEPRECATE_MIN_PYTHON_SUPPORTED_VERSION = False


# TODO: Consider moving the following helpers inside the plugin class as methods to use `self.logger`.
def _validate_python_version(info: dict[str, Any]) -> bool:
    """
    Validate the running Python version.

    TODO: - avoid hardcoding the min supported version.

    Args:
      info (dict): Dictionary to store information to present in ansible logs

    Returns:
        bool: False if the python version is not valid.
    """
    info["python_version_info"] = {
        "major": sys.version_info.major,
        "minor": sys.version_info.minor,
        "micro": sys.version_info.micro,
        "releaselevel": sys.version_info.releaselevel,
        "serial": sys.version_info.serial,
    }
    info["python_path"] = sys.path

    running_version = ".".join(str(v) for v in sys.version_info[:3])
    min_version = ".".join(str(v) for v in MIN_PYTHON_SUPPORTED_VERSION)
    if sys.version_info < MIN_PYTHON_SUPPORTED_VERSION:
        LOGGER.error("Python Version running %s - Minimum Version required is %s", running_version, min_version)
        return False
    # Keeping this for next deprecation adjust the message as required
    if DEPRECATE_MIN_PYTHON_SUPPORTED_VERSION and sys.version_info[:2] == MIN_PYTHON_SUPPORTED_VERSION:
        msg = (
            f"You are currently running Python version {running_version}. "
            f"AVD version 5.0.0 will drop support for Python version {min_version}. "
            "The decision has been taken to remove Python version 3.9 support in AVD "
            "collection to anticipate its removal in `ansible-core`. `ansible-core` "
            "version 2.15 End-Of-Life is scheduled for November 2024 and it will be the "
            "last `ansible-core` version supporting Python version 3.9 as documented here: "
            "https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix."
        )
        warnings.warn(msg, DeprecationWarning, stacklevel=2)

    return True


def _parse_requirements(req_str: str) -> tuple[Requirement, list[str]]:
    """Parse a requirement string and return the parsed object an a list of extras requirements to parse if any."""
    try:
        req = Requirement(req_str)
    except InvalidRequirement as exc:
        msg = f"Wrong format for requirement {req_str}"
        raise ValueError(msg) from exc

    extras = []
    if req.extras:
        for subreq_name in metadata(req.name).get_all("Requires-Dist"):
            subreq = Requirement(subreq_name)
            if subreq.marker:
                extras = [subreq_name for marker in subreq.marker._markers if str(marker[0]) == "extra" and str(marker[2]) in req.extras]

    return req, extras


def _check_requirement(req: Requirement, requirements_dict: dict[str, Any]) -> bool:
    """
    Check one requirement and in-place update requirement_dict.

    Returns:
        boolean: True if the check succeeds, False otherwise
    """
    try:
        installed_version = version(req.name)
        LOGGER.debug("Found %s %s installed!", req.name, installed_version)

        # If some old dist-info files are leftover in Python site-packages, it is possible
        # to find multiple Distributions for the installed version
        potential_dists = Distribution.discover(name=req.name)
        detected_versions = [dist.version for dist in potential_dists]
        valid_versions = [version for version in detected_versions if req.specifier.contains(version)]
        if len(detected_versions) > 1:
            LOGGER.info("Found %s %s metadata - this could mean legacy dist-info files are present in your site-packages folder.", req.name, detected_versions)
    except PackageNotFoundError:
        requirements_dict["not_found"][req.name] = {
            "installed": None,
            "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
        }
        # OK to ignore TRY400 since we don't need the traceback
        LOGGER.error("Python library '%s' required but not found - requirement is %s", req.name, str(req))  # noqa: TRY400
        return False

    if req.specifier.contains(installed_version):
        requirements_dict["valid"][req.name] = {
            "installed": installed_version,
            "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
        }
    elif len(valid_versions) > 0:
        # More than one dist found and at least one was matching - output a warning
        requirements_dict["valid"][req.name] = {
            "installed": installed_version,
            "detected_versions": detected_versions,
            "valid_versions": valid_versions,
            "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
        }
        warning_msg = (
            f"Found {req.name} valid versions {valid_versions} among {detected_versions} from metadata - assuming a valid version is running - more"
            " information available with -v"
        )
        LOGGER.warning(warning_msg)
        info_msg = (
            "The Arista AVD collection relies on Python built-in library `importlib.metadata` to detect running versions. In some cases where legacy"
            " dist-info folders are leftovers in the site-packages folder, there can be misdetection of the version. This module assumes that if any"
            " version matches the required one, then the requirement is met. This could led to false positive results. Please make sure to clean the"
            " leftovers dist-info folders."
        )
        LOGGER.info(info_msg)
    elif len(detected_versions) > 1:
        # More than one dist found and none matching the requirements
        LOGGER.error("Python library '%s' detected versions %s - requirement is %s - more information available with -v", req.name, detected_versions, str(req))
        requirements_dict["mismatched"][req.name] = {
            "installed": installed_version,
            "detected_versions": detected_versions,
            "valid_versions": None,
            "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
        }
        LOGGER.error("Python library '%s' version running %s - requirement is %s", req.name, installed_version, str(req))
    else:
        LOGGER.error("Python library '%s' version running %s - requirement is %s", req.name, installed_version, str(req))
        requirements_dict["mismatched"][req.name] = {
            "installed": installed_version,
            "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
        }
        return False

    return True


def _validate_python_requirements(requirements: list[str], info: dict[str, Any]) -> bool:
    """
    Validate python lib versions.

    If any extra is present and not running from source, validate the extras as well.

    Args:
      requirements (list): List of requirements for pythom modules
      info (dict): Dictionary to store information to present in ansible logs

    Returns:
        bool: False if any python requirement is not valid.
    """
    valid = True

    requirements_dict: dict[str, Any] = {
        "not_found": {},
        "valid": {},
        "mismatched": {},
        "parsing_failed": [],
    }

    # Remove the comments including inline comments
    requirements = [req.split(" #", maxsplit=1)[0] for req in requirements if req[0] != "#"]
    for raw_req in requirements:
        req, extras = _parse_requirements(raw_req)
        if RUNNING_FROM_SOURCE and req.name == "pyavd":
            LOGGER.debug("AVD is running from source, *not* checking pyavd version nor any extra.")
            requirements_dict["valid"][req.name] = {
                "installed": "running from source",
                "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            continue

        requirements.extend(extras)

        valid = valid and _check_requirement(req, requirements_dict)

    info["python_requirements"] = requirements_dict
    return valid


def _validate_ansible_version(collection_name: str, running_version: str, info: dict[str, Any]) -> bool:
    """
    Validate ansible version in use, running_version, based on the collection requirements.

    Args:
      collection_name (str): The collection name
      running_version (str): A string representing the current Ansible version being run
      info (dict): Dictionary to store information to present in ansible logs

    Returns:
        bool: False if Ansible version is not valid.
    """
    collection_meta = _get_collection_metadata(collection_name)
    specifiers_set = SpecifierSet(collection_meta.get("requires_ansible", ""))
    deprecation_specifiers_set = SpecifierSet()
    info["ansible_version"] = running_version

    if len(specifiers_set) > 0:
        info["requires_ansible"] = str(specifiers_set)
    if not specifiers_set.contains(running_version):
        LOGGER.error("Ansible Version running %s - Requirement is %s", running_version, str(specifiers_set))
        return False
    # Keeping this for next deprecation - set the value of deprecation_specifiers_set when needed and adjust message
    if not deprecation_specifiers_set.contains(running_version):
        msg = (
            f"You are currently running ansible-core {running_version}. The next minor release of AVD after November 6th 2023 will drop support for"
            " ansible-core<2.14. Python 3.8 support will be dropped at the same time as ansible-core>=2.14 does not support it. See the following link"
            " for more details: https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix"
        )
        warnings.warn(msg, DeprecationWarning, stacklevel=2)

    return True


def _validate_ansible_collections(running_collection_name: str, info: dict[str, Any]) -> bool:
    """
    Verify the version of required ansible collections running based on the collection requirements.

    Args:
      running_collection_name (str): The collection name
      info (dict): Dictionary to store information to present in ansible logs

    Returns:
        bool: True if all collection requirements are valid, False otherwise.
    """
    valid = True

    collection_path = _get_collection_path(running_collection_name)
    with Path(collection_path, "requirements.yml").open("rb") as fd:
        metadata = yaml.safe_load(fd)
    if "collections" not in metadata:
        # no requirements
        return True

    requirements_dict: dict[str, Any] = {
        "not_found": {},
        "valid": {},
        "mismatched": {},
        "parsing_failed": [],
    }

    for collection_dict in metadata["collections"]:
        if "name" not in collection_dict:
            LOGGER.error("key `name` required but not found in collections requirement - please raise an issue on GitHub")
            continue

        collection_name: str = collection_dict["name"]
        # Check if there is a version requirement
        specifiers_set = SpecifierSet(collection_dict.get("version", ""))

        try:
            collection_path = _get_collection_path(collection_name)
        except ModuleNotFoundError:
            requirements_dict["not_found"][collection_name] = {
                "installed": None,
                "required_version": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
            # OK to ignore TRY400 since we don't need the traceback
            if specifiers_set:
                LOGGER.error("%s required but not found - required version is %s", collection_name, specifiers_set)  # noqa: TRY400
            else:
                LOGGER.error("%s required but not found", collection_name)  # noqa: TRY400
            valid = False
            continue

        installed_version = _get_collection_version(collection_path)

        if specifiers_set.contains(installed_version):
            requirements_dict["valid"][collection_name] = {
                "installed": installed_version,
                "required_version": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
        else:
            LOGGER.error("%s version running %s - required version is %s", collection_name, installed_version, str(specifiers_set))
            requirements_dict["mismatched"][collection_name] = {
                "installed": installed_version,
                "required_version": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
            valid = False

    info["collection_requirements"] = requirements_dict
    return valid


def _get_collection_path(collection_name: str) -> str:
    """Retrieve the collection path based on the collection_name."""
    collection = import_module(f"ansible_collections.{collection_name}")
    return str(Path(collection.__file__).parent)


def _get_collection_version(collection_path: str) -> str:
    """Returns the collection version based on the collection path."""
    # Trying to find the version based on either galaxy.yml or MANIFEST.json
    try:
        galaxy_file = Path(collection_path, "galaxy.yml")
        with galaxy_file.open("rb") as fd:
            metadata = yaml.safe_load(fd)
    except FileNotFoundError:
        manifest_file = Path(collection_path, "MANIFEST.json")
        with manifest_file.open("rb") as fd:
            metadata = json.load(fd)["collection_info"]

    return metadata["version"]


def _get_running_collection_version(running_collection_name: str, result: dict[str, Any]) -> None:
    """Stores the version collection in result."""
    collection_path = _get_collection_path(running_collection_name)
    version = _get_collection_version(collection_path)

    try:
        # Try to detect a git tag
        # Using subprocess for now
        with Popen(["git", "describe", "--tags"], stdout=PIPE, stderr=PIPE, cwd=collection_path) as process:  # noqa: S607
            output, err = process.communicate()
            if err:
                # Not that when molecule runs, it runs in a copy of the directory that is not a git repo
                # so only the latest tag is being returned
                LOGGER.debug("Not a git repository")
            else:
                LOGGER.debug("This is a git repository, overwriting version with 'git describe --tags output'")
                version = output.decode("UTF-8").strip()
    except FileNotFoundError:
        # Handle the case where `git` is not installed or not in the PATH
        LOGGER.debug("Could not find 'git' executable, returning collection version")

    result["collection"] = {
        "name": running_collection_name,
        "path": str(Path(collection_path).parents[1]),
        "version": version,
    }


def check_running_from_source() -> bool:
    """
    Check if running from sources, if so recompile schemas and templates as needed.

    Returns:
        bool: True if schemas or templates were recompiled, False otherwise.
    """
    if not RUNNING_FROM_SOURCE:
        return False

    # if running from source, path to pyavd and schema_tools has already been prepended to Python Path
    from schema_tools.check_schemas import check_schemas, rebuild_schemas  # noqa: PLC0415
    from schema_tools.compile_templates import check_templates, recompile_templates  # noqa: PLC0415

    if schemas_recompiled := check_schemas():
        LOGGER.info("Schemas have changed, rebuilding...", extra={"color": C.COLOR_CHANGED})
        rebuild_schemas()
        LOGGER.info("Done.", extra={"color": C.COLOR_CHANGED})

    if templates_recompiled := check_templates():
        LOGGER.info("Templates have changed, recompiling...", extra={"color": C.COLOR_CHANGED})
        recompile_templates()
        LOGGER.info("Done.", extra={"color": C.COLOR_CHANGED})

    return schemas_recompiled or templates_recompiled


class ActionModule(AvdActionPlugin):
    _logging_config = AvdLoggingConfig(add_role_context=True)

    def main(self, task_vars: dict[str, Any]) -> None:
        if not HAS_PACKAGING:
            msg = "packaging is required to run this plugin"
            raise ImportError(msg)

        if not (self._task.args and "requirements" in self._task.args):
            msg = "The argument 'requirements' must be set"
            raise ValueError(msg)

        py_requirements = self._task.args.get("requirements")
        avd_ignore_requirements = self._task.args.get("avd_ignore_requirements", False)
        if avd_ignore_requirements in ["true", "True"]:
            avd_ignore_requirements = True

        if not isinstance(py_requirements, list):
            msg = "The argument 'requirements' is not a list"
            raise TypeError(msg)

        running_ansible_version = task_vars["ansible_version"]["string"]
        running_collection_name = task_vars["ansible_collection_name"]

        self.result["failed"] = False

        error_message = "Set 'avd_ignore_requirements=True' to ignore validation error(s)."
        info: dict[str, Any] = {
            "ansible": {},
            "python": {},
        }

        _get_running_collection_version(running_collection_name, info["ansible"])

        if check_running_from_source():
            self.result["changed"] = True

        self.logger.info("AVD version %s", info["ansible"]["collection"]["version"], extra={"color": C.COLOR_OK})
        if RUNNING_FROM_SOURCE:
            self.logger.info("AVD is running from source using PyAVD at '%s'", PYTHON_AVD_PATH, extra={"color": C.COLOR_OK})

        if not _validate_python_version(info["python"]):
            self.result["failed"] = True
        if not _validate_python_requirements(py_requirements, info["python"]):
            self.result["failed"] = True
        if not _validate_ansible_version(running_collection_name, running_ansible_version, info["ansible"]):
            self.result["failed"] = True
        if not _validate_ansible_collections(running_collection_name, info["ansible"]):
            self.result["failed"] = True

        serialized_info = json.dumps(info, indent=4)
        self.logger.info(serialized_info)

        if avd_ignore_requirements is True:
            self.result["failed"] = False
        elif self.result["failed"] is True:
            self.result["msg"] = error_message
