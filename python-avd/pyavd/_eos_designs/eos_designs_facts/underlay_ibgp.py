# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from collections.abc import Mapping

    from .generator import EosDesignsFactsGenerator

MSG_PREFIX = "Invalid combination of inputs."


def validate_underlay_ibgp_route_reflectors(peer_facts_generators: Mapping[str, EosDesignsFactsGenerator]) -> None:
    """
    Validate the route reflector groups and their cluster IDs for 'underlay_routing_protocol: ibgp', once for the whole fabric.

    Must be called after 'cross_pollinate()'.

    The clients of a route reflector (RR) are its downlink switches. The RRs sharing the same clients form an RR group,
    which must be a full mesh with its clients and use one 'bgp_cluster_id', unique across the groups.

    Only iBGP underlay routers with 'uplink_type: p2p' are considered as clients, and only their iBGP uplink switches as RRs.
    Other neighbors are rejected while generating the structured config of either end, with a more specific error.

    Raises:
        AristaAvdInvalidInputsError: If an RR group is not a full mesh, or if its 'bgp_cluster_id' is missing, inconsistent or used by another group.
    """
    rrs_by_client: dict[str, frozenset[str]] = {}
    clients_by_rr: dict[str, list[str]] = {}
    for hostname, generator in peer_facts_generators.items():
        if not generator.shared_utils.underlay_ibgp or generator.shared_utils.uplink_type != "p2p":
            continue
        if not (rrs := [peer for peer in generator.uplink_peers if generator.get_peer_facts_generator(peer).shared_utils.underlay_ibgp]):
            continue
        rrs_by_client[hostname] = frozenset(rrs)
        for rr in rrs:
            clients_by_rr.setdefault(rr, []).append(hostname)

    members_by_cluster_id: dict[str, list[str]] = {}
    grouped_rrs: set[str] = set()
    for rr, clients in clients_by_rr.items():
        if rr in grouped_rrs:
            continue

        members = _get_rr_group_members(rr, clients, rrs_by_client, clients_by_rr)
        grouped_rrs.update(members)

        cluster_ids = {member: peer_facts_generators[member].shared_utils.node_config.bgp_cluster_id for member in members}
        if missing := [member for member, cluster_id in cluster_ids.items() if cluster_id is None]:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'bgp_cluster_id' on all route reflectors, but it is not set on {missing}. "
                f"It must be the same on all the route reflectors sharing the same clients: {members}."
            )
            raise AristaAvdInvalidInputsError(msg, host=rr)

        cluster_id, *other_cluster_ids = {cluster_id for cluster_id in cluster_ids.values() if cluster_id is not None}
        if other_cluster_ids:
            msg = f"{MSG_PREFIX} 'bgp_cluster_id' must be the same on all the route reflectors {members} sharing the same clients, but got {cluster_ids}."
            raise AristaAvdInvalidInputsError(msg, host=rr)

        # TODO: Verify if EOS accepts the integer form of the cluster ID, like '33686018' for '2.2.2.2'.
        # If it does, compare normalized values here. If not, add a pattern for the dotted form to the 'bgp_cluster_id' schema.
        if (other_members := members_by_cluster_id.get(cluster_id)) is not None:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires a unique 'bgp_cluster_id' per group of route reflectors, "
                f"but {other_members} and {members} both use '{cluster_id}'."
            )
            raise AristaAvdInvalidInputsError(msg, host=rr)
        members_by_cluster_id[cluster_id] = members


def _get_rr_group_members(
    rr: str,
    clients: list[str],
    rrs_by_client: dict[str, frozenset[str]],
    clients_by_rr: dict[str, list[str]],
) -> list[str]:
    """
    Return the naturally sorted RRs of the group of the given RR.

    The group is the common set of RRs of all the clients of the given RR. All the RRs in the group must have the same clients.

    Raises:
        AristaAvdInvalidInputsError: If the clients and the RRs do not form a full mesh.
    """
    first_client = clients[0]
    rr_set = rrs_by_client[first_client]
    for client in clients[1:]:
        if (client_rrs := rrs_by_client[client]) != rr_set:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires all clients of a route reflector to have the same 'ibgp' uplink switches, "
                f"but '{first_client}' has {natural_sort(rr_set)} and '{client}' has {natural_sort(client_rrs)}."
            )
            raise AristaAvdInvalidInputsError(msg, host=rr)

    client_set = frozenset(clients)
    members = natural_sort(rr_set)
    for member in members:
        if (member_clients := frozenset(clients_by_rr[member])) != client_set:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires all route reflectors sharing clients to have the same 'ibgp' downlink switches, "
                f"but '{rr}' has {natural_sort(client_set)} and '{member}' has {natural_sort(member_clients)}."
            )
            raise AristaAvdInvalidInputsError(msg, host=rr)
    return members
