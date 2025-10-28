// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

// When running from Python we wish to cache Store inside Rust,
// to avoid sending the huge object back and forth.
// The store is initialized on first access with the included store (built from YAML fragments during compilation).
// It is possible to replace the store by calling `init_store_from_fragments` which will replace the inner option of the Mutex.

use std::sync::OnceLock;

use avdschema::Store;
use included_store::get_store as get_included_store;
use pyo3::pymodule;

static STORE: OnceLock<Store> = OnceLock::new();

fn get_store() -> &'static Store {
    STORE.get_or_init(get_included_store)
}

#[pymodule]
mod validation {
    use log::info;
    use std::path::PathBuf;

    use avdschema::{LoadFromFragments, Store, any::AnySchema, resolve_schema};

    use pyo3::{Bound, PyResult, exceptions::PyRuntimeError, pyfunction, types::PyModule};

    use validation::{
        Coercion as _, Context, StoreValidate as _, Validation as _, ValidationResult,
    };

    use super::{STORE, get_store};

    #[pymodule_init]
    fn init(_m: &Bound<'_, PyModule>) -> PyResult<()> {
        pyo3_log::init();
        Ok(())
    }

    #[pymodule_export]
    use ::validation::feedback::{
        CoercionNote, Feedback, Issue, Type, Value, Violation, ViolationValidValues,
    };

    #[pyfunction]
    pub fn init_store_from_fragments(
        eos_cli_config_gen: PathBuf,
        eos_designs: PathBuf,
    ) -> PyResult<()> {
        let mut eos_cli_config_gen_schema =
            AnySchema::from_fragments(eos_cli_config_gen).map_err(|err| {
                pyo3::exceptions::PyRuntimeError::new_err(format!(
                    "Error while reading the EosCliConfigGen schema fragments: {err}",
                ))
            })?;
        let mut eos_designs_schema = AnySchema::from_fragments(eos_designs).map_err(|err| {
            pyo3::exceptions::PyRuntimeError::new_err(format!(
                "Error while reading the EosDesigns schema fragments: {err}",
            ))
        })?;

        // First create the store without resolving schemas.
        let mut store = Store {
            eos_cli_config_gen: eos_cli_config_gen_schema.clone(),
            eos_designs: eos_designs_schema.clone(),
        };

        // Next resolve all $ref in each schema, updating the store as we go, to avoid re-resolving nested refs many times.
        let _ = resolve_schema(&mut eos_cli_config_gen_schema, &store);
        store.eos_cli_config_gen = eos_cli_config_gen_schema;
        let _ = resolve_schema(&mut eos_designs_schema, &store);
        store.eos_designs = eos_designs_schema;

        // Finally insert the resolved store into the OnceLock.
        STORE.set(store).map_err(|_| {
            PyRuntimeError::new_err(
                "Unable to initialize the schema store. \
                 Initialization can only happen once, and must be done before running any validations."
                    .to_string(),
            )
            }).inspect(|_| info!("Initialized the schema store from fragments."))
    }

    #[pyfunction]
    pub fn validate_json(data_as_json: &str, schema_name: &str) -> PyResult<ValidationResult> {
        get_store()
            .validate_json(data_as_json, schema_name, None)
            .map_err(|err| PyRuntimeError::new_err(format!("Invalid JSON in data: {err}")))
    }

    #[pyfunction]
    pub fn validate_json_with_adhoc_schema(
        data_as_json: &str,
        schema_as_json: &str,
    ) -> PyResult<ValidationResult> {
        // Parse schema JSON
        let schema: AnySchema = serde_json::from_str(schema_as_json).map_err(|err| {
            PyRuntimeError::new_err(format!("Invalid JSON in adhoc schema: {err}"))
        })?;
        // Parse data JSON
        let mut data: serde_json::Value = serde_json::from_str(data_as_json)
            .map_err(|err| PyRuntimeError::new_err(format!("Invalid JSON in data: {err}")))?;

        let mut ctx = Context::new(get_store(), None);
        schema.coerce(&mut data, &mut ctx);
        schema.validate_value(&data, &mut ctx);

        Ok(ctx.into())
    }
}

#[cfg(test)]
mod tests {
    use pyo3::{types::PyAnyMethods as _};
    use super::validation;

    #[test]
    fn validate_json_py_ok() {
        // Partial implementation of the pytest but here using pyo3 wrappers in Rust, to ensure we get coverage data
        // and that we can catch issues in Rust without building the Python first.
        pyo3::append_to_inittab!(validation);
        pyo3::Python::initialize();
        pyo3::Python::attach(|py| {
            let crate_dir = std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR"));
            let eos_cli_config_gen_fragment_dir = crate_dir
                .join("../../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments");
            let eos_designs_fragment_dir =
                crate_dir.join("../../../python-avd/pyavd/_eos_designs/schema/schema_fragments");

            let module = py.import("validation").unwrap();
            {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs.set_item("eos_cli_config_gen", eos_cli_config_gen_fragment_dir).unwrap();
                kwargs.set_item("eos_designs", eos_designs_fragment_dir).unwrap();
                module.call_method("init_store_from_fragments", args, Some(&kwargs)).unwrap();
            };

            let data_as_json_str = serde_json::json!({"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}, {"name": "Ethernet1"}, {}]}).to_string();
            let validation_result = {
                let args = ();
                let kwargs= pyo3::types::PyDict::new(py);
                kwargs.set_item("data_as_json", data_as_json_str).unwrap();
                kwargs.set_item("schema_name", "eos_cli_config_gen").unwrap();
                module.call_method("validate_json", args, Some(&kwargs)).unwrap()
            };
            assert!(validation_result.hasattr("violations").unwrap());
            let violations = validation_result.getattr("violations").unwrap();
            assert!(violations.is_instance_of::<pyo3::types::PyList>());
            assert_eq!(violations.len().unwrap(), 3);

            let issue_enum = module.getattr("Issue").unwrap();
            let violation_enum = module.getattr("Violation").unwrap();

            // Checking the first violation only. The rest are checked in the pytest implementation.
            let feedback = violations.get_item(0).unwrap();
            let path = feedback.getattr("path").unwrap().cast_into_exact::<pyo3::types::PyList>().unwrap();
            let expected_path = pyo3::types::PyList::new(py, ["ethernet_interfaces", "2"]).unwrap();
            assert!(path.eq(expected_path).unwrap());
            let issue = feedback.getattr("issue").unwrap();
            let expected_issue = issue_enum.getattr("Validation").unwrap();
            assert!(issue.get_type().eq(expected_issue).unwrap());
            let violation = issue.getattr("_0").unwrap();
            let expected_violation = violation_enum.getattr("MissingRequiredKey").unwrap();
            assert!(violation.get_type().eq(expected_violation).unwrap());
            let key = violation.getattr("key").unwrap();
            let expected_key = pyo3::types::PyString::new(py, "name");
            assert!(key.eq(expected_key).unwrap());
        });
    }
}
