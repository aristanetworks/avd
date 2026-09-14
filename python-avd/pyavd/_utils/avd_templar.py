# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar


class AVDTemplar:
    """
    Wrapper around Ansible Templar that also stores the DataLoader and searchpath.

    This allows us to pass templar, loader, and searchpath together,
    avoiding the need to access templar._loader and templar.environment (which are deprecated).

    Attributes:
        templar: Ansible Templar instance
        loader: Ansible DataLoader instance
        searchpath: List of paths to search for templates
    """

    templar: Templar
    """Ansible Templar instance"""

    loader: DataLoader
    """Ansible DataLoader instance"""

    searchpath: list[str]
    """List of paths to search for templates"""

    ansible_above_2_19: bool
    """Bool to signal if we are running on Ansible 2.19 or above."""

    def __init__(self, templar: Templar, loader: DataLoader, searchpath: list[str], ansible_above_2_19: bool) -> None:
        """
        Initialize AVDTemplar with an Ansible Templar, DataLoader, and searchpath.

        Args:
            templar: Ansible Templar instance
            loader: Ansible DataLoader instance
            searchpath: List of paths to search for templates
            ansible_above_2_19: Bool to signal if we are running on Ansible 2.19 or above.
        """
        self.templar = templar
        self.loader = loader
        self.searchpath = searchpath
        self.ansible_above_2_19 = ansible_above_2_19
