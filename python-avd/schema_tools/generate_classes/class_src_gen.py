# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from keyword import iskeyword
from typing import TYPE_CHECKING

from .src_generators import ClassVarSrc, FieldSrc, FieldTypeHintSrc, ModelSrc, SrcData
from .utils import generate_class_name, generate_class_name_from_ref

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AvdSchemaBool, AvdSchemaDict, AvdSchemaField, AvdSchemaInt, AvdSchemaList, AvdSchemaStr


class SrcGenBase:
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    # TODO: add deprecation handling
    #       dynamic_valid_values
    #       Create a base model for lists so child items can be rendered by their own generators instead of trying to handle it inside lists.

    def generate_class_src(self, schema: AvdSchemaField, class_name: str | None = None) -> SrcData:
        """
        Returns SrcData for the given schema.

        Recursively walks child schemas and creates nested classes and fields.
        """
        self.schema = schema
        self.class_name = class_name

        if schema.deprecation and schema.deprecation.removed:
            return SrcData(field=None, cls=None)

        return SrcData(field=self.get_field(), cls=self.get_class())

    def get_field(self) -> FieldSrc | None:
        """Returns FieldSrc for the given schema to be used for the field definition in the parent object."""
        if not self.schema._key:
            msg = f"No key set for schema {self.schema.type}"
            raise ValueError(msg)

        return FieldSrc(
            name=self.get_field_name(),
            key=self.get_key(),
            type_hints=self.get_type_hints(),
            optional=not (bool(self.schema.required) or self.schema._is_primary_key),
            default_value=self.get_default(),
            description=self.schema.description,
        )

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        """Returns a list of FieldTypeHintSrc representing the type hints for this schema."""
        field_type = cls.name if (cls := self.get_class()) else self.schema.type

        return [
            FieldTypeHintSrc(
                field_type=field_type,
                # TODO: For annotation based validation we need this: annotations=get_annotations_for_field(self.schema),
            )
        ]

    def get_class_name(self) -> str:
        """Returns the class name to be used for the class definition in the parent object."""
        if self.class_name:
            return generate_class_name(self.class_name)

        return generate_class_name(self.get_key())

    def get_class(self) -> ModelSrc | None:
        """Returns ModelSrc for the given schema to be used for the class definition in the parent object."""
        return None

    def get_key(self) -> str:
        """Returns the key name after stripping dynamic key syntax."""
        return self.schema._key.replace("<", "").replace(">", "").replace(".", "_")

    def get_field_name(self) -> str:
        """
        Returns the name to be used for the field definition in the parent object.

        Python reserved keywords pr mixed case keys will get a prefix of "field_".
        """
        if not self.valid_key:
            return f"field_{self.get_key()}"
        return self.get_key()

    @property
    def valid_key(self) -> bool:
        """Check if the key name can be used as field name."""
        return not iskeyword(self.schema._key) and self.schema._key.islower()

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        if self.schema.default is not None:
            return str(self.schema.default)
        return None


class SrcGenInt(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaInt


class SrcGenBool(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaBool


class SrcGenStr(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaStr

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        if self.schema.default is not None:
            return f'"{self.schema.default}"'
        return None


class SrcGenList(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaList

    def get_class(self) -> ModelSrc | None:
        """Returns ModelSrc for the given schema to be used for the class definition in the parent object."""
        if not self.schema.items:
            return None

        if self.schema.items.type != "dict":
            return None

        fields = []
        classes = []

        if self.schema.items.keys:
            fields.append(
                FieldSrc(
                    name="_custom_data",
                    optional=False,
                    type_hints=[FieldTypeHintSrc(field_type="dict[str, Any]")],
                )
            )
            for childschema in self.schema.items.keys.values():
                fieldsrc = childschema._generate_class_src()
                if fieldsrc.field:
                    fields.append(fieldsrc.field)
                if fieldsrc.cls:
                    classes.append(fieldsrc.cls)

        return ModelSrc(
            name=f"{self.get_class_name()}Item",
            base_classes=self.get_base_classes(),
            classes=classes,
            fields=fields,
            allow_extra=self.schema.items.allow_other_keys,
            # TODO: figure out if we need this: description=self.get_description(),
        )

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        """Returns a list of FieldTypeHintSrc representing the type hints for this schema."""
        if not self.schema.items:
            return [FieldTypeHintSrc(field_type="list", list_item_type="Any")]

        item_type = cls.name if (cls := self.get_class()) else self.schema.items.type

        return [
            FieldTypeHintSrc(
                field_type="list",
                list_item_type=FieldTypeHintSrc(
                    field_type=item_type,
                ),
            )
        ]

    def get_base_classes(self) -> list[str]:
        """Return a list of base classes. Only used if there is an unresolved $ref in the schema."""
        if not self.schema.items or not self.schema.items.field_ref:
            return []

        return [generate_class_name_from_ref(self.schema.items.field_ref)]

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        if self.schema.default is None:
            return None
        default_value_as_str = str(self.schema.default).replace("'", '"')
        item_type = self.get_type_hints()[0].list_item_type
        if isinstance(item_type, FieldTypeHintSrc) and item_type.field_type[0].isupper():
            item_type = f"self.__class__.{item_type.field_type}"
            return f"lambda cls: coerce_type({default_value_as_str}, target_type=list, list_items_type=cls)"

        return default_value_as_str


class SrcGenDict(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaDict

    def get_class(self) -> ModelSrc | None:
        """Returns ModelSrc for the given schema to be used for the class definition in the parent object."""
        if not self.schema.keys:
            if not self.schema.field_ref:
                return None

            classes, fields = [], []

        else:
            classes, fields = self.get_children_classes_and_fields()
        return ModelSrc(
            name=self.get_class_name(),
            base_classes=self.get_base_classes(),
            classes=classes,
            fields=fields,
            imports=self.get_imports(),
            allow_extra=self.schema.allow_other_keys,
            # TODO: figure out if we need this? description=self.get_description(),
        )

    def get_base_classes(self) -> list[str]:
        """Return a list of base classes. Only used if there is an unresolved $ref in the schema."""
        if not self.schema.field_ref:
            return []

        return [generate_class_name_from_ref(self.schema.field_ref)]

    def get_imports(self) -> set[str]:
        """Return a set of strings with Python imports that are needed for this class."""
        imports = set()
        imports.add("from typing import Any")
        if self.schema.field_ref:
            schema_name = self.schema.field_ref.split("#", maxsplit=1)[0]
            imports.add(f"from pyavd._{schema_name}.schema import {generate_class_name(schema_name)}")

        return imports

    def get_children_classes_and_fields(self) -> tuple[list[ModelSrc], list[FieldSrc]]:
        """Return lists of ModelSrc and FieldSrc for any nested fields."""
        classes = []
        fields = []

        if not isinstance(self, SrcGenRootDict):
            fields.append(
                FieldSrc(
                    name="_custom_data",
                    optional=False,
                    type_hints=[FieldTypeHintSrc(field_type="dict[str, Any]")],
                )
            )

        if self.schema.keys:
            for childschema in self.schema.keys.values():
                fieldsrc = childschema._generate_class_src()
                if fieldsrc.field:
                    fields.append(fieldsrc.field)
                if fieldsrc.cls:
                    classes.append(fieldsrc.cls)

        return classes, fields

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        # TODO: Improve this to assign a class instance directly instead of using coerce_type.
        if self.schema.default is None:
            return None
        default_value_as_str = str(self.schema.default).replace("'", '"')
        target_type = self.get_type_hints()[0].field_type
        if target_type[0].isupper():
            return f"lambda cls: coerce_type({default_value_as_str}, target_type=cls)"

        return default_value_as_str


class SrcGenRootDict(SrcGenDict):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    def get_field(self) -> None:
        """
        Returns FieldSrc for the given schema to be used for the field definition in the parent object.

        For the root dict there is no parent, so this always returns None.
        """

    def get_children_classes_and_fields(self) -> tuple[list[ModelSrc], list[FieldSrc]]:
        """
        Return lists of ModelSrc and FieldSrc for any nested fields.

        For the EosDesigns root dict we also insert placeholders for custom structured configuration and dynamic keys.
        """
        classes, fields = super().get_children_classes_and_fields()
        if self.get_class_name() != "EosDesigns":
            return classes, fields

        classes.append(
            ModelSrc(
                name="_CustomStructuredConfigurationsItem",
                classes=[],
                fields=[
                    FieldSrc(
                        name="key",
                        type_hints=[FieldTypeHintSrc(field_type="str")],
                        description="Complete key including prefix",
                        optional=False,
                    ),
                    FieldSrc(
                        name="value",
                        type_hints=[FieldTypeHintSrc(field_type="EosCliConfigGen")],
                        description="Structured config including the suffix part of the key.",
                        optional=False,
                    ),
                ],
            )
        )
        fields.append(
            FieldSrc(
                name="_custom_structured_configurations",
                type_hints=[FieldTypeHintSrc(field_type="list", list_item_type="_CustomStructuredConfigurationsItem")],
            )
        )
        if self.schema.dynamic_keys:
            """
            Build a data model like this:
            dynamic_keys:
              _dynamic_key_maps:
                - dynamic_keys_path: "node_type_keys.key"
                  model_key: "node_type_keys"
              node_type_keys:
                - key: "l2leaf"
                  value: NodeTypeKeysKey
            }
            """
            dyn_classes = []
            dyn_fields = []
            _dynamic_key_maps = []
            for dynamic_keys_path, childschema in self.schema.dynamic_keys.items():
                # dynamic_key_type will be "node_type_keys", "connected_endpoints_keys" or "network_services_keys"
                dynamic_key_type = dynamic_keys_path.split(".", maxsplit=1)[0]
                dynamic_key_model_name = generate_class_name(f"dynamic_{dynamic_key_type}")
                _dynamic_key_maps.append({"dynamic_keys_path": dynamic_keys_path, "model_key": dynamic_key_type})
                fieldsrc = childschema._generate_class_src()
                # Overriding the details from the autocreated field. This way we can reuse the field definition with types and type hints
                fieldsrc.field.name = "value"
                fieldsrc.field.description = "Value of dynamic key"
                dyn_classes.append(
                    ModelSrc(
                        name=dynamic_key_model_name,
                        classes=[fieldsrc.cls],
                        fields=[
                            FieldSrc(
                                name="key",
                                type_hints=[FieldTypeHintSrc(field_type="str")],
                                description="Key used as dynamic key",
                                optional=False,
                            ),
                            fieldsrc.field,
                        ],
                    )
                )
                dyn_fields.append(
                    FieldSrc(
                        name=dynamic_key_type,
                        optional=False,
                        type_hints=[FieldTypeHintSrc(field_type="list", list_item_type=dynamic_key_model_name)],
                        description=f"List of dynamic '{dynamic_key_type}'.",
                    )
                )
            class_vars = [
                ClassVarSrc(
                    name="_dynamic_key_maps",
                    type_hint=FieldTypeHintSrc(field_type="tuple", list_item_type="dict, ..."),
                    description="Internal tuple of mappings from dynamic_keys_path to model_key.",
                    value=str(tuple(_dynamic_key_maps)),
                )
            ]

            classes.append(
                ModelSrc(
                    name="_DynamicKeys",
                    classes=dyn_classes,
                    fields=dyn_fields,
                    class_vars=class_vars,
                    description="Data models for dynamic keys.",
                )
            )
            fields.append(
                FieldSrc(
                    name="_dynamic_keys",
                    optional=False,
                    type_hints=[FieldTypeHintSrc(field_type="_DynamicKeys")],
                    description="Dynamic keys",
                )
            )

        return classes, fields
