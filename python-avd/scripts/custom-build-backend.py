# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from subprocess import Popen

from setuptools import build_meta as _orig
from setuptools.build_meta import *  # noqa: F401,F403 # pylint:disable=wildcard-import,unused-wildcard-import


def get_requires_for_build_wheel(config_settings=None):
    print("Running 'make dep' to vendor various scripts and templates from arista.avd ansible collection")
    with Popen("make dep", shell=True) as make_process:
        if make_process.wait() != 0:
            raise RuntimeError("Something went wrong during 'make dep'")
    return _orig.get_requires_for_build_wheel(config_settings)
