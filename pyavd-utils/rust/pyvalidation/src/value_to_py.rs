// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use pyo3::{
    IntoPyObject as _, IntoPyObjectExt as _, Py, PyAny, PyErr, PyResult, Python,
    exceptions::PyValueError,
    types::{PyDict, PyList, PyNone},
};

fn value_to_py(value: serde_json::Value, py: Python) -> PyResult<Py<PyAny>> {
    match value {
        serde_json::Value::Null => todo!(),
        serde_json::Value::Bool(boolean) => boolean.into_py_any(py),
        serde_json::Value::Number(number) => {
            if let Some(float) = number.as_f64() {
                float.into_py_any(py)
            } else {
                number
                    .as_i64()
                    .ok_or_else(|| {
                        PyValueError::new_err(format!(
                            "The number '{}' is not a supported format.",
                            number.as_str()
                        ))
                    })?
                    .into_py_any(py)
            }
        }
        serde_json::Value::String(_) => todo!(),
        serde_json::Value::Array(values) => values
            .into_iter()
            .map(|item| value_to_py(item, py))
            .collect::<PyResult<Vec<_>>>()
            .and_then(|items| items.into_py_any(py)),
        serde_json::Value::Object(map) => {
            PyDict::from_sequence(map.into_iter().map(|(map_key, map_value)| {
                Ok((map_key.into_py_any(py)?, value_to_py(map_value, py)?))
            }))
            .map(|py_dict| py_dict.unbind().as_any())
        }
    }
}
