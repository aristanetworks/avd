# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Picklable wrapper for Ansible DataLoader with vault encryption and file loading support."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

from ansible.parsing.vault import match_encrypt_secret

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader


class LoaderWrapper:
    """
    Picklable wrapper for DataLoader that handles vault encryption and file loading.

    Attributes:
        loader: The Ansible DataLoader instance.
        vault_id: Optional vault identity to use for encryption.
        has_vault: Whether vault secrets are configured.
    """

    loader: DataLoader
    vault_id: str | None
    has_vault: bool

    def __init__(self, loader: DataLoader, vault_id: str | None = None) -> None:
        """
        Initialize the wrapper with a DataLoader instance.

        Args:
            loader: The Ansible DataLoader instance.
            vault_id: Optional vault identity to use for encryption. If None, uses the first
                     vault identity in the list (default Ansible behavior).
        """
        self.loader = loader
        self.vault_id = vault_id
        self.has_vault = bool(loader._vault.secrets)

    def load_file(self, file_path: Path | str) -> bytes:
        """
        Load a file efficiently, with vault decryption only if needed.

        When vault is configured: checks if file is vaulted and decrypts if needed

        Args:
            file_path: Path to the file to load.

        Returns:
            bytes: Raw file content (decrypted if vaulted).

        Raises:
            AnsibleVaultError: If vault decryption fails.
        """
        # Read file content
        file_content = Path(file_path).read_bytes()

        if self.has_vault and self.loader._vault.is_encrypted(file_content):
            decrypted_data, _vault_id, _vault_secret = self.loader._vault.decrypt_and_get_vault_id(file_content)
            return decrypted_data

        return file_content

    def load_file_as_json(self, file_path: Path | str) -> dict[str, Any]:
        """
        Load a JSON file efficiently, with vault decryption only if needed.

        This is a convenience method that combines load_file() with JSON parsing.

        Args:
            file_path: Path to the JSON file to load.

        Returns:
            Parsed JSON data as a dictionary.

        Raises:
            AnsibleVaultError: If vault decryption fails.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        file_content = self.load_file(file_path)
        return json.loads(file_content)

    def encrypt_if_needed(self, data: bytes) -> bytes:
        """
        Encrypt data if vault secrets are configured.

        Args:
            data: Data to potentially encrypt.

        Returns:
            Encrypted data if vault is configured, otherwise the original data.

        Note:
            - If vault_id is None, uses the first vault identity in the list.
            - If vault_id is specified, uses that specific vault identity's secret.
            - We use match_encrypt_secret() to find the correct secret and pass both
              secret and vault_id to encrypt() due to an Ansible bug where
              encrypt(data, secret=None, vault_id='X') sets the header to 'X' but
              uses the first secret for encryption.
        """
        if not self.has_vault:
            return data

        vault_id, secret = match_encrypt_secret(self.loader._vault.secrets, self.vault_id)

        # Pass both secret and vault_id to work around Ansible VaultLib bug
        # match_encrypt_secret is called without passing the vault_id if secret=None...
        # https://github.com/ansible/ansible/blob/29086acfa61f32a9e5b087abdaf4336330ab5456/lib/ansible/parsing/vault/__init__.py#L606
        return self.loader._vault.encrypt(data, secret=secret, vault_id=vault_id)
