# Requirements

## Arista EOS version

- EOS **4.21.8M** or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista CloudVision

If you leverage [CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [CloudVision Ansible collection](https://cvp.avd.sh/)

## Python

- Python **3.8** or later

## Supported Ansible Versions

- ansible-core from **2.11.3** to **2.12.x** excluding **2.12.0** to **2.12.5**

Excluded versions have an issue in `ansible-core`, which is [fixed](https://github.com/ansible/ansible/blob/v2.12.6/changelogs/CHANGELOG-v2.12.rst#bugfixes) in **2.12.6** and **2.13.1**.

!!! note
    Plugin loader will now load config data for plugin by name instead of by file to avoid issues with the same file being loaded under different names (Fully-Qualified-Collection-Name + short-name).

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
