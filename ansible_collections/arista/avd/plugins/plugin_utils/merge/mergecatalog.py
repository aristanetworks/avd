# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

try:
    from deepmerge import always_merger
except ImportError as imp_exc:
    DEEPMERGE_IMPORT_ERROR = imp_exc
else:
    DEEPMERGE_IMPORT_ERROR = None


def merge_catalogs(*args: dict) -> dict:
    """Merge catalogs according to the ANTA catalog structure.

    Args:
    ----
        *args (dict): Catalogs to merge.

    Returns:
    -------
        dict: The merged catalog.

    Raises:
    ------
        AristaAvdError: Raised if the required 'deepmerge' Python library cannot be imported.
    """
    if DEEPMERGE_IMPORT_ERROR:
        raise AristaAvdError(message="AVD requires Python deepmerge to be installed") from DEEPMERGE_IMPORT_ERROR

    merged_catalog = {}
    for catalog in args:
        always_merger.merge(merged_catalog, catalog)

    return merged_catalog
