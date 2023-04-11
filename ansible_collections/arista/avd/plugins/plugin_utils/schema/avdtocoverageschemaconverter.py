from __future__ import absolute_import, annotations, division, print_function

from functools import cached_property


class CoverageNode:
    def __init__(self, key, parent, is_dynamic=False, primary_key=None, valid_values=None):
        self.parent = parent
        self.root = self.parent.root if self.parent else self
        self.key = key
        self.is_dynamic = is_dynamic
        self.value = None
        # if this node is in a list keep the value of the parent
        self.ancestor_primary_key_paths = []
        self.primary_key = primary_key
        self.primary_key_values = []
        self.valid_values = valid_values
        self.hitcount = 0
        self.children = []
        # Keep track of unknown keys
        self.unknown_keys = {}

    # Children
    def add_child(self, child_node: CoverageNode) -> None:
        self.children.append(child_node)

    def get_child(self, key):
        for child in self.children:
            if child.key == key:
                return child
        return None

    # Path
    @cached_property
    def _path_list(self):
        # Handle root case
        if self.parent is None:
            return []
        else:
            if self.primary_key:
                node_path = [f"{self.key}[<{self.primary_key}>]"]
            elif self.is_dynamic:
                node_path = [f"{self.key}[<DYNAMIC>]"]
            else:
                node_path = [self.key]

        return self.parent._path_list + node_path

    @cached_property
    def path(self):
        path_list = self._path_list
        return "/" + "/".join(path_list)

    def render_ancestors_path(self, ancestors_path):
        def _list(node, ancestors_path):
            if node.parent is None:
                return []
            if node.primary_key:
                node_path = [f"{node.key}[{node.primary_key}:{ancestors_path[-1]}]"]
                ancestors_path = ancestors_path[:-1]
            elif node.is_dynamic:
                node_path = [f"{ancestors_path[-1]}"]
                ancestors_path = ancestors_path[:-1]
            else:
                node_path = [self.key]
            return _list(node.parent, ancestors_path) + node_path

        return "/" + "/".join(_list(self, ancestors_path))

    def get_coverage(self, data: dict, ancestor_primary_key_path):
        """
        Parse a data dictionnary and keep track of the hits
        by descending into the dictionnary
        """
        if isinstance(data, dict):
            self.hit(ancestor_primary_key_path)
            for key, value in data.items():
                # if self.key == "__root__":
                #     for child in self.children:
                #         print(f"{child.key} - {child.is_dynamic}")
                key_found = False
                for child in [child for child in self.children if not child.is_dynamic]:
                    if child.key == key:
                        child.get_coverage(value, ancestor_primary_key_path=ancestor_primary_key_path)
                        key_found = True
                # check if it could be a dynamic key
                for child in [child for child in self.children if child.is_dynamic]:
                    # Need to see if the key could be one of the dynamic values
                    # TODO - could be a problem if multiple children have the same dynamic key
                    dynamic_key_values = self._get_dynamic_key_values(child.key)
                    # print(f"DK {dynamic_key_values}")
                    if key in dynamic_key_values:
                        child_apkp = ancestor_primary_key_path.copy()
                        child_apkp.append(key)
                        child.get_coverage(value, ancestor_primary_key_path=child_apkp)
                        key_found = True
                if not key_found:
                    # keep track of the unknown keys
                    self.unknown_keys.setdefault(key, []).append(value)
                    # TODO make this a log instead
                    print(f"{key} was provided in data but not found in schema for {self.path}")
        elif isinstance(data, list):
            for element in data:
                if self.primary_key is not None:
                    elem_pk = element[self.primary_key]
                    self.primary_key_values.append(elem_pk)
                    elem_apkp = ancestor_primary_key_path.copy()
                    elem_apkp.append(elem_pk)
                    self.get_coverage(element, ancestor_primary_key_path=elem_apkp)
                else:
                    self.get_coverage(element, ancestor_primary_key_path=ancestor_primary_key_path)
        else:
            self.hit(ancestor_primary_key_path)

    def _get_dynamic_key_values(self, key):
        """
        TODO
        This is a dynamic key which is necessarily a top level key for now (TBC with Claus)
        The key has the format of a path from root e.g.  node_type_keys.key

        # Assume for now we look for primary key values in before last
        """
        key_as_list = key.split(".")
        current_node = self.root
        for elem in key_as_list[:-1]:
            # print(f"CURRENT {current_node.key}, path: {key_as_list}, elem: {elem}")
            current_node = current_node.get_child(elem)
        # print(f"FINAL CURRENT {current_node.key}, pkv: {current_node.primary_key_values}")
        return current_node.primary_key_values

    def get_coverage_percentage(self) -> float:
        def inner_percentage(node):
            zero_hit = 1 if node.hitcount == 0 else 0
            total_nodes = 1
            for child in node.children:
                child_zero, child_total = inner_percentage(child)
                zero_hit += child_zero
                total_nodes += child_total

            return zero_hit, total_nodes

        zero_hit, total_nodes = inner_percentage(self)
        if total_nodes == 0:
            # TODO raise / print something
            return 0.0
        return 100 * (total_nodes - zero_hit) / total_nodes

    def hit(self, ancestor_primary_key_path) -> None:
        if ancestor_primary_key_path != []:
            self.ancestor_primary_key_paths.append(ancestor_primary_key_path)
        self.hitcount += 1

    # Printing functions
    def get_unknown_keys(self):
        return self.umknown_keys

    def tree_repr(self, depth=0, indent=2, max_depth=10, skip_zero=False):
        def _as_list_of_strings(node, depth=0, indent=2, max_depth=10, skip_zero=False):
            current_indent = " " * (indent * depth)
            if not (skip_zero and node.hitcount == 0):
                ret = [f"{current_indent}* {node.key}: {node.hitcount}"]
                if depth <= max_depth:
                    for child in node.children:
                        ret.extend(
                            _as_list_of_strings(
                                child,
                                depth=depth + 1,
                                indent=indent,
                                max_depth=max_depth,
                                skip_zero=skip_zero,
                            )
                        )
                return ret
            return []

        return "\n".join(
            _as_list_of_strings(
                self,
                depth=depth,
                indent=indent,
                max_depth=max_depth,
                skip_zero=skip_zero,
            )
        )

    def path_repr(self, depth=0, max_depth=10, skip_zero=False, only_zero=False, include_paths=False):
        def inner(node, depth=0, max_depth=2, skip_zero=False, only_zero=False):
            ret = []
            if only_zero:
                if node.path != "/" and node.hitcount == 0:
                    ret.append(f"{node.path}: {node.hitcount}")
                if depth <= max_depth:
                    for child in node.children:
                        ret.extend(
                            inner(
                                child,
                                depth=depth + 1,
                                max_depth=max_depth,
                                skip_zero=skip_zero,
                                only_zero=only_zero,
                            )
                        )
                return ret
            elif not (skip_zero and node.hitcount == 0):
                if node.path != "/":
                    ret = [f"{node.path}: {node.hitcount}"]
                    if len(node.primary_key_values) > 0 and node.primary_key is not None:
                        ret[-1] += f" - {node.primary_key_values}"
                    if include_paths:
                        for apkp in node.ancestor_primary_key_paths:
                            ret[-1] += f"\n  - {node.render_ancestors_path(apkp)}"
                if depth <= max_depth:
                    for child in node.children:
                        ret.extend(
                            inner(
                                child,
                                depth=depth + 1,
                                max_depth=max_depth,
                                skip_zero=skip_zero,
                                only_zero=only_zero,
                            )
                        )
                return ret
            return []

        return "\n".join(
            inner(self, depth=depth, max_depth=max_depth, skip_zero=skip_zero, only_zero=only_zero),
        )

    @classmethod
    def merge_nodes(cls, *nodes, parent=None):
        """
        TODO merge hit_aths as well
        WARNING
        TODO this method is out of date
        """
        # no argument means empty tuple
        if nodes:
            return None
        if len(nodes) == 1:
            # only one node
            return nodes[0]
        common_key = nodes[0].key
        for node in nodes:
            if node.key != common_key:
                raise KeyError("Trying to merge CoverageNodes with different keys!")

        result_node = CoverageNode(common_key, parent)
        child_dicts = {}
        for node in nodes:
            result_node.hitcount += node.hitcount
            # todo handle duplicates for the next one
            result_node.primary_key_values.extend(node.primary_key_values)
            for child in node.children:
                child_dicts.setdefault(child.key, []).append(child)
        for key, children in child_dicts:
            merged_child = CoverageNode.merge_nodes(children, parent=result_node)
            result_node.add_child(merged_child)

        return result_node

    def __str__(self):
        msg = [f"****************** {self.path}"]
        msg.append(f"{self.primary_key}")
        msg.append("******************")
        return "\n".join(msg)


class AvdToCoverageSchemaConverter:
    """
    This converter will convert a regular avdschema to a coverage schema

    The documentation schema is a flatter representation of the AVD schema

    """

    def __init__(self, avdschema):
        self._avdschema = avdschema

    def convert_schema(self):
        root_node = CoverageNode("__root__", None)

        # Get fully resolved schema (where all $ref has been expanded recursively)
        schema = self._avdschema.resolved_schema

        self.build_node(root_node, schema)

        return root_node

    def build_node(self, parent_node: CoverageNode, schema: dict) -> None:
        primary_key = None
        schema_keys = {}
        if schema.get("type") == "dict":
            schema_keys = self._get_keys(schema)
        elif schema.get("type") == "list":
            primary_key, schema_keys = self._get_items(schema)

        for key, childschema in schema_keys.items():
            output_node = CoverageNode(key, parent_node)
            if primary_key is not None:
                parent_node.primary_key = primary_key
            parent_node.add_child(output_node)
            self.build_node(output_node, childschema)

        # Handle dynamic keys
        if schema.get("type") == "dict":
            dynamic_schema_keys = self._get_dynamic_keys(schema)
            for key, childschema in dynamic_schema_keys.items():
                output_node = CoverageNode(key, parent_node, is_dynamic=True)
                if primary_key is not None:
                    parent_node.primary_key = primary_key
                parent_node.add_child(output_node)
                self.build_node(output_node, childschema)

    def _get_items(self, schema: dict):
        primary_key = schema.get("primary_key")
        keys = {}
        if (items := schema.get("items")) is not None:
            keys = self._get_keys(items)
        return primary_key, keys

    def _get_keys(self, schema: dict):
        keys = schema.get("keys", {})
        # TODO - HACK - remove keys that should be definitions
        keys_which_are_defs = [
            "node_type",
        ]
        for key in keys_which_are_defs:
            keys.pop(key, None)

        return keys

    def _get_dynamic_keys(self, schema: dict):
        keys = {}
        dynamic_keys = schema.get("dynamic_keys", {})
        keys.update({f"{dynamic_key}": subschema for dynamic_key, subschema in dynamic_keys.items()})
        return keys
