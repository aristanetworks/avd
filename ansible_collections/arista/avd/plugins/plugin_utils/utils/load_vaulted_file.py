# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Utility function to load files with optional vault decryption."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader


def load_vaulted_file(loader: DataLoader, file_path: Path | str) -> bytes:
    """
    Load a file efficiently, with vault decryption only if needed.

    Args:
        loader: The Ansible DataLoader instance.
        file_path: Path to the file to load.

    Returns:
        Raw file content as bytes (decrypted if vaulted).

    Raises:
        AnsibleVaultError: If vault decryption fails.
    """
    file_content = Path(file_path).read_bytes()

    has_vault = bool(loader._vault.secrets)

    if has_vault and loader._vault.is_encrypted(file_content):
        decrypted_data, _vault_id, _vault_secret = loader._vault.decrypt_and_get_vault_id(file_content)
        return decrypted_data

    # File is not vaulted or no vault configured - return content as-is
    return file_content
