# Table of Contents <!-- omit in toc -->
- [Ansible and AVD Overview](#ansible-and-avd-overview)
  - [Day 1 operation i.e. provisioning a network from scratch](#day-1-operation-ie-provisioning-a-network-from-scratch)
  - [What is Ansible](#what-is-ansible)
  - [What is required to run Ansible](#what-is-required-to-run-ansible)
  - [What is Ansible AVD (Ansible collection for Arista Validated Designs)](#what-is-ansible-avd-ansible-collection-for-arista-validated-designs)
  - [When to use Ansible AVD and when not to](#when-to-use-ansible-avd-and-when-not-to)
  - [How does Ansible work](#how-does-ansible-work)
    - [Inventories](#inventories)
    - [Playbooks](#playbooks)
  - [How do I use Ansible AVD:](#how-do-i-use-ansible-avd)
  - [Day 2 Operations](#day-2-operations)

# Ansible and AVD Overview
## Day 1 operation i.e. provisioning a network from scratch
Imagine being tasked with installing and configuring a leaf-spine network with 2 spine switches and 4 leaf switches from scratch:

![Figure 1: Arista Leaf Spine topology](../_media/getting-started/LS-Topology.png)

Traditionally, one would grab a laptop, a console cable and perhaps a USB key containing the Arista EOS image of choice. This would mean a tedious device by device process of performing a software upgrade and typing configuration commands manually. Alternatively by using pre-developed config snippets based on reading the relevant Arista design guides and/or previous experience *(did anyone think of copy/paste from existing devices!?)*.
The configurations would be manually adapted per device, which is time consuming. The operator could easily become burned out, leading to user and design errors.

Using Ansible Arista Validated Designs (AVD), such a task is automated, greatly simplified and many times faster, where all the “basic” network configuration is guaranteed to be identical across the entire fabric from day one. No longer do you have to manually inspect each and every device for errors and this also applies when updating the configuration in day 2 operations. In addition, you do not have to spend any time integrating the Arista Design and Deployment Guides, since Ansible AVD is built on those as a foundation. Ansible AVD also fully integrates with Arista Cloudvision, which adds a full change control workflow, continuous compliance checks, network topology overview as well as real time streaming telemetry including flow based data and more.

## What is Ansible
Ansible is an open source tool, that can be thought of as an “automation engine” that will execute the tasks you tell it to, in a uniform and secure way with idempotency built in. Idempotency!? It’s just a funky word for describing that repeating a task will not change or overwrite anything.
Tasks in Ansible are executed based on structure data, in a format called YAML.<br>
YAML will be covered later in the section “How does Ansible Work”.

Ansible can be used to automate many things. In this document, we’re only focusing on the use of Ansible to help us automate the provisioning of Arista network devices either directly from Ansible or via Arista Cloudvision.

## What is required to run Ansible
Ansible can run on almost anything, but in production scenarios, we typically see Ansible deployed on a virtual Linux server, running on the customer’s preferred hypervisor. This Ansible server then communicates either directly with the Arista network devices or with Arista CloudVision Portal, which in turn communicates with the Arista network devices. Controlling what Ansible does is typically done using a SSH terminal session to the Ansible server from the Operator’s computer.
Using Ansible to control an Arista network infrastructure is agentless, i.e. it requires nothing additional to be installed on the Arista network devices or Arista CloudVision Portal.

![Figure 2: Ansible and CVP](../_media/getting-started/Ansible-and-CVP-httpapi.png)

## What is Ansible AVD (Ansible collection for Arista Validated Designs)
While Ansible is the automation engine, Ansible AVD is a “collection” added to Ansible. It is an open source project hosted on GitHub and maintained by Arista, letting users contribute directly. 
A “collection” is a distribution format for Ansible content that can include roles, modules, and plugins. These topics are most likely new to you, but do not worry, they will be described in later sections. For now, just remember that a “collection” is a way to easily share and distribute Ansible data. You can install and use collections through Ansible Galaxy, which is Ansible’s official hub for sharing Ansible content.

![Figure 3: Arista Leaf Spine topology](../_media/getting-started/Ansible-AVD.png)

In the illustration above, the Ansible AVD collection is shown as the box with the red background on the right hand side. 
When designing an EVPN Layer 3 Leaf Spine (L3LS) fabric you don't need to be an expert on Arista Design and Deployment Guides. All those rules and guidelines are integrated in the Ansible collection for Arista Validated Designs (AVD), or in short: Ansible AVD.<br>
Ansible AVD is an opinionated collection, meaning that field experiences and best practices are also included. With Ansible AVD, users get up and running quickly without having to invent every part of the network configuration from scratch. This means only the most basic information must be provided by the user to get a new fabric up and running.
 
Examples could be:
- Username/password for network devices and Cloudvision
- OOB management IP range
- IP scope for link addresses
- IP scope for loopback interfaces
- VLAN and VNI ranges
- Device hostnames
- And so on

All are details that must be decided upon in any fabric design. In a standard spine-leaf topology, Ansible AVD takes care of all the work past the theoretical design.

## When to use Ansible AVD and when not to
It’s important to mention when to, and perhaps more importantly, when not to use Ansible AVD:<br> Automating provisioning of a network infrastructure makes most sense when the network is designed and built using clearly defined, repeatable patterns. It makes less sense when a network infrastructure is using a non-uniform design. Although you can use Ansible AVD to provision a non-uniform network while harvesting some benefits, you’re creating a lot of manual work and customization of Ansible AVD to achieve what you need, essentially making it much harder to maintain going forward.

Below is a table highlighting a few things to consider before jumping head first into automation with Ansible AVD. The table is by no means conclusive and the answer to whether or not to use Ansible AVD quickly becomes “it depends”, but hopefully the table can provide a baseline for what to consider.


Consider using Ansible AVD when|Reconsider using Ansible AVD when
:---|:---
The network is a leaf-spine topology where expanding the fabric means repeating the steps used to add the initial devices | The network is a mix-and-match of various topologies without any clear, repeatable pattern
Port configuration towards end systems (e.g. servers, storage systems etc.) can be clearly defined, templated and repeated e.g. using port profiles | Port configuration towards end systems (e.g. servers, storage systems etc.) changes significantly from port to port
It matters that you’re building your network using the Arista Validated Designs, i.e. topologies and design decisions proven in some of the largest data center networks in the world | Your network design is custom built and may not conform to things like the Arista Design and Deployment Guides.
Ansible AVD covers e.g. 90% of what you need and the remaining 10% must be customized. You as a user can customize or extend Ansible AVD as you see fit. | Ansible AVD covers e.g. 10% of what you need and the remaining 90% must be customized. Customizing the AVD design to your planned topology would be more work than doing it by hand

## How does Ansible work
Before we can tell Ansible to do anything, Ansible needs to know about the devices (or hosts as Ansible calls it) it handles. 
This is defined in the Ansible ***inventory***.

### Inventories
An example of an inventory could be the following shown on the left below (subset of this example for clarity).
Note that this one is in YAML format. Also note that the IP addresses shown below are only an example of the management IP addresses for the different devices. These can of course be adapted to fit any topology.

```all:
  children:    
    # DC1_Fabric - EVPN Fabric
    DC1:
      children:
        DC1_FABRIC:
          children:
            DC1_SPINES:
              hosts:
                DC1-SPINE1:
                  ansible_host: 10.255.0.11
                DC1-SPINE2:
                  ansible_host: 10.255.0.12
            DC1_L3LEAFS:
              children:
                DC1_LEAF1:
                  hosts:
                    DC1-LEAF1A:
                      ansible_host: 10.255.0.13
                    DC1-LEAF1B:
                      ansible_host: 10.255.0.14
                DC1_LEAF2:
                  hosts:
                    DC1-LEAF2A:
                      ansible_host: 10.255.0.15
                    DC1-LEAF2B:
                      ansible_host: 10.255.0.16
```
The multi-colored figure below is just a visualization of the text file, showing the different grouping and parent/children relationships.

![Figure 2: Ansible Inventory](../_media/getting-started/Inventory.png)

Don’t confuse ***hosts*** with servers or similar. A ***host*** can be anything that can be accessed via SSH or an API, including Arista switches, which will be what we’re focusing on going forward.

The inventory file is defined in a tree-like structure using what is called ***groups***, used to make it easier to apply common configuration to a group of devices.
The ***all*** line at the top is a default ***group*** that contains all ***hosts*** i.e. all switches. Don’t worry too much about that for now.
The ***children:*** keyword is used to define “groups of groups” i.e. just an internal keyword to differentiate between hosts and groups.
Key takeaway is that configuration defined at a higher (parent) level will be inherited by the children, but if needed, this can be overridden by specifying it again i.e. most specific wins. 
More information about Ansible inventories here.

### Playbooks
Now that the Ansible inventory is defined, we can tell Ansible what to do on the switches.
This is defined in one or more ***playbooks*** as they’re called in Ansible-lingo.
A ***playbook***, like an inventory file, is a text file written using YAML format and it contains one or more ***plays***, that group a set of instructions to be executed in an ordered list. 
The terms ***playbook*** and ***play*** are sports analogies. Each play executes part of the overall goal of the playbook, running one or more tasks. Each task calls an Ansible role or module, such as “ansible.avd.eos_cli_config_gen”. 
A playbook runs in order from top to bottom. Within each play, tasks also run in order from top to bottom. Playbooks with multiple “plays” can orchestrate multi-machine deployments, running one play on your Ansible development machine, another on your CV instance, and another on each EOS device you look to configure. 
At a minimum, each play defines two things:
the managed devices (***hosts***) to target, referenced from the inventory we defined earlier
One or more tasks to execute on the targets defined

The ***hosts*** specified in a ***playbook*** references variables defined in the ***inventory***. From a ***playbook*** you can select large or small groups of the ***inventory***, right down to individual ***hosts*** to be as specific as possible with any configuration changes.

A simple example of a ***play*** defined in a ***playbook*** could be the following:

```
# Play to build EOS configuration from EOS_DESIGNS
- hosts: DC1_FABRIC
  tasks:
    # BUILD EOS configuration
    - name: generate intended variables
      import_role:
         name: arista.avd.eos_designs
    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen
```

Reading from the top, the ***hosts*** references the variable ***DC1_FABRIC***, which is defined in the ***inventory*** as all ***hosts*** further defined within DC1. In an actual deployment, this would likely include groups of devices, such as ***DC1_SPINES***, ***DC1_L3LEAFS*** and so on - again naming convention used here is just an example, not set in stone.
The ***tasks*** are then defined and the first task imports a ***role*** called ***arista.avd.eos_designs***. A ***role*** is where the majority of things done with Ansible happen. In the ***arista.avd.eos_designs*** role, we generate the variables used for further processing in subsequent roles, such as the second one shown above called ***arista.avd.eos_cli_config_gen***. This role generates the intended configuration along with documentation in markdown format.
The “source of truth” exists inside Ansible AVD at any point in time, meaning you have a full overview of your entire designed network configuration without having to look at individual network devices. This also means that by design you have an always available backup of your network configuration including automated documentation in markdown format. No longer do you have to remember to update documentation about which interface is connected to which device etc. It’s all done automatically based on the configuration built and applied to the network devices by Ansible.

**insert example of documentation**

## How do I use Ansible AVD:

Links to rest of documentation
- With eos_design
- With eos_cli_config_gen
- With tower
- With CI/CD
- With eos_config_deploy_cvp / eos_config_deploy_eapi

As stated above, Ansible AVD comes with pre-built templates that you can either decide to re-use as-is or adapt to your liking.
<much more description on how and which variables/templates should be used to define the fabric inserted here>
<br>
<br>
Once the templates reflect your desired network configuration, you deploy the configuration either directly to the Arista EOS devices or via Arista Cloudvision using its internal change management system, where the changes can be reviewed, approved and executed in accordance with existing company requirements.
The deployment is executed typically using CLI commands or via the GUI available with Ansible Tower. 
Here, we will be showing examples using CLI commands:
ansible-playbook playbooks/dc1-fabric-deploy-cvp.yml --tags build will run the playbook playbooks/dc1-fabric-deploy-cvp.yml with the tag build. 

Once the configuration has been deployed, an automated validation of the designed configuration versus the running configuration can be executed using the included validation playbook, to ensure that e.g. all links are operational and cabled as desired, BGP adjacencies are operational etc. This quickly identifies any issues that could otherwise be overlooked and a redundant link could sit non-operational for months unless cumbersome manual testing is executed again per-device throughout the fabric.

## Day 2 Operations
The term “Day 2 Operations” describes most if not all network configuration changes that occur after the initial day 1 configuration. The really time consuming day-to-day tasks such as adding/removing new leaf switches, VLANs, creating/modifying/deleting port profiles, configuring/modifying ports towards end systems etc. no longer have to be performed on a device-by-device basis across the entire fabric.<br>
A configuration change can easily be applied to the Ansible YAML files and the scope for a given change can be specified. E.g. should the new VLAN 100 be added to all or a subset of leaf switches. Once your changes are complete, you re-deploy the configuration changes to the relevant network devices, again either directly or via Cloudvision Portal.