# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

try:
    from yaml import CSafeDumper as YamlDumper
except ImportError:
    from yaml import YamlDumper


# https://ttl255.com/yaml-anchors-and-aliases-and-how-to-disable-them/
class NoAliasDumper(YamlDumper):
    def ignore_aliases(self, data):
        return True


__all__ = ["NoAliasDumper", "YamlDumper"]
