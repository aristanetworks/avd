// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

mod sha512crypt;

use pyo3::pymodule;

#[pymodule]
#[pyo3(name = "passwords")]
mod passwords {

    use crate::sha512crypt;
    use pyo3::{Bound, PyResult, pyfunction, types::PyModule};

    #[pymodule_init]
    fn init(_m: &Bound<'_, PyModule>) -> PyResult<()> {
        Ok(())
    }

    #[pyfunction]
    /// Computes the SHA512 crypt value for the password given the salt
    pub fn sha512_crypt(password: String, salt: String) -> String {
        let result = sha512crypt::main(password, salt);

        match result {
            Ok(res) => res,
            Err(e) => format!("{e:?}").to_string(),
            // Err(e) => serde_json::to_string(&e).unwrap(),
        }
    }
}
