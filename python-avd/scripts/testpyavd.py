#!/usr/bin/env python3

# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from sys import path
from timeit import repeat

# Override global path to load pyavd from pwd instead of any installed version.
path.insert(0, ".")

print(
    repeat(
        'from pyavd import eos_cli_config_gen; print(eos_cli_config_gen("test", {"ethernet_interfaces": [{"name": "Ethernet1", "shutdown": False}]}))',
        number=1,
        repeat=10,
    )
)

import cProfile
import pstats

from pyavd import eos_cli_config_gen

cprofile_file = "testpyavd-firstrun.prof"
profiler = cProfile.Profile()
profiler.enable()

print(eos_cli_config_gen("test", {}))

profiler.disable()
stats = pstats.Stats(profiler).sort_stats("cumtime")
stats.dump_stats(cprofile_file)

cprofile_file = "testpyavd-secondrun.prof"
profiler = cProfile.Profile()
profiler.enable()

print(eos_cli_config_gen("test", {}))

profiler.disable()
stats = pstats.Stats(profiler).sort_stats("cumtime")
stats.dump_stats(cprofile_file)
