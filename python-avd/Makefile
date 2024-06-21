CURRENT_DIR = $(shell pwd)
PACKAGE_DIR = pyavd
ANSIBLE_AVD_DIR ?= ..
VENDOR = vendor
VENDOR_DIR = $(PACKAGE_DIR)/$(VENDOR)
VENDOR_IMPORT = $(PACKAGE_DIR).$(VENDOR)
J2_DIR = $(VENDOR_DIR)/j2
TESTS_ARTIFACTS = $(CURRENT_DIR)/tests/pyavd/artifacts
TOOLS_DIR = $(PACKAGE_DIR)/tools
SCRIPTS_DIR = $(CURRENT_DIR)/scripts
SCHEMAS_DIR = $(VENDOR_DIR)/schemas
EOS_DESIGNS_MODULES_DIR = $(VENDOR_DIR)/eos_designs
PYAVD_FILTER_IMPORT = $(PACKAGE_DIR).j2filters
PYAVD_TEST_IMPORT = $(PACKAGE_DIR).j2tests
EOS_DESIGNS_IMPORT = $(PACKAGE_DIR)._eos_designs

# export PYTHONPATH=$(CURRENT_DIR) # Uncomment to test from source

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: dep
dep: update-requirements-and-templates compile-schemas ## Copy and Fix Ansible AVD python files & compile schemas

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

.PHONY: compile-schemas
compile-schemas:
	$(SCRIPTS_DIR)/build-schemas.py

.PHONY: update-requirements-and-templates
update-requirements-and-templates:
	cp $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/requirements.txt requirements-ansible-avd.txt
	grep "ansible-core" $(ANSIBLE_AVD_DIR)/ansible_collections/arista/avd/requirements-dev.txt >> requirements-ansible-avd.txt
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
	ANSIBLE_COLLECTIONS_PATH="..:/usr/share/ansible/collections" ansible-playbook \
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

	ANSIBLE_COLLECTIONS_PATH="..:/usr/share/ansible/collections" ansible-playbook \
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
