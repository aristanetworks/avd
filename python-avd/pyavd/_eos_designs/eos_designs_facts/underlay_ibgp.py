# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from collections.abc import Iterable

    from .generator import EosDesignsFactsGeneratorProtocol

MSG_PREFIX = "Invalid combination of inputs."


def _quoted(items: Iterable[str]) -> str:
    """Return the items quoted and comma-separated, in natural sort order, for error messages."""
    return ", ".join(f"'{item}'" for item in natural_sort(items))


class UnderlayIbgpMixin(EosDesignsFactsProtocol, Protocol):
    """
    Mixin Class used to validate the route reflector groups of 'underlay_routing_protocol: ibgp' per device.

    Class should only be used as Mixin to the EosDesignsFacts class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.

    The route reflectors (RRs) sharing the same clients form an RR group, which must be a full mesh with its clients
    and use one 'bgp_cluster_id', unique across the groups:
    - Each client checks that its RRs have the same 'bgp_cluster_id'.
    - Each RR checks that all its clients have the same RRs, and that no RR outside of its group uses its 'bgp_cluster_id'.

    The checks only read data available before rendering the facts: the uplink peers, the inputs of the peers,
    the downlink switches and the shared dict of RRs by cluster ID filled by 'cross_pollinate()'.
    """

    @cached_property
    def _underlay_ibgp_route_reflectors(self: EosDesignsFactsGeneratorProtocol) -> frozenset[str]:
        """
        The iBGP uplink switches of this device, which are its route reflectors.

        Empty if this device is not an iBGP underlay router with 'uplink_type: p2p'.
        Other neighbors are rejected while generating the structured config of either end, with a more specific error.
        """
        if not self.shared_utils.underlay_ibgp or self.shared_utils.uplink_type != "p2p":
            return frozenset()
        return frozenset(peer for peer in self.uplink_peers if self.get_peer_facts_generator(peer).shared_utils.underlay_ibgp)

    def _populate_underlay_ibgp_route_reflectors_by_cluster_id(self: EosDesignsFactsGeneratorProtocol) -> None:
        """
        Register the route reflectors of this device in the shared dict of route reflectors by 'bgp_cluster_id'.

        Only nodes with iBGP clients are registered, so a 'bgp_cluster_id' set on a leaf raises a more specific error later.

        Invoked by the cross_pollinate method.
        """
        for route_reflector in self._underlay_ibgp_route_reflectors:
            if (cluster_id := self.get_peer_facts_generator(route_reflector).shared_utils.node_config.bgp_cluster_id) is not None:
                self._underlay_ibgp_route_reflectors_by_cluster_id.setdefault(cluster_id, set()).add(route_reflector)

    def _validate_underlay_ibgp_uplink_switches(self: EosDesignsFactsGeneratorProtocol) -> None:
        """Validate that the route reflectors of this device have the same 'bgp_cluster_id'."""
        cluster_ids = {
            route_reflector: self.get_peer_facts_generator(route_reflector).shared_utils.node_config.bgp_cluster_id
            for route_reflector in natural_sort(self._underlay_ibgp_route_reflectors)
        }
        if missing := [route_reflector for route_reflector, cluster_id in cluster_ids.items() if cluster_id is None]:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'bgp_cluster_id' on all route reflectors, but it is not set on {_quoted(missing)}."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        if len(set(cluster_ids.values())) > 1:
            got = ", ".join(f"'{cluster_id}' on '{route_reflector}'" for route_reflector, cluster_id in cluster_ids.items())
            msg = (
                f"{MSG_PREFIX} 'bgp_cluster_id' must be the same on all the uplink switches of a node with 'underlay_routing_protocol: ibgp', "
                f"since they are route reflectors for the same clients, but got {got}."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

    def _validate_underlay_ibgp_route_reflector_group(self: EosDesignsFactsGeneratorProtocol) -> None:
        """
        Validate that this route reflector forms a full mesh with its clients, and that its 'bgp_cluster_id' is unique per RR group.

        When every route reflector checks that all its clients have the same route reflectors, the RR groups and their clients form full meshes.
        """
        clients = [client for client in natural_sort(self._downlink_switches) if self.get_peer_facts_generator(client)._underlay_ibgp_route_reflectors]
        if not clients:
            return

        first_client, *other_clients = clients
        route_reflectors = self.get_peer_facts_generator(first_client)._underlay_ibgp_route_reflectors
        for client in other_clients:
            if (client_route_reflectors := self.get_peer_facts_generator(client)._underlay_ibgp_route_reflectors) != route_reflectors:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires all clients of a route reflector to have the same 'ibgp' uplink switches, "
                    f"but the uplink switches of '{first_client}' are {_quoted(route_reflectors)}, "
                    f"while those of '{client}' are {_quoted(client_route_reflectors)}."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        # A missing 'bgp_cluster_id' is reported by the clients.
        if (cluster_id := self.shared_utils.node_config.bgp_cluster_id) is None:
            return

        # TODO: Verify if EOS accepts the integer form of the cluster ID, like '33686018' for '2.2.2.2'.
        # If it does, compare normalized values here. If not, add a pattern for the dotted form to the 'bgp_cluster_id' schema.
        if other_route_reflectors := self._underlay_ibgp_route_reflectors_by_cluster_id[cluster_id] - route_reflectors:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires a unique 'bgp_cluster_id' per group of route reflectors, "
                f"but '{cluster_id}' is used by the group {_quoted(route_reflectors)} and also by {_quoted(other_route_reflectors)}."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)
