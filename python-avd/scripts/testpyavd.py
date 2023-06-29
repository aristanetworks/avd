#!/usr/bin/env python3

from timeit import repeat

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
