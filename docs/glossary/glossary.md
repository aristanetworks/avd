# Glossary

### 3-Stage Clos

A network topology consisting of three layers: spine, leaf, and optionally overlay controllers.
Also referred to as a POD (Point of Delivery) in AVD terminology. This architecture provides
non-blocking, scalable connectivity.


### 5-Stage Clos

An extended Clos topology adding super-spine and border leaf layers to the traditional
3-stage design, enabling larger scale deployments across multiple PODs or data centers.


### ACT

Arista Cloud Test - A cloud-based virtual lab environment for testing and validating
network designs using virtual Arista EOS instances.


### ANTA

Arista Network Test Automation - A Python framework for validating the operational state
of Arista EOS devices. Integrated with AVD to provide automated testing of deployed configurations.


### anta_runner

An AVD Ansible role that validates the operational state of Arista EOS devices using
the ANTA (Arista Network Test Automation) framework. It can generate test catalogs
from AVD structured configurations or execute user-defined test catalogs, reporting
results in JSON, CSV, and Markdown formats.


### AVD

Arista Validated Designs - A framework for design-driven network automation that provides
extensible fabric-wide network models, simplifying configuration, delivering consistency,
and reducing errors across data center, campus, and wide area networks.


### AVD Design

AVD Design data models provide opinionated yet flexible network-wide data models expressing the
intent of your network design and configuration. AVD Design data models are transformed by the
Arista AVD framework to generate configuration, documentation and tests.


### build_output_folders

An AVD Ansible role that creates the necessary directory structure for storing
generated configurations, documentation, and other AVD outputs. Typically run
before eos_designs and eos_cli_config_gen roles.


### Change Control

In CloudVision, a change control is a workflow mechanism that manages network configuration
changes with approval processes, scheduling, and rollback capabilities.


### CloudVision Studio

A feature of CloudVision that provides visual workflow automation and configuration
management capabilities, including Static Configuration Studio and Access Interface
Configuration Studio.


### cv_deploy

An AVD Ansible role that deploys EOS device configurations and tags to CloudVision.
It manages the full deployment workflow including workspace creation, configuration
push, change control creation, and approval processes for both CVaaS and on-premises
CloudVision instances.


### CVaaS

CloudVision as a Service - Arista's cloud-based network management and automation platform
that provides centralized visibility, telemetry, and configuration management for Arista devices.


### Digital Twin

A virtual replica of a production AVD fabric optimized for specific simulation environments
like ACT (Arista Cloud Test). AVD automatically generates artifacts required to deploy
digital twins with features adjusted for the target environment.


### eAPI

Arista's RESTful API for programmatic access to EOS devices. Enables automation tools
like Ansible to configure and manage Arista switches.


### EOS Config

The EOS Config provides device-centric data models for expressing the Arista EOS device
configurations syntax. These data models are also referred to as “structured config” within
the AVD Design data models and can be leveraged with custom structured configuration to
extend or override the behaviour of Arista AVD.


### eos_cli_config_gen

An AVD Ansible role that generates EOS CLI syntax and device documentation from
structured configuration data. It converts YAML-based structured configs into
EOS CLI commands and creates device-specific documentation in Markdown format.


### eos_config_deploy_eapi

An AVD Ansible role that deploys configurations directly to Arista EOS devices using
eAPI. It performs configuration replacement and can optionally save configurations
to startup-config.


### eos_designs

An AVD Ansible role that provides an abstracted data model to deploy various network
designs and use cases. It generates structured configurations from fabric-wide intent
data models, supporting L3LS EVPN, L2LS, MPLS, and WAN designs. The role outputs
structured YAML configurations and fabric documentation.


### eos_snapshot

An AVD Ansible role that collects operational state snapshots from EOS devices.
Useful for capturing the current state before and after changes for comparison
and validation purposes.


### eos_validate_state

A legacy AVD Ansible role for validating the operational state of EOS devices.
This role has been superseded by the anta_runner role which provides more
comprehensive testing capabilities using the ANTA framework.


### Fabric

In AVD, a fabric refers to the entire network infrastructure managed as a single entity,
including all switches, links, and services. AVD generates configurations for the entire
fabric from a unified data model.


### L2LS

Layer 2 Leaf-Spine - A network architecture where leaf switches are connected to spine
switches using Layer 2 protocols, typically with spanning tree for loop prevention.


### L3LS

Layer 3 Leaf-Spine - A network architecture where leaf switches are connected to spine
switches using Layer 3 routing protocols. This is the foundation for modern data center
designs with EVPN/VXLAN overlays.


### Node Type

A classification of network devices in AVD (e.g., spine, leaf, super-spine, border-leaf).
Node types determine the role and configuration template applied to devices.


### POD

Point of Delivery - A self-contained network segment in a Clos architecture, typically
consisting of spine switches, L3 leaf switches, and L2 leaf switches.


### Structured Config

Device-centric configuration data in YAML format that directly maps to EOS CLI commands.
Structured config can be used to extend or override the configuration generated by AVD
Design data models.


### Tenant

In AVD, a tenant is an abstraction layer above VRFs that groups related network services.
Tenants help organize and manage multi-tenant network configurations.


### Workspace

In CloudVision, a workspace is a staging area for configuration changes that can be built,
reviewed, and submitted before being applied to network devices.

