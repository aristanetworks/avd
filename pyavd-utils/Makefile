CURRENT_DIR = $(shell pwd)
ANSIBLE_AVD_DIR ?= ..
SCRIPTS_DIR = $(CURRENT_DIR)/scripts

# export PYTHONPATH=$(CURRENT_DIR) # Uncomment to test from source

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Build pyavd-utils package
	rm -rf $(CURRENT_DIR)/build/ $(CURRENT_DIR)/dist/ $(CURRENT_DIR)/pyavd.egg-info/ $(CURRENT_DIR)/pyavd_utils/*.so

.PHONY: build
build: clean check-cargo ## Build pyavd-utils package
	pip3 install build
	python3 -m build --wheel

.PHONY: uv-build
uv-build: clean check-cargo ## Build pyavd-utils package
	uv pip install build
	python3 -m build --wheel

.PHONY: publish
publish: ## Publish pyavd package to PyPI (build first)
	pip3 install twine && \
	twine check dist/* && \
	twine upload -r testpypi dist/* && \
	twine upload dist/*

.PHONY: uv-publish
uv-publish: ## Publish pyavd package to PyPI (build first)
	uv pip install twine && \
	twine check dist/* && \
	twine upload -r testpypi dist/* && \
	twine upload dist/*

.PHONY: check-cargo
check-cargo: ## Checks for the presence of the 'cargo' command.
	@echo "--- Checking for Rust toolchain (cargo)..."
	@if [ -n "$(CARGO)" ]; then \
		echo "Found cargo via CARGO environment variable: $(CARGO)"; \
	elif command -v cargo >/dev/null 2>&1; then \
		echo "Found cargo in system PATH: $(shell which cargo)"; \
	else \
		echo "======================================================================"; \
		echo "ERROR: Rust Toolchain (cargo) is NOT installed or not found in PATH."; \
		echo "       The 'cargo' command is required to build this project."; \
		echo "       Please install the official Rust toolchain via rustup, or set"; \
		echo "       the CARGO environment variable to the path of your cargo binary."; \
		echo "       Run 'make install-rust' to get started."; \
		echo "======================================================================"; \
		exit 1; \
	fi
	@echo "--- Rust toolchain check passed."

.PHONY: install-rust
install-rust: ## Provides the standard command to install the Rust toolchain using rustup.
	@echo "--- Installing the official Rust Toolchain via rustup ---"
	@echo "This script downloads and runs the official installation tool."
	@echo "Follow the on-screen prompts (usually selecting option 1 for default installation)."
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
	@echo "======================================================================"
	@echo "Installation complete. You may need to restart your shell or run:"
	@echo "  source "$$HOME/.cargo/env""
	@echo "for the 'cargo' command to be immediately available in your current terminal session."
	@echo "======================================================================"
