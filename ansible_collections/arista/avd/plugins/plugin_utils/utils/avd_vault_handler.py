# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Ansible Vault handler for AVD plugins."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ansible.parsing.vault import match_encrypt_secret

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultSecret


class AVDVaultHandler:
    """Handles Ansible Vault encryption and decryption operations."""

    _loader: DataLoader
    _encrypt_vault_id: str | None
    _encrypt_secret: VaultSecret | None

    def __init__(self, loader: DataLoader, vault_id: str | None = None) -> None:
        """
        Initialize the vault handler.

        Args:
            loader: The Ansible DataLoader instance.
            vault_id: Optional vault ID to use for encryption. If None, uses the first vault ID in the list (default Ansible behavior).
        """
        self._loader = loader

        # Pre-compute encryption secret if vault is configured
        if loader._vault.secrets:
            self._encrypt_vault_id, self._encrypt_secret = match_encrypt_secret(loader._vault.secrets, vault_id)
        else:
            self._encrypt_vault_id = None
            self._encrypt_secret = None

    @property
    def has_vault(self) -> bool:
        """Whether vault secrets are configured."""
        return bool(self._loader._vault.secrets)

    def encrypt_if_needed(self, data: bytes) -> bytes:
        """
        Encrypt data if vault secrets are configured.

        Args:
            data: Data to potentially encrypt.

        Returns:
            Encrypted data if vault is configured, otherwise the original data.

        """
        if not self.has_vault:
            return data

        return self._loader._vault.encrypt(data, secret=self._encrypt_secret, vault_id=self._encrypt_vault_id)

    def decrypt_if_needed(self, data: bytes) -> bytes:
        """
        Decrypt data if it is vault encrypted.

        Args:
            data: Data to potentially decrypt.

        Returns:
            Decrypted data if it was vault encrypted, otherwise the original data.

        Raises:
            AnsibleVaultError: If vault decryption fails.
        """
        if self.has_vault and self._loader._vault.is_encrypted(data):
            # Vault is configured and data is encrypted, decrypt it
            decrypted_data, _vault_id, _vault_secret = self._loader._vault.decrypt_and_get_vault_id(data)
            return decrypted_data

        # Data is not vaulted or no vault configured - return data as-is
        return data
