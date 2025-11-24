// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::Store;

use crate::feedback::{ErrorIssue, Feedback, InfoIssue, Path, WarningIssue};

/// The Context object is passed along during coercion and validation.
/// All coercions and violations will be registered in the context with the path carried in the context.
/// The store is used for looking up schema references.
#[derive(Debug)]
pub struct Context<'a> {
    pub configuration: Configuration,
    pub store: &'a Store,
    pub result: ValidationResult,
    pub(crate) state: State,
}

impl<'a> Context<'a> {
    pub fn new(store: &'a Store, configuration: Option<&'a Configuration>) -> Self {
        Self {
            configuration: configuration.cloned().unwrap_or_default(),
            store,
            result: Default::default(),
            state: Default::default(),
        }
    }
    pub(crate) fn add_error(&mut self, error: impl Into<ErrorIssue>) {
        self.result.errors.push(Feedback {
            path: self.state.path.to_owned(),
            issue: error.into(),
        });
    }

    pub(crate) fn add_warning(&mut self, warning: impl Into<WarningIssue>) {
        self.result.warnings.push(Feedback {
            path: self.state.path.to_owned(),
            issue: warning.into(),
        });
    }

    pub(crate) fn add_info(&mut self, info: impl Into<InfoIssue>) {
        self.result.infos.push(Feedback {
            path: self.state.path.to_owned(),
            issue: info.into(),
        });
    }
}

/// Validation state set on Context during validation.
#[derive(Clone, Debug, Default)]
pub(crate) struct State {
    /// Don't validate required keys.
    /// Used for structured_config where we overload other config, and only the final result should be validated for required keys.
    pub(crate) relaxed_validation: bool,
    pub(crate) path: Path,
}

/// Configuration to use during validation.
#[derive(Clone, Debug, Default)]
pub struct Configuration {
    pub ignore_required_keys_on_root_dict: bool,
    pub return_coercion_infos: bool,
    /// By default Null/None values are ignored no matter which data type is expected.
    /// Setting this will instead emit type errors for Null values.
    pub restrict_null_values: bool,
}

#[derive(Clone, Debug, Default)]
pub struct ValidationResult {
    pub errors: Vec<Feedback<ErrorIssue>>,
    pub warnings: Vec<Feedback<WarningIssue>>,
    pub infos: Vec<Feedback<InfoIssue>>,
}
