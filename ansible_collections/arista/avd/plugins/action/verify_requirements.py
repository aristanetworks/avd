from __future__ import absolute_import, division, print_function

__metaclass__ = type

import importlib.metadata
import re
import sys

from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleActionFail
from ansible.utils.display import Display

HAS_PIP = True
try:
    from pip._vendor.packaging.specifiers import SpecifierSet
except ImportError:
    HAS_PIP = False

python_version_info = dict(
    major=sys.version_info[0],
    minor=sys.version_info[1],
    micro=sys.version_info[2],
    releaselevel=sys.version_info[3],
    serial=sys.version_info[4],
)


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PIP:
            raise AnsibleActionFail("pip is required to run this plugin")

        dependencies_dict = {
            "not_found": {},
            "valid": {},
            "mismatched": {},
            "parsing_failed": [],
        }

        if not (self._task.args and "dependencies" in self._task.args):
            raise AnsibleActionFail("The argument 'dependencies' must be set")

        dependencies = self._task.args.get("dependencies")

        if not isinstance(dependencies, list):
            raise AnsibleActionFail("The argument 'dependencies' is not a list")

        # Can match this format
        # requests [security] >=2.8.1, == 2.8.* ; python_version < "2.7"
        req_re = re.compile(
            r"(^[a-zA-Z][a-zA-Z0-9_-]+) ?((?:\[[a-zA-Z0-9]+\])?) ?((?:(?:==|[!><~]=?) ?(?:[0-9.*]+),? ?)*)(?: ?; ?(.*))?$"
        )

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

        result["python_version_info"] = python_version_info
        result["python_path"] = sys.path
        result["dependencies"] = dependencies_dict

        return result
