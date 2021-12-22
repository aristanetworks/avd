# Requirements

## Arista EOS version

- EOS __4.21.8M__ or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista Cloudvision

If you leverage [Cloudvision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [Cloudvision ansible collection](https://cvp.avd.sh/)

## Python

- Python __3.8__ or later

## Supported Ansible Versions

- ansible-core from __2.11.3__ to __2.12.x__

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

If the collection is cloned from GitHub, the requirements file can be referenced directly:

```shell
pip3 install -r ansible-avd/ansible_collections/arista/avd/requirements.txt
```

!!! warning
    Depending of your operating system settings, `pip3` might be replaced by `pip`.
