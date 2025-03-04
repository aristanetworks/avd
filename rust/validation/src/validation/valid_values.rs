// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::base::DataValue;
use avdschema::base::valid_values::ValidValues;

use crate::feedback::MiscViolation;

use crate::context::Context;

pub(crate) trait ValidateValidValues<T> {
    fn validate(&self, input: &T, ctx: &mut Context);
}
impl<T: DataValue + PartialEq> ValidateValidValues<T> for ValidValues<T> {
    fn validate(&self, input: &T, ctx: &mut Context) {
        if self
            .valid_values
            .as_ref()
            .map(|valid_values| !valid_values.contains(input))
            .unwrap_or_default()
        {
            ctx.add_violation(MiscViolation::DisallowedValue);
        }
    }
}
