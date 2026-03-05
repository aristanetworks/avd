# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Ansible Vault handler for AVD plugins."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ansible.parsing.vault import match_encrypt_secret

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader


class AVDVaultHandler:
    """Handles Ansible Vault encryption and decryption operations."""

    __slots__ = ("__encrypt_secret", "__encrypt_vault_id", "__loader")

    def __init__(self, loader: DataLoader, vault_id: str | None = None) -> None:
        """
        Initialize the Vault handler.

        Args:
            loader: The Ansible DataLoader instance.
            vault_id: Optional Vault ID to use for encryption. If None, uses the first Vault ID in the list (default Ansible behavior).
        """
        self.__loader = loader

        # Pre-compute encryption credentials if Vault secrets are configured.
        if loader._vault.secrets:
            self.__encrypt_vault_id, self.__encrypt_secret = match_encrypt_secret(loader._vault.secrets, vault_id)
        else:
            self.__encrypt_vault_id = None
            self.__encrypt_secret = None

    @property
    def has_vault_secrets(self) -> bool:
        """Whether Vault secrets are configured."""
        return self.__encrypt_secret is not None

    def encrypt_if_needed(self, data: bytes) -> bytes:
        """
        Encrypt data if needed.

        Args:
            data: Data to potentially encrypt.

        Returns:
            Encrypted data if Vault secrets are configured, otherwise the original data.
        """
        if not self.has_vault_secrets:
            return data

        return self.__loader._vault.encrypt(data, secret=self.__encrypt_secret, vault_id=self.__encrypt_vault_id)

    def decrypt_if_needed(self, data: bytes) -> bytes:
        """
        Decrypt data if needed.

        Args:
            data: Data to potentially decrypt.

        Returns:
            Decrypted data if Vault secrets are configured and data is encrypted, otherwise the original data.

        Raises:
            AnsibleVaultError: If Vault decryption fails.
        """
        if self.has_vault_secrets and self.__loader._vault.is_encrypted(data):
            return self.__loader._vault.decrypt(data)

        return data
