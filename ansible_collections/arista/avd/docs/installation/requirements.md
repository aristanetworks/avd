# Requirements

## Arista EOS version

- EOS __4.21.8M__ or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista CloudVision

If you leverage [CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [CloudVision Ansible collection](https://cvp.avd.sh/)

## Python

- Python __3.8__ or later

## Supported Ansible Versions

- ansible-core from __2.11.3__ to __2.12.x__ excluding __2.12.0__ to __2.12.5__

Excluded versions have an [issue](## "plugin loader will now load config data for plugin by name instead of by file to avoid issues with the same file being loaded under different names (Fully-Qualified-Collection-Name + short-name).")
in `ansible-core`, which is [fixed](https://github.com/ansible/ansible/blob/v2.12.6/changelogs/CHANGELOG-v2.12.rst#bugfixes)
in __2.12.6__ and __2.13.1__.

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
