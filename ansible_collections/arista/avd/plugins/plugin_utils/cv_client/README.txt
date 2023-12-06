This package is expected to move to the pip-installable "cloudvision" package in the future.
For now we will maintain it here, as only AVD components rely on it.

./api/    gRPC client bindings for CloudVision Resource APIs using betterproto==2.0.0b6
./client/ Mid level abstraction of the CloudVision API, to hide some of the suboptimal APIs.
./*.py    High level workflow abstrations to be moved to pyavd once pyavd becomes a dependency of Ansible-AVD.
