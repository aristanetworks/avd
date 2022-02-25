from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.modules.configlet_build_config import get_configlet
import os
import logging
import pytest

CONFIGLETS_DIR = os.path.dirname(os.path.realpath(
    __file__)) + "../../inventory/intended/configs"

CONFIGLETS_DATA = {
    "valid_source": {"src_folder": CONFIGLETS_DIR, "prefix": "AVD"},
    "default_prefix": {"src_folder": CONFIGLETS_DIR},
    "non_default_prefix": {"src_folder": CONFIGLETS_DIR, "prefix": "CFG"}
}


class TestConfigletBuildConfig():
    def verify_configlets(self, src_folder, prefix, extension, output):
        suffixes = ['.cfg']
        for dirpath, dirnames, filenames in os.walk(src_folder):
            for filename in filenames:
                filesplit = os.path.splitext(filename)
                if not prefix:
                    key = filesplit[0]
                else:
                    key = prefix + '_' + filesplit[0]
                if filesplit[1] in suffixes:
                    assert key in output.keys()

                    # Compare contents of each file
                    with open(os.path.join(dirpath, filename), 'r', encoding='utf8') as f:
                        assert f.read() == output[key]

    @pytest.mark.parametrize("DATA", CONFIGLETS_DATA.values(), ids=CONFIGLETS_DATA.keys())
    def test_get_configlet(self, DATA):
        prefix = DATA.get('prefix', None)
        extension = DATA.get('extension', 'cfg')
        src_folder = DATA['src_folder']

        if prefix:
            output = get_configlet(src_folder=src_folder,
                                   prefix=prefix, extension=extension)
        else:
            output = get_configlet(src_folder=src_folder, extension=extension)
            prefix = "AVD"
        assert isinstance(output, dict)
        self.verify_configlets(src_folder, prefix, extension, output)

    def test_get_configlet_invalid_source(self):
        output = get_configlet()
        assert output == dict()

    def test_get_configlet_none_prefix(self):
        extension = 'cfg'
        output = get_configlet(src_folder=CONFIGLETS_DIR, prefix='none')
        assert isinstance(output, dict)
        self.verify_configlets(CONFIGLETS_DIR, "", extension, output)
