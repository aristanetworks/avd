// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use pyo3::pymodule;

#[pymodule]
#[pyo3(name = "passwords")]
mod passwords {

    use pyo3::{PyResult, pyfunction};

    #[pyfunction]
    /// Computes the SHA512 crypt value for the password given the salt
    pub fn sha512_crypt(password: String, salt: String) -> PyResult<String> {
        passwords::sha512_crypt(&password, &salt).map_err(|err| {
            // Mapping our crates error to Python errors.
            match err {
                passwords::Sha512CryptError::InvalidSalt(_) => {
                    pyo3::exceptions::PyValueError::new_err(format!("{err}"))
                }
                passwords::Sha512CryptError::ShaCrypt(_) => {
                    pyo3::exceptions::PyRuntimeError::new_err(format!("{err}"))
                }
            }
        })
    }
}

// Implementation of the pytests but here using pyo3 wrappers in Rust, to ensure we get coverage data
// and that we can catch issues in Rust without building the Python first.
#[cfg(test)]
mod tests {
    use super::passwords;
    use pyo3::types::PyAnyMethods as _;

    // Initializing python only once. Otherwise things may crash when running in multiple threads.
    static INIT_PY: std::sync::Once = std::sync::Once::new();
    fn setup() {
        INIT_PY.call_once(|| {
            pyo3::append_to_inittab!(passwords);
            pyo3::Python::initialize();
        })
    }

    #[test]
    fn sha512_crypt_valid_hash_with_salt_ok() {
        setup();
        pyo3::Python::attach(|py| {
            let module = py.import("passwords").unwrap();
            let args = ();
            let kwargs = pyo3::types::PyDict::new(py);
            kwargs
                .set_item("password", pyo3::types::PyString::new(py, "arista"))
                .unwrap();
            kwargs
                .set_item("salt", pyo3::types::PyString::new(py, "1234567890ABCDEF"))
                .unwrap();
            let result = module
                .call_method("sha512_crypt", args, Some(&kwargs))
                .unwrap();

            let expected_hash = pyo3::types::PyString::new(
                py,
                // Ignoring test data.
                // NOSONAR
                "$6$1234567890ABCDEF$5h/.K2RuwSPqXTncNaqmw./4HduYZNE4RHDfivjrQ8nrYX3AcB8gKSsKFC1VSVOl3E46/QFZ85uHZWhxQGTeS0",
            );
            assert!(result.eq(expected_hash).unwrap());
        });
    }

    #[test]
    fn sha512_crypt_empty_salt_err() {
        setup();
        pyo3::Python::attach(|py| {
            let module = py.import("passwords").unwrap();
            let args = ();
            let kwargs = pyo3::types::PyDict::new(py);
            kwargs
                .set_item("password", pyo3::types::PyString::new(py, "arista"))
                .unwrap();
            kwargs
                .set_item("salt", pyo3::types::PyString::new(py, ""))
                .unwrap();
            let err = module
                .call_method("sha512_crypt", args, Some(&kwargs))
                .unwrap_err();

            assert_eq!(
                err.value(py).to_string(),
                "Invalid Salt: Salt cannot be empty."
            );
        });
    }

    #[test]
    fn sha512_crypt_invalid_character_in_salt_err() {
        setup();
        pyo3::Python::attach(|py| {
            let module = py.import("passwords").unwrap();
            let args = ();
            let kwargs = pyo3::types::PyDict::new(py);
            kwargs
                .set_item("password", pyo3::types::PyString::new(py, "arista"))
                .unwrap();
            kwargs
                .set_item("salt", pyo3::types::PyString::new(py, "🐍"))
                .unwrap();
            let err = module
                .call_method("sha512_crypt", args, Some(&kwargs))
                .unwrap_err();

            assert_eq!(
                err.value(py).to_string(),
                "Invalid Salt: Salt contains an invalid character: '🐍'"
            );
        });
    }
}
