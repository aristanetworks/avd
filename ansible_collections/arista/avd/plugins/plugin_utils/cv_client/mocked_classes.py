# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Dummy class for mock aristaproto. Required to pass ansible sanity tests.
Once things move away from the ansible collection this can be removed again.
"""

ARISTAPROTO_ATTRIBUTES = [
    "Casing",
    "DATETIME_ZERO",
    "Enum",
    "FIXED_TYPES",
    "FieldMetadata",
    "INFINITY",
    "INT_64_TYPES",
    "Message",
    "NAN",
    "NEG_INFINITY",
    "PACKED_TYPES",
    "PLACEHOLDER",
    "ParsedField",
    "ProtoClassMetadata",
    "SIZE_DELIMITED",
    "ServiceStub",
    "TYPE_BOOL",
    "TYPE_BYTES",
    "TYPE_DOUBLE",
    "TYPE_ENUM",
    "TYPE_FIXED32",
    "TYPE_FIXED64",
    "TYPE_FLOAT",
    "TYPE_INT32",
    "TYPE_INT64",
    "TYPE_MAP",
    "TYPE_MESSAGE",
    "TYPE_SFIXED32",
    "TYPE_SFIXED64",
    "TYPE_SINT32",
    "TYPE_SINT64",
    "TYPE_STRING",
    "TYPE_UINT32",
    "TYPE_UINT64",
    "WIRE_FIXED_32",
    "WIRE_FIXED_32_TYPES",
    "WIRE_FIXED_64",
    "WIRE_FIXED_64_TYPES",
    "WIRE_LEN_DELIM",
    "WIRE_LEN_DELIM_TYPES",
    "WIRE_VARINT",
    "WIRE_VARINT_TYPES",
    "bool_field",
    "bytes_field",
    "casing",
    "datetime_default_gen",
    "decode_varint",
    "double_field",
    "dump_varint",
    "encode_varint",
    "enum_field",
    "fixed32_field",
    "fixed64_field",
    "float_field",
    "int32_field",
    "int64_field",
    "load_fields",
    "load_varint",
    "map_field",
    "message_field",
    "parse_fields",
    "serialized_on_wire",
    "sfixed32_field",
    "sfixed64_field",
    "sint32_field",
    "sint64_field",
    "size_varint",
    "string_field",
    "uint32_field",
    "uint64_field",
    "which_one_of",
]


class mocked_aristaproto:
    pass


class mocked_grpclib:
    class const:
        class Handler:
            pass


def dummy_callable(*args, **kwargs):
    pass


for attribute in ARISTAPROTO_ATTRIBUTES:
    if attribute.isupper():
        setattr(mocked_aristaproto, attribute, "dummyvalue")
    elif attribute[:1].isupper():
        setattr(mocked_aristaproto, attribute, object)
    else:
        setattr(mocked_aristaproto, attribute, dummy_callable)
