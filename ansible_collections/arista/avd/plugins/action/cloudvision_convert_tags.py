"""

This plugin handles the conversion of the data structure
from what eos_designs generates in structrued_config
to the format that cv_tags_v3 expects.

"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import cProfile
import pstats

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        result["ansible_facts"] = {"cloudvision_tags": self._generate_cloudvision_tags(task_vars)}

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result

    def _generate_cloudvision_tags(self, task_vars):
        """

        Generate the data strucutre that cv_tags_v3 expects for each device.
        """
        hostname = task_vars.get("inventory_hostname", "not_found")
        existing_tags = task_vars.get("cloudvision_tags", {})

        # convert the label names
        self._convert_label(existing_tags)

        single_device_tags = {"device": hostname, "device_tags": existing_tags["device_tags"]}

        if existing_tags.get("interface_tags"):
            single_device_tags["interface_tags"] = existing_tags["interface_tags"]

        return [single_device_tags]

    @staticmethod
    def _convert_label(existing_tags):
        if existing_tags.get("device_tags"):
            for tag in existing_tags["device_tags"]:
                tag["name"] = tag["label"]
                tag.pop("label", None)

        if existing_tags.get("interface_tags"):
            for interface in existing_tags["interface_tags"]:
                for tag in interface["tags"]:
                    tag["name"] = tag["label"]
                    tag.pop("label", None)
