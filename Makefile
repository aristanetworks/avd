CURRENT_DIR = $(shell pwd)
# option to run ansible-test sanity: must be either venv or docker (default is venv)
ANSIBLE_TEST_MODE ?= venv
MUFFET_TIMEOUT ?= 60

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s", $$1, $$2}'

#########################################
# Ansible Collection actions            #
#########################################
.PHONY: collection-build
collection-build: ## Build arista.avd collection locally.
	ansible-galaxy collection build --force ansible_collections/arista/avd

#########################################
# pyavd actions                         #
#########################################
.PHONY: pyavd-build
pyavd-build: ## Build PyAVD Python package locally.
	cd python-avd && $(MAKE) build

.PHONY: uv-pyavd-build
uv-pyavd-build: ## Build PyAVD Python package locally.
	cd python-avd && $(MAKE) uv-build

.PHONY: pyavd-test
pyavd-test: ## Test PyAVD Python code with tox.
	tox run -r

.PHONY: pyavd-publish
pyavd-publish: ## Build and publish PyAVD Python package.
	cd python-avd && $(MAKE) build publish

.PHONY: uv-pyavd-publish
uv-pyavd-publish: ## Build and publish PyAVD Python package.
	cd python-avd && $(MAKE) uv-build uv-publish

.PHONY: pyavd-install
pyavd-install: pyavd-build ## Build and install PyAVD Python package.
	pip install python-avd/dist/* --force-reinstall

# The editable_mode=compat is required for pylance to pick up the editable install.
.PHONY: pyavd-editable-install
pyavd-editable-install: ## Build and install PyAVD as editable
	pip install -e python-avd --config-settings editable_mode=compat --force-reinstall

.PHONY: uv-pyavd-install
uv-pyavd-install: pyavd-build ## Build and install PyAVD Python package.
	uv pip install python-avd/dist/* --force-reinstall

# The editable_mode=compat is required for pylance to pick up the editable install.
.PHONY: uv-pyavd-editable-install
uv-pyavd-editable-install: ## Build and install PyAVD as editable
	uv pip install -e python-avd --config-settings editable_mode=compat --force-reinstall

#########################################
# Code Validation using ansible-test 	#
#########################################

.PHONY: sanity
sanity: sanity-info sanity-lint sanity-import ## Run ansible-test sanity validation.

.PHONY: sanity-info
sanity-info: ## Show information about ansible-test.
	cd ansible_collections/arista/avd/ ; ansible-test env

.PHONY: sanity-lint
sanity-lint: ## Run ansible-test sanity for code sanity. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test sanity --requirements --$(ANSIBLE_TEST_MODE) --skip-test import

.PHONY: sanity-import
sanity-import: ## Run ansible-test sanity for code import. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test sanity --requirements --$(ANSIBLE_TEST_MODE) --test import

.PHONY: galaxy-importer
galaxy-importer:  ## Run galaxy importer tests.
	rm -f *.tar.gz && \
	ansible-galaxy collection build --force ansible_collections/arista/avd && \
	python -m galaxy_importer.main *.tar.gz

#############################################
# Run unit test cases using ansible-test    #
#############################################

.PHONY: unit-tests
unit-tests: ## Run unit test cases using ansible-test. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test units --requirements --$(ANSIBLE_TEST_MODE) -vv

###################################################
# Run integration test cases using ansible-test   #
###################################################

.PHONY: integration-tests
integration-tests: ## Run integration test cases using ansible-test. Specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
	cd ansible_collections/arista/avd/ ; \
	ansible-test integration --requirements --$(ANSIBLE_TEST_MODE)

################
# Bump version #
################

.PHONY: bump-dev
bump-dev: ## Bump dev release. 6.0.0-dev0 -> 6.0.0-dev1
	bump-my-version bump pre_n

.PHONY: bump-release
bump-release: ## Bump from dev to final release. 6.2.0-dev2 -> 6.2.0
	bump-my-version bump pre_l

.PHONY: bump-minor
bump-minor: ## Bump minor release. 6.1.4 -> 6.2.0-dev0
	bump-my-version bump minor

.PHONY: bump-major
bump-major: ## Bump major release. 6.2.4 -> 7.0.0-dev0
	bump-my-version bump major

.PHONY: bump-patch
bump-patch: ## Bump patch release. 6.2.4 -> 6.2.5-dev0
	bump-my-version bump patch

####################
# Random shortcuts #
####################

.PHONY: config-diff
config-diff: ## Run git diff comparing molecule configs with 'devel' using our special config diff ignoring reordering of config lines.
	@GIT_EXTERNAL_DIFF=development/compare.py git diff devel --ext-diff -- **/configs/*.cfg

#########################################
# Documentation                         #
#########################################

SCHEMA_EXPLORER_SRC   = tools/schema-explorer
SCHEMA_EXPLORER_BUILD = tools/schema-explorer/build

.PHONY: schema-explorer-build
schema-explorer-build: ## Build the Schema Explorer (static assets + SQLite) into tools/schema-explorer/build/ for local inspection.
	uv run --group doc python $(SCHEMA_EXPLORER_SRC)/generate.py \
		--avd-root . --site-dir $(SCHEMA_EXPLORER_BUILD)

.PHONY: docs-serve
docs-serve: ## Run `mkdocs serve` on http://127.0.0.1:8000. The Schema Explorer hook builds its own cache outside the watched repo tree.
	uv run --group doc mkdocs serve --dev-addr=127.0.0.1:8000 -f mkdocs.yml

.PHONY: docs-serve-docker
docs-serve-docker: ## Same as docs-serve, but inside the webdoc_avd container (no host deps required).
	docker compose -f development/docker-compose.yml up


##########################
# Rerun End-to-end tests #
##########################

.PHONY: e2e
e2e: ##Run end-to-end tests regenerating all outputs and capturing errors to files.

	@echo ########################### examples/campus-fabric ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/examples/campus-fabric

	@echo ########################### examples/dual-dc-l3ls ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/examples/dual-dc-l3ls \
		--p2p-links-csv \
		--topology-csv

	@echo ########################### examples/isis-ldp-ipvpn ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/examples/isis-ldp-ipvpn \
		--p2p-links-csv \
		--topology-csv

	@echo ########################### examples/l2ls-fabric ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/examples/l2ls-fabric \
		--include-connected-endpoints

	@echo ########################### examples/single-dc-l3ls ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/examples/single-dc-l3ls \
		--p2p-links-csv \
		--topology-csv

	@echo ########################### examples/single-dc-l3ls-ipv6 ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/examples/single-dc-l3ls-ipv6 \
		--p2p-links-csv \
		--topology-csv

	@echo ########################### examples/single-dc-multipod-l3ls ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/examples/single-dc-multipod-l3ls \
		--p2p-links-csv \
		--topology-csv

	@echo ########################### molecule/digital_twin ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/digital_twin \
		--inventory-file inventory/hosts.yml

	@echo ########################### molecule/digital_twin digital-twin ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/digital_twin \
		--inventory-file inventory/hosts.yml \
		--output-dir digital_twin/intended \
		--docs-dir digital_twin/documentation \
		--digital-twin

#	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_cli_config_gen \
		--inventory-file inventory/hosts.yml
#	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_cli_config_gen_deprecated_vars \
		--inventory-file inventory/hosts.yml
#	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_cli_config_gen_negative_unit_tests \
		--inventory-file inventory/hosts.yml

	@echo ########################### molecule/eos_designs_deprecated_vars ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_designs_deprecated_vars \
		--inventory-file inventory/hosts.yml \
		--no-device-docs \
		--no-fabric-doc

	@echo ########################### molecule/eos_designs-l2ls ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_designs-l2ls \
		--inventory-file inventory/hosts.yml \
		--no-toc \
		--topology-csv \
		--p2p-links-csv

	@echo ########################### molecule/eos_designs-mpls-isis-sr-ldp ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_designs-mpls-isis-sr-ldp \
		--inventory-file inventory/hosts.yml \
		--topology-csv \
		--p2p-links-csv

	@echo ########################### molecule/eos_designs_negative_unit_tests ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_designs_negative_unit_tests \
		--inventory-file inventory/hosts.yml \
		--no-fabric-doc \
		--no-device-configs \
		--no-device-docs

	@echo ########################### molecule/eos_designs-twodc-5stage-clos ###########################
	uv run --refresh tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_designs-twodc-5stage-clos \
		--inventory-file inventory/hosts.yml \
		--include-connected-endpoints \
		--topology-csv \
		--p2p-links-csv \
		--custom-templates

	@echo ########################### molecule/eos_designs-twodc-5stage-clos digital-twin ###########################
	uv run --refresh tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_designs-twodc-5stage-clos \
		--inventory-file inventory/hosts.yml \
		--output-dir digital_twin/intended \
		--docs-dir digital_twin/documentation \
		--include-connected-endpoints \
		--topology-csv \
		--p2p-links-csv \
		--custom-templates \
		--digital-twin

	@echo ########################### molecule/eos_designs_unit_tests ###########################
	PYTHONPATH=ansible_collections/arista/avd/extensions/molecule/eos_designs_unit_tests/custom_modules \
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/eos_designs_unit_tests \
		--inventory-file inventory/hosts.yml \
		--no-device-docs \
		--no-fabric-doc

	@echo ########################### molecule/evpn_underlay_ebgp_overlay_ebgp ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/evpn_underlay_ebgp_overlay_ebgp \
		--inventory-file inventory/hosts.yml \
		--topology-csv \
		--p2p-links-csv \
		--custom-templates

	@echo ########################### molecule/evpn_underlay_isis_overlay_ibgp ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/evpn_underlay_isis_overlay_ibgp \
		--inventory-file inventory/hosts.yml

	@echo ########################### molecule/evpn_underlay_ospf_overlay_ebgp ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/evpn_underlay_ospf_overlay_ebgp \
		--inventory-file inventory/hosts.yml

	@echo ########################### molecule/evpn_underlay_rfc5549_overlay_ebgp ###########################
	uv run tools/e2e-test-avd.py \
		ansible_collections/arista/avd/extensions/molecule/evpn_underlay_rfc5549_overlay_ebgp \
		--inventory-file inventory/hosts.yml \
		--p2p-links-csv
