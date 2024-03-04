# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface
from typing import Mapping

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item

from .config_manager import ConfigManager
from .mixins import LoggingMixin


class DeviceUtils(LoggingMixin):
  """"""
  def __init__(self, config_manager: ConfigManager):
    """"""
    super().__init__()
    self.config_manager = config_manager


  def update_interface_shutdown(self, interface: dict, host: str | None = None) -> None:
      """
      Update the interface shutdown key, considering EOS default.

      For Ethernet interfaces:
      - If the interface shutdown key is not set, the host interface_defaults.ethernet.shutdown key is used
      - If the host interface_defaults.ethernet.shutdown key is not set, the interface shutdown key is set to False.

      For other interfaces, the shutdown key is updated using the interface shutdown key if available or set to False.

      Args:
          interface (dict): The interface to verify.
          host (str): Host to verify. Defaults to the host running the test.
      """
      host_struct_cfg = self.config_manager.get_host_structured_config(host=host) if host else self.config_manager.structured_config
      if "Ethernet" in get(interface, "name", ""):
          interface["shutdown"] = default(get(interface, "shutdown"), get(host_struct_cfg, "interface_defaults.ethernet.shutdown"), False)
      else:
          interface["shutdown"] = get(interface, "shutdown", default=False)


  def is_peer_available(self, peer: str) -> bool:
      """
      Check if a peer is deployed by looking at his `is_deployed` key.

      Args:
          peer (str): The peer to verify.

      Returns:
          bool: True if the peer is deployed, False otherwise.
      """
      if peer not in self.config_manager.hostvars:
          self.log_skip_message(message=f"Peer '{peer}' is not configured by AVD.")
          return False
      if not get(self.config_manager.hostvars[peer], "is_deployed", default=True):
          self.log_skip_message(message=f"Peer '{peer}' is marked as not deployed.")
          return False
      return True
  
  def get_interface_ip(self, interface_model: str, interface_name: str, host: str | None = None) -> str | None:
      """
      Retrieve the IP address of a specified host interface.

      Args:
          interface_model (str): Interface model in the structured config (e.g., ethernet_interfaces).
          interface_name (str): Interface name to retrive the IP.
          host (str): Host to verify. Defaults to the host running the test.

      Returns:
          str | None: IP address of the host interface or None if unavailable.
      """
      host_struct_cfg = self.config_manager.get_host_structured_config(host=host) if host else self.config_manager.structured_config
      try:
          # TODO Change var names
          peer_interfaces = get(host_struct_cfg, interface_model, required=True)
          peer_interface = get_item(peer_interfaces, "name", interface_name, required=True)
          return get(peer_interface, "ip_address", required=True)
      except AristaAvdMissingVariableError:
          self.log_skip_message(message=f"Host '{host or self.config_manager.device_name}' interface '{interface_name}' IP address is unavailable.", logging_level="WARNING")
          return None

  def is_subinterface(self, interface: dict) -> bool:
      """
      TODO - Logging
      """
      return "." in interface.get("name", "")