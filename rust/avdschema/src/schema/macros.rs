// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

/// Macro to avoid repeating the match for AnySchema just to call the same method on each variant.
///
/// ```rust
/// delegate_anyshcema_method!(self, is_required,)
/// ```
///
/// will generate
///
/// ```rust
/// match $self {
///     Self::Bool(schema) => schema.is_required(),
///     Self::Int(schema) => schema.is_required(),
///     Self::Str(schema) => schema.is_required(),
///     Self::List(schema) => schema.is_required(),
///     Self::Dict(schema) => schema.is_required(),
/// }
/// ```
///
/// It is also possible to give extra arguments to the called method like:
///
/// ```rust
/// delegate_anyshcema_method!(self, my_method, arg1, arg2)
/// ```
#[macro_export]
macro_rules! delegate_anyshcema_method {
    ($self:ident, $method:ident, $($arg:expr),*) => {
        match $self {
            Self::Bool(schema) => schema.$method($($arg,)*),
            Self::Int(schema) => schema.$method($($arg,)*),
            Self::Str(schema) => schema.$method($($arg,)*),
            Self::List(schema) => schema.$method($($arg,)*),
            Self::Dict(schema) => schema.$method($($arg,)*),
        }
    };
}
