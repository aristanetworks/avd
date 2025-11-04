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
    use super::{STORE, get_store};
    use avdschema::{LoadFromFragments, Store, any::AnySchema, resolve_schema};
    use log::info;
    use pyo3::{Bound, PyResult, exceptions::PyRuntimeError, pyclass, pyfunction, types::PyModule};
    use std::path::PathBuf;
    use validation::{
        Coercion as _, Context, StoreValidate as _, Validation as _, ValidationResult,
    };

    #[pyclass(frozen, get_all)]
    pub struct GetValidatedDataResult {
        pub validation_result: ValidationResult,
        pub validated_data: String,
    }

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
    pub fn get_validated_data(
        data_as_json: &str,
        schema_name: &str,
    ) -> PyResult<GetValidatedDataResult> {
        // The Value here will be in-place coerced to the correct data types.
        let mut data_as_value = serde_json::from_str::<serde_json::Value>(data_as_json)
            .map_err(|err| PyRuntimeError::new_err(format!("Invalid JSON in data: {err}")))?;

        let validation_result = get_store().validate_value(&mut data_as_value, schema_name, None);
        Ok(GetValidatedDataResult {
            validation_result,
            validated_data: serde_json::to_string(&data_as_value).map_err(|err| {
                PyRuntimeError::new_err(format!("Invalid JSON in coerced data: {err}"))
            })?,
        })
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

// Partial implementation of the pytests but here using pyo3 wrappers in Rust, to ensure we get coverage data
// and that we can catch issues in Rust without building the Python first.
#[cfg(test)]
mod tests {
    use super::validation;
    use pyo3::types::PyAnyMethods as _;
    const CRATE_DIR: &str = env!("CARGO_MANIFEST_DIR");
    const EOS_CLI_CONFIG_GEN_FRAGMENTS_DIR: &str =
        "../../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments";
    const EOS_DESIGNS_FRAGMENTS_DIR: &str =
        "../../../python-avd/pyavd/_eos_designs/schema/schema_fragments";

    // Initializing python only once. Otherwise things may crash when running in multiple threads.
    static INIT_PY: std::sync::Once = std::sync::Once::new();
    fn setup() {
        INIT_PY.call_once(|| {
            pyo3::append_to_inittab!(validation);
            pyo3::Python::initialize();
        })
    }

    fn get_dir(fragments_dir: &str) -> std::path::PathBuf {
        std::path::PathBuf::from(CRATE_DIR).join(fragments_dir)
    }

    // Initialize the store and ignoring errors for duplicate initialization.
    // This avoids false negatives when multiple tests are executed at once.
    fn shared_init_store(py: pyo3::Python<'_>) {
        let module = py.import("validation").unwrap();
        {
            let args = ();
            let kwargs = pyo3::types::PyDict::new(py);
            kwargs
                .set_item(
                    "eos_cli_config_gen",
                    get_dir(EOS_CLI_CONFIG_GEN_FRAGMENTS_DIR),
                )
                .unwrap();
            kwargs
                .set_item("eos_designs", get_dir(EOS_DESIGNS_FRAGMENTS_DIR))
                .unwrap();
            let _ = module.call_method("init_store_from_fragments", args, Some(&kwargs));
        };
    }

    #[test]
    fn validate_json_py_ok() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let data_as_json_str = serde_json::json!({"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}, {"name": "Ethernet1"}, {}]}).to_string();
            let validation_result = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs.set_item("data_as_json", data_as_json_str).unwrap();
                kwargs
                    .set_item("schema_name", "eos_cli_config_gen")
                    .unwrap();
                module
                    .call_method("validate_json", args, Some(&kwargs))
                    .unwrap()
            };
            assert!(validation_result.hasattr("violations").unwrap());
            let violations = validation_result.getattr("violations").unwrap();
            assert!(violations.is_instance_of::<pyo3::types::PyList>());
            assert_eq!(violations.len().unwrap(), 3);

            let issue_enum = module.getattr("Issue").unwrap();
            let violation_enum = module.getattr("Violation").unwrap();

            // Checking the first violation only. The rest are checked in the pytest implementation.
            let feedback = violations.get_item(0).unwrap();
            let path = feedback
                .getattr("path")
                .unwrap()
                .cast_into_exact::<pyo3::types::PyList>()
                .unwrap();
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

    #[test]
    fn init_store_py_invalid_fragment_paths() {
        setup();
        pyo3::Python::attach(|py| {
            let module = py.import("validation").unwrap();

            // Test with invalid eos_cli_config_gen path
            let err = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs
                    .set_item("eos_cli_config_gen", "invalid_path")
                    .unwrap();
                kwargs
                    .set_item("eos_designs", get_dir(EOS_DESIGNS_FRAGMENTS_DIR))
                    .unwrap();
                module
                    .call_method("init_store_from_fragments", args, Some(&kwargs))
                    .unwrap_err()
            };
            assert_eq!(
                err.value(py).to_string(),
                "Error while reading the EosCliConfigGen schema fragments: No files found."
            );

            // Test with invalid eos_designs path
            let err = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs
                    .set_item(
                        "eos_cli_config_gen",
                        get_dir(EOS_CLI_CONFIG_GEN_FRAGMENTS_DIR),
                    )
                    .unwrap();
                kwargs.set_item("eos_designs", "invalid_path").unwrap();
                module
                    .call_method("init_store_from_fragments", args, Some(&kwargs))
                    .unwrap_err()
            };
            assert_eq!(
                err.value(py).to_string(),
                "Error while reading the EosDesigns schema fragments: No files found."
            );
        });
    }

    #[test]
    fn init_store_py_twice() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let err = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs
                    .set_item(
                        "eos_cli_config_gen",
                        get_dir(EOS_CLI_CONFIG_GEN_FRAGMENTS_DIR),
                    )
                    .unwrap();
                kwargs
                    .set_item("eos_designs", get_dir(EOS_DESIGNS_FRAGMENTS_DIR))
                    .unwrap();
                module
                    .call_method("init_store_from_fragments", args, Some(&kwargs))
                    .unwrap_err()
            };

            assert_eq!(
                err.value(py).to_string(),
                "Unable to initialize the schema store. \
                 Initialization can only happen once, and must be done before running any validations."
            )
        })
    }

    #[test]
    fn validate_json_py_invalid_json() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let err = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs.set_item("data_as_json", "invalid_json").unwrap();
                kwargs
                    .set_item("schema_name", "eos_cli_config_gen")
                    .unwrap();
                module
                    .call_method("validate_json", args, Some(&kwargs))
                    .unwrap_err()
            };
            assert_eq!(
                err.value(py).to_string(),
                "Invalid JSON in data: expected value at line 1 column 1"
            )
        });
    }

    #[test]
    fn validate_json_with_adhoc_schema_py_ok() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let validation_result = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs
                    .set_item("data_as_json", serde_json::json!(1234).to_string())
                    .unwrap();
                kwargs
                    .set_item(
                        "schema_as_json",
                        serde_json::json!({"type": "int", "max": 1233}).to_string(),
                    )
                    .unwrap();
                module
                    .call_method("validate_json_with_adhoc_schema", args, Some(&kwargs))
                    .unwrap()
            };
            assert!(validation_result.hasattr("violations").unwrap());
            let violations = validation_result.getattr("violations").unwrap();
            assert!(violations.is_instance_of::<pyo3::types::PyList>());
            assert_eq!(violations.len().unwrap(), 1);

            let issue_enum = module.getattr("Issue").unwrap();
            let violation_enum = module.getattr("Violation").unwrap();

            // Checking the first violation only. The rest are checked in the pytest implementation.
            let feedback = violations.get_item(0).unwrap();
            let path = feedback
                .getattr("path")
                .unwrap()
                .cast_into_exact::<pyo3::types::PyList>()
                .unwrap();
            assert_eq!(path.len().unwrap(), 0);
            let issue = feedback.getattr("issue").unwrap();
            let expected_issue = issue_enum.getattr("Validation").unwrap();
            assert!(issue.get_type().eq(expected_issue).unwrap());
            let violation = issue.getattr("_0").unwrap();
            let expected_violation = violation_enum.getattr("ValueAboveMaximum").unwrap();
            assert!(violation.get_type().eq(expected_violation).unwrap());
            let expected_maximum = pyo3::types::PyInt::new(py, 1233);
            let maximum = violation.getattr("maximum").unwrap();
            assert!(maximum.eq(expected_maximum).unwrap());
            let expected_found = pyo3::types::PyInt::new(py, 1234);
            let found = violation.getattr("found").unwrap();
            assert!(found.eq(expected_found).unwrap());
        });
    }

    #[test]
    fn validate_json_with_adhoc_schema_py_invalid_json() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let err = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs.set_item("data_as_json", "invalid_json").unwrap();
                kwargs
                    .set_item(
                        "schema_as_json",
                        serde_json::json!({"type": "dict"}).to_string(),
                    )
                    .unwrap();
                module
                    .call_method("validate_json_with_adhoc_schema", args, Some(&kwargs))
                    .unwrap_err()
            };
            assert_eq!(
                err.value(py).to_string(),
                "Invalid JSON in data: expected value at line 1 column 1"
            )
        });
    }

    #[test]
    fn validate_json_with_adhoc_schema_py_invalid_schema() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let err = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs.set_item("data_as_json", "{}").unwrap();
                kwargs
                    .set_item(
                        "schema_as_json",
                        serde_json::json!({"tpe": "dict"}).to_string(),
                    )
                    .unwrap();
                module
                    .call_method("validate_json_with_adhoc_schema", args, Some(&kwargs))
                    .unwrap_err()
            };
            assert_eq!(
                err.value(py).to_string(),
                "Invalid JSON in adhoc schema: missing field `type` at line 1 column 14"
            )
        });
    }

    #[test]
    fn get_validated_data_ok() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let data_as_json_str = serde_json::json!({"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}]}).to_string();
            let get_validated_data_result = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs.set_item("data_as_json", data_as_json_str).unwrap();
                kwargs
                    .set_item("schema_name", "eos_cli_config_gen")
                    .unwrap();
                module
                    .call_method("get_validated_data", args, Some(&kwargs))
                    .unwrap()
            };
            let validated_data = get_validated_data_result.getattr("validated_data").unwrap();
            let expected_data = pyo3::types::PyString::new(
                py,
                &serde_json::json!(
                {
                    "ethernet_interfaces":[
                        {
                            "name":"Ethernet1",
                            "description":"12345",
                            "ospf_authentication_key_type":"7"
                        }
                    ],
                    // These are defaults inserted by the validation tooling.
                    "avd_data_validation_mode":"error",
                    "config_end":false,
                    "generate_default_config":false,
                    "generate_device_documentation":true,
                    "transceiver_qsfp_default_mode_4x10":true
                })
                .to_string(),
            );
            assert!(
                validated_data.eq(&expected_data).unwrap(),
                "Different data: {validated_data} vs {expected_data}"
            );
            let validation_result = get_validated_data_result
                .getattr("validation_result")
                .unwrap();
            let violations = validation_result.getattr("violations").unwrap();
            assert!(violations.is_instance_of::<pyo3::types::PyList>());
            assert_eq!(violations.len().unwrap(), 0);

            let coercions = validation_result.getattr("coercions").unwrap();
            assert!(coercions.is_instance_of::<pyo3::types::PyList>());

            // The coercions also contains feedback for insertion of default values, so we first filter to only have actual coercions.
            let issue_enum = module.getattr("Issue").unwrap();
            let coercion_feedbacks = coercions
                .cast_exact::<pyo3::types::PyList>()
                .unwrap()
                .into_iter()
                .filter(|feedback| {
                    let issue = feedback.getattr("issue").unwrap();
                    let coercion_type = issue_enum.getattr("Coercion").unwrap();
                    issue.get_type().eq(coercion_type).unwrap()
                })
                .collect::<Vec<pyo3::Bound<'_, pyo3::PyAny>>>();
            assert_eq!(coercion_feedbacks.len(), 1);

            let feedback = coercion_feedbacks.first().unwrap();
            let path = feedback.getattr("path").unwrap();
            let expected_path =
                pyo3::types::PyList::new(py, ["ethernet_interfaces", "0", "description"]).unwrap();
            assert!(path.eq(expected_path).unwrap());
            let issue = feedback.getattr("issue").unwrap();

            let coercion_note = issue.getattr("_0").unwrap();
            let found = coercion_note
                .getattr("found")
                .unwrap()
                .getattr("_0")
                .unwrap();
            let expected_found = pyo3::types::PyInt::new(py, 12345);
            assert!(
                found.eq(expected_found).unwrap(),
                "Found something else: {}",
                found
            );
            let made = coercion_note
                .getattr("made")
                .unwrap()
                .getattr("_0")
                .unwrap();
            let expected_made = pyo3::types::PyString::new(py, "12345");
            assert!(made.eq(expected_made).unwrap());
        });
    }

    #[test]
    fn get_validated_data_not_ok() {
        setup();
        pyo3::Python::attach(|py| {
            shared_init_store(py);

            let module = py.import("validation").unwrap();
            let data_as_json_str = serde_json::json!({"ethernet_interfaces": [{"name": "Ethernet1", "unknown": 12345}]}).to_string();
            let get_validated_data_result = {
                let args = ();
                let kwargs = pyo3::types::PyDict::new(py);
                kwargs.set_item("data_as_json", data_as_json_str).unwrap();
                kwargs
                    .set_item("schema_name", "eos_cli_config_gen")
                    .unwrap();
                module
                    .call_method("get_validated_data", args, Some(&kwargs))
                    .unwrap()
            };
            let validated_data = get_validated_data_result.getattr("validated_data").unwrap();
            let expected_data = pyo3::types::PyString::new(
                py,
                &serde_json::json!(
                {
                    "ethernet_interfaces":[
                        {
                            "name":"Ethernet1",
                            "unknown":12345,
                            "ospf_authentication_key_type":"7"
                        }
                    ],
                    // These are defaults inserted by the validation tooling.
                    "avd_data_validation_mode":"error",
                    "config_end":false,
                    "generate_default_config":false,
                    "generate_device_documentation":true,
                    "transceiver_qsfp_default_mode_4x10":true
                })
                .to_string(),
            );
            assert!(
                validated_data.eq(&expected_data).unwrap(),
                "Different data: {validated_data} vs {expected_data}"
            );
            let validation_result = get_validated_data_result
                .getattr("validation_result")
                .unwrap();
            let violations = validation_result.getattr("violations").unwrap();
            assert!(violations.is_instance_of::<pyo3::types::PyList>());
            assert_eq!(violations.len().unwrap(), 1);

            let issue_enum = module.getattr("Issue").unwrap();
            let violation_enum = module.getattr("Violation").unwrap();

            let violation_feedbacks = violations.cast_exact::<pyo3::types::PyList>().unwrap();
            assert_eq!(violation_feedbacks.len().unwrap(), 1);

            let feedback = violations.get_item(0).unwrap();
            let path = feedback.getattr("path").unwrap();
            let expected_path =
                pyo3::types::PyList::new(py, ["ethernet_interfaces", "0", "unknown"]).unwrap();
            assert!(path.eq(expected_path).unwrap());

            let issue = feedback.getattr("issue").unwrap();
            let expected_issue = issue_enum.getattr("Validation").unwrap();
            assert!(issue.get_type().eq(expected_issue).unwrap());

            let violation = issue.getattr("_0").unwrap();
            let expected_violation = violation_enum.getattr("UnexpectedKey").unwrap();
            assert!(violation.get_type().eq(expected_violation).unwrap());
        });
    }
}
