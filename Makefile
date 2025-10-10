CURRENT_DIR = $(shell pwd)
# option to run ansible-test sanity: must be either venv or docker (default is venv)
ANSIBLE_TEST_MODE ?= venv
MUFFET_TIMEOUT ?= 60

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

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
	cd python-avd && $(MAKE) && tox -r

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
