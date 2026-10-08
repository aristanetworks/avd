# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from multiprocessing import cpu_count


def get_workers(num_devices: int, ansible_forks: int, use_multiprocessing: bool = True) -> tuple[int, int]:
    """
    Calculate the optimal number of multiprocessing and multithreading workers for an Ansible action plugin.

    Args:
        num_devices: Total number of devices to process.
        ansible_forks: Ansible forks setting.
        use_multiprocessing: Use multiprocessing. Returns 0 for mp_workers if false.

    Returns:
        A tuple of (mp_workers, mt_workers):
        - mp_workers: Number of multiprocessing workers. Limited by available CPU cores - 1
          (leaving one for main process/OS), ansible_forks, and num_devices.
          0 if 'use_multiprocessing' is false.
        - mt_workers: Number of multithreading workers. Limited by ansible_forks and num_devices.
    """
    available_cores = max(1, cpu_count() - 1)
    # Don't spawn more workers than there are devices (to avoid creating idle processes for small inventories).
    mp_workers = max(min(available_cores, ansible_forks, num_devices), 1) if use_multiprocessing else 0
    mt_workers = max(min(ansible_forks, num_devices), 1)
    return mp_workers, mt_workers
