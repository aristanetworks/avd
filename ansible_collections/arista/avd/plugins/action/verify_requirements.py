from __future__ import absolute_import, division, print_function

__metaclass__ = type

import importlib.metadata
import os
import re
import sys

import yaml
from ansible.errors import AnsibleActionFail
from ansible.module_utils.compat.importlib import import_module
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

HAS_PIP = True
try:
    from pip._vendor.packaging.specifiers import SpecifierSet
except ImportError:
    HAS_PIP = False

# Python >= 3.8
MIN_PYTHON_SUPPORTED_VERSION = (3, 8)
# Ansible >=2.11.3
# TODO check if we can use meta/runtimes.yml
ANSIBLE_SPECIFIERS = ">=2.11.3,<2.13.0"

python_version_info = dict(
    major=sys.version_info[0],
    minor=sys.version_info[1],
    micro=sys.version_info[2],
    releaselevel=sys.version_info[3],
    serial=sys.version_info[4],
)


class ActionModule(ActionBase):
    def _validate_python_version(self, result):
        """
        TODO - avoid hardcoding this
        """
        if sys.version_info < MIN_PYTHON_SUPPORTED_VERSION:
            running_version = ".".join(str(v) for v in sys.version_info[:3])
            min_version = ".".join(str(v) for v in MIN_PYTHON_SUPPORTED_VERSION)
            Display().error(
                f"Python Version running {running_version} - Minimum Version required is {min_version}",
                False,
            )
            result["failed"] = True
        result["python_version_info"] = python_version_info
        result["python_path"] = sys.path

    def _validate_python_dependencies(self, dependencies, result):
        """
        Validate python lib versions
        """
        dependencies_dict = {
            "not_found": {},
            "valid": {},
            "mismatched": {},
            "parsing_failed": [],
        }

        # Can match this format
        # requests [security] >=2.8.1, == 2.8.* ; python_version < "2.7"
        req_re = re.compile(r"(^[a-zA-Z][a-zA-Z0-9_-]+) ?((?:\[[a-zA-Z0-9]+\])?) ?((?:(?:==|[!><~]=?) ?(?:[0-9.*]+),? ?)*)(?: ?; ?(.*))?$")

        for dep in dependencies:
            match = req_re.match(dep)
            if not match:
                dependencies_dict["parsing_failed"].append(dep)
                continue
            pkg, label, specifiers_str, extra = match.groups()
            specifiers_set = SpecifierSet(specifiers_str)

            try:
                installed_version = importlib.metadata.version(pkg)
                Display().vvvv(f"Found {pkg} {installed_version} installed!", False)
            except importlib.metadata.PackageNotFoundError:
                dependencies_dict["not_found"][pkg] = {
                    "installed": None,
                    "desired": str(specifiers_set) if len(specifiers_set) > 0 else None,
                }
                result["failed"] = True
                continue

            if specifiers_set.contains(installed_version):
                dependencies_dict["valid"][pkg] = {
                    "installed": installed_version,
                    "desired": str(specifiers_set) if len(specifiers_set) > 0 else None,
                }
            else:
                dependencies_dict["mismatched"][pkg] = {
                    "installed": installed_version,
                    "desired": str(specifiers_set) if len(specifiers_set) > 0 else None,
                }
                result["failed"] = True

        result["dependencies"] = dependencies_dict

    def _validate_ansible_version(self, running_version, result):
        """
        Validate ansible version

        TODO - avoid hardcoding this
        """
        specifiers_set = SpecifierSet(ANSIBLE_SPECIFIERS)
        if not specifiers_set.contains(running_version):
            Display().error(
                f"Ansible Version running {running_version} - Requirement is {ANSIBLE_SPECIFIERS}",
                False,
            )
            result["failed"] = True

        result["ansible_version"] = running_version

    def _validate_ansible_collections(self, result):
        """ """
        # TODO
        pass

    def __maybe_get_git_commit(self, collection_path):
        def is_sha1(maybe_sha1):
            try:
                assert len(maybe_sha1) == 40
                int(maybe_sha1, 16)
                return True
            except Exception:
                return False

        maybe_git_root = os.path.dirname(os.path.dirname(os.path.dirname(collection_path)))
        maybe_git_dir = os.path.join(maybe_git_root, ".git")
        if os.path.exists(maybe_git_dir):
            # it is a git repo
            with open(os.path.join(maybe_git_dir, "HEAD"), "r") as fd:
                data = fd.read().strip()
            if is_sha1(data):
                return data[:9]

            # HEAD is probably a ref
            head = yaml.safe_load(data)
            ref = head["ref"]
            with open(os.path.join(maybe_git_dir, ref), "r") as fd:
                data = fd.read().strip()
            if is_sha1(data):
                return data[:9]

            # TODO - we failed parsing

        return None

    def _get_running_collection_version(self, running_collection_name, result):
        """
        TODO
        """
        collection = import_module(f"ansible_collections.{running_collection_name}")
        collection_path = os.path.dirname(collection.__file__)
        galaxy_file = os.path.join(collection_path, "galaxy.yml")
        with open(galaxy_file, "rb") as fd:
            metadata = yaml.safe_load(fd)

        version = metadata["version"]

        # Try to detect a git tag
        # if it was cloned from git the git root will be two levels above
        git_commit = self.__maybe_get_git_commit(collection_path)
        # Not in theory `BLAH` should be the number of commits between version and the
        # commit id but it is hard to compute without git API and the goal is to
        # not add any additional dependencies
        # TODO - decide if we want to keep this
        if git_commit:
            version = f"v{version}-BLAH-d{git_commit}"

        result["collection"] = {
            "name": running_collection_name,
            "path": os.path.dirname(os.path.dirname(collection_path)),
            "version": version,
        }

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PIP:
            raise AnsibleActionFail("pip is required to run this plugin")

        if not (self._task.args and "dependencies" in self._task.args):
            raise AnsibleActionFail("The argument 'dependencies' must be set")

        dependencies = self._task.args.get("dependencies")

        if not isinstance(dependencies, list):
            raise AnsibleActionFail("The argument 'dependencies' is not a list")

        running_ansible_version = task_vars["ansible_version"]["string"]
        running_collection_name = task_vars["ansible_collection_name"]
        self._get_running_collection_version(running_collection_name, result)

        self._validate_python_version(result)
        self._validate_python_dependencies(dependencies, result)
        self._validate_ansible_version(running_ansible_version, result)
        self._validate_ansible_collections(result)

        return result
