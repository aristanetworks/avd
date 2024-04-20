# Example to add experimental protos:
# EXTRA_EXTRA_DIRS="-I ~/go/src/arista/resources" EXTRA_EXTRA_PROTOS="~/go/src/arista/resources/arista/configlet.v1/configlet.proto ~/go/src/arista/resources/arista/configlet.v1/services.gen.proto" make
VENDORPATH=cloudvision-apis
EXTRA_PROTOS=${PWD}/extra_cv_protos/arista/swg.v1/swg.proto ${PWD}/extra_cv_protos/arista/swg.v1/services.gen.proto
EXTRA_DIRS=-I ${PWD}/extra_cv_protos
EXTRA_EXTRA_DIRS?=
EXTRA_EXTRA_PROTOS?=
DUMMY := $(shell \
  rm -rf $(VENDORPATH); \
  git clone --single-branch --branch trunk https://github.com/aristanetworks/cloudvision-apis.git $(VENDORPATH); \
)

APIPATH=api

PYTHON ?= python3

ALL_PROTOS=$(shell find $(VENDORPATH) -name "*.proto")

IMPORTS_TO_TRY_EXCEPT_1 = import aristaproto\nimport grpclib\nfrom aristaproto\.grpc\.grpclib_server import ServiceBase
TRY_EXCEPTED_IMPORTS_1 = try:\n    import aristaproto\n    import grpclib\n    from aristaproto.grpc.grpclib_server import ServiceBase\nexcept ImportError:\n    HAS_ARISTAPROTO = False\n    from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.mocked_classes import mocked_aristaproto as aristaproto\n    from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.mocked_classes import mocked_grpclib as grpclib\n    ServiceBase = object\nelse:\n    HAS_ARISTAPROTO = True
IMPORTS_TO_TRY_EXCEPT_2 = ^import aristaproto
TRY_EXCEPTED_IMPORTS_2 = try:\n    import aristaproto\nexcept ImportError:\n    HAS_ARISTAPROTO = False\n    from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.mocked_classes import mocked_aristaproto as aristaproto\nelse:\n    HAS_ARISTAPROTO = True

default: api

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

api-dir:
	mkdir -p api
	rm -rf ./api/*

api-models: api-dir
	$(PYTHON) -m grpc_tools.protoc -I $(VENDORPATH) $(EXTRA_DIRS) $(EXTRA_EXTRA_DIRS) --python_aristaproto_out=$(APIPATH) $(ALL_PROTOS) $(EXTRA_PROTOS) $(EXTRA_EXTRA_PROTOS)

api-ansible-sanity-import: api-models
# For most arista protos
	find $(APIPATH) -name '*.py' -exec sed -z -i -e 's/$(IMPORTS_TO_TRY_EXCEPT_1)/$(TRY_EXCEPTED_IMPORTS_1)/g' {} +
# For fmp, subscriptions, time proto
	find $(APIPATH) -name '*.py' -exec sed -i -e 's/$(IMPORTS_TO_TRY_EXCEPT_2)/$(TRY_EXCEPTED_IMPORTS_2)/g' {} +

api: api-dir api-models api-ansible-sanity-import  ## Build/refresh gRPC bindings in ./api
	@rm -rf $(VENDORPATH)
	@pre-commit run insert-license --files $(shell find $(APIPATH)/ -name "*.py") || true
	@echo "--- done"
	@echo "If you got here, everything went well."
	@echo "All the output above is just because we use pre-commit to insert licenses into the generated files."
