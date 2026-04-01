<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Proxy Server Support in cv_deploy

The `arista.avd.cv_deploy` role supports connecting to CloudVision through an [HTTP CONNECT](https://en.wikipedia.org/wiki/HTTP_tunnel#HTTP_CONNECT_method) proxy server, with or without basic authentication.

!!! Warning

    Authentication credentials (when used) are sent to the proxy server via ***HTTP Basic authentication*** over an unencrypted HTTP connection (credentials are only Base64-encoded, not encrypted). Proxy server credentials can be exposed by intercepting and analyzing raw TCP/IP traffic between AVD and the proxy server. Please always use additional filtering and identification mechanisms (such as HTTP filtering based on the client’s SRC IP, requested destination domains, etc.) to mitigate security risks.

    It is important to note that AVD uses plain HTTP only for the initial CONNECT request to establish a tunnel to CloudVision through the proxy server. After the TCP tunnel to CloudVision through the proxy server is active, all subsequent AVD communication — including both REST and gRPC calls — is protected within a secure TLS session(s) established between AVD and CloudVision ***inside*** the TCP proxy tunnel.

There are two ways to enable proxy server for `cv_deploy`: explicit and via environment variables.

## Configure proxy settings explicitly

To enable proxy server explicitly, set `proxy_host`. Setting `proxy_port` (port `TCP/8080` will be used by default), `proxy_username` and `proxy_password` is optional.

If valid `proxy_host` (must be non-empty string) and `proxy_port` (1-65535) are set, `cv_deploy` will ignore (for both REST and gRPC calls) any proxy-related environment variables (`https_proxy`/`HTTPS_PROXY`/`all_proxy`/`ALL_PROXY`/`no_proxy`/`NO_PROXY`) and will force all REST and gRPC egress connections through this proxy.

Example configuration to use an unauthenticated HTTP proxy using the CONNECT method:

```yaml
proxy_host: proxy.local.domain
proxy_port: 3128
```

Example configuration to use an authenticated HTTP proxy using the CONNECT method:

```yaml
proxy_host: proxy.local.domain
proxy_port: 3128
proxy_username: "avd_proxy_user"
proxy_password: "avd_proxy_password"
```

!!! None

    All special symbols present in the explicitly passed proxy username and password will be automatically encoded by AVD.

    Example:

    ```yaml
    proxy_host: proxy.local.domain
    proxy_port: 3128
    proxy_username: "p:r/o$x@yuser"
    proxy_password: "p:r/o$x@ypassword"
    ```

    Will be equal to setting the following via the environment variable: `http://p%3Ar%2Fo%24x%40yuser:p%3Ar%2Fo%24x%40ypassword@proxy.local.domain:3128`

## Configure proxy settings using environment variables

If proxy-related settings are not passed to `cv_deploy` explicitly, `cv_deploy` will try to discover a usable proxy server (scheme is `http`, host is a non-empty string, port is in the range 1-65535) using environment variables in the following order:

1. Check if proxy bypass is requested for CloudVision

    ```mermaid
    flowchart LR
        A(["start"]) --> B
        B{"'no_proxy' is set and\nis a non-empty string?"} -- No --> D{"'NO_PROXY' is set and\nis a non-empty string?"}
        B -- Yes --> C{"CloudVision\nmatches 'no_proxy'?"}
        C -- Yes --> E([Do not use proxy])
        C -- No --> F([Proceed to step 2])
        D -- Yes --> G{"CloudVision\nmatches 'NO_PROXY'?"}
        D -- No --> F
        G -- Yes --> H([Do not use proxy])
        G -- No --> F
    ```

2. Discover proxy server

    ```mermaid
    flowchart LR
        A(["start"]) --> B
        B{"'https_proxy' is set and\nis a non-empty string?"} -- No --> C{"'HTTPS_PROXY' is set and\nis a non-empty string?"}
        B -- Yes --> B2{"'https_proxy'\ncontent valid?"}
        B2 -- Yes --> UseProxy1(["Use 'https_proxy'"])
        B2 -- No --> Exc1(["Raise exception"])
        C -- No --> E{"'all_proxy' is set and\nis a non-empty string?"}
        C -- Yes --> D{"'HTTPS_PROXY'\ncontent valid?"}
        D -- Yes --> UseProxy2(["Use 'HTTPS_PROXY'"])
        D -- No --> Exc2(["Raise exception"])
        E -- No --> G{"'ALL_PROXY' is set and\nis a non-empty string?"}
        E -- Yes --> F{"'all_proxy'\ncontent valid?"}
        F -- Yes --> UseProxy3(["Use 'all_proxy'"])
        F -- No --> Exc3(["Raise exception"])
        G -- No --> NoProxy(["Do not use proxy"])
        G -- Yes --> H{"'ALL_PROXY'\ncontent valid?"}
        H -- Yes --> UseProxy4(["Use 'ALL_PROXY'"])
        H -- No --> Exc4(["Raise exception"])
    ```

Examples below show values that can be used for `https_proxy`/`HTTPS_PROXY`/`all_proxy`/`ALL_PROXY` environment variables to influence proxy server settings in `cv_deploy`:

```code
# Asumming 10.10.10.10 and proxy-server.local being examples of the proxy servers
http://10.10.10.10:8081
http://proxy-server.local:8081
http://user1:pass1@10.10.10.10:8081
http://user1:pass1@proxy-server.local:8081
```

!!! None

    When setting proxy credentials via environment variables, make sure to quote all special symbols (like `:`, `@`, etc. ) otherwise such proxy URI string will be invalid.

Examples below show invalid values of `https_proxy`/`HTTPS_PROXY`/`all_proxy`/`ALL_PROXY` environment variables which will be ignored by `cv_deploy`:

```code
# Asumming 10.10.10.10 and proxy-server.local being examples of the proxy servers
# `https` scheme is not supported. Only `http`.
https://10.10.10.10:8081
# Unspecified proxy server port
http://proxy-server.local
# Specified proxy server port is out of expected range
http://proxy-server.local:65555
```

### Proxy bypass syntax and limitations

Value of the proxy bypass environment variables (`no_proxy`/`NO_PROXY`) supported by AVD must be a comma-separated string of the following supported items:

| Item type | Example(s) |
| --------- | ---------- |
| Literal `*` | `*` |
| FQDN | `www.arista.io` |
| FQDN + PORT | `www.arista.io:443` |
| wildcard domain | `.arista.io` |
| wildcard domain + PORT | `.arista.io:443` |
| IPv4 address | `34.67.65.165` |
| IPv4 CIDR | `34.67.65.165/32`, `34.67.65.0/24` |
| IPv6 address | `2a06:98c1:58::1f6` |
| IPv6 CIDR | `2a06:98c1:58::1f6/128`, `2a06:98c1:58::/64` |

Example of a valid string containing all supported item types:

```code
export no_proxy='*,www.arista.io,www.arista.io:443,.arista.io,.arista.io:443,34.67.65.165,34.67.65.165/32,34.67.65.0/24,2a06:98c1:58::1f6,2a06:98c1:58::1f6/128,2a06:98c1:58::/64'
```

Table below explains how each of the items in the environment variable above would impact an AVD decision tree of selecting proxy bypass settings:

!!! Note

    Convention `<fqdn/ip>:<port>` used in `Matching CloudVision destinations` and `Non-matching CloudVision destinations` columns of the table below means that AVD is instructed to run deployment against CloudVision / CVaaS `<fqdn/ip>` over port `<port>`. Non-standard port assumes usage of an intermediate proxy/load-balancer.

| Item | Comment | Matching CloudVision destinations | Non-matching CloudVision destinations |
| ---- | ------- | ----------------- | --------------------- |
| `*` | Matches all destination.<br>Effectively disables proxy server for AVD. | `www.arista.io`:443<br>`cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 | |
| `www.arista.io` | Full FQDN match. | `www.arista.io`:443 | `cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 |
| `www.arista.io:443` | Full FQDN + port match | `www.arista.io`:443 | `cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 |
| `.arista.io` | Wildcard domain match | `www.arista.io`:443 | `cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 |
| `.arista.io:443` | Wildcard domain + port match | `www.arista.io`:443 | `cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 |
| `34.67.65.165` | IPv4 address match | `34.67.65.165`:443<br>`34.67.65.165`:9443 | `www.arista.io`:443<br>`cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 |
| `34.67.65.165/32` | IPv4 CIDR match | `34.67.65.165`:443<br>`34.67.65.165`:9443 | `www.arista.io`:443<br>`cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 |
| `34.67.65.0/24` | IPv4 CIDR match | `34.67.65.165`:443<br>`34.67.65.165`:9443 | `www.arista.io`:443<br>`cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443<br>`2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 |
| `2a06:98c1:58::1f6` | IPv6 address match | `2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 | `www.arista.io`:443<br>`cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443 |
| `2a06:98c1:58::1f6/128` | IPv6 CIDR match | `2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 | `www.arista.io`:443<br>`cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443 |
| `2a06:98c1:58::/64` | IPv6 CIDR match | `2a06:98c1:58::1f6`:443<br>`2a06:98c1:58::1f6`:9443 | `www.arista.io`:443<br>`cvp1.local.domain`:443<br>`cvp1.local.domain`:9443<br>`34.67.65.165`:443<br>`34.67.65.165`:9443<br>`192.168.100.20`:443<br>`192.168.100.20`:9443 |
