# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest


######################
## Helper functions ##
######################
def unset_proxy_related_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unsets all proxy-related environment variables prior to the start of the proxy tests."""
    for env_var in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY", "no_proxy", "NO_PROXY"]:
        monkeypatch.delenv(env_var, raising=False)


def form_proxy_string(
    proxy_schema: str | None, proxy_username: str | None, proxy_password: str | None, proxy_host: str | None, proxy_port: str | int | None
) -> str:
    """Forms proxy server URL based on the input variables."""
    if proxy_username and proxy_password:
        return f"{proxy_schema}://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port!s}"  # NOSONAR

    return f"{proxy_schema}://{proxy_host}:{proxy_port!s}"
