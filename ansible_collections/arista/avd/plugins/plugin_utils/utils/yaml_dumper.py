# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import yaml


# https://ttl255.com/yaml-anchors-and-aliases-and-how-to-disable-them/
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True
