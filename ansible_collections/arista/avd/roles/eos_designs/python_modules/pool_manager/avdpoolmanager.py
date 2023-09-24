# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING

from ansible.parsing.yaml.dumper import AnsibleDumper
from yaml import dump, safe_load

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils


class AvdPoolManager:
    """
    Class used to handle pooled resources.

    This class is imported and initialized once in eos_designs_facts
    and given to shared_utils for each device.
    """

    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.changed_id_files: set[Path] = set()

    def save_updated_pools(self):
        for id_file in self.changed_id_files:
            id_file.write_text(dump(self.id_pool_data(id_file), Dumper=AnsibleDumper), encoding="UTF-8")
        self.id_pool_data.cache_clear()

    @lru_cache
    def id_pool_data(self, id_file: Path) -> dict:
        if not id_file.exists():
            # Try to create the dir and file.
            id_file.parent.mkdir(mode=0o775, parents=True, exist_ok=True)
            id_file.touch(mode=0o664)

        # Read from file or assign an empty data model.
        id_data = safe_load(id_file.read_text(encoding="UTF-8")) or {"id_pools": []}

        if not isinstance(id_data, dict) or not isinstance(id_data.get("id_pools"), list):
            raise AristaAvdError(f"Invalid ID pool manager data when reading {id_file}. Expecting {'id_pools': []}")

        return id_data

    def get_id(self, shared_utils: SharedUtils) -> int | None:
        """
        Returns the ID of this device if found in the pool.
        If not found a new entry is inserted and returned.
        """
        fabric_name = get(shared_utils.hostvars, "fabric_name", required=True)
        default_id_file_path = f"{self.output_dir}/data/{fabric_name}-id_assignments.yml"
        id_file = Path(get(shared_utils.hostvars, "pool_manager.id.path", default=default_id_file_path))
        id_data = self.id_pool_data(id_file)

        id_pool = None
        for id_data_id_pool in id_data["id_pools"]:
            if (
                id_data_id_pool.get("fabric_name") == fabric_name
                and id_data_id_pool.get("dc_name") == shared_utils.dc_name
                and id_data_id_pool.get("pod_name") == shared_utils.pod_name
                and id_data_id_pool.get("type") == shared_utils.type
            ):
                id_pool = id_data_id_pool
                break

        if not id_pool:
            # Create a new dict, add to the list of pools.
            id_pool = {
                "fabric_name": fabric_name,
                "dc_name": shared_utils.dc_name,
                "pod_name": shared_utils.pod_name,
                "type": shared_utils.type,
                "id_assignments": [],
            }
            id_data["id_pools"].append(id_pool)

        if id_assignment := get_item(id_pool["id_assignments"], "hostname", shared_utils.hostname):
            # Found an ID, so return quickly.
            return id_assignment["id"]

        pool_sorted_on_id = sorted(id_pool["id_assignments"], key=lambda x: x.get("id"))
        first_available_id = next((index for index, id_assignment in enumerate(pool_sorted_on_id + [{"id": 0}], 1) if id_assignment["id"] != index))
        id_assignment = {
            "hostname": shared_utils.hostname,
            "id": first_available_id,
        }
        id_pool["id_assignments"].append(id_assignment)

        # Since we assigned a new ID, we have to mark the id pool as changed to have it saved once the build is done.
        self.changed_id_files.add(id_file)
        return first_available_id
