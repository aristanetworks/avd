# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import ssl
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network, ip_address, ip_network
from logging import getLogger
from os import environ
from typing import TYPE_CHECKING, Final, Literal, TypeGuard, overload
from urllib.parse import ParseResult, quote, urlparse

from grpclib.client import Channel
from python_socks.async_.asyncio import Proxy

from pyavd._errors import AristaAvdInvalidInputsError

from .exceptions import CVClientException

if TYPE_CHECKING:
    import socket

    from grpclib.protocol import H2Protocol
    from typing_extensions import Self

    T_ProxyConfigurationSource = Literal["explicit", "https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"]
    T_ProxyEnvVars = Literal["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"]
    T_NoProxyEnvVars = Literal["no_proxy", "NO_PROXY"]
    T_ProxyBypassRuleType = Literal["all", "ipv4_address", "ipv4_cidr", "ipv6_address", "ipv6_cidr", "wildcard_domain", "fqdn"]
    T_HostFormat = Literal["ipv4_address", "ipv6_address", "fqdn"]
    Ip = IPv4Address | IPv6Address
    IpOrStr = IPv4Address | IPv6Address | str
    IpOrCidr = Ip | IPv4Network | IPv6Network


LOGGER = getLogger(__name__)

PROXY_CONFIGURATION_SOURCE: Final[tuple[str, ...]] = ("explicit", "https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY")
PROXY_ENV_VARS: Final[tuple[str, ...]] = ("https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY")
NO_PROXY_ENV_VARS: Final[tuple[str, ...]] = ("no_proxy", "NO_PROXY")


class CVConnectionManager:
    """Connection manager for CloudVision connections."""

    _target_host: str
    _target_port: int
    cv_proxy_manager: CVProxyManager

    def __init__(
        self,
        target_host: str,
        target_port: int,
        proxy_scheme: str | None = None,
        proxy_host: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
    ) -> None:
        """
        Initialize CloudVision connection manager.

        Args:
            target_host: Target CloudVision server hostname.
            target_port: Target CloudVision server port.
            proxy_scheme: Proxy server scheme.
            proxy_host: Proxy server hostname or IP address.
            proxy_port: Proxy server port.
            proxy_username: Proxy server authentication username.
            proxy_password: Proxy server authentication password.
        """
        LOGGER.debug("Initializing CVConnectionManager...")
        # Set attributes related to the target CloudVision instance
        self._target_host = target_host
        self._target_port = target_port

        # Initialize CV proxy manager
        self.cv_proxy_manager = CVProxyManager(
            target_host=target_host,
            target_port=target_port,
            proxy_scheme=proxy_scheme,
            proxy_host=proxy_host,
            proxy_port=proxy_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        )

    def create_proxy_channel(self, ssl_context: ssl.SSLContext | bool) -> Channel:
        """
        Create a gRPC channel using the CloudVision connection manager.

        Args:
            ssl_context: SSL context for destination server connection.

        Returns:
            Configured gRPC Channel instance.
        """
        # Create the channel first
        channel = Channel(host=self._target_host, port=self._target_port, ssl=ssl_context)

        if not self.use_proxy:
            LOGGER.debug("<CVConnectionManager>.create_proxy_channel: No proxy server. Building standard gRPC Channel.")
            return channel

        # Create custom connector that uses proxy
        async def proxy_connection() -> H2Protocol:
            loop = asyncio.get_running_loop()

            try:
                # Create socket through proxy using python-socks
                proxy_sock = await self.cv_proxy_manager.create_socket_for_grpc()

                # Create the gRPC protocol using the proxy socket
                _, protocol = await loop.create_connection(
                    channel._protocol_factory,
                    sock=proxy_sock,
                    ssl=channel._ssl,
                    server_hostname=self._target_host if ssl_context else None,
                )

            except Exception as e:
                msg = f"Failed to create proxy connection: {type(e).__name__}: {e}"
                raise CVClientException(msg) from e

            return protocol

        # Override the standard method from grpclib with our proxy variant.
        LOGGER.debug("<CVConnectionManager>.create_proxy_channel: Proxy server is used. Building gRPC Channel through proxy server.")
        channel._create_connection = proxy_connection
        return channel

    @staticmethod
    def get_ssl_context(verify_certs: bool) -> ssl.SSLContext | bool:
        """
        Initialize the default SSL context with relaxed verification if needed.

        Otherwise we just return True.
        The return value (The default ssl context or True) will be passed to grpclib.
        Requests will pick it up from ssl lib itself.
        """
        if not verify_certs:
            LOGGER.debug("<CVConnectionManager>.get_ssl_context: Using relaxed 'ssl_context' (no hostname or certificate validation).")
            # Accepting SonarLint issue: We are purposely implementing no verification of certs.
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  # NOSONAR
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # NOSONAR
            context.set_alpn_protocols(["h2"])
        else:
            LOGGER.debug("<CVConnectionManager>.get_ssl_context: Using regular 'ssl_context'.")
            context = True
        return context

    @property
    def use_proxy(self) -> bool:
        return self.cv_proxy_manager.use_proxy

    @property
    def requests_proxies(self) -> dict[str, str]:
        return self.cv_proxy_manager.get_requests_proxies()


class CVProxyManager:
    """
    Proxy manager for CloudVision.

    This class handles all work related to discovering proxy server settings and establishing egress connections through it.
    It as well handles proxy bypass.
    """

    use_proxy: bool
    _target_host: str
    _target_host_format: T_HostFormat
    _target_port: int
    _proxy_scheme: str | None
    _proxy_host: str | None
    _proxy_host_format: T_HostFormat | None
    _proxy_port: int | None
    _proxy_username: str | None
    _proxy_password: str | None

    cv_proxy_bypass_manager: CVProxyBypassManager

    _proxy_configuration_source: T_ProxyConfigurationSource
    """Source of the proxy server information."""
    _env_var_proxy_name: T_ProxyEnvVars
    """Name of the selected environment variable."""
    _env_var_proxy_content: str
    """Raw content of the selected environment variables."""
    _parsed_env_var_proxy_content: ParseResult
    """Parsed proxy server information."""

    def __init__(
        self,
        target_host: str,
        target_port: int,
        proxy_scheme: str | None = None,
        proxy_host: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
    ) -> None:
        LOGGER.debug("Initializing CVProxyManager...")
        # Set attributes related to the target CloudVision instance
        self._target_host = target_host
        self._target_port = target_port

        # Do not use proxy server by default
        self.use_proxy = False

        # Check if usage of the proxy server was requested using explicit inputs
        if proxy_host is not None:
            LOGGER.info("<CVProxyManager>: Proxy server information is passed explicitly. Verifying its validity...")

            # Identify format of the proxy host
            self._proxy_host_format = self._identify_host_format(proxy_host)

            # Verify that all mandatory settings comply with validity requirements
            if self._proxy_candidate_is_valid(proxy_scheme, proxy_host, proxy_port, "explicit"):
                LOGGER.debug("<CVProxyManager>: Explicitly passed proxy server information passed all validations.")
                self.use_proxy = True
                self._proxy_configuration_source = "explicit"
                self._proxy_scheme = proxy_scheme
                self._proxy_host = proxy_host
                self._proxy_port = proxy_port
                # Use urllib.parse.quote to convert all special symbols in username and password
                self._proxy_username = quote(proxy_username, safe="") if isinstance(proxy_username, str) else None
                self._proxy_password = quote(proxy_password, safe="") if isinstance(proxy_password, str) else None
                # Valid proxy server settings successfully discovered using explicit parameters
                return

        LOGGER.info("<CVProxyManager>: Trying to discover proxy server settings using environment variables...")
        # Fallback to discovering proxy-related settings passed via environment variables
        # Identify format of the target CloudVision host
        self._target_host_format = self._identify_host_format(self._target_host)
        LOGGER.debug("<CVProxyManager>: Target CloudVision destination is specified using '%s' format.", self._target_host_format)

        LOGGER.debug("<CVProxyManager>: Checking if target CloudVision destination is matching any proxy bypass environment variables...")
        # Check if target CloudVision instance is listed as a part of the proxy bypass variables.
        # Initialize proxy bypass manager
        self.cv_proxy_bypass_manager = CVProxyBypassManager()

        # Check if targeted CloudVision host is matched by the proxy bypass
        if self.cv_proxy_bypass_manager.proxy_bypass_discovered and self.cv_proxy_bypass_manager.bypass_proxy_for_destination(
            self._target_host, self._target_host_format, self._target_port
        ):
            LOGGER.info(
                "<CVProxyManager>: Target CloudVision matched proxy bypass rule specified in environment variable '%s'. Proxy server will not be used by AVD.",
                self.cv_proxy_bypass_manager.env_var_no_proxy_name,
            )
            self.use_proxy = False
            return

        LOGGER.debug("<CVProxyManager>: Target CloudVision has not matched any proxy bypass environment variables.")
        # Read interesting proxy-related environment variables
        self._get_env_proxy()

        if not self.proxy_discovered:
            LOGGER.info("<CVProxyManager>: No proxy environment variables discovered. AVD will not use proxy server.")
            self.use_proxy = False
            return

        LOGGER.info(
            "<CVProxyManager>: Proxy settings were discovered using environment variable '%s'.",
            self._env_var_proxy_name,
        )
        self._parse_env_var_proxy_content()

        # Verify that all mandatory settings comply with validity requirements
        # Raise an exception if any of the explicitly provided settings does not pass validity checks
        LOGGER.debug(
            "<CVProxyManager>: Verifying validity of the proxy settings discovered using environment variable '%s'.",
            self._env_var_proxy_name,
        )
        if self._proxy_candidate_is_valid(
            self._parsed_env_var_proxy_content.scheme,
            self._parsed_env_var_proxy_content.hostname,
            self._parsed_env_var_proxy_content.port,
            self._env_var_proxy_name,
        ):
            # Identify format of the proxy host
            self._proxy_host_format = self._identify_host_format(self._parsed_env_var_proxy_content.hostname)

            self.use_proxy = True
            self._proxy_configuration_source = self._env_var_proxy_name
            self._proxy_scheme = self._parsed_env_var_proxy_content.scheme
            self._proxy_host = self._parsed_env_var_proxy_content.hostname
            self._proxy_port = self._parsed_env_var_proxy_content.port
            # Proxy username and password in evn variables are expected to have all special symbols quoted
            self._proxy_username = self._parsed_env_var_proxy_content.username
            self._proxy_password = self._parsed_env_var_proxy_content.password
            LOGGER.info(
                "<CVProxyManager>: Discovered proxy server settings passed all validity checks. AVD will use proxy server '%s'.",
                self.get_proxy_url(hide_password=True),
            )

    def _get_env_proxy(self) -> None:
        LOGGER.debug("<CVProxyManager>: Reading proxy environment variables: '%s'...", PROXY_ENV_VARS)
        for env_variable_candidate in PROXY_ENV_VARS:
            if env_proxy_candidate := environ.get(env_variable_candidate):
                LOGGER.debug("<CVProxyManager>: Environment variable '%s' is found.", env_variable_candidate)
                self._env_var_proxy_name = env_variable_candidate
                self._env_var_proxy_content = env_proxy_candidate
                return
        LOGGER.debug("<CVProxyManager>: No proxy environment variables found.")

    def _parse_env_var_proxy_content(self) -> None:
        LOGGER.debug("<CVProxyManager>: Parsing content of the environment variable '%s'...", self._env_var_proxy_name)
        try:
            self._parsed_env_var_proxy_content = urlparse(self._env_var_proxy_content)
            # urlparse will success parsing any URL <str> but will raise at access time if port value is invalid
            # Try accessing proxy port attribute to catch any issues with its value
            _ = self._parsed_env_var_proxy_content.port
        except Exception as e:
            msg = (
                f"AVD faced an exception trying to extract proxy server settings from string '{self._env_var_proxy_content}' learned using environment"
                f" variable '{self._env_var_proxy_name}'"
            )
            raise AristaAvdInvalidInputsError(msg) from e

    def _proxy_candidate_is_valid(
        self,
        proxy_scheme_candidate: str | None,
        proxy_host_candidate: str | None,
        proxy_port_candidate: int | None,
        candidate_source: T_ProxyConfigurationSource | None,
    ) -> bool:
        """Verify that all mandatory proxy server sub-settings are set and valid for the proxy server candidate."""
        return all(
            [
                self._proxy_scheme_is_valid(proxy_scheme_candidate, candidate_source),
                self._proxy_host_is_valid(proxy_host_candidate, candidate_source),
                self._proxy_port_is_valid(proxy_port_candidate, candidate_source),
            ]
        )

    def get_requests_proxies(self) -> dict[str, str]:
        """
        Generate proxy configuration for requests library.

        When proxy server is used we explicitly pass `"no_proxy": "_"` to prevent `requests`/`urllib` from reading `no_proxy`/`NO_PROXY`
        again as we already did this.
        When proxy server is not used we pass `"no_proxy": self.target_host` to make sure `requests`/`urllib` don't fallback to using proxy for cv_deploy flows.

        Returns:
            Dictionary with proxy configuration for requests.
        """
        return {"http": self.get_proxy_url(), "https": self.get_proxy_url(), "no_proxy": "_"} if self.use_proxy else {"no_proxy": self._target_host}

    async def create_socket_for_grpc(self) -> socket.socket:
        """
        Create a socket for gRPC connections through the proxy.

        Returns:
            Raw socket connected to target through proxy.
        """
        LOGGER.debug("<CVProxyManager>.create_socket_for_grpc: Building a Socket through a proxy server...")
        # Create proxy using python-socks
        proxy = Proxy.from_url(self.get_proxy_url())

        # Connect through proxy to target
        return await proxy.connect(dest_host=self._target_host, dest_port=self._target_port)

    @overload
    @staticmethod
    def _identify_host_format(host: None) -> None: ...

    @overload
    @staticmethod
    def _identify_host_format(host: str) -> Literal["ipv4_address", "ipv6_address", "fqdn"]: ...

    @staticmethod
    def _identify_host_format(host: str | None) -> Literal["ipv4_address", "ipv6_address", "fqdn"] | None:
        if host is None:
            return None
        """Identify if host is passed as an IPv4 address, an IPv6 address or an FQDN."""
        try:
            # Check if used format is IPv4 or IPv6 address
            ip_candidate = ip_address(host)
            match ip_candidate.version:
                case 4:
                    return "ipv4_address"
                # It is IPv6 otherwise
                case _:
                    return "ipv6_address"
        # The only exception that can be raised is a ValueError meaning input string was not an IP address
        except ValueError:
            # If it is not an IPv4 or IPv6 address we treat it as an FQDN.
            return "fqdn"

    @staticmethod
    def _proxy_scheme_is_valid(proxy_scheme_candidate: str | None, candidate_source: T_ProxyConfigurationSource | None) -> TypeGuard[str]:
        """
        Verifies validity of the requested proxy server scheme.

        Raises:
            AristaAvdInvalidInputsError if provided proxy_scheme_candidate is not compliant with AVD requirements.
        """
        if not (result := proxy_scheme_candidate == "http"):
            msg = f"Scheme '{proxy_scheme_candidate}' of the proxy server requested via '{candidate_source}' is not supported by AVD."
            raise AristaAvdInvalidInputsError(msg)

        return result

    @staticmethod
    def _proxy_host_is_valid(proxy_host_candidate: str | None, candidate_source: T_ProxyConfigurationSource | None) -> TypeGuard[str]:
        """
        Verifies validity of the requested proxy server host.

        Raises:
            AristaAvdInvalidInputsError if provided proxy_host_candidate is not compliant with AVD requirements.
        """
        if not (result := isinstance(proxy_host_candidate, str) and len(proxy_host_candidate) > 0):
            msg = f"Host '{proxy_host_candidate}' of the proxy server requested via '{candidate_source}' is not supported by AVD."
            raise AristaAvdInvalidInputsError(msg)

        return result

    @staticmethod
    def _proxy_port_is_valid(proxy_port_candidate: int | None, candidate_source: T_ProxyConfigurationSource | None) -> TypeGuard[int]:
        """
        Verifies validity of the requested proxy server port.

        Raises:
            AristaAvdInvalidInputsError if provided proxy_port_candidate is not compliant with AVD requirements.
        """
        if not (result := isinstance(proxy_port_candidate, int) and 1 <= proxy_port_candidate <= 65535):
            msg = f"Port '{proxy_port_candidate!s}' of the proxy server requested via '{candidate_source}' is not supported by AVD."
            raise AristaAvdInvalidInputsError(msg)

        return result

    @staticmethod
    def _proxy_username_is_set(proxy_username_candidate: str | None) -> TypeGuard[str]:
        """Verifies if proxy server username is set."""
        return isinstance(proxy_username_candidate, str) and len(proxy_username_candidate) > 0

    @staticmethod
    def _proxy_password_is_set(proxy_password_candidate: str | None) -> TypeGuard[str]:
        """Verifies if proxy server password is set."""
        return isinstance(proxy_password_candidate, str) and len(proxy_password_candidate) > 0

    @property
    def proxy_discovered(self) -> bool:
        return bool(self.get_env_var_proxy_name() and self.get_env_var_proxy_content())

    def get_env_var_proxy_name(self) -> T_ProxyEnvVars | None:
        return getattr(self, "_env_var_proxy_name", None)

    def get_env_var_proxy_content(self) -> str | None:
        return getattr(self, "_env_var_proxy_content", None)

    def get_proxy_url(self, hide_password: bool = False) -> str:
        """
        Generate proxy URL.

        Returns:
            HTTP proxy URL.
        """
        if not self.use_proxy:
            return ""
        formatted_proxy_host = f"[{self._proxy_host}]" if self._proxy_host_format == "ipv6_address" else self._proxy_host
        if self._proxy_username_is_set(self._proxy_username) and self._proxy_password_is_set(self._proxy_password):
            # Excempting the lines below from Sonar since we cannot use HTTPS here.
            return (
                f"{self._proxy_scheme}://"
                f"{self._proxy_username}:"
                f"{'<removed>' if hide_password else self._proxy_password}@"
                f"{formatted_proxy_host}:"
                f"{self._proxy_port}"
            )  # NOSONAR
        return f"{self._proxy_scheme}://{formatted_proxy_host}:{self._proxy_port}"  # NOSONAR


class CVProxyBypassManager:
    """
    Proxy bypass manager for CloudVision connections.

    This class verifies if egress connections towards CloudVision should bypass proxy server.
    Decision is made based on the content of the special environment variables and targeted CloudVision server.
    """

    _env_var_no_proxy_name: T_NoProxyEnvVars
    """Name of the used environment variable."""
    _env_var_no_proxy_content: str
    """Raw content of the `no_proxy` or `NO_PROXY` environment variables."""
    _all_no_proxy_rule: bool
    _ipv4_address_no_proxy_rules: list[ProxyBypassRule]
    _ipv4_cidr_no_proxy_rules: list[ProxyBypassRule]
    _ipv6_address_no_proxy_rules: list[ProxyBypassRule]
    _ipv6_cidr_no_proxy_rules: list[ProxyBypassRule]
    _wildcard_domain_no_proxy_rules: list[ProxyBypassRule]
    _fqdn_no_proxy_rules: list[ProxyBypassRule]

    def __init__(self) -> None:
        LOGGER.debug("Initializing CVProxyBypassManager...")
        self._all_no_proxy_rule = False
        self._ipv4_address_no_proxy_rules = []
        self._ipv4_cidr_no_proxy_rules = []
        self._ipv6_address_no_proxy_rules = []
        self._ipv6_cidr_no_proxy_rules = []
        self._wildcard_domain_no_proxy_rules = []
        self._fqdn_no_proxy_rules = []

        # Read interesting environment variables
        self._get_env_no_proxy()

        if not self.proxy_bypass_discovered:
            LOGGER.info("<CVProxyBypassManager>: No proxy bypass environment variables discovered.")
            return

        LOGGER.info(
            "<CVProxyBypassManager>: The following proxy bypass settings were discovered using environment variable '%s': '%s'.",
            self._env_var_no_proxy_name,
            self._env_var_no_proxy_content,
        )
        # Process raw content to build bypass rules
        self._process_env_var_no_proxy_content()

    def _get_env_no_proxy(self) -> None:
        LOGGER.debug("<CVProxyBypassManager>: Reading proxy bypass environment variables: '%s'...", NO_PROXY_ENV_VARS)
        for env_variable_candidate in NO_PROXY_ENV_VARS:
            if env_no_proxy_candidate := environ.get(env_variable_candidate):
                LOGGER.debug("<CVProxyBypassManager>: Environment variable '%s' is found.", env_variable_candidate)
                self._env_var_no_proxy_name = env_variable_candidate
                self._env_var_no_proxy_content = env_no_proxy_candidate
                return
        LOGGER.debug("<CVProxyBypassManager>: No proxy bypass environment variables found.")

    def _process_env_var_no_proxy_content(self) -> None:
        LOGGER.info("<CVProxyBypassManager>: Parsing content of the environment variable '%s' to form proxy bypass rules...", self._env_var_no_proxy_name)
        for raw_rule_input in self._env_var_no_proxy_content.split(","):
            rule_candidate = ProxyBypassRule.from_raw_value(raw_rule_input)
            match rule_candidate.rule_type:
                case "all":
                    self._all_no_proxy_rule = True
                case "ipv4_address":
                    self._ipv4_address_no_proxy_rules.append(rule_candidate)
                case "ipv4_cidr":
                    self._ipv4_cidr_no_proxy_rules.append(rule_candidate)
                case "ipv6_address":
                    self._ipv6_address_no_proxy_rules.append(rule_candidate)
                case "ipv6_cidr":
                    self._ipv6_cidr_no_proxy_rules.append(rule_candidate)
                case "wildcard_domain":
                    self._wildcard_domain_no_proxy_rules.append(rule_candidate)
                case _:
                    self._fqdn_no_proxy_rules.append(rule_candidate)

    @property
    def proxy_bypass_discovered(self) -> bool:
        return bool(self._get_env_var_no_proxy_name() and self._get_env_var_no_proxy_content())

    def _get_env_var_no_proxy_name(self) -> T_NoProxyEnvVars | None:
        return getattr(self, "_env_var_no_proxy_name", None)

    def _get_env_var_no_proxy_content(self) -> str | None:
        return getattr(self, "_env_var_no_proxy_content", None)

    def bypass_proxy_for_destination(self, target_host: str, target_host_format: T_HostFormat, target_port: int) -> bool:
        """Check if target destination and port match any proxy bypass rule and thereofre should not go through proxy server."""
        # If '*' is present in the bypass string - bypass proxy for any destination
        if self._all_no_proxy_rule:
            return True
        match target_host_format:
            case "ipv4_address":
                processed_target_host = ip_address(target_host)
                # Check if provided IPv4 address match any of discovered IPv4 addresses
                if any(processed_target_host == rule.rule_content for rule in self._ipv4_address_no_proxy_rules if isinstance(rule.rule_content, IPv4Address)):
                    return True
                # Check if provided IPv4 address falls into any of the IPv4 CIDRs
                if any(processed_target_host in rule.rule_content for rule in self._ipv4_cidr_no_proxy_rules if isinstance(rule.rule_content, IPv4Network)):
                    return True
            case "ipv6_address":
                processed_target_host = ip_address(target_host)
                # Check if provided IPv6 address match any of discovered IPv6 addresses
                if any(processed_target_host == rule.rule_content for rule in self._ipv6_address_no_proxy_rules if isinstance(rule.rule_content, IPv6Address)):
                    return True
                # Check if provided IPv6 address falls into any of the IPv6 CIDRs
                if any(processed_target_host in rule.rule_content for rule in self._ipv6_cidr_no_proxy_rules if isinstance(rule.rule_content, IPv6Network)):
                    return True
            # Default case for FQDN
            case _:
                # Check if target destination (with and without ports) matches any discovered bypass FQDNs
                bypass_targets = {target_host, f"{target_host}:{target_port}"}
                if any(rule.rule_content in bypass_targets for rule in self._fqdn_no_proxy_rules if isinstance(rule.rule_content, str)):
                    return True
                # Check if target destination matches any discovered wildcard domains
                if any(
                    (target_host.endswith(rule.rule_content) or f"{target_host}:{target_port}".endswith(rule.rule_content))
                    for rule in self._wildcard_domain_no_proxy_rules
                    if isinstance(rule.rule_content, str)
                ):
                    return True
        # Use proxy otherwise
        return False

    @property
    def env_var_no_proxy_name(self) -> T_NoProxyEnvVars:
        return self._env_var_no_proxy_name


class ProxyBypassRule:
    """Class representing single rule of the proxy bypass logic."""

    _rule_type: T_ProxyBypassRuleType
    _rule_content: IpOrCidr | str
    """Matching content of the bypass rule."""

    def __init__(self, rule_type: T_ProxyBypassRuleType, rule_content: IpOrCidr | str) -> None:
        self._rule_type = rule_type
        self._rule_content = rule_content

    @classmethod
    def from_raw_value(cls, input_data: str) -> Self:
        # case for the * (proxy bypass for all destinations)
        if input_data == "*":
            return cls(rule_type="all", rule_content=input_data)
        # case for the wildcard domain ('.arista.io')
        if input_data.startswith("."):
            return cls(rule_type="wildcard_domain", rule_content=input_data)
        # case for IPv4/IPv6 address/CIDRs
        try:
            # IPv4/IPv6 address
            ip_candidate = ip_address(input_data)
            if ip_candidate.version == 4:
                return cls(rule_type="ipv4_address", rule_content=ip_candidate)
            if ip_candidate.version == 6:
                return cls(rule_type="ipv6_address", rule_content=ip_candidate)
        except ValueError:
            try:
                # check if it is an IPv4/IPv6 CIDR
                cidr_candidate = ip_network(input_data)
                if cidr_candidate.version == 4:
                    return cls(rule_type="ipv4_cidr", rule_content=cidr_candidate)
                if cidr_candidate.version == 6:
                    return cls(rule_type="ipv6_cidr", rule_content=cidr_candidate)
            except ValueError:
                pass
        # default case
        return cls(rule_type="fqdn", rule_content=str(input_data))

    @property
    def rule_type(self) -> T_ProxyBypassRuleType:
        return self._rule_type

    @property
    def rule_content(self) -> IpOrCidr | str:
        return self._rule_content
