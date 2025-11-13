// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::base::valid_values::ValidValues;

use crate::feedback::Violation;

use crate::context::Context;

pub(crate) trait ValidateValidValues<T> {
    /// Validate that the value is one of the valid values.
    fn validate(&self, input: &T, ctx: &mut Context);
}

impl ValidateValidValues<i64> for ValidValues<i64> {
    fn validate(&self, input: &i64, ctx: &mut Context) {
        if let Some(valid_values) = self.valid_values.as_ref()
            && !valid_values.contains(input) {
                ctx.add_error(Violation::InvalidValue {
                    expected: valid_values.to_owned().into(),
                    found: input.to_owned().into(),
                });
            }
    }
}

impl ValidateValidValues<String> for ValidValues<String> {
    fn validate(&self, input: &String, ctx: &mut Context) {
        if let Some(valid_values) = self.valid_values.as_ref()
            && !valid_values.contains(input) {
                ctx.add_error(Violation::InvalidValue {
                    expected: valid_values.to_owned().into(),
                    found: input.to_owned().into(),
                });
            }
    }
}
