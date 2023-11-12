# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC
from keyword import iskeyword
from typing import TYPE_CHECKING

from .models import EnumClassSrc, FieldTypeHintSrc, PydanticFieldSrc, PydanticModelSrc, PydanticSrcData
from .utils import generate_class_name, generate_class_name_from_ref, get_annotations_for_field

if TYPE_CHECKING:
    from ..metaschema.meta_schema_model import AvdSchemaBool, AvdSchemaDict, AvdSchemaField, AvdSchemaInt, AvdSchemaList, AvdSchemaStr


class PydanticSrcGenBase(ABC):
    # TODO:
    # Optimize ref handling?
    # add deprecation handling
    # dynamic_valid_values
    # format
    # Create a base model for lists so child items can be rendered by their own generators instead of trying to handle it inside lists.

    def generate_pydantic_src(self, schema: AvdSchemaField, class_name: str | None = None) -> PydanticFieldSrc:
        """
        Yields PydanticModelSrc for the given schema.
        Requires an input schema of type "AvdSchemaDict".

        Recursively walks child schemas and creates nested classes and fields.
        """
        self.schema = schema
        self.class_name = class_name

        if schema.deprecation and schema.deprecation.removed:
            return PydanticSrcData(field=None, cls=None)

        return PydanticSrcData(field=self.get_field(), cls=self.get_class())

    def get_field(self) -> PydanticFieldSrc | None:
        if not self.schema._key:
            raise ValueError(f"No key set for schema {self.schema.type}")

        return PydanticFieldSrc(
            name=self.get_field_name(),
            type_hints=self.get_type_hints(),
            optional=not (bool(self.schema.required) or self.schema._is_primary_key),
            default_value=self.get_default_or_field(),
            description=self.schema.description,
        )

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        if cls := self.get_class():
            field_type = cls.name
        else:
            field_type = self.schema.type

        return [
            FieldTypeHintSrc(
                field_type=field_type,
                annotations=get_annotations_for_field(self.schema),
            )
        ]

    def get_class_name(self) -> str:
        if self.class_name:
            return generate_class_name(self.class_name)

        return generate_class_name(self.get_key())

    def get_class(self) -> PydanticModelSrc | EnumClassSrc | None:
        return None

    def get_key(self) -> str:
        return self.schema._key.replace("<", "").replace(">", "").replace(".", "_")

    def get_field_name(self) -> str:
        if not self.valid_key:
            return f"field_{self.get_key()}"
        return self.get_key()

    @property
    def valid_key(self) -> bool:
        # Set alias for reserved keywords
        return not iskeyword(self.schema._key) and self.schema._key.islower()

    def get_default(self) -> str:
        return str(self.schema.default)

    def get_default_or_field(self) -> str:
        field_args = self.get_field_args()
        if field_args:
            field_args.insert(0, self.get_default())
            return f"Field({', '.join(field_args)})"

        return self.get_default()

    def get_field_args(self) -> list[str]:
        field_args = []
        if not self.valid_key:
            field_args.append(f'alias="{self.schema._key}"')
        if self.schema.type in ["dict", "list"] and self.schema.default is not None:
            field_args.append("validate_default=True")
        if self.schema.display_name:
            field_args.append(f'title="{self.schema.display_name}"')

        return field_args


class PydanticSrcGenInt(PydanticSrcGenBase):
    schema: AvdSchemaInt

    def get_field_args(self) -> list[str]:
        field_args = super().get_field_args()
        if self.schema.min is not None:
            field_args.append(f"ge={self.schema.min}")
        if self.schema.max is not None:
            field_args.append(f"le={self.schema.max}")

        return field_args

    def get_class(self) -> PydanticModelSrc | EnumClassSrc | None:
        if not self.schema.valid_values:
            return None

        return EnumClassSrc(
            name=f"{self.get_class_name()}Enum",
            value_type="int",
            values=self.schema.valid_values,
        )


class PydanticSrcGenBool(PydanticSrcGenBase):
    schema: AvdSchemaBool


class PydanticSrcGenStr(PydanticSrcGenBase):
    schema: AvdSchemaStr

    def get_field_args(self) -> list[str]:
        field_args = super().get_field_args()
        if self.schema.min_length is not None:
            field_args.append(f"min_length={self.schema.min_length}")
        if self.schema.max_length is not None:
            field_args.append(f"max_length={self.schema.max_length}")
        if self.schema.pattern:
            field_args.append(f'pattern=r"{self.schema.pattern}"')
        return field_args

    def get_default(self) -> str:
        if self.schema.default:
            return f'"{self.schema.default}"'
        else:
            return str(self.schema.default)

    def get_type_hints(self) -> list[str]:
        if cls := self.get_class():
            field_type = cls.name
        else:
            field_type = "str"

        return [
            FieldTypeHintSrc(
                field_type=field_type,
                annotations=get_annotations_for_field(self.schema),
            )
        ]

    def get_class(self) -> PydanticModelSrc | EnumClassSrc | None:
        if not self.schema.valid_values:
            return None

        return EnumClassSrc(
            name=f"{self.get_class_name()}Enum",
            value_type="str",
            values=self.schema.valid_values,
        )


class PydanticSrcGenList(PydanticSrcGenBase):
    """
    Provides the method "generate_pydantic_src_class" used to build source code for Pydantic models representing the schema.
    """

    schema: AvdSchemaList

    def get_field_args(self) -> list[str]:
        field_args = super().get_field_args()
        if self.schema.min_length is not None:
            field_args.append(f"min_length={self.schema.min_length}")
        if self.schema.max_length is not None:
            field_args.append(f"max_length={self.schema.max_length}")
        return field_args

    def get_class(self) -> PydanticModelSrc | None:
        if not self.schema.items:
            return None

        if self.schema.items.type != "dict":
            return None

        fields = []
        classes = []

        if self.schema.items.keys:
            for childschema in self.schema.items.keys.values():
                fieldsrc = childschema._generate_pydantic_src()
                if fieldsrc.field:
                    fields.append(fieldsrc.field)
                if fieldsrc.cls:
                    classes.append(fieldsrc.cls)

        return PydanticModelSrc(
            name=f"{self.get_class_name()}Item",
            base_classes=self.get_base_classes(),
            classes=classes,
            fields=fields,
            allow_extra=self.schema.items.allow_other_keys,
            # description=self.get_description(),
        )

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        if not self.schema.items:
            return [FieldTypeHintSrc(field_type="list", list_item_type="Any")]

        if cls := self.get_class():
            item_type = cls.name
        else:
            item_type = self.schema.items.type

        return [
            FieldTypeHintSrc(
                field_type="list",
                list_item_type=FieldTypeHintSrc(
                    field_type=item_type,
                    annotations=get_annotations_for_field(self.schema.items),
                ),
            )
        ]

    def get_base_classes(self) -> list[str]:
        if not self.schema.items or not self.schema.items.field_ref:
            # Using special AvdDictBaseModel to handle custom data starting with _.
            return ["AvdDictBaseModel"]

        return [generate_class_name_from_ref(self.schema.items.field_ref)]

    def get_default(self) -> str:
        return str(self.schema.default).replace("'", '"')


class PydanticSrcGenDict(PydanticSrcGenBase):
    """
    Provides the method "generate_pydantic_src_class" used to build source code for Pydantic models representing the schema.
    """

    schema: AvdSchemaDict

    def get_class(self) -> PydanticModelSrc | None:
        if not self.schema.keys and not self.schema.field_ref:
            return None

        classes, fields = self.get_children_classes_and_fields()
        return PydanticModelSrc(
            name=self.get_class_name(),
            base_classes=self.get_base_classes(),
            classes=classes,
            fields=fields,
            imports=self.get_imports(),
            allow_extra=self.schema.allow_other_keys,
            # description=self.get_description(),
        )

    def get_base_classes(self) -> list[str]:
        if not self.schema.field_ref:
            # Using special AvdDictBaseModel to handle custom data starting with _.
            return ["AvdDictBaseModel"]

        return [generate_class_name_from_ref(self.schema.field_ref)]

    def get_imports(self) -> set[str]:
        imports = set()
        if self.schema.field_ref:
            schema_name = self.schema.field_ref.split("#", maxsplit=1)[0]
            imports.add(f"from .{schema_name} import {generate_class_name(schema_name)}")
        else:
            imports = {"from .models import AvdDictBaseModel"}

        return imports

    def get_children_classes_and_fields(self) -> ([PydanticModelSrc], [AvdSchemaField]):
        classes = []
        fields = []
        if self.schema.keys:
            for childschema in self.schema.keys.values():
                fieldsrc = childschema._generate_pydantic_src()
                if fieldsrc.field:
                    fields.append(fieldsrc.field)
                if fieldsrc.cls:
                    classes.append(fieldsrc.cls)

        return classes, fields


class PydanticSrcGenRootDict(PydanticSrcGenDict):
    def get_field(self) -> PydanticFieldSrc | None:
        return None

    def get_base_classes(self) -> list[str]:
        if self.get_class_name() == "EosDesigns":
            return ["AvdEosDesignsRootDictBaseModel"]
        return ["BaseModel"]

    def get_imports(self) -> set[str]:
        imports = super().get_imports() or set()
        if self.get_class_name() == "EosDesigns":
            imports.add("from .models import AvdEosDesignsRootDictBaseModel")
        return imports

    def get_children_classes_and_fields(self) -> ([PydanticModelSrc], [AvdSchemaField]):
        classes, fields = super().get_children_classes_and_fields()
        if self.get_class_name() != "EosDesigns":
            return classes, fields

        classes.append(
            PydanticModelSrc(
                name="CustomStructuredConfiguration",
                classes=[],
                fields=[
                    PydanticFieldSrc(
                        name="key",
                        type_hints=[FieldTypeHintSrc(field_type="str")],
                        description="Complete key including prefix",
                        optional=False,
                    ),
                    PydanticFieldSrc(
                        name="value",
                        type_hints=[FieldTypeHintSrc(field_type="EosCliConfigGen")],
                        description="Structured config including the suffix part of the key.",
                        optional=False,
                    ),
                ],
            )
        )
        fields.append(
            PydanticFieldSrc(
                name="custom_structured_configurations",
                type_hints=[FieldTypeHintSrc(field_type="list", list_item_type="CustomStructuredConfiguration")],
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
                fieldsrc = childschema._generate_pydantic_src()
                # Overriding the details from the autocreated field. This way we can reuse the field definition with types and type hints
                fieldsrc.field.name = "value"
                fieldsrc.field.description = "Value of dynamic key"
                dyn_classes.append(
                    PydanticModelSrc(
                        name=dynamic_key_model_name,
                        classes=[fieldsrc.cls],
                        fields=[
                            PydanticFieldSrc(
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
                    PydanticFieldSrc(
                        name=dynamic_key_type,
                        type_hints=[FieldTypeHintSrc(field_type="list", list_item_type=dynamic_key_model_name)],
                        description=f"List of dynamic '{dynamic_key_type}'.",
                    )
                )
            dyn_fields.append(
                PydanticFieldSrc(
                    name="_dynamic_key_maps",
                    type_hints=[FieldTypeHintSrc(field_type="list", list_item_type="dict")],
                    description="Internal list of mappings from dynamic_keys_path to model_key.",
                    default_value=str(_dynamic_key_maps),
                    optional=False,
                )
            )
            classes.append(
                PydanticModelSrc(
                    name="DynamicKeys",
                    classes=dyn_classes,
                    fields=dyn_fields,
                    description="Data models for dynamic keys",
                )
            )
            fields.append(
                PydanticFieldSrc(
                    name="dynamic_keys",
                    type_hints=[FieldTypeHintSrc(field_type="DynamicKeys")],
                    description="Dynamic keys",
                )
            )

        return classes, fields
