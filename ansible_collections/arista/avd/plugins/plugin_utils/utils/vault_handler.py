# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from ansible.parsing.vault import match_encrypt_secret

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader

try:
    from pyavd_utils.passwords import vault_decrypt, vault_encrypt

    HAS_PYAVD_UTILS = True
except ImportError:
    HAS_PYAVD_UTILS = False


class VaultHandler:
    """Picklable wrapper for Ansible Vault secret and vault_id."""

    vault_id: str | None
    secret: str | None

    def __init__(self, loader: DataLoader, vault_id: str | None = None) -> None:
        """
        Initialize the VaultHandler.

        Args:
            loader: Ansible DataLoader with or without configured vault secrets.
            vault_id: Vault identity to use for encryption. If None, uses the first vault identity.
        """
        if not HAS_PYAVD_UTILS:
            msg = "The 'arista.avd' collection requires the 'pyavd-utils' Python library."
            raise ImportError(msg)

        if not loader._vault.secrets:
            # No vault configured - set attributes to None
            self.vault_id = None
            self.secret = None
            return

        # Get the vault_id and secret using Ansible's match_encrypt_secret
        self.vault_id, vault_secret = match_encrypt_secret(loader._vault.secrets, vault_id)
        self.secret = vault_secret.bytes.decode("utf-8") if isinstance(vault_secret.bytes, bytes) else vault_secret.bytes

    def maybe_encrypt(self, data: bytes) -> bytes:
        """
        Encrypt data using Ansible Vault format if vault is configured, otherwise return data unchanged.

        Args:
            data: The plaintext data to encrypt (as bytes).

        Returns:
            The encrypted data as bytes if vault is configured, otherwise original data.
        """
        if self.secret is None:
            return data

        return vault_encrypt(data, self.secret, vault_id=self.vault_id).encode("utf-8")

    def maybe_decrypt(self, encrypted_data: bytes) -> bytes:
        """
        Decrypt data from Ansible Vault format if vault is configured, otherwise return data unchanged.

        Args:
            encrypted_data: The encrypted data as bytes (Ansible Vault format string).

        Returns:
            The decrypted data as bytes if vault is configured, otherwise original data.
        """
        if self.secret is None:
            return encrypted_data

        # Decrypt using vault_decrypt (returns tuple of (bytes, vault_id))
        decrypted_data, _vault_id = vault_decrypt(encrypted_data.decode("utf-8"), self.secret)

        return decrypted_data
