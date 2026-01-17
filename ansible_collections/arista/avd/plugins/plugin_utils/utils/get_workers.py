# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from multiprocessing import cpu_count


def get_workers(num_hosts: int, ansible_forks: int) -> tuple[int, int]:
    """
    Get the multiprocessing and multithreading worker counts.

    MP workers count: The smallest between CPU count - 1 (leave one for main/OS) and ansible_forks.

    MT workers count: Follow ansible_forks.
    """
    available_cores = max(1, cpu_count() - 1)
    # Don't spawn more workers than there are hosts (to avoid creating idle process for small inventories).
    mp = min(available_cores, ansible_forks, num_hosts) or 1
    mt = min(ansible_forks, num_hosts) or 1
    return mp, mt
