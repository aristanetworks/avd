CURRENT_DIR = $(shell pwd)
PACKAGE_DIR = pyavd
ANSIBLE_AVD_DIR ?= ..
VENDOR = vendor
VENDOR_DIR = $(PACKAGE_DIR)/$(VENDOR)
VENDOR_IMPORT = $(PACKAGE_DIR).$(VENDOR)
J2_DIR = $(VENDOR_DIR)/j2
TESTS_ARTIFACTS = $(CURRENT_DIR)/tests/artifacts
TOOLS_DIR = $(PACKAGE_DIR)/tools
SCRIPTS_DIR = $(CURRENT_DIR)/scripts
EOS_CLI_CONFIG_GEN_TEMPLATE_DIR = $(VENDOR_DIR)/templates
SCHEMAS_DIR = $(VENDOR_DIR)/schemas
EOS_DESIGNS_MODULES_DIR = $(VENDOR_DIR)/eos_designs
# export PYTHONPATH=$(CURRENT_DIR) # Uncomment to test from source

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: dep
dep: copy-libs fix-libs ## Copy and Fix Ansible AVD python files

.PHONY: test-dep
test-dep: copy-test-data ## Copy and Fix Ansible AVD test files

.PHONY: clean
clean: ## Delete vendor dir
	rm -rf $(VENDOR_DIR)

.PHONY: build
build: ## Build pyavd package
	pip3 install build
	rm -rf $(CURRENT_DIR)/build/ $(CURRENT_DIR)/dist/ $(CURRENT_DIR)/pyavd.egg-info/
	python3 -m build --wheel

.PHONY: publish
publish: ## Publish pyavd package to PyPI (build first)
	pip3 install twine && \
	twine check dist/* && \
	twine upload -r testpypi dist/* && \
	twine upload dist/*

.PHONY: copy-libs
copy-libs: ## Copy files from Ansible AVD collection
	rm -rf $(VENDOR_DIR)
	mkdir -p $(VENDOR_DIR)
	mkdir -p $(J2_DIR)
	mkdir -p $(SCHEMAS_DIR)
	mkdir -p $(EOS_CLI_CONFIG_GEN_TEMPLATE_DIR)
	mkdir -p $(EOS_DESIGNS_MODULES_DIR)

	cp $(ANSIBLE_AVD_DIR)/LICENSE $(PACKAGE_DIR)/LICENSE
	cp -r $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/plugins/plugin_utils/* $(VENDOR_DIR)
	cp -r $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/plugins/module_utils/* $(VENDOR_DIR)
	cp -r $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/plugins/filter $(J2_DIR)
	cp -r $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/plugins/test $(J2_DIR)
	cp -r $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/roles/eos_cli_config_gen/templates/* $(EOS_CLI_CONFIG_GEN_TEMPLATE_DIR)
	cp $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/roles/eos_cli_config_gen/schemas/eos_cli_config_gen.schema.yml $(SCHEMAS_DIR)/
	rm -f $(EOS_CLI_CONFIG_GEN_TEMPLATE_DIR)/avd_schema_documentation.j2

	cp -r $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/roles/eos_designs/python_modules/* $(EOS_DESIGNS_MODULES_DIR)/
	mv $(VENDOR_DIR)/eos_designs_* $(EOS_DESIGNS_MODULES_DIR)/
	cp -r $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/roles/eos_designs/schemas/eos_designs.schema.yml $(SCHEMAS_DIR)/

.PHONY: fix-libs
fix-libs: ## Fix/remove various Ansible specifics things from python files
	rm -f $(VENDOR_DIR)/schema/avdschematools.py

	find $(PACKAGE_DIR) -name '__pycache__' -exec rm -rf {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/^from __future__ import.*/from __future__ import annotations/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e '/^__metaclass__ = type/d' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/from ansible.errors import /from $(VENDOR_IMPORT).errors import /g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/AnsibleFilterError/AristaAvdError/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/AnsibleError/AristaAvdError/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/AnsibleActionFail/AristaAvdError/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/ansible_collections\.arista\.avd\.plugins\.plugin_utils\.schema\.avdschematools/pyavd.avd_schema_tools/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/ansible_collections\.arista\.avd\.plugins\.plugin_utils\.eos_designs_shared_utils/$(VENDOR_IMPORT)\.eos_designs\.eos_designs_shared_utils/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/ansible_collections\.arista\.avd\.plugins\.plugin_utils/$(VENDOR_IMPORT)/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/ansible_collections\.arista\.avd\.plugins\.module_utils/$(VENDOR_IMPORT)/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/ansible_collections\.arista\.avd\.plugins\.filter/$(VENDOR_IMPORT)\.j2\.filter/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/ansible_collections\.arista\.avd\.roles\.eos_designs\.python_modules/$(VENDOR_IMPORT)\.eos_designs/g' {} +
	find $(PACKAGE_DIR) -name '*.py' -exec sed -i -e 's/from ansible\.utils\.display/from $(VENDOR_IMPORT)\.utils\.display/g' {} +

	cp -r $(CURRENT_DIR)/vendor_overrides/* $(VENDOR_DIR)/

	$(SCRIPTS_DIR)/compile_schemas.py
	$(SCRIPTS_DIR)/compile_templates.py

.PHONY: copy-test-data
copy-test-data: ## Copy inventory files from AVD collection Molecule scenario.
	rm -rf $(TESTS_ARTIFACTS)

## EOS_CLI_CONFIG_GEN

## Workaround to get the lookup plugin to resolve this TCAM profile before exporting vars
	mkdir -p $(SCRIPTS_DIR)/inventory
	cp $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/molecule/eos_cli_config_gen/inventory/TCAM_TRAFFIC_POLICY.conf $(SCRIPTS_DIR)/inventory/

## Excluding prompt because the unsafe marker is lost during the export of hostvars.
## Excluding custom-templates since there is no jinja support in pyavd
	ANSIBLE_COLLECTIONS_PATHS="..:/usr/share/ansible/collections" ansible-playbook \
		--limit 'all:!prompt:!custom-templates' \
		-i $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/molecule/eos_cli_config_gen/inventory/hosts.ini \
		$(SCRIPTS_DIR)/export_test_vars.yml \
		-e testdir=eos_cli_config_gen \
		-f 10

	rm -rf $(SCRIPTS_DIR)/inventory/

## Remove excluded tests
	rm $(TESTS_ARTIFACTS)/eos_cli_config_gen/configs/prompt.cfg
	rm $(TESTS_ARTIFACTS)/eos_cli_config_gen/configs/custom-templates.cfg

## EOS_DESIGNS

	ANSIBLE_COLLECTIONS_PATHS="..:/usr/share/ansible/collections" ansible-playbook \
		-i $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/molecule/eos_designs_unit_tests/inventory/hosts.yml $(SCRIPTS_DIR)/export_test_vars.yml \
		-e testdir=eos_designs_unit_tests \
		-f 10

## Remove tests with custom templates
	rm $(TESTS_ARTIFACTS)/eos_designs_unit_tests/vars/CUSTOM-TEMPLATES*.json
	rm $(TESTS_ARTIFACTS)/eos_designs_unit_tests/structured_configs/CUSTOM-TEMPLATES*.yml
	rm $(TESTS_ARTIFACTS)/eos_designs_unit_tests/configs/CUSTOM-TEMPLATES*.cfg
	rm $(TESTS_ARTIFACTS)/eos_designs_unit_tests/vars/CUSTOM-PYTHON_MODULES*.json
	rm $(TESTS_ARTIFACTS)/eos_designs_unit_tests/structured_configs/CUSTOM-PYTHON_MODULES*.yml
	rm $(TESTS_ARTIFACTS)/eos_designs_unit_tests/configs/CUSTOM-PYTHON_MODULES*.cfg
