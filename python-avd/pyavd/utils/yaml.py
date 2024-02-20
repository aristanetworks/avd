# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from yaml import dump, load

try:
    from yaml import CDumper as YamlDumper
    from yaml import CLoader as YamlLoader
except ImportError:
    from yaml import YamlDumper, YamlLoader


# https://ttl255.com/yaml-anchors-and-aliases-and-how-to-disable-them/
class NoAliasDumper(YamlDumper):
    def ignore_aliases(self, data):
        return True


def yaml_load(stream):
    return load(stream, Loader=YamlLoader)


def yaml_dump():
    return dump(data=None, stream=None, Dumper=NoAliasDumper)
