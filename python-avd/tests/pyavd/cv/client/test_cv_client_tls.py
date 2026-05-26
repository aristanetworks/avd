# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from logging import WARNING
from os import environ
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException
from pyavd._cv.client.models import CVTLSSettings

if TYPE_CHECKING:
    from pathlib import Path

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


# === Test Helpers ===


def _make_verify_paths(cafile: str | None = None, capath: str | None = None) -> ssl.DefaultVerifyPaths:
    """Build a `ssl.DefaultVerifyPaths` for tests (only cafile and capath attributes are used. All others are just placeholders)."""
    return ssl.DefaultVerifyPaths(
        cafile=cafile,
        capath=capath,
        openssl_cafile_env="SSL_CERT_FILE",
        openssl_cafile="/etc/ssl/cert.pem",
        openssl_capath_env="SSL_CERT_DIR",
        openssl_capath="/etc/ssl/certs",
    )


# === Test Fixtures ===


@pytest.fixture
def onprem_cvp_self_signed_ca_pem(tmp_path: Path) -> str:
    """Fetch the on-prem CVP's self-signed certificate and write it to a temp PEM file."""
    cvp_server = environ.get("CV_ONPREM_SERVER")
    if not cvp_server:
        pytest.skip("CV_ONPREM_SERVER is not set")

    # Strip optional scheme and port to extract the host for ssl.get_server_certificate().
    host = cvp_server.split("://")[-1].split(":")[0]
    onprem_cvp_pem = ssl.get_server_certificate((host, 443))
    bundle = tmp_path / "onprem-self-signed-ca.pem"
    bundle.write_text(onprem_cvp_pem)
    return str(bundle)


# === _resolve_tls_settings Tests ===

_OS_TRUST_STORE_BOTH = _make_verify_paths(cafile="/etc/ssl/certs/ca-certificates.crt", capath="/etc/ssl/certs")
_OS_TRUST_STORE_CAFILE_ONLY = _make_verify_paths(cafile="/etc/ssl/certs/ca-certificates.crt", capath=None)
_OS_TRUST_STORE_CAPATH_ONLY = _make_verify_paths(cafile=None, capath="/etc/ssl/certs")
_OS_TRUST_STORE_EMPTY = _make_verify_paths(cafile=None, capath=None)


@pytest.mark.parametrize("use_system_certs", [False, True], ids=["USE_SYSTEM_CERTS_FALSE", "USE_SYSTEM_CERTS_TRUE_IGNORED"])
def test_cv_client_resolve_tls_settings_verify_disabled(use_system_certs: bool, caplog: pytest.LogCaptureFixture) -> None:
    """Test that when `verify_certs=False`, both GRPC and REST get permissive settings and `use_system_certs` is ignored."""
    with caplog.at_level(WARNING):
        client = CVClient(servers="127.0.0.1", token="test-token", verify_certs=False, use_system_certs=use_system_certs)  # noqa: S106

    tls = client._tls
    assert isinstance(tls, CVTLSSettings)
    assert tls.requests_verify is False
    # gRPC side: permissive context (no hostname check, no peer verification)
    assert isinstance(tls.grpc_ssl, ssl.SSLContext)
    assert tls.grpc_ssl.check_hostname is False
    assert tls.grpc_ssl.verify_mode == ssl.CERT_NONE
    assert "no system trust store was found" not in caplog.text


@pytest.mark.parametrize(
    ("use_system_certs", "mocked_verify_paths", "expected_grpc_ssl", "expected_requests_verify", "warning_expected"),
    [
        pytest.param(False, None, True, True, False, id="USE_SYSTEM_CERTS_FALSE_CERTIFI_DEFAULT"),
        pytest.param(True, _OS_TRUST_STORE_BOTH, _OS_TRUST_STORE_BOTH, "/etc/ssl/certs/ca-certificates.crt", False, id="OS_HAS_BOTH_PREFERS_CAFILE"),
        pytest.param(True, _OS_TRUST_STORE_CAFILE_ONLY, _OS_TRUST_STORE_CAFILE_ONLY, "/etc/ssl/certs/ca-certificates.crt", False, id="OS_HAS_CAFILE_ONLY"),
        pytest.param(True, _OS_TRUST_STORE_CAPATH_ONLY, _OS_TRUST_STORE_CAPATH_ONLY, "/etc/ssl/certs", False, id="OS_HAS_CAPATH_ONLY"),
        pytest.param(True, _OS_TRUST_STORE_EMPTY, True, True, True, id="NO_OS_TRUST_STORE_SOFT_FALLBACK_TO_CERTIFI"),
    ],
)
def test_cv_client_resolve_tls_settings_verify_enabled(
    use_system_certs: bool,
    mocked_verify_paths: ssl.DefaultVerifyPaths | None,
    expected_grpc_ssl: ssl.DefaultVerifyPaths | bool,
    expected_requests_verify: bool | str,
    warning_expected: bool,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test that when `verify_certs=True`, TLS settings depend on `use_system_certs` and OS trust store availability."""
    with (
        caplog.at_level(WARNING),
        patch("pyavd._cv.client.ssl.get_default_verify_paths", return_value=mocked_verify_paths),
    ):
        client = CVClient(servers="127.0.0.1", token="test-token", verify_certs=True, use_system_certs=use_system_certs)  # noqa: S106

    tls = client._tls
    assert isinstance(tls, CVTLSSettings)
    assert tls.grpc_ssl is expected_grpc_ssl
    assert tls.requests_verify == expected_requests_verify
    if warning_expected:
        assert "no system trust store was found" in caplog.text
    else:
        assert "no system trust store was found" not in caplog.text


# === Live TLS Tests against CVaaS ===


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy TLS tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("targeted_cv"),
    [
        pytest.param(
            {
                "cv_access_token": environ.get("CV_PRD_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_PRD_SERVER", default=""),
            },
            id="CVAAS_PRD",
        ),
        pytest.param(
            {
                "cv_access_token": environ.get("CV_STG_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_STG_SERVER", default=""),
            },
            id="CVAAS_STG",
        ),
    ],
)
@pytest.mark.parametrize(
    ("verify_certs", "use_system_certs"),
    [
        pytest.param(False, False, id="VERIFY_CERTS_FALSE"),
        pytest.param(True, False, id="USE_CERTIFI"),
        pytest.param(True, True, id="USE_SYSTEM_CERTS"),
    ],
)
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_cvclient_tls_cvaas(
    targeted_cv: dict[str, str],
    verify_certs: bool,
    use_system_certs: bool,
) -> None:
    """
    Test ability to complete TLS handshake to CVaaS across all `verify_certs` / `use_system_certs` combinations.

    CVaaS endpoints use publicly-trusted CAs present in both `certifi` and any standard OS trust store.
    Every combination is expected to succeed on a normal CI runner.
    """
    with does_not_raise():
        async with CVClient(
            servers=targeted_cv["cv_server"],
            token=targeted_cv["cv_access_token"],
            verify_certs=verify_certs,
            use_system_certs=use_system_certs,
        ) as cvclient:
            result = await cvclient.get_inventory_devices(devices=[(None, None, "nonexisting-avd-ci-hostname")])
        assert result == []


# === Live TLS Tests against on-prem CVP ===


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy TLS tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("verify_certs", "use_system_certs", "use_env_override", "expected_exception"),
    [
        pytest.param(False, False, False, does_not_raise(), id="VERIFY_CERTS_FALSE_SUCCESS"),
        pytest.param(True, False, False, pytest.raises(CVClientException, match="SSL"), id="USE_CERTIFI_UNTRUSTED_FAILURE"),
        pytest.param(True, True, False, pytest.raises(CVClientException, match="SSL"), id="USE_SYSTEM_CERTS_NO_OVERRIDE_FAILURE"),
        pytest.param(True, True, True, does_not_raise(), id="USE_SYSTEM_CERTS_WITH_SSL_CERT_FILE_OVERRIDE_SUCCESS"),
    ],
)
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_cvclient_tls_onprem(
    onprem_cvp_self_signed_ca_pem: str,
    verify_certs: bool,
    use_system_certs: bool,
    use_env_override: bool,
    expected_exception: ExpectedExceptionContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test full TLS handshake against a self-signed on-prem CVP with different `verify_certs` / `use_system_certs` combinations."""
    server = environ.get("CV_ONPREM_SERVER", "")
    token = environ.get("CV_ONPREM_ACCESS_TOKEN", "")
    if not server or not token:
        pytest.skip("CV_ONPREM_SERVER or CV_ONPREM_ACCESS_TOKEN is not set")

    # Flush any pre-existing SSL_CERT_FILE / SSL_CERT_DIR env vars.
    monkeypatch.delenv("SSL_CERT_FILE", raising=False)
    monkeypatch.delenv("SSL_CERT_DIR", raising=False)

    if use_env_override:
        monkeypatch.setenv("SSL_CERT_FILE", onprem_cvp_self_signed_ca_pem)

    with expected_exception:
        async with CVClient(
            servers=server,
            token=token,
            verify_certs=verify_certs,
            use_system_certs=use_system_certs,
        ) as cvclient:
            result = await cvclient.get_inventory_devices(devices=[(None, None, "nonexisting-avd-ci-hostname")])
        assert result == []
