# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""File handler with automatic Ansible Vault support for AVD plugins."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

# Remove once we drop ansible-core <2.20; ansible-test then pins coverage >=7.10.1.
if TYPE_CHECKING:  # pragma: no cover
    from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_vault_handler import AVDVaultHandler


class AVDFileHandler:
    """Handles file operations with automatic Ansible Vault support."""

    _vault_handler: AVDVaultHandler

    def __init__(self, vault_handler: AVDVaultHandler) -> None:
        """
        Initialize the file handler.

        Args:
            vault_handler: The AVDVaultHandler instance to use for Vault operations.
        """
        self._vault_handler = vault_handler

    def read_file(self, file_path: Path | str) -> bytes:
        """
        Read a file with automatic Vault decryption, returning raw bytes.

        This method reads a file and automatically decrypts it if it is Vault encrypted.

        Args:
            file_path: Path to the file to read.

        Returns:
            Raw file content as bytes (decrypted if Vault encrypted).
        """
        file_content = Path(file_path).read_bytes()
        return self._vault_handler.decrypt_if_needed(file_content)

    def write_file(self, file_path: Path | str, data: bytes) -> None:
        """
        Write bytes to a file with automatic Vault encryption.

        This method encrypts the data if Vault secrets are configured, then writes to the file.

        Args:
            file_path: Path to the file to write.
            data: Raw bytes to write.
        """
        encrypted_data = self._vault_handler.encrypt_if_needed(data)
        Path(file_path).write_bytes(encrypted_data)

    def load_json(self, file_path: Path | str) -> Any:
        """
        Load and parse a JSON file with automatic Vault decryption.

        Args:
            file_path: Path to the JSON file to load.

        Returns:
            Parsed JSON data as a Python object.
        """
        file_content = self.read_file(file_path)
        return json.loads(file_content)
