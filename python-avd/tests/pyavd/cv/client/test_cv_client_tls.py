# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import shutil
import ssl
import subprocess
from contextlib import nullcontext as does_not_raise
from logging import WARNING
from os import environ
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException
from pyavd._cv.workflows.models import CloudVision, CVTLSConfiguration

if TYPE_CHECKING:
    from pathlib import Path


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


def _cloudvision(
    *,
    servers: tuple[str, ...] = ("127.0.0.1",),
    token: str = "test-token",  # noqa: S107
    tls_configuration: CVTLSConfiguration | None = None,
) -> CloudVision:
    return CloudVision(
        servers=servers,
        token=token,
        username=None,
        password=None,
        tls_configuration=tls_configuration or CVTLSConfiguration(),
    )


def _install_cert_with_openssl_subject_hash(pem_path: str, cert_dir: Path) -> None:
    """Copy `pem_path` into `cert_dir` under the OpenSSL subject-hash filename so the cert is discoverable via `SSL_CERT_DIR`."""
    result = subprocess.run(  # noqa: S603
        ["openssl", "x509", "-in", pem_path, "-noout", "-subject_hash"],  # noqa: S607
        check=True,
        capture_output=True,
        text=True,
    )
    shutil.copy(pem_path, cert_dir / f"{result.stdout.strip()}.0")


# === Test Fixtures ===


@pytest.fixture
def onprem_cvp_self_signed_ca_pem(tmp_path: Path) -> str:
    """Fetch the on-prem CVP's self-signed certificate and write it to a temp PEM file."""
    cvp_server = environ.get("CV_ONPREM_SERVER")
    if not cvp_server:
        pytest.fail("CV_ONPREM_SERVER env variable is not set.")

    # Strip optional scheme and port to extract the host for ssl.get_server_certificate().
    host = cvp_server.split("://")[-1].split(":")[0]
    onprem_cvp_pem = ssl.get_server_certificate((host, 443))
    bundle = tmp_path / "onprem-self-signed-ca.pem"
    bundle.write_text(onprem_cvp_pem)
    return str(bundle)


@pytest.fixture
def clean_ssl_cert_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Flush any pre-existing TLS-related env vars so each test starts from a clear state.

    Covers:
        - `SSL_CERT_FILE` / `SSL_CERT_DIR`: used by Python's `ssl` module and CVClient's TLS resolver.
        - `REQUESTS_CA_BUNDLE` / `CURL_CA_BUNDLE`: used by `requests.Session` when `verify is True`.
    """
    for var in ("SSL_CERT_FILE", "SSL_CERT_DIR", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"):
        monkeypatch.delenv(var, raising=False)


# === TLS Configuration Tests ===

_OS_TRUST_STORE_BOTH = _make_verify_paths(cafile="/etc/ssl/certs/ca-certificates.crt", capath="/etc/ssl/certs")
_OS_TRUST_STORE_CAFILE_ONLY = _make_verify_paths(cafile="/etc/ssl/certs/ca-certificates.crt", capath=None)
_OS_TRUST_STORE_CAPATH_ONLY = _make_verify_paths(cafile=None, capath="/etc/ssl/certs")
_OS_TRUST_STORE_EMPTY = _make_verify_paths(cafile=None, capath=None)


@pytest.mark.parametrize("use_system_certs", [False, True], ids=["USE_SYSTEM_CERTS_FALSE", "USE_SYSTEM_CERTS_TRUE_IGNORED"])
def test_cv_client_configure_tls_settings_verify_disabled(use_system_certs: bool, caplog: pytest.LogCaptureFixture) -> None:
    """Test that when `verify_certs=False`, REST is permissive and `use_system_certs` is ignored."""
    with caplog.at_level(WARNING):
        client = CVClient(
            cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(verify_certs=False, use_system_certs=use_system_certs)),
        )

    assert client._tls.requests_verify is False
    assert client._tls.grpc_tls.root_certificates is None
    assert "no system trust store was found" not in caplog.text


def test_cv_client_configure_tls_settings_use_system_certs_false(caplog: pytest.LogCaptureFixture) -> None:
    """When `use_system_certs=False`, gRPC uses grpcio default roots and requests uses its default verification behavior."""
    with caplog.at_level(WARNING):
        client = CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(use_system_certs=False)))

    assert client._tls.grpc_tls.root_certificates is None
    assert client._tls.requests_verify is True
    assert "no system trust store was found" not in caplog.text


@pytest.mark.usefixtures("clean_ssl_cert_env")
@pytest.mark.parametrize(
    ("os_trust_store", "expected_requests_verify"),
    [
        pytest.param(_OS_TRUST_STORE_BOTH, "/etc/ssl/certs/ca-certificates.crt", id="OS_HAS_BOTH_PREFERS_CAFILE"),
        pytest.param(_OS_TRUST_STORE_CAFILE_ONLY, "/etc/ssl/certs/ca-certificates.crt", id="OS_HAS_CAFILE_ONLY"),
        pytest.param(_OS_TRUST_STORE_CAPATH_ONLY, "/etc/ssl/certs", id="OS_HAS_CAPATH_ONLY"),
    ],
)
def test_cv_client_configure_tls_settings_use_system_certs_true_with_os_trust_store(
    os_trust_store: ssl.DefaultVerifyPaths,
    expected_requests_verify: str,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """When `use_system_certs=True` and the OS has a trust store, both transports use it. cafile is preferred over capath when both are present."""
    with (
        caplog.at_level(WARNING),
        patch("pyavd._cv.client.ssl.get_default_verify_paths", return_value=os_trust_store),
        patch("pyavd._cv.client._read_root_certificates", return_value=b"root-certificates") as mock_read_root_certificates,
    ):
        client = CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(use_system_certs=True)))
        grpc_root_certificates = client._tls.grpc_tls.root_certificates
        requests_verify = client._tls.requests_verify

    assert grpc_root_certificates == b"root-certificates"
    assert requests_verify == expected_requests_verify
    mock_read_root_certificates.assert_called_once_with(os_trust_store.cafile, os_trust_store.capath)
    assert "no system trust store was found" not in caplog.text


@pytest.mark.usefixtures("clean_ssl_cert_env")
def test_cv_client_configure_tls_settings_use_system_certs_true_with_empty_os_trust_store(caplog: pytest.LogCaptureFixture) -> None:
    """When `use_system_certs=True` but the OS has no usable trust store, soft-fall back to library defaults and emit a warning."""
    with (
        caplog.at_level(WARNING),
        patch("pyavd._cv.client.ssl.get_default_verify_paths", return_value=_OS_TRUST_STORE_EMPTY),
        patch("pyavd._cv.client._read_root_certificates", return_value=None),
    ):
        client = CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(use_system_certs=True)))
        grpc_root_certificates = client._tls.grpc_tls.root_certificates
        requests_verify = client._tls.requests_verify

    assert grpc_root_certificates is None
    assert requests_verify is True
    assert "no system trust store was found" in caplog.text


@pytest.mark.usefixtures("clean_ssl_cert_env")
def test_cv_client_configure_tls_settings_user_ssl_cert_dir_env_wins_over_os_default_cafile(monkeypatch: pytest.MonkeyPatch) -> None:
    """When the user sets only `SSL_CERT_DIR` TLS resolver returns `capath` even though an OS-default cafile exists."""
    monkeypatch.setenv("SSL_CERT_DIR", "/user/cert-dir")
    # Simulate what `ssl.get_default_verify_paths()` returns when only SSL_CERT_DIR is set: cafile = OS default, capath = user's value.
    mocked_paths = _make_verify_paths(cafile="/etc/ssl/certs/ca-certificates.crt", capath="/user/cert-dir")

    with (
        patch("pyavd._cv.client.ssl.get_default_verify_paths", return_value=mocked_paths),
        patch("pyavd._cv.client._read_root_certificates", return_value=b"root-certificates"),
    ):
        client = CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(use_system_certs=True)))
        requests_verify = client._tls.requests_verify
        grpc_root_certificates = client._tls.grpc_tls.root_certificates

    assert requests_verify == "/user/cert-dir"
    assert grpc_root_certificates == b"root-certificates"


@pytest.mark.usefixtures("clean_ssl_cert_env")
def test_cv_client_configure_tls_settings_user_both_env_vars_set_does_not_flip_precedence(monkeypatch: pytest.MonkeyPatch) -> None:
    """When the user sets both env vars, cafile wins."""
    monkeypatch.setenv("SSL_CERT_FILE", "/user/file.pem")
    monkeypatch.setenv("SSL_CERT_DIR", "/user/cert-dir")
    mocked_paths = _make_verify_paths(cafile="/user/file.pem", capath="/user/cert-dir")

    with (
        patch("pyavd._cv.client.ssl.get_default_verify_paths", return_value=mocked_paths),
        patch("pyavd._cv.client._read_root_certificates", return_value=b"root-certificates"),
    ):
        client = CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(use_system_certs=True)))
        requests_verify = client._tls.requests_verify

    assert requests_verify == "/user/file.pem"


@pytest.mark.usefixtures("clean_ssl_cert_env")
@pytest.mark.parametrize("env_var", ["REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"])
def test_cv_client_configure_tls_settings_unaffected_by_requests_bundle_env_vars(env_var: str, monkeypatch: pytest.MonkeyPatch) -> None:
    """The resolver must not read `REQUESTS_CA_BUNDLE` / `CURL_CA_BUNDLE`."""
    monkeypatch.setenv(env_var, "/some/path.pem")

    client = CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(use_system_certs=False)))

    # Resolver returns True. requests will substitute the env var later, in Session.merge_environment_settings.
    assert client._tls.requests_verify is True
    assert client._tls.grpc_tls.root_certificates is None


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
        pytest.param(True, False, id="USE_GRPCIO_DEFAULT_ROOTS"),
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

    CVaaS endpoints use publicly-trusted CAs present in grpcio default roots and any standard OS trust store.
    Every combination is expected to succeed on a normal CI runner.
    """
    with does_not_raise():
        async with CVClient(
            cloudvision=_cloudvision(
                servers=(targeted_cv["cv_server"],),
                token=targeted_cv["cv_access_token"],
                tls_configuration=CVTLSConfiguration(verify_certs=verify_certs, use_system_certs=use_system_certs),
            ),
        ) as cvclient:
            result = await cvclient.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
        assert result == []


# === Live TLS Tests against on-prem CVP ===


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy TLS tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.usefixtures("clean_ssl_cert_env")
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_cvclient_tls_onprem_verify_disabled() -> None:
    """With `verify_certs=False` the handshake completes against the self-signed on-prem CVP."""
    server = environ.get("CV_ONPREM_SERVER", "")
    token = environ.get("CV_ONPREM_ACCESS_TOKEN", "")
    async with CVClient(cloudvision=_cloudvision(servers=(server,), token=token, tls_configuration=CVTLSConfiguration(verify_certs=False))) as cvclient:
        result = await cvclient.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
    assert result == []


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy TLS tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.usefixtures("clean_ssl_cert_env")
@pytest.mark.parametrize("use_system_certs", [False, True], ids=["USE_GRPCIO_DEFAULT_ROOTS", "USE_SYSTEM_CERTS_NO_OVERRIDE"])
async def test_cvclient_tls_onprem_verify_enabled_fails_without_trusted_ca(use_system_certs: bool) -> None:
    """With `verify_certs=True` and no trusted CA in scope, the handshake fails for both grpcio default roots or the OS trust store."""
    server = environ.get("CV_ONPREM_SERVER", "")
    token = environ.get("CV_ONPREM_ACCESS_TOKEN", "")
    with pytest.raises(CVClientException, match="SSL"):
        async with CVClient(
            cloudvision=_cloudvision(servers=(server,), token=token, tls_configuration=CVTLSConfiguration(use_system_certs=use_system_certs))
        ) as cvclient:
            await cvclient.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy TLS tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.usefixtures("clean_ssl_cert_env")
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_cvclient_tls_onprem_verify_enabled_succeeds_with_ssl_cert_file_override(
    onprem_cvp_self_signed_ca_pem: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """With `verify_certs=True`, `use_system_certs=True`, and `SSL_CERT_FILE` pointing at the on-prem CVP's self-signed CA, the handshake succeeds."""
    server = environ.get("CV_ONPREM_SERVER", "")
    token = environ.get("CV_ONPREM_ACCESS_TOKEN", "")
    monkeypatch.setenv("SSL_CERT_FILE", onprem_cvp_self_signed_ca_pem)

    async with CVClient(cloudvision=_cloudvision(servers=(server,), token=token, tls_configuration=CVTLSConfiguration(use_system_certs=True))) as cvclient:
        result = await cvclient.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
    assert result == []


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy TLS tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.usefixtures("clean_ssl_cert_env")
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_cvclient_tls_onprem_verify_enabled_succeeds_with_ssl_cert_dir_override(
    onprem_cvp_self_signed_ca_pem: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """With `verify_certs=True`, `use_system_certs=True`, and `SSL_CERT_DIR` pointing at a dir with the on-prem CVP's self-signed CA, the handshake succeeds."""
    cert_dir = tmp_path / "ssl-certs"
    cert_dir.mkdir()
    _install_cert_with_openssl_subject_hash(onprem_cvp_self_signed_ca_pem, cert_dir)
    monkeypatch.setenv("SSL_CERT_DIR", str(cert_dir))

    server = environ.get("CV_ONPREM_SERVER", "")
    token = environ.get("CV_ONPREM_ACCESS_TOKEN", "")
    async with CVClient(cloudvision=_cloudvision(servers=(server,), token=token, tls_configuration=CVTLSConfiguration(use_system_certs=True))) as cvclient:
        result = await cvclient.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
    assert result == []
