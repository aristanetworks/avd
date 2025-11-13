// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::Store;

use crate::feedback::{ErrorIssue, Feedback, InfoIssue, WarningIssue};

/// The Context object is passed along during coercion and validation.
/// All coercions and violations will be registered in the context with the path carried in the context.
/// The store is used for looking up schema references.
#[derive(Debug)]
pub struct Context<'a> {
    pub configuration: Configuration,
    pub store: &'a Store,
    pub path: Vec<String>,
    pub result: ValidationResult,
}

impl<'a> Context<'a> {
    pub fn new(store: &'a Store, configuration: Option<&'a Configuration>) -> Self {
        Self {
            configuration: configuration.cloned().unwrap_or_default(),
            store,
            path: Default::default(),
            result: Default::default(),
        }
    }
    pub(crate) fn add_error(&mut self, error: impl Into<ErrorIssue>) {
        self.result.errors.push(Feedback {
            path: self.path.to_owned().into(),
            issue: error.into(),
        });
    }

    pub(crate) fn add_warning(&mut self, warning: impl Into<WarningIssue>) {
        self.result.warnings.push(Feedback {
            path: self.path.to_owned().into(),
            issue: warning.into(),
        });
    }

    pub(crate) fn add_info(&mut self, info: impl Into<InfoIssue>) {
        self.result.infos.push(Feedback {
            path: self.path.to_owned().into(),
            issue: info.into(),
        });
    }
}

/// Configuration to use during validation.
#[derive(Clone, Debug, Default)]
pub struct Configuration {
    pub ignore_required_keys_on_root_dict: bool,
    pub return_default_value_inserted_infos: bool,
    pub return_coercion_infos: bool,
}

#[derive(Clone, Debug, Default)]
pub struct ValidationResult {
    pub errors: Vec<Feedback<ErrorIssue>>,
    pub warnings: Vec<Feedback<WarningIssue>>,
    pub infos: Vec<Feedback<InfoIssue>>,
}
