# Getting Started

**An example playbook to deploy VXLAN/EVPN Fabric via CloudVision:**

![Figure 1: Example Playbook CloudVision Deployment](media/figure-1-example-playbook-evpn-deploy-cvp.gif)

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: generate intended variables
      import_role:
         name: arista.avd.eos_l3ls_evpn

    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

    - name: deploy configuration via CVP
      import_role:
         name: arista.avd.eos_config_deploy_cvp
```

**An example playbook to deploy VXLAN/EVPN Fabric via eAPI:**

![Figure 2: Example Playbook CloudVision Deployment](media/figure-2-example-playbook-evpn-deploy-eapi.gif)

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: generate intended variables
      import_role:
         name: arista.avd.eos_l3ls_evpn

    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

    - name: deploy configuration to device
      import_role:
         name: arista.avd.eos_config_deploy_eapi
```

