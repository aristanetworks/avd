# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

CV_REGION_TO_SERVER_MAP = {
    "auto": "arista.io",
    "us-central1-a": "cv-prod-us-central1-a.arista.io",
    "us-central1-b": "cv-prod-us-central1-b.arista.io",
    "us-central1-c": "cv-prod-us-central1-c.arista.io",
    "us-4": "cv-prod-us-4.arista.io",
    "apnortheast-1": "cv-prod-apnortheast-1.arista.io",
    "euwest-2": "cv-prod-euwest-2.arista.io",
    "eu-3": "cv-prod-eu-3.arista.io",
    "ausoutheast-1": "cv-prod-ausoutheast-1.arista.io",
    "na-northeast1-b": "cv-prod-na-northeast1-b.arista.io",
    "uk-1": "cv-prod-uk-1.arista.io",
    "india-1": "cv-prod-india-1.arista.io",
    "staging": "cv-staging.corp.arista.io",
    "dev": "cv-dev.corp.arista.io",
    "play": "cv-play.corp.arista.io",
}
CVAAS_STREAMING_PREFIX = "apiserver"
CVAAS_API_PREFIX = "www"

CVAAS_BASE_FQDNS = frozenset(CV_REGION_TO_SERVER_MAP.values())
CVAAS_API_ENDPOINTS = frozenset(f"{CVAAS_API_PREFIX}.{cvaas_base_fqdn}" for cvaas_base_fqdn in CVAAS_BASE_FQDNS)
CVAAS_STREAMING_ENDPOINTS = frozenset(f"{CVAAS_STREAMING_PREFIX}.{cvaas_base_fqdn}" for cvaas_base_fqdn in CVAAS_BASE_FQDNS)
