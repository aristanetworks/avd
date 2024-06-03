
MOLECULE ?= eos_cli_config_gen
ANSIBLE_OPTIONS ?= --forks 5

.PHONY: help
help: ## Display help message.
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

################################################################
#                      Molecule Execution                      #
################################################################

.PHONY: test
test: ## Execute molecule "converge" sequence. Specify scenario name with `MOLECULE=<scenario_name>` (default: `eos_cli_config_gen`) and Ansible options with `ANSIBLE_OPTIONS=<options>` (default: `--forks 5`).
	cd .. && \
	molecule test --scenario-name $(MOLECULE) -- $(ANSIBLE_OPTIONS)

.PHONY: converge
converge: ## Execute molecule "converge" sequence. Specify scenario name with `MOLECULE=<scenario_name>` (default: `eos_cli_config_gen`) and Ansible options with `ANSIBLE_OPTIONS=<options>` (default: `--forks 5`).
	cd .. && \
	molecule converge --scenario-name $(MOLECULE) -- $(ANSIBLE_OPTIONS)

.PHONY: refresh-facts
refresh-facts: ## Run all "eos_designs" and "eos_cli_config_gen" molecule scenarios.
	@while read -r MOLECULE_SCENARIO; do \
		if [ -d "$$MOLECULE_SCENARIO" ]; then\
			echo "Run scenario for "$$MOLECULE_SCENARIO && \
			cd .. ; \
			molecule converge --scenario-name $$MOLECULE_SCENARIO -- $(ANSIBLE_OPTIONS); \
			cd ./molecule ; \
		fi \
	done <MOLECULE_SCENARIOS.txt
