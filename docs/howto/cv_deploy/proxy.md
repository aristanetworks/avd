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
# Assuming 10.10.10.10 and proxy-server.local being examples of the proxy servers
http://10.10.10.10:8081
http://proxy-server.local:8081
http://user1:pass1@10.10.10.10:8081
http://user1:pass1@proxy-server.local:8081
```

!!! None

    When setting proxy credentials via environment variables, make sure to quote all special symbols (like `:`, `@`, etc. ) otherwise such proxy URI string will be invalid.

Examples below show invalid values of `https_proxy`/`HTTPS_PROXY`/`all_proxy`/`ALL_PROXY` environment variables which will be ignored by `cv_deploy`:

```code
# Assuming 10.10.10.10 and proxy-server.local being examples of the proxy servers
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

## Troubleshooting

!!! Note
    This documentation section uses `www.cv-prod-us-central1-c.arista.io` CVaaS cluster in all examples.
    When running commands from this section to troubleshoot your issues, please use `www.arista.io` or the FQDN of the actual CVaaS cluster holding your Tenant.

    All examples also use the following proxy-related settings:

    - **proxy server IP**: `10.10.10.100`
    - **proxy server port**: `9876`
    - **proxy server username**: `fake_proxy_username`
    - **proxy server password**: `fake_proxy_password`

When the HTTP CONNECT proxy server is set up correctly, and proper proxy-related inputs are passed to AVD, the `cv_deploy` run should succeed without raising any network or proxy-related exceptions.

The following `curl` test commands should return `{"version":"CVaaS"}` in case the proxy server is set up correctly and all proxy-related variables passed to `curl` are correct as well:

```code
# When the proxy server requires credentials
curl -k -x http://<proxy_server_ip_or_fqdn>:<proxy_server_port> --proxy-user <proxy_server_username>:<proxy_server_password> https://<cluster_fqdn_of_your_cvaas_tenant>/cvpservice/cvpInfo/getCvpInfo.do

# When the proxy server does not require credentials
curl -k -x http://<proxy_server_ip_or_fqdn>:<proxy_server_port> https://<cluster_fqdn_of_your_cvaas_tenant>/cvpservice/cvpInfo/getCvpInfo.do
```

Example:

```code
# command
curl -k -x http://10.10.10.100:9876 --proxy-user fake_proxy_username:fake_proxy_password https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
# response
{"version":"CVaaS"}
```

Sections below contain examples of errors that may be seen when trying to run AVD in an environment that restricts access to CVaaS via an HTTP CONNECT proxy server only.

### Attempt to connect directly (TCP SYNs dropped with returned TCP RST)

**Issue**: AVD's `cv_deploy` is configured to connect to CVaaS directly (bypassing the proxy server) although such connections are blocked (by transit network equipment which returns a TCP RST).

**Symptoms**: Attempt to run `cv_deploy` immediately returns the following exception:

```code
pyavd._cv.client.exceptions.CVClientException: Unable to get version from CloudVision server due to the following error: (MaxRetryError('HTTPSConnectionPool(host=\'www.cv-prod-us-central1-c.arista.io\', port=443): Max retries exceeded with url: /cvpservice/cvpInfo/getCvpInfo.do (Caused by NewConnectionError("HTTPSConnection(host=\'www.cv-prod-us-central1-c.arista.io\', port=443): Failed to establish a new connection: [Errno 111] Connection refused"))'),).
```

**Solution**:

- Run the `curl` equivalent to confirm symptoms:

```code
curl -v -k https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
* Host www.cv-prod-us-central1-c.arista.io:443 was resolved.
* IPv6: (none)
* IPv4: 162.159.142.2, 172.66.1.251
*   Trying 162.159.142.2:443...
* connect to 162.159.142.2 port 443 from 172.18.0.7 port 39956 failed: Connection refused
*   Trying 172.66.1.251:443...
* connect to 172.66.1.251 port 443 from 172.18.0.7 port 43126 failed: Connection refused
* Failed to connect to www.cv-prod-us-central1-c.arista.io port 443 after 6 ms: Could not connect to server
* closing connection #0
curl: (7) Failed to connect to www.cv-prod-us-central1-c.arista.io port 443 after 6 ms: Could not connect to server
```

- Force `cv_deploy` through the proxy server by passing correct proxy-related settings using explicit `cv_deploy` inputs or supported environment variables.

### Attempt to connect directly (TCP SYNs silently dropped)

**Issue**: AVD's `cv_deploy` is configured to connect to CVaaS directly (bypassing proxy server), although such connections are silently dropped (by transit network equipment).

**Symptoms**: Attempt to run `cv_deploy` returns the following exception after a variable delay (actual time depends on the TCP stack of your environment and its TCP SYN retransmit logic):

```code
pyavd._cv.client.exceptions.CVClientException: Unable to get version from CloudVision server due to the following error: (MaxRetryError("HTTPSConnectionPool(host='www.cv-prod-us-central1-c.arista.io', port=443): Max retries exceeded with url: /cvpservice/cvpInfo/getCvpInfo.do (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.cv-prod-us-central1-c.arista.io', port=443) at 0xffffb13de660>, 'Connection to www.cv-prod-us-central1-c.arista.io timed out. (connect timeout=None)'))"),).
```

**Solution**:

- Run the `curl` equivalent to confirm symptoms:

```code
curl -v -k https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
* Host www.cv-prod-us-central1-c.arista.io:443 was resolved.
* IPv6: (none)
* IPv4: 162.159.142.2, 172.66.1.251
*   Trying 162.159.142.2:443...
* connect to 162.159.142.2 port 443 from 172.18.0.7 port 45568 failed: Connection timed out
*   Trying 172.66.1.251:443...
* connect to 172.66.1.251 port 443 from 172.18.0.7 port 42138 failed: Connection timed out
* Failed to connect to www.cv-prod-us-central1-c.arista.io port 443 after 271527 ms: Could not connect to server
* closing connection #0
curl: (28) Failed to connect to www.cv-prod-us-central1-c.arista.io port 443 after 271527 ms: Could not connect to server
```

- Force `cv_deploy` through the proxy server by passing correct proxy-related settings using explicit `cv_deploy` inputs or supported environment variables.

### Proxy server does not exist

**Issue**: Proxy server passed to `cv_deploy` does not exist on the network (does not respond to ARP requests).

**Symptoms**: Attempt to run `cv_deploy` returns the following exception:

```code
pyavd._cv.client.exceptions.CVClientException: Unable to get version from CloudVision server due to the following error: (MaxRetryError('HTTPSConnectionPool(host=\'www.cv-prod-us-central1-c.arista.io\', port=443): Max retries exceeded with url: /cvpservice/cvpInfo/getCvpInfo.do (Caused by ProxyError(\'Unable to connect to proxy\', NewConnectionError("HTTPSConnection(host=\'10.10.10.100\', port=9876): Failed to establish a new connection: [Errno 111] Connection refused")))'),).
```

**Solution**:

- Run the `curl` equivalent to confirm symptoms:

```code
curl -v -k -x http://10.10.10.100:9876 https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
*   Trying 10.10.10.100:9876...
* connect to 10.10.10.100 port 9876 from 172.18.0.7 port 33976 failed: Connection refused
* Failed to connect to 10.10.10.100 port 9876 after 7108 ms: Could not connect to server
* closing connection #0
curl: (7) Failed to connect to 10.10.10.100 port 9876 after 7108 ms: Could not connect to server
```

- Force `cv_deploy` through the correct/existing proxy server by passing correct proxy-related settings using explicit `cv_deploy` inputs or supported environment variables.

### Incorrect proxy server port

**Issue**: Proxy server port passed to `cv_deploy` is incorrect (is not `listened` to by the proxy service or the proxy service is not running).

**Symptoms**: Attempt to run `cv_deploy` returns the following exception:

```code
pyavd._cv.client.exceptions.CVClientException: Unable to get version from CloudVision server due to the following error: (MaxRetryError('HTTPSConnectionPool(host=\'www.cv-prod-us-central1-c.arista.io\', port=443): Max retries exceeded with url: /cvpservice/cvpInfo/getCvpInfo.do (Caused by ProxyError(\'Unable to connect to proxy\', NewConnectionError("HTTPSConnection(host=\'10.10.10.100\', port=9876): Failed to establish a new connection: [Errno 111] Connection refused")))'),).
```

**Solution**:

- Run the `curl` equivalent to confirm symptoms:

```code
curl -v -k -x http://10.10.10.100:9876 https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
*   Trying 10.10.10.100:9876...
* connect to 10.10.10.100 port 9876 from 172.18.0.7 port 45108 failed: Connection refused
* Failed to connect to 10.10.10.100 port 9876 after 35 ms: Could not connect to server
* closing connection #0
curl: (7) Failed to connect to 10.10.10.100 port 9876 after 35 ms: Could not connect to server
```

- Pass the correct proxy server port to `cv_deploy` or make sure the proxy service is running.

### No proxy server credentials provided

**Issue**: Proxy server requires verification of credentials but credentials are not provided to `cv_deploy`.

**Symptoms**: Attempt to run `cv_deploy` returns the following exception:

```code
pyavd._cv.client.exceptions.CVClientException: Unable to get version from CloudVision server due to the following error: (MaxRetryError("HTTPSConnectionPool(host='www.cv-prod-us-central1-c.arista.io', port=443): Max retries exceeded with url: /cvpservice/cvpInfo/getCvpInfo.do (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: 407 Proxy Authentication Required')))"),).
```

**Solution**:

- Run the `curl` equivalent to confirm symptoms:

```code
curl -v -k -x http://10.10.10.100:9876 https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
*   Trying 10.10.10.100:9876...
* CONNECT tunnel: HTTP/1.1 negotiated
* allocate connect buffer
* Establish HTTP proxy tunnel to www.cv-prod-us-central1-c.arista.io:443
> CONNECT www.cv-prod-us-central1-c.arista.io:443 HTTP/1.1
> Host: www.cv-prod-us-central1-c.arista.io:443
> User-Agent: curl/8.14.1
> Proxy-Connection: Keep-Alive
>
< HTTP/1.1 407 Proxy Authentication Required
< Server: squid/5.9
< Mime-Version: 1.0
< Date: Thu, 02 Apr 2026 00:41:55 GMT
< Content-Type: text/html;charset=utf-8
< Content-Length: 3606
< X-Squid-Error: ERR_CACHE_ACCESS_DENIED 0
< Vary: Accept-Language
< Content-Language: en
< Proxy-Authenticate: Basic realm="proxy"
< X-Cache: MISS from a0077641e437
< X-Cache-Lookup: NONE from a0077641e437:9443
< Via: 1.1 a0077641e437 (squid/5.9)
< Connection: keep-alive
<
* Ignore 3606 bytes of response-body
* CONNECT tunnel failed, response 407
* closing connection #0
curl: (56) CONNECT tunnel failed, response 407
```

- Pass correct proxy server credentials to `cv_deploy`

### Incorrect proxy server credentials provided

**Issue**: Proxy server requires verification of credentials but credentials provided to `cv_deploy` are incorrect.

**Symptoms**: Attempt to run `cv_deploy` returns the following exception:

```code
pyavd._cv.client.exceptions.CVClientException: Unable to get version from CloudVision server due to the following error: (MaxRetryError("HTTPSConnectionPool(host='www.cv-prod-us-central1-c.arista.io', port=443): Max retries exceeded with url: /cvpservice/cvpInfo/getCvpInfo.do (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: 407 Proxy Authentication Required')))"),).
```

**Solution**:

- Run the `curl` equivalent to confirm symptoms:

```code
curl -v -k -x http://10.10.10.100:9876 --proxy-user fake_proxy_username:fake_proxy_password  https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
*   Trying 10.10.10.100:9876...
* CONNECT tunnel: HTTP/1.1 negotiated
* allocate connect buffer
* Proxy auth using Basic with user 'fake_proxy_username'
* Establish HTTP proxy tunnel to www.cv-prod-us-central1-c.arista.io:443
> CONNECT www.cv-prod-us-central1-c.arista.io:443 HTTP/1.1
> Host: www.cv-prod-us-central1-c.arista.io:443
> Proxy-Authorization: Basic ZmFrZV9wcm94eV91c2VybmFtZTpmYWtlX3Byb3h5X3Bhc3N3b3Jk
> User-Agent: curl/8.14.1
> Proxy-Connection: Keep-Alive
>
< HTTP/1.1 407 Proxy Authentication Required
< Server: squid/5.9
< Mime-Version: 1.0
< Date: Thu, 02 Apr 2026 02:20:29 GMT
< Content-Type: text/html;charset=utf-8
< Content-Length: 3738
< X-Squid-Error: ERR_CACHE_ACCESS_DENIED 0
< Vary: Accept-Language
< Content-Language: en
< Proxy-Authenticate: Basic realm="proxy"
* Basic authentication problem, ignoring.
< X-Cache: MISS from a0077641e437
< X-Cache-Lookup: NONE from a0077641e437:9443
< Via: 1.1 a0077641e437 (squid/5.9)
< Connection: keep-alive
<
* CONNECT tunnel failed, response 407
* closing connection #0
curl: (56) CONNECT tunnel failed, response 407
```

- Pass the correct proxy server credentials to `cv_deploy`

### Proxy server rules block access to CVaaS

**Issue**: `cv_deploy` successfully authenticates to proxy server but rules/configuration of the proxy server deny access to CVaaS.

**Symptoms**: Attempt to run `cv_deploy` returns the following exception:

```code
pyavd._cv.client.exceptions.CVClientException: Unable to get version from CloudVision server due to the following error: (MaxRetryError("HTTPSConnectionPool(host='www.cv-prod-us-central1-c.arista.io', port=443): Max retries exceeded with url: /cvpservice/cvpInfo/getCvpInfo.do (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: 403 Forbidden')))"),)
```

**Solution**:

- Run the `curl` equivalent to confirm symptoms:

```code
curl -v -k -x http://10.10.10.100:9876 --proxy-user fake_proxy_username:fake_proxy_password https://www.cv-prod-us-central1-c.arista.io/cvpservice/cvpInfo/getCvpInfo.do
*   Trying 10.10.10.100:9876...
* CONNECT tunnel: HTTP/1.1 negotiated
* allocate connect buffer
* Proxy auth using Basic with user 'fake_proxy_username'
* Establish HTTP proxy tunnel to www.cv-prod-us-central1-c.arista.io:443
> CONNECT www.cv-prod-us-central1-c.arista.io:443 HTTP/1.1
> Host: www.cv-prod-us-central1-c.arista.io:443
> Proxy-Authorization: Basic ZmFrZV9wcm94eV91c2VybmFtZTpmYWtlX3Byb3h5X3Bhc3N3b3Jk
> User-Agent: curl/8.14.1
> Proxy-Connection: Keep-Alive
>
< HTTP/1.1 403 Forbidden
< Server: squid/5.9
< Mime-Version: 1.0
< Date: Thu, 02 Apr 2026 01:00:22 GMT
< Content-Type: text/html;charset=utf-8
< Content-Length: 3584
< X-Squid-Error: ERR_ACCESS_DENIED 0
< Vary: Accept-Language
< Content-Language: en
< X-Cache: MISS from a0077641e437
< X-Cache-Lookup: NONE from a0077641e437:9443
< Via: 1.1 a0077641e437 (squid/5.9)
< Connection: keep-alive
<
* CONNECT tunnel failed, response 403
* closing connection #0
curl: (56) CONNECT tunnel failed, response 403
```

- Make sure that the configuration of the proxy server allows `cv_deploy` to connect to CVaaS over HTTPS (TCP/443)
