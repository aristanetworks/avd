# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import os
import tempfile
from functools import cache
from pathlib import Path

from ansible import constants as ansible_constants


def get_tmp_path() -> Path:
    """
    Return a Path object set to the directory where to place temporary AVD files.

    The Path will be created if missing with 700 permissions.

    This can be set to one of the following (in order):
    - The environment variable AVDTMPDIR.
      Note this will *not* be cleaned up automatically. It should only be used for debugging or AVD CI purposes.
    - An "arista_avd" directory under Ansible's "local_tmp" directory which will be removed after the play by Ansible.
    - Fall back to "arista_avd_<random>" directory under the system default temp directory.
    """
    # Return the same tmp_path as last time unless ansible cleaned it up in the meanwhile. Ansible maintains a separate local_tmp folder per play.
    tmp_path = _cached_tmp_path()
    if not tmp_path.exists():
        _cached_tmp_path.cache_clear()
        return _cached_tmp_path()
    return tmp_path


@cache
def _cached_tmp_path() -> Path:
    """Create and return a new tmp_path. Cached for next time."""
    path_str = os.environ.get("AVDTMPDIR")
    if not path_str and hasattr(ansible_constants, "DEFAULT_LOCAL_TMP"):
        path_str = ansible_constants.DEFAULT_LOCAL_TMP
    if not path_str:
        path_str = tempfile.mkdtemp(prefix="arista_avd_")

    # If using Ansible/system tmp, append our subdir to keep things organized.
    tmp_path = Path(path_str)
    if "arista_avd" not in tmp_path.name:
        tmp_path = tmp_path / "arista_avd"

    try:
        tmp_path.mkdir(mode=0o700, parents=True, exist_ok=True)
    except (PermissionError, OSError) as e:
        msg = f"Unable to create AVD temporary directory {tmp_path}: {e}"
        raise type(e)(msg) from e

    return tmp_path
