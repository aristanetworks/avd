# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from ansible.parsing.vault import match_encrypt_secret

if TYPE_CHECKING:
    from ansible.parsing.dataloader import DataLoader


class VaultHandler:
    """Picklable wrapper for Ansible Vault secret and vault_id."""

    def __init__(self, loader: DataLoader, vault_id: str | None = None) -> None:
        """
        Initialize the VaultHandler.

        Args:
            loader: Ansible DataLoader with configured vault secrets.
            vault_id: Vault identity to use for encryption. If None, uses the first vault identity.

        Raises:
            Exception: If vault is not configured.
        """
        if not loader._vault.secrets:
            msg = "No vault secret found in the DataLoader"
            raise ValueError(msg)

        self.vault_id, secret = match_encrypt_secret(loader._vault.secrets, vault_id)
        self.secret = secret.bytes.decode("utf-8")


def create_vault_handler(loader: DataLoader, vault_id: str | None = None) -> VaultHandler | None:
    """
    Create a VaultHandler if vault is configured, otherwise return None.

    Args:
        loader: Ansible DataLoader.
        vault_id: Vault identity to use for encryption.

    Returns:
        VaultHandler instance if vault is configured, None otherwise.
    """
    if not loader._vault.secrets:
        return None

    return VaultHandler(loader, vault_id)
