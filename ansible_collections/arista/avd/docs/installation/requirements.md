# Requirements

## Arista EOS version

- EOS **4.21.8M** or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista CloudVision

If you leverage [CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [CloudVision Ansible collection](https://cvp.avd.sh/)

> ***NOTE:*** When using ansible-cvp modules, the user who is executing the ansible-playbook must have access to both CVP and the EOS CLI.

## Python

- Python **3.8** or later

## Additional Python Libraries required

```pip
--8<--
requirements.txt
--8<--
```

### Python requirements installation

In a shell, run the following commands after installing the collection from ansible-galaxy:

```shell
export ARISTA_AVD_DIR=$(ansible-galaxy collection list arista.avd --format yaml | head -1 | cut -d: -f1)
pip3 install -r ${ARISTA_AVD_DIR}/arista/avd/requirements.txt
```

If the collection is cloned from GitHub, we can reference the requirements file directly:

```shell
pip3 install -r ansible-avd/ansible_collections/arista/avd/requirements.txt
```

!!! warning
    Depending of your operating system settings, `pip3` might be replaced by `pip`.

### Ansible Configuration INI file

- enable jinja2 extensions: loop controls and do
  - [Jinja2 Extensions Documentation](https://jinja.palletsprojects.com/extensions/)
- By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend to change to error instead and stop playbook execution when a duplicate key is detected.

```ini
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```
